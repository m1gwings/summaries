---
marp: true
theme: summary
math: mathjax
---
# Sequence2Sequence models and transformers

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

**Sequence to sequence** (**seq2seq**) models take sequences in input and produce sequences in output. They are used in tasks like **translation**, **summarization**, and **dialog systems**. Many (if not all) tasks in NLP (and not only), can be posed as seq2seq problems.

## Encoder-decoder architecture

A typical seq2seq task is **translation**. Translation models are realized through LSTMs by training two different networks: an **encoder** and a **decoder**. The encoder reads in the input text and generates a representation for the sequence; the decoder takes the output of the encoder and serializes it, by generating one word at a time.

### Attention

An issue with the standard encoder-decoder architecture is that sometimes the information in the input sequence is too much to be compressed successfully by the encoder. **Attention** tries to solve this problem. It enables models to concentrate processing on specific regions of the input text when making predictions.
The idea is to make the encoded input (at each step) available to the decoder, providing a direct route for the information to flow from the input to the output. One may ask why not directly mapping input words to output words. Across languages, different number of tokens are required to describe the same concept and many times different word order is often used. Indeed, generating the right output word, often requires knowing more than just the current word in input: it can require the knowledge of a future word in the sentence. We need a compact representation of concepts which is extracted by the encoder. What information flows into the decoder is controlled by the previous state of the decoder. In particular, similarity is computed between the **state of the decoder** and the output of the encoder at each step.
**Soft-attention** produces a **weighted average** over encoder outputs, where the weights are obtained through softmax activation of the similarities.
There are different ways to compute similarity.
- In **additive attention**, similarity is computed by concatenating the decoder state and encoder output ina  feed-forward network.
- In (more common) **multiplicative** attention: the similarity is computed through the **dot product** between the decoder state and the encoder output. The dot product is normalized by the square root of the encoder output size, so that the standard deviation doesn't change.

---

Named $\mathbf{h}_{i-1}$ the state of the decoder at the previous step, $\mathbf{e}_j$ the output of the encoder at the $j$-th step and $d$ the dimension of $\mathbf{e}_j$, multiplicative attention computes:
$$
\mathbf{z}_i = \sum_j \text{softmax}\left( \frac{1}{\sqrt{d}} \left[ \mathbf{h}_{i-1} \mathbf{e}_1 \ \mathbf{h}_{i-1} \mathbf{e}_2 \ \dots  \right]^T \right)_j \mathbf{e}_j.
$$
We can generalize this notation introducing:
- **queries**: what is being looked up;
- **keys**: index of what to find;
- **values**: the information stored at the key.

In this wat, we get:
$$
\mathbf{z}_i = \sum_j \text{softmax}\left( \frac{1}{\sqrt{d}} \left[ \mathbf{q}_{i} \mathbf{k}_1 \ \mathbf{q}_{i} \mathbf{k}_2 \ \dots  \right]^T \right)_j \mathbf{v}_j.
$$
The query, key, and value are usually obtained by linear transformations:
$$
\mathbf{q}_i = W_q \mathbf{h}_{i-1}, \mathbf{k}_j = W_k \mathbf{e}_j, \mathbf{v}_j = W_v \mathbf{e}_j
$$
where $W_q, W_k, W_v \in \mathbb{R}^{d \times d}$.

An hypothetical example could be:
- **query**: I need an adjective that describes a person;
- **key**: I have an adjective that describes people and animals;
- **value**: friendly.

## Transformers

The issue with the encoder-decoder architecture is that each sequence must be processed serially, this can be a significant bottleneck when we want to train our models on long texts. Observe that during training we don't want to use the models in "auto-regressive" mode (as needs to be done during inference where we generate a new token at a time) since all the inputs needed to predict each output token do not depend on previous outputs of the model, being part of the ground truth text. Thus, it would be extremely useful to design an architecture which can produce all the output tokens by processing the inputs in parallel. This is achieved in the **transformer** architecture by removing the recurrent links both from the encoder and the decoder. They just use a NN encoder/decoder without any recurrence.
Anyway this approach causes two problems:
1. What should we use for the query? (_Remember that in the traditional architecture, we transform the decoder state to get a query_).
2. We lose all information about the order of words.

---

The possible solutions are:
1. Use the current output of the encoder as a query (_but what would that even mean?_).
2. Add position information directly to the data provided to the encoder.

This approach is known as **self-attention**: a mechanism for combining word embedding vectors to produce new embedding vectors (here with embedding we refer to the output of the encoder). Each "high-level" embedding is a weighted average of the word embeddings below it. The weights are computed based on the similarity between embeddings in respective positions. Now, all query, key, and values are obtained by linear transformation of the embeddings.

Self-attention models are trained to either:
- **Recover missing words** from the input text based on the surrounding context (_this is known as Masked Language Modelling task_);
- **Predict** the **next word** from **previous words** in text.

In a transformer there are:
- **multiple attention heads** working in parallel;
- **feed-forward network**, with **residual connections** and **normalization**.

The decoder uses encoder-decoder attention on the embeddings processed by multiple layers of self-attention by the encoder; the query for the encoder-decoder attention is again obtained by another pipeline (different from that in the encoder) of self-attention applied to the original sequence.

The **rationale** which motivates self-attention is the following: words take on **different meanings** depending on their context, the attention mechanism allows representations to depend on the surrounding context by learning a weighting function over lower-level embeddings of context terms.

### Transformer block in detail

Let $\mathbf{e}$ be the input to the transformer block. The embedding is first processed by a self-attention layer, producing a residual $\mathbf{z}$. This residual is normalized by a _layer normalization_ component and then added to $\mathbf{e}$. This intermediate result is processed by a FFNN which again computes a residual which is then normalized and added.

The self-attention layers is **multi-headed**: the embedding $\mathbf{e}$ of size $d$ is mapped to $h$ lower dimensional representations, each of size $d/h$. Each reduced embedding is processed in parallel with self-attention with different query, key, and value matrices. Let $\mathbf{e}_{i,k}$ be the reduced embedding of the $i$-th token for the $k$-th self-attention head. First of all we compute the query $\mathbf{q}_{i,k} = W_{q,k} \mathbf{e}_{i,k}$ and key $\mathbf{k}_{i,k} = W_{k,k} \mathbf{e}_{i,k}$ values through matrix multiplication with the query and key matrices.

---

We can arrange these values for all the reduced embeddings in some matrices:
$$
\mathbf{Q}_k = \begin{bmatrix}
\mathbf{q}_{1,k}^T \\
\dots \\
\mathbf{q}_{n,k}^T
\end{bmatrix},
\mathbf{K}^T_k = \begin{bmatrix}
\mathbf{k}_{1,k} & \vdots & \mathbf{k}_{n,k}
\end{bmatrix}.
$$
By taking the product $\mathbf{Q}_k \mathbf{K}_k^T$ we get all the similarities for all tokens, which we can activate row-wise with softmax.
During training we apply masking to all the similarity values above the main diagonal, so that each embedding is processed just with the information of the preceding tokens in the sequence, as it happens in auto-regressive mode. Then we multiply the **attention weights** for the value matrix:
$$
\mathbf{V}_k = \begin{bmatrix}
\mathbf{v}_{1,k}^T \\ 
\dots \\
\mathbf{v}_{n,k}^T
\end{bmatrix}.
$$
Finally we concatenate the values we get for each head and we post-multiply a matrix $\mathbf{W}^O$ to get the desired output dimension.

### Tokenization for transformers

Transformers use sub-word tokens. They learn how to break words into sub-word tokens from the data. They find frequent character sequences by performing byte-pair encoding which iteratively replace the most frequent consecutive characters by new characters. In this wat, common prefixed/suffixes become vocabulary elements.

### Adding positional information

Transformer architecture is symmetric with respect to input features and thus agnostic with respect to their ordering. We need a way to inform the model about the order of words in text. The simplest way to that would be to use a binary encoding of the position. But, since the embedding vector is made of floating point values, it makes more sense to encode the positions using sinusoids.

### BERT vs GPT

There are two famous adaptations of the original transformer architecture.

- **BERT** (Bidirectional Encoder Representations from Transformers) is an auto-encoder which recovers (potentially corrected) the input. It is learnt by **masking** random tokens and recovering them on output. It is great for **representing text**.

- **GPT** (Generative Pre-trained Transformer) is an auto-regressive model which predicts the next token at the top of each column. It is learnt by masking future tokens and is great for generating text.

---

### Sizing

Transformers come in multiple sizes, depending on:
- the number of self-attention layers;
- the size of the embedding used at each layer;
- the number of parallel attention heads.

The typical sizing for BERT models is 110 M parameters for the base model, and 340 M for the large model.
The typical sizing for the GPT-2 models is 1.5 B parameters for a vocabulary of 50257.

More parameters result in better performance, but longer training times, and larger memory requirements.

