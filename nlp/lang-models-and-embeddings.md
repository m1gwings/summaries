---
marp: true
theme: summary
math: mathjax
---
# Language models and embeddings

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

A statistical **language model** is a **probability distribution** over **sequences of words**. If we have a distribution over sequences of words, we can **condition** the next word on previous words and **sample new sequences** from it. In other words, **language models** are general-purpose **text generators**.

Language models discover **statistical regularities** in text and use them to predict the next word.

## Markov Models

An approach to build language models is to use markov models. Markov Models solve the following issue: natural language utterance can be of **arbitrary length** but the model is constrained to have a finite number of parameters. The idea of Markov Models is to learn a model which predict the next word given a <u>fixed number</u> of previous words.
The simplest models count **$n$-grams** (ordered sequences of $n$ words) in large corpus. The conditional probability can be estimated from the counts:
$$
\mathbb{P}[\text{croquet} \ | \ \text{play}] = \frac{\mathbb{N}[\text{play croquet}]}{\mathbb{N}[\text{play}]}.
$$
Longer $n$-grams give better predictions.

To **prevent zero probabilities** for $n$-grams which were not present in the training corpus there are different techniques.
- **Smoothing**: it consists in adding a small constant to all counts before estimating the probabilities:
$$
\mathbb{P}[w_n \ | \ w_{n-1}, w_{n-2}] = \frac{\mathbb{N}[w_{n-2} w_{n-1} w_{n}] + \alpha}{\mathbb{N}[w_{n-2} w_{n-1}] + V \alpha}
$$
> where $\alpha$ is a _pseudocount_ (often $\alpha = 1$) and $V$ is the vocab size.

- **Backoff**: it consists in just backing off to $(n-1)$-gram for unseen $n$-grams.

- **Interpolation**: it consists in interpolating between higher and lower order (higher and lower order refer to the $n$ value for the considered $n$-grams) models. The interpolation coefficients can be learned on a validation set.

---

### Generating text from a Markov Model

There different ways of using th estimate of the next word probability to generate text.
- **Greedy**: it consists in choosing the most probable term:
$$
w^* = w_1 \dots w_n t^* \text{, where } t^* \in \arg\max \mathbb{P}[w_n = t \ | \ w_1 \dots w_{n-1}].
$$
- **Random sampling**: it samples the next word according to the estimated probabilities.
- **Top-$k$ sampling**: it limits the sampling the the $k$ most likely terms.
- **Temperature search**: it limits the sampling to likely terms by raising the probabilities to the power $1/T$ where $T$ is a parameter known as temperature (higher temperature corresponds to more uniform sampling).
- **Beam search**: we search forward one step at a time for most likely sequences while limiting the search space to a maximum set of $k$ candidate sequences.

## Evaluating language models

There are two kinds of **evaluation of language models**.
In **extrinsic** evaluation you use a model in a downstream task (e.g. as a spelling corrector) and evaluate the performance on that task.
In **intrinsic** evaluation you train the parameters of the mode on a training set and test the model performance on held-out dataset. You use the likelihood that the model would produce the new data to evaluate how well it is doing.

### Intrinsic evaluation

An intrinsic evaluation metric for language models is **perplexity**. The perplexity of a language model quantifies the level of **surprise**/**confusion** at seeing new text. In particular, it measures how unlikely the observed data is under the model.
It is computed as follows:
1. Compute the probability of the observed sequence under the model:
$$
\mathbb{P}[w_1 w_2 \dots w_n] = \mathbb{P}[w_1] \mathbb{P}[w_2 \ | \ w_1] \mathbb{P}[w_3 \ | \ w_2] \dots \mathbb{P}[w_n \ | w_{n_1}] \text{ (in a bigram model)}.
$$
2. Normalize the probability for the length of the text sequence:
$$
\mathbb{P}[w_1 w_2 \dots w_n]^{\frac{1}{n}}.
$$
3. Invert the probability to compute the uncertainty:
$$
PP(\mathbf{w}) = \mathbb{P}[\mathbf{w}]^{-\frac{1}{n}}.
$$

Minimizing the perplexity is the same as maximizing the probability. Thus a lower perplexity means having a better model.

---

Perplexity is strongly related to other measures often used in training. Indeed:
$$
PP(\mathbf{w}) = 2^{\text{nLL}(\mathbf{w})}
$$
where $\text{nLL}$ is the **negative per-word log likelihood** of the sequence.

## Word Embeddings

Markov Models have some problems. When $n$ gets larger, the chance of finding a certain sequence in a corpus drops exponentially. This means that there is almost never enough training data. At the same time, continuously backing off to shorter $n$-grams greatly limits the power of the model. Indeed, in order to generate reasonable language, it is necessary to model **very long distance dependencies**. Memory and data requirements of Markov models scale exponentially in length of observable dependency. We need a method that can both **generalize** from limited data and handle **longer dependencies**.

The solution to this scaling problem is provided by **word embeddings**. Word embeddings are dense vectors representing words in a high dimensional space, which typically has between 100 and 1000 dimensions. They are very low dimensional if compared to **one-hot encoding** of terms, since typical document collection have vocabularies of $100 \ k$ to $1 \ M$ tokens.
Just like one-hot encoding, word embeddings can be **aggregated** to represent sentences and documents.
Embeddings are produced by **supervised machine learning models**. In particular, by models trained to **predict missing word** based on the **surrounding context**. In causal models, the context includes only the previous words. In non-causal models, it includes also future words.
The supervised learning problem is framed as follows. The features are the words in the current context. The target is the missing word from the sequence.
On this task, a standard **linear classifier** would require a **very large number of parameters** (the square of the vocabulary size).

### Word2Vec

**Word2Vec** is one of the most popular models to produce embeddings. It solved the parameter space issue by using bag-of-words representation and a neural netwrok with a single linear hidden layer (to reduce the number of parameters). The hidden layer is a lowe dimensional layer which provides distributed representation of context words. The weights from the input to the hidden layer are the same (transposed) from the hidden layer to the output. There are two versions of Word2Vec.
- The **Continuous Bag of Words** (CBOW) model is trained to predicted the observed word based on all surrounding context words. The context consists of all terms occurring in **symmetric window** around the target term.
- The **Skip-gram** model is trained to predict the observed word given a single context word.

So skip-gram is just 1-to-1 prediction, while CBOW is many-to-1 prediction.

---

Word embeddings can be seen as a form of **matrix decomposition**. Consider a square count matrix with dimension vocabulary size $\times$ vocabulary size which contains the number of word co-occurrences in text withing a fixed-size context window. Factorizing generalizes the information in those windows and produces word embeddings vectors.

To reduce computational complexity, the skip gram version was simplified into a binary classification model in which the model was given word pairs and had to predict if they belonged to the corpus or were _negative examples_ which were added artificially.

### GloVe

An alternative technique for embedding if **GloVe**. The aim is to give a probabilistic interpretation to translation in embedding space. For example, the translation in space from "steam" to "ice" should increase the chance of seeing the word "solid". So, the projection of "ice" minus "steam" onto the vector "solid" should be function of conditional probabilities:
$$
(\mathbf{w}_\text{ice} - \mathbf{w}_\text{steam})^T \widetilde{\mathbf{w}}_\text{solid} \approx f\left( \frac{\mathbb{P}[\text{solid} \ | \ \text{ice}]}{\mathbb{P}[\text{solid} \ | \ \text{steam}]} \right).
$$
This can be achieved by fitting the following objective:
$$
\mathbf{w}_i^T \widetilde{\mathbf{w}}_k + b_i + \widetilde{b}_k = \log(X_{ik})
$$
where $\mathbf{w}_i$ and $\widetilde{\mathbf{w}}_k$ are the embedding vectors, $b_i$ and $b_k$ are the biases, and $X_{ik}$ is their co-occurrence count.
The objective is approximated by minimizing a weighted least squares objective, with some ticks needed for convergence.

### Properties of word embeddings

Word embeddings have many **interesting properties**.

- **Semantic clustering**: neighbors in the embedding space are **semantically related** to one another.

- **Translation is meaningful**: certain directions in the space have meaning, which means that **semantics** is often **additive** and **analogies** are encoded in the embedding (e.g. _man_ is to _woman_ as _king_ is to _queen_).

- **Discovery of all sorts of relationships between words**: including part-of-speech (e.g. help → helpful, pain → painful), type-of relationships (e.g. red, green, blue → colors), synonyms (e.g. brave $\approx$ courageous), geographic (e.g. Chicago + state → Illinois).

---

### Uses of word embeddings

The low-dimensional representation provided by word-embeddings causes similar terms to share similar descriptions and allows a model to **generalize** from semantically related **examples**.

Since embeddings place similar concepts close together, they are useful for discovering implied (but unknown) properties of them.

### Sub-word embeddings

Word embeddings work well if the vocabulary is fixed: they cannot deal with new words in the test set.
If we see a new word: e.g. a made-up word like **hippopotamification** (the act of magically turning someone into a hippopotamus), we don't have an embedding for it and we must ignore it despite the fact that we can guess its meaning from the letters contained in it.

**Fasttext** has been introduced to solve this problem. Words are split into fixed-length character sequences. It learns embeddings for character $n$-grams and combines the embeddings to form words. This approach deals nicely with morphologically related terms.
