---
marp: true
theme: summary
math: mathjax
---
# Sequential data problems

<div class="author">

Cristiano Migali

</div>

## Introduction

Up to now we've considered only **static models**, i.e. models which take as input a vector $\underline{x} \in \mathbb{R}^n$. In this set of notes we will deal with **sequential data**, i.e. data described as sequences of $\tau$ values $\{ \underline{x}^{(t)} \}_{t=1}^\tau$ where $\underline{x}^{(t)} \in \mathbb{R}^n$ and $\tau$ can verify between samples.

There are different ways to deal with **sequential data**.
In particular we distinguish between:
- **memory-less models**, and
- **models with memory**.

### Memory-less models

In **memory-less models** we use just a **fixed size** portion of the input sequence to make predictions. Usually this portion is taken from the end of the sequence and its size is known as lag.

#### Auto-regressive models

**Auto-regressive** models are memory-less models which, given a sequence in input, try to predict the next value relying only on the last $k$ values of the sequence. The prediction is usually obtained through a linear model which takes as input $\underline{x}^{(\tau-k+1)}, \ldots, \underline{x}^{(\tau)}$.

#### FFNNs

We can use FFNNs as memory-less models. In particular, given an input sequence $\{ \underline{x}^{(t)} \}_{t=1}^\tau$ and the corresponding outputs $\{\underline{y}^{(t)} \}_{t=1}^\tau$ we can feed the last $k$ values of both sequences ($\underline{x}^{(\tau-k+1)}, \ldots, \underline{x}^{(\tau)}, \underline{y}^{(\tau-k+1)}, \ldots, \underline{y}^{(\tau)}$) to a FFNN to predict the next output $\underline{y}^{(\tau+1)}$.

### Models with memory

**Models with memory** rely on an hidden state $\underline{h}^{(t)}$ to compress information regarding the whole sequence $\underline{x}^{(1)}, \ldots, \underline{x}^{(t)}$. The output of the model depends on the hidden state (and, sometimes, on the input). The hidden state is computed recursively through a function which takes as input the current input and the state at the previous step and produces the current state:
$$
\underline{h}^{(t)} = f(\underline{x}^{(t)}, \underline{h}^{(t-1)}).
$$

---

## Types of sequential data problems

There are different kinds of sequential data problems:
- **one to one**: this is a _degenerate case_, the input is fixed-sized and the output is fixed-sized (we're dealing with a static dataset) (e.g. image classification);
- **one to many**: we take a fixed-sized input and produce a sequence in output (e.g. image captioning);
- **many to one**: we take as input a sequence and produce a fixed-sized output (e.g. sentiment analysis);
- **many to many**: we take as input a sequence and produce a sequence as output (e.g. machine translation);
- **many to many, synced**: as the previous one, but each entry of the output sequence is in 1-1 correspondence with one entry of the input sequence.

### Examples

- In **image captioning** we have in input a single image and get a sequence of words which describe it as output. The image has fixed size, but the output has varying length.

- In **sentiment classification/analysis** the input is a sequence of characters or words (e.g. a tweet) which we want to classify into positive or negative sentiment. The input has varying lengths, but the output has a fixed type and size.

- In **language translation**, having some text in a particular language, e.g. English, we wish to translate it in another, e.g. French. Each language has its own semantics and it has varying lengths for the same sentence.

## Sequence-to-sequence problems

**Sequence-to-sequence** problems are often formulated as follows: we're given an input sequence $x_1, \ldots, x_\tau$ and we aim to find an output sequence which maximizes the conditional probability $p(y_1, \ldots, y_n | x_1, \ldots, x_m)$.
In particular:
$$
y^* = \arg \max_y p(y_1, \ldots, y_n | x_1, \ldots, x_m)
$$

### Conditional language models

On special case is **conditional language models** in which the probability of an output sentence is conditioned ona source sentence. We can model each sentence as a sequence of words.

---

We can model **machine translation** under this framework.
In particular we can model the translation of a sentence from a language to another as a conditional probability distribution $p(\{y_i\}|\{x_i\})$ where $\{ x_i \}$ is the sentence to translate as a sequence of words, and $\{ y_i \}$ are the possible translations. The probability $p$ is unknown; in machine translation we try to estimate it through a parametric model:
$$
y = \arg \max_y p(y|x, \theta).
$$
In order to do so we need to answer the following questions.
- **Modeling**: how does the model $p(y|x, \theta)$ look like?
- **Learning**: how do we find the parameters $\theta$?
- **Search**: how do we compute the $\arg \max$?

For sequence-to-sequence modeling, we can exploit the **encoder-decoder architecture**.
The encoder processes the source sentence and produces a compact representation. The decoder takes as input the compact representation and produces a corresponding sentence in the desired language.
The decoder generates the translation one _token_ at the time. Usually it computes the estimated probability of the next token, given the compact representation of the source sentence and the previous generated tokens.
