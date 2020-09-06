# Parts of Speech Tagging

- [Parts of Speech Tagging](#parts-of-speech-tagging)
  * [Overview](#overview)
  * [Lookup Table](#lookup-table)
  * [Bigrams](#bigrams)
  * [Hidden Markov Models](#hidden-markov-models)
    + [Emission Probabilities](#emission-probabilities)
    + [Transition Probability](#transition-probability)
    + [Hidden Markov Model](#hidden-markov-model)



## Overview

In corpus linguistics, part-of-speech tagging (POS tagging or PoS tagging or POST), also called grammatical tagging is the process of marking up a word in a text (corpus) as corresponding to a particular part of speech, based on both its definition and its context.

<img src="./images/1. pos tagging.png" height="150"></img>

## Lookup Table

In look-up table we try to create a matrix, where each word is tagged. Using look-up table we try to tag parts of speech of a new sentence. For example - <br>
<img src="./images/2. look-up table.png" height="240"></img><br>

Considering the above example, the problem with look-up tables is that it is tagging *Will* also as a *Modal* and not a *Noun*. This problem can be solved using *Bigrams*

## Bigrams

In Bigrams, we not just look at words, we look at their neighbours as well and we tag *pairs of words* instead. <br>
<img src="./images/3. Bigrams.png" height="240"></img>

## Hidden Markov Models

Problem with n-gram or bi-gram is that sometimes all pairs doesn't appear. This is where Hidden Markov Model comes into picture. Consider the situation below, how likely is the probability that *noun is followed by a modal, modal by a verb and verb by a noun.* These are called *transitional probabilities.* Now the probabilities that the *noun will be Jane and modal is will etc..* are called *Emission Probabilities.*<br>
<img src="./images/4. ET probabilities.png" height="150"></img>


### Emission Probabilities
Here, we are calculating the probability that if we see a noun, what is the probability that that word is Mary or Jane etc as below -<br>
<img src="./images/5. Emission Probability.png" height="240"></img>

### Transition Probability
Transition probability is a probability that one part of speech will follow another part of speech. Here we add *start and end tag* and will treat them as part of speech as well and we create a look-up table to calculate the count of pairs of parts of speech.<br>
  
<img src="./images/7. Transition Probability.png" height="240"></img>

### Hidden Markov Model
Below is a sample hidden markov model. The words below are called *observations*, then we plot a graph of their respective transition and emission probabilities as below-<br>
<img src="./images/6. Hidden Markov Model.png" height="240"></img><br>

In order to generate sentences via Hidden Markov Model see the below graph for transitional probability -<br>
<img src="./images/8. Sentence generation.png" height="240"></img><br>





