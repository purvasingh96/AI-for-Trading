# Feature Extraction & Embeddings

- [Feature Extraction & Embeddings](#feature-extraction---embeddings)
  * [Bag of Words](#bag-of-words)
  * [TF-IDF](#tf-idf)
  * [One-Hot Encoding](#one-hot-encoding)
  * [Word Embeddings](#word-embeddings)
    + [Word2Vec](#word2vec)
    + [GloVe](#glove)

## Bag of Words

You can treat a collection of documents as a bag-of-words for comparison purposes. For instance, if you want to check the plagirism of student's essays, then you can treat each essay as bag of words. In order to obtain BOW, we need to follow appropriate pre-processing (normalization, cleaning, lemmatization etc) steps.<br>

<img src="./images/1. BOW.png" height="200"></img><br><br>

 But after pre-processing, keeping them as separate sets is very inefficient.<br>
 
 <img src="./images/2. text cleaning.png" height="160"></img><br><br>
 
 
A better approach is to treat each word document into vector of numbers. A set of documents is known as *Corpus*. First step is to collect all unique words from your corpus to form a *Vocabulary*.<br><br>

 <img src="./images/4. Corpus & Vocab.png" height="200"></img><br><br>


Second, we need to create a *document-text table* where we fill in the frequency of each word occuring in the document. <br><br>

<img src="./images/3. matrix.png" height="200"></img><br><br>

## TF-IDF

One disadvantage of BOW is that it treats every word equally even though we know that there are some words which are of greater importance/weightage. To overcome this we introduce TF-IDF resemblency, where in the document-matrix, we also take note of in how many documents did that word appear and divide the frequency of words by the number of documents in which that word has appeared. <br>

<img src="./images/6. TF-IDF Matrix.png" height="200"></img><br><br>


*This gives us a metrics which is directly propotional to term frequency (TF) but is inversely propotional to document frequency (IDF). Hence the term TF-IDF.*

<img src="./images/5. TF-IDF.png" height="200"></img><br><br>



## One-Hot Encoding

One-hot encoding is similar to BOW except here, we treat each word like a class and assign it a vector that has 1 in a single pre-determined position for that word and 0 for the rest.<br><br>

<img src="./images/7. One-Hot Encoding.png" height="200"></img><br><br>


## Word Embeddings

BOW works in some situations but breaks down when we have large vocabulary. We need a way to control the size of our word reporesentation by limiting it to a fixed-size vector. For example, if 2 words are similar in meaning, they should be closer to each other in vector space as compared to other words that are dissimilar.<br>

<img src="./images/9. Word Embeddings - 1.png" height="200"></img><br><br>

And if 2 pairs of words have a similar difference in their meanings, they should be approximately equally separated in vector space. This property can be used in variety of use-case like finding synonyms, analogies etc.<br><br>

<img src="./images/8. Word Embeddings.png" height="200"></img><br><br>

Below I have mentioned few models related to word-embeddings.

### Word2Vec

Word2Vec is the most popular form of word embeddings. As the name suggests, it transforms words to vectors. The core idea behind word2vec is : <br>
1. Given a word, the model should predict its neighbouring, most likely words that might surround that prime word. This type of model is called *Skip Gram*
2. Given the neighbouring words, the model predicts the prime word. This type of model is called *Continous BOW (C-BOW)*<br>

<img src="./images/10. Word2Vec.png" height="200"></img><br><br>

In the Skip-gram model, you take a word, convert it into one-hot encoded vector, feed it into neural network that is designed to predict the neighbouring words and using the loss function, we optimize the weights while training the model till it learns to predict context words as best as it can.<br>

<img src="./images/9. Skip-gram model.png" height="200"></img><br><br>


### GloVe

GloVe : Global vectors for word representation is another form of word embeddings that tries to directly optimize vector representation of each word using co-occurance probabilities.<br>

First, we compute the probability that the word *j* appears in the context of word *i* is computed i.e. `P (j|i)`. This probability is computed for all words in a given corpus. This means we need to compute probability that word *j* either appears next to word *i* or is a few words away from *i*. After calculating the probabilities, we initialize 2 random vectors : one for the word when it is acting as *Context* & one, when it is acting as *Target*.<br><br>

For any given vector *i, j*, we want the *dot product of their word vectors* to be equal to their *co-occurance probability*. The resultant vector should be a set of vectors that capture the similarity and difference between individual words.<br><br>


<img src="./images/12. Dot product.png" height="200"></img><br><br>

Consider the below example of *2 context words : ice and steam* v/s *2 Target words : solid and water.*  The target word *solid* would come across context word *ice* more often than *steam*, but, the *target term water* can come across *ice and steam equally likely* and this is exactly what co-occurance probability reflects.<br><br> 

 <img src="./images/11. Co-occurance probability.png" height="200"></img><br><br>








