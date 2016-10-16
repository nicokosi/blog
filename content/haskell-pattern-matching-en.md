Title: Let's play with pattern matching in Haskell
Date: 2016-09-27 00:00
Tags: haskell, pattern-matching
Slug: haskell-pattern-matching
Author: Nicolas Kosinski
Summary: Let's discover Haskell pattern matching
Lang: en

Let's discover Haskell and pattern matching via basic examples similar to ["Let's play with pattern matching in Scala"](https://nicokosi.github.io/scala-pattern-matching-en.html).

<br/>
## Step #1: create an enumeration


We can create an enumeration that represent the four suites in French playing cards:

```haskell
data CardSuite = Club | Diamond | Heart | Spade
  deriving (Eq, Enum, Show)
```
We have just created our own _data type_ which:

* has four constructors (_value constructors_)
* inherits from Haskell's base types:
    * `Eq` in order to know if two values are equal or not
    * `Enum` so that all values are known and ordered (_sequentially ordered types_)
    * `Show` so that we can have a string representation for debugging/troubleshooting


We can then use `ghci` (_Glascow Haskell Compiler Interactive environment_), the Haskell REPL, to illustrate how we can use this enumeration:
```haskell
*Main> Heart == Heart
True
*Main> Heart < Spade
True
*Main> succ Heart
Spade
```

<br/>

## Pattern matching examples

### Example #1

The following function returns the Unicode symbol for a given card suite:
```haskell
symbol :: CardSuite -> String
symbol cardSuite =
  case cardSuite of
    Club -> "♣"
    Diamond ->"♦"
    Heart -> "♥"
    Spade -> "♠"
```
Let's evaluate it :
```haskell
*Main> putStrLn $ symbol $ Heart
♥
```

Notice that:

* The `$` operator allows is a way chain function calls, omitting to use nested parenthesis (`putStrLn(symbol(Heart))`).
* the `putStrLn` standard function can display Unicode characters, whereas the standard function `show` only displays ASCII characters. 😎

<br/>
Morevover, the Haskell compiler can detect a non-exhaustive pattern matching. For instance, the following code :
```haskell
symbol :: CardSuite -> String
symbol cardSuite =
  case cardSuite of
    Club -> "♣"
```
generates a compile-time warning :
```haskell
warning: [-Wincomplete-patterns]
    Pattern match(es) are non-exhaustive
    In a case alternative:
        Patterns not matched:
            Diamond
            Heart
            Spade
```
and the following evaluation triggers an error :
```haskell
*Main> symbol Diamond
"*** Exception: test-en.hs:(13,3)-(14,15): Non-exhaustive patterns in case
```

<br/>

### Example #2, share expression with a 'where' block

Let's implement a `color` function that returns "red" or "black" depending on the input card suite:

```haskell
color :: CardSuite -> String
color cardSuite =
  case cardSuite of
    Club -> black
    Diamond -> red
    Heart -> red
    Spade -> black
    where
      red = "red"
      black = "black"
```

Let's evaluate it:
```
*Main> color Heart
"red"
```

The `where` keyword is used there to share some expressions.
<br/>
<br/>

### Example #3: destructuring

Let's say we want to define our custom type `Card` that combines a rank (1, 2, 3, ..., Jack, Queen, King) and a suite:

```haskell
data Rank =
  R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | Jack | Queen | King
  deriving (Eq, Ord, Enum, Show)

data Card = Card {
  rank :: Rank,
  suite :: CardSuite
} deriving (Eq, Show)
```
The `Card` type uses the _record_ syntax that allows to name fields.

We can then use pattern matching in order to de-structure a card, filtering some fields.
For instance, the following function determines if two cards have the same suite:

```haskell
sameSuite :: (Card, Card) -> Bool
sameSuite ((Card _ suite1), (Card _ suite2)) =
  suite1 == suite2
```

Call examples:
```
*Main> :{
*Main| sameSuite (
*Main|        Card {rank=R1, suite=Diamond},
*Main|        Card {rank=R1, suite=Heart} )
*Main| :}
False
*Main> :{
*Main| sameSuite (
*Main|      Card {rank=Jack, suite=Heart},
*Main|      Card {rank=R1, suite=Diamond} )
*Main| :}
False
```

Card ranks, that are not needed by our function, have been filtered using the _wild-card_ symbol (`_`).

That's all, folks! 🤓
