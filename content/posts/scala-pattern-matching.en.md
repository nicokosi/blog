+++
date = "2016-09-14T00:00:00+01:00"
title = "Let's play with pattern matching in Scala"
description = "Pattern matching is a powerful technique for filtering and testing variables. This article aims at illustrating pattern matching in Scala using a simple example."
tags = [ "scala", "pattern-matching", "console", "repl" ]
slug = "scala-pattern-matching"
+++

Pattern matching is a powerful technique for filtering and testing variables. This article aims at illustrating pattern matching in Scala using a simple example.
Let's say we want to return the color (red or black) of a playing card.

Notes: The code below "shows" the console output using comments (ex: `"foo" // foo`). I have used a [IntelliJ IDEA worksheet](https://confluence.jetbrains.com/display/IntelliJIDEA/Working+with+Scala+Worksheet) but the standard Scala console can also be used (REPL FTW!)

<br/>
## Step #1: let's create a simple class

Let's create a immutable class for the "club" suite:

```scala
class Club {
  val symbol = "♣"
  val label = "club"
}

val club: Club = new Club()
club.symbol // ♣
```

So far, so good. Instances can be compared by identity (reference) but not by value because we did not override the `equals` method:
```scala
club.equals(club) // true
club == new Club // false
club.eq(new Club) // false
club.equals(new Club) // false
```

`hashCode` and `toString` are also default ones:
```scala
club // Club@1ac88f64
club.hashCode() // 1976061787
new Club().hashCode() // 1751431390
```

<br/>
## Step #2: let's create a case class

A `case class` has two benefits:

1. auto-implement `equals`, `hashCode` and `toString` methods.
2. enhance pattern matching capability via two methods: a "constructor" method, `apply`, and a "de-constructor" method, `unapply`.

```scala
case class CardSuite(symbol: String, label: String)
```

`apply` method is a kind of free constructor. By the way, we don't need to use the `new` keyword:
```scala
CardSuite("♣", "club") // CardSuite(♣,club)
```

`equals`, `hashCode` and `toString` methods are also implemented for free:
```scala
CardSuite("♣", "club").symbol
CardSuite("♣", "club") == CardSuite("♣", "club") // true
CardSuite("♣", "club").equals(CardSuite("♣", "club")) // true
CardSuite("♣", "club").eq(CardSuite("♣", "club")) // false
CardSuite("♣", "club").hashCode() // 1302714609
CardSuite("♣", "club").hashCode() // 1302714609
```

<br/>
## "Bonus" step: use an enumeration

Since there are four suites in French playing cards, we can create an enumeration. This is not directly related to our pattern matching example, but let's do it, for fun and profit. ;-)
```scala
object CardSuites {
  val CLUB = CardSuite("♣", "club")
  val DIAMOND = CardSuite("♦", "diamond")
  val HEART = CardSuite("♥", "heart")
  val SPADE = CardSuite("♠", "spade")
  def values() = List(DIAMOND, HEART, SPADE, CLUB)
}
CardSuites.CLUB != CardSuites.DIAMOND // true
CardSuites.values // List(CardSuite(♦,diamond), CardSuite(♥,heart), CardSuite(♠,spade), CardSuite(♣,club))
```

<br/>
## Last step: let's use pattern matching!

### First example

Here is a first pattern matching example, used in a function that returns the color of a suite card:
```scala
def justColor(cardSuite: CardSuite): String = cardSuite match {
  case CardSuites.CLUB | CardSuites.SPADE => "black"
  case CardSuites.DIAMOND | CardSuites.HEART => "red"
  case _ => "none"
}

justColor(CardSuites.SPADE) // black
```
This example demonstrates:

- the `|` notation (_disjunction_) that can be used to group several cases;
- the `_` notation (_wildcard_) for "other cases".

### Second example

Here is a second example to demonstrate field filtering, also known as "de-structuring":
```scala
def describeColor(cardSuite: CardSuite): String = cardSuite match {
  case CardSuite(_, label) => s"$label is ${justColor(cardSuite)}"
}

describeColor(CardSuites.SPADE) // spade is black
```
We only keep the suite label using the `unapply` method of our case class.

That's all folks! 🤓


PS: Thanks to Jérôme Prudent for the Scala tips and for the review. Jérôme contributes to the [Arolla blog](http://www.arolla.fr/blog) ([direct link to his posts](http://www.arolla.fr/blog/author/jerome-prudent/)).
