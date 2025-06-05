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

**Sequence to sequence** (**seq2seq**) models take sequences in input and produce sequences in output. They are used in tasks like **translation**, **summarization**, and **dialog systems**. Many (if not all) the tasks in NLP (and not only), can be posed as seq2seq problems.

## Encoder-decoder architecture

Translation models are realized through LSTMs by training two different networks: an **encoder** and a **decoder**. The encoder reads in the input text and generates a representation for the sequence; the decoder takes the output of the encoder and serializes it, by generating one word at a time.

### Attention

An issue with the standard encoder-decoder architecture is that sometimes the information in the input sequence is too much to be compressed successfully by the encoder. **Attention** tries to solve this problem. It enables models to concentrate processing on specific regions of the input text when making predictions.
The idea is to make the encoded input (at each step) available to the decoder, providing a direct route for the information to flow from the input to the output. One may ask why not directly mapping input words to output words. Across languages, different number of tokens are required to describe the same concept and many times different word order is often used. Indeed, generating the right output word, often requires knowing more than just the current word in input: it can require the knowledge of a future word in the sentence. We need a compact representation of concepts which is extracted by the encoder. What information flows into the decoder is controlled by the previous state of the decoder. In particular, similarity is computed between the **state of the decoder** and the output of the encoder at each step.
**Soft-attention** produces a **weighted average** over encoder outputs, where the weights are obtained through softmax activation of the similarities.
There are different ways to compute similarity.
- In **additive attention**, similarity is computed by concatenating the decoder state and encoder output ina  feed-forward network.
- In (more common) **multiplicative** attention: the similarity is computed through the **dot product** between the decoder state and the encoder output. The dot product is normalized by the square root of the encoder output size, so that the standard deviation doesn't change.

---

Named $\mathbf{h}_{i-1}$ the tate of the decoder at the previous step, $\mathbf{e}_j$ the output of the encoder at the $j$-th step and $d$ the dimension of $\mathbf{e}_j$, multiplicative attention computes:
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
The possible solutions are:
1. Use the current output of the encoder as a query (_but what would that even mean?_).
2. Add position information directly to the data provided to the encoder.

---

This approach is known as **self-attention**: a mechanism for combining word embedding vectors to produce new embedding vectors (here with embedding we refer to the output of the encoder). Each "high-level" embedding is a weighted average of the word embeddings below it. The weights are computed based on the similarity between embeddings in respective positions. Now, all query, key, and values are obtained by linear transformation of the embeddings.

Self-attention models are trained to either:
- **Recover missing words** from the input text based on the surrounding context (_this is known as Masked Language Modelling task_);
- **Predict** the **next word** from **previous words** in text.

In a transformer there are:
- **multiple attention heads** working in parallel;
- **feed-forward network**, with **residual connections** and **normalization**.

The decoder use encoder-decoder attention on the embeddings processed by multiple layers of self-attention, the query for the encoder-decoder attention is again obtained by another pipeline (different from that in the encoder) of self-attention applied to the original sequence.

Resume from motivating self-attention...
