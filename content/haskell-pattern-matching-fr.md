Title: Jouons avec le pattern matching en Haskell
Date: 2016-09-27 00:00
Tags: haskell, pattern-matching
Slug: haskell-pattern-matching
Author: Nicolas Kosinski
Summary: Découvrons par l'exemple le pattern matching en Haskell.
Lang: fr

Découvrons le pattern matching en Haskell en reprenant l'exemple des cartes à jouer utilisé dans l'article ["Jouons avec le pattern matching en Scala"](https://nicokosi.github.io/scala-pattern-matching.html).

<br/>
## Préambule : création d'une énumération

Codons notre énumération correspondant à nos quatre enseignes (carreau, cœur, pique et trèfle) :
```haskell
data Enseigne = Carreau | Coeur | Pique | Trèfle
  deriving (Eq, Enum, Show)
```
Nous venons de créer notre propre type (_data type_) qui :

* a quatre constructeurs (_value constructors_)
* hérite des classes de base :
    * `Eq` pour implémenter l'égalité entre deux valeurs
    * `Enum` pour que les valeurs sont finies et ordonnées (_sequentially ordered types_)
    * `Show` pour avoir une représentation sous forme de chaîne de caractères, ce qui peut être utile pour débugguer ou pour évaluer interactivement du code via le REPL.


Utilisons maintenant `ghci` (_Glascow Haskell Compiler Interactive environment_), le REPL d'Haskell, pour interagir avec cette énumération :
```haskell
*Main> Coeur == Coeur
True
*Main> succ Coeur
Pique
```

<br/>

## Exemples de pattern matching

### Premier exemple basique

La fonction suivante retourne le symbole d'une enseigne :
```haskell
symbole :: Enseigne -> String
symbole enseigne =
  case enseigne of
    Carreau ->"♦"
    Coeur -> "♥"
    Pique -> "♠"
    Trèfle -> "♣"    
```
Exemple d'appel :
```haskell
*Main> putStrLn $ symbole $ Coeur
♥
```

Notons que :

* L'opérateur `$` nous permet de chaîner nos fonctions, plutôt que de les imbriquer dans des parenthèses (`putStrLn(symbole(Coeur))`).
* la fonction `putStrLn` permet d'afficher des caractères Unicode, à l'inverse de la fonction standard `show` qui ne retourne que des chaînes ASCII. 😎

<br/>
Remarque : le compilateur sait détecter un pattern matching non exhaustif. Par exemple, le code suivant :
```haskell
symbole :: Enseigne -> String
symbole enseigne = case enseigne of
    Carreau ->"♦"
```
génère un avertissement de compilation :
```haskell
warning: [-Wincomplete-patterns]
    Pattern match(es) are non-exhaustive
    In a case alternative:
        Patterns not matched:
            Coeur
            Pique
            Trèfle
```
Et l'appel de cette fonction génére une exception :
```haskell
*Main> symbole Coeur
"*** Exception: test.hs:(5,20)-(6,17): Non-exhaustive patterns in case
```

<br/>

### Deuxième exemple, partage d'expression via un bloc 'where'

Autre exemple, implémentons une fonction `couleur` qui retourne la couleur d'une enseigne (chaîne de caractères "rouge" ou "noir") :

```haskell
couleur :: Enseigne -> String
couleur enseigne = case enseigne of
    Carreau -> rouge
    Coeur -> rouge
    Pique -> noir
    Trèfle -> noir
    where
      rouge = "rouge"
      noir = "noir"
```

Exemple d'appel :
```
*Main> couleur(Coeur)
"rouge"
```

Nous avons ici utilisé le mot-clé `where` qui nous permet de partager des expressions.
<br/>
<br/>

### Troisième exemple, déstructuration

Définissons notre propre type `Carte` combinant un rang (1, 2, 3, ..., valet, dame, roi) et une enseigne :

```haskell
data Rang =
  R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | Valet | Dame | Roi
  deriving (Eq, Ord, Enum, Show)

data Carte = Carte {
  rang :: Rang,
  enseigne :: Enseigne
} deriving (Eq, Show)
```
Le type `Carte` utilise la syntaxe _record_ permettant de nommer les champs.

Nous pouvons ainsi utiliser le pattern matching pour "déstructurer" une carte en filtrant les champs. Par exemple, la fonction suivante permet de déterminer si deux cartes, associées par un _tuple_, sont de même enseigne :

```haskell
mêmeEnseigne :: (Carte, Carte) -> Bool
mêmeEnseigne ((Carte _ enseigne1), (Carte _ enseigne2)) =
  enseigne1 == enseigne2
```

Exemples d'appel :
```
*Main> :{
*Main| mêmeEnseigne (
*Main|     Carte {rang=R1, enseigne=Carreau},
*Main|     Carte {rang=R1, enseigne=Coeur} )
*Main| :}
False
*Main> :{
*Main| mêmeEnseigne (
*Main|     Carte {rang=Valet, enseigne=Coeur},
*Main|     Carte {rang=R1, enseigne=Coeur} )
*Main| :}
True
```

Les rangs, que l'on n'utilise pas dans la fonction, ont été filtrés via le caractère _wild-card_ (`_`).

Et voilà ! 🤓
