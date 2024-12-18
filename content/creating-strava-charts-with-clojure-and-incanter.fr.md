+++
title = "Générer ses graphiques Strava avec Clojure et Incanter"
description = "Utilisation de la librairie Clojure Incanter pour générer des graphiques Strava"
date = 2017-04-09
[taxonomies]
tags = ["strava", "charts", "clojure", "incanter"]
+++
# Générer ses graphiques Strava avec Clojure et Incanter

J'utilise [Strava](https://www.strava.com/) pour enregistrer mes sessions de jogging : après avoir enregistré une session avec mon smartphone, je la publie pour pouvoir la partager et la revoir plus tard.

Strava fournit quelques tableaux de bord mais je voulais générer mes propres graphiques afin de visualiser ma progression.


<br/>
##Premier essai avec R
J'ai d'abord essayé d'utiliser [RStudio](https://www.rstudio.com/), un IDE pour le langage R. Je pense que c'est un outil adapté mais je le connais très peu. Après avoir essayé pendant quelques heures d'importer mes données et de les transformer, j'ai abandonné !

![RStudio : un IDE pour la plate-forme R](RStudio.png)

J'essairai une autre fois ! 😅


<br/>
##Deuxième essai avec Clojure et Incanter
J'ai ensuite essayé d'utiliser [Incanter](incanter.org), une librairie Clojure inspirée de R :
> Clojure-based, R-like platform for statistical computing and graphics.

J'avais besoin de faire 3 choses :

1. appeler l'API Strava pour récupérer les données au format JSON
2. faire quelques transformations, essentiellement des conversions (m/s en km/h, secondes en minutes)
3. afficher des graphiques (exemple : évolution de la vitesse moyenne par sortie en fonction du temps)

Allons-y !


<br/>
###1. Récupérer les données Strava

La fonction suivante appelle l'[API Strava "activities"](http://strava.github.io/api/v3/activities/) avec un jeton d'autorisation (access token) et récupère les 200 dernières sorties ("activities" = activité de course à pied, vélo ou natation) sous forme d'un tableau d'objets JSON :
```clojure
(defn strava-activities [token]
  (json/read-str (:body
                   (http-client/get
                     "https://www.strava.com/api/v3/activities"
{:query-params {:access_token token :per_page 200}}))))
```


<br/>
###2. Transformer les données

On définit les fonctions suivantes pour transformer les données :
```clojure
; Convertir les vitesses en km/h (l'API Strava retourne des m/s) :
(def meters-per-second->kilometers-per-hour (partial * 3.6))

; Convertir les durées en minutes (l'API Strava API retourne des secondes) :
(defn- seconds->minutes [s] (/ s 60))

; Incanter peut seulement générer des graphiques à partir de données numériques, les dates au format ISO doivent donc être converties en timestamps :
(defn- string-date->millis [str-date]
  (.getTime
    (clojure.instant/read-instant-date str-date)))
```

Ces fonctions peuvent être appliquées aux données brutes, en utilisant par exemple l'opérateur "thread-last" (```->>```), bien pratique pour chaîner les appels de fonctions :
```clojure
(->> (strava-activities token)
       (map #(update-in % ["average_speed"] meters-per-second->kilometers-per-hour))
       (map #(update-in % ["start_date_local"] string-date->millis))
       (map #(update-in % ["elapsed_time"] seconds->minutes))
       (map #(update-in % ["moving_time"] seconds->minutes)))
```


<br/>
###3. Affichage d'un graphique avec Incanter

La dernière étape consiste à utiliser l'une des fonctions de la librairie Incanter pour afficher un graphique. L'exemple de code suivant affiche l'évolution de la vitesse moyenne de chaque sortie en fonction de la date de la sortie :
```clojure
(defn display-chart [token]
  (let [activities (get-activities token)]
    (with-data
      (to-dataset activities)
      #_(view $data)
      (view
        (time-series-plot
          ($ :start_date_local)
          ($ :average_speed)
          :group-by ($ :type)
          :title "Average speed over time"
          :x-label "time"
          :y-label "average speed (km/h)"
          :points true
          :legend true)))))
```

Le graphique généré :
![Chart: average speed over time](chart-average-speed-over-time.png)


Le code complet, qui affiche plusieurs graphiques similaires, se trouve sur le [repository GitHub strava-activity-graphs](https://github.com/nicokosi/strava-activity-graphs/).
