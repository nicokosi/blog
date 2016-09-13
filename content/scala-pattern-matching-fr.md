Title: Jouons avec le pattern matching en Scala
Date: 2016-09-13 00:00
Tags: scala, pattern-matching, console, repl
Slug: scala-pattern-matching
Author: Nicolas Kosinski
Summary: Le pattern matching est une technique puissante permettant de filtrer et de tester la valeur de variables. Le but de cet article est d'illuster par l'exemple le pattern matching en Scala.
Lang: fr

# Jouons avec le pattern matching en Scala

Le pattern matching est une technique puissante permettant de filtrer et de tester la valeur de variables. Le but de cet article est d'illuster par l'exemple le pattern matching en Scala.

Supposons que nous voulions créer une fonction retournant la couleur (noir / rouge) d'une enseigne d'une carte à jouer (les quatre enseignes du jeu français étant : trêfle, coeur, carreau et pique).

Notes :
 1. dans le code ci-dessous, les commentaires se trouvant à la fin de chaque ligne correspondent à la sortie standard de la console
 2. j'ai utilisé un [worksheet IntelliJ IDEA](https://confluence.jetbrains.com/display/IntelliJIDEA/Working+with+Scala+Worksheet) pour coder interactivement cet exemple, mais on peut bien sûr utiliser la console Scala

## 1ère étape : création d'une simple classe

Commençons par créer une classe immuable représentant l'enseigne "trèfle" : 

```scala
class Trèfle {
   val symbole = "♣"
   val libellé = "trèfle"
}

val trèfle: Trèfle = new Trèfle()
trèfle.symbole // ♣
```

Notons que cette classe permet de comparer des objets par l'identité (référence) et non par valeur car on ne surcharge pas la méthode `equals` :
```scala
trèfle.equals(trèfle) // true
trèfle == new Trèfle // false
trèfle.eq(new Trèfle) // false
trèfle.equals(new Trèfle) // false
```

De même, les méthodes `hashCode`, `toString` sont celles par défaut :
```scala
trèfle // Trèfle@1ac88f64
trèfle.hashCode() // 123717365
new Trèfle().hashCode() // 1323753063
```

## 2ème étape : création d'une case class

La création d'une `case class` permet :
 1. d'auto-implémenter les méthodes `equals`, `hashCode` et `toString`.
 2. de bénéficier de deux méthodes utiles au pattern matching :
  - un "constructeur", la méthode `apply`
  - un "déconstructeur", la méthode `unapply` 

```scala
case class Enseigne(symbole: String, libellé: String)
```

Nous avons un constructeur "gratuit", la méthode `apply`:
```scala
Enseigne("♣", "trèfle") // Enseigne(♣,trèfle)
```

Nous avons également une implémentation "gratuite", basée sur les champs, des méthodes `equals`, `hashCode` et `toString` :
```scala
Enseigne("♣", "trèfle").symbole // ♣
Enseigne("♣", "trèfle") == Enseigne("♣", "trèfle") // true
Enseigne("♣", "trèfle").equals(Enseigne("♣", "trèfle")) // true
Enseigne("♣", "trèfle").eq(Enseigne("♣", "trèfle")) // false
Enseigne("♣", "trèfle").hashCode() // 841520215
Enseigne("♣", "trèfle").hashCode() // 841520215
```

## Etape "bonus" : création d'une énumération

Puisque nous avons quatre enseignes, nous pouvons créer une énumération. Ca ne servira pas directement à implémenter notre exemple final mais l'exemple s'y prête bien.
```scala
object Enseignes {
  val TREFLE = Enseigne("♣", "trèfle")
  val CARREAU = Enseigne("♦", "carreau")
  val COEUR = Enseigne("♥", "coeur")
  val PIQUE = Enseigne("♠", "pique")
  def values() = List(CARREAU, COEUR, PIQUE, TREFLE)
}
Enseignes.TREFLE != Enseignes.CARREAU // true
Enseignes.values // List[Enseigne] = List(Enseigne(♦,carreau), Enseigne(♥,coeur), Enseigne(♠,pique), Enseigne(♣,trèfle))
```

## Dernière étape : pattern matchons !

Un premier exemple de pattern matching, utilisé dans une fonction qui retourne la couleur de l'enseigne :
```scala
def indiquerJusteLaCouleur(cardSuite: Enseigne): String = cardSuite match {
  case Enseignes.TREFLE | Enseignes.PIQUE => "noir"
  case Enseignes.CARREAU | Enseignes.COEUR => "rouge"
  case _ => "aucune"
}

indiquerJusteLaCouleur(Enseignes.PIQUE) // noir
```
Ce premier exemple met en avant :
 - la notation `|` (_disjunction_) permettant de regrouper plusieurs cas ;
 - la notation `_` (_wildcard_) pour gérer les autres cas.


Voici un deuxième exemple montrant comment récupérer sélectivement certains champs (ici, le libellé de l'enseigne) en "destructurant" notre instance de `case class`, via la méthode `unapply`.
```scala
def décrireLaCouleur(enseigne: Enseigne): String = enseigne match {
  case Enseigne(_, libellé) => s"$libellé is ${indiquerJusteLaCouleur(enseigne)}"
}

décrireLaCouleur(Enseignes.PIQUE) // pique est noir
```

Et voilà ! 🤓

