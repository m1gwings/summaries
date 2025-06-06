---
marp: true
theme: summary
math: mathjax
---
# Applications of transformers

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

We ca distinguish between 3 main architectures for transformers.
- **Encoder-decoder models**: they include the original transformer architecture, which was designed for translation, but also the T5 (Text-to-Text Transfer Transformer) model from 2019. It is useful it the input and output text have **different vocabularies**.

- **Encoder-only models**: they are pre-trained as noisy **auto-encoders** to recover **masked input**. They are great for **representing text**. An example is **BERT**.

- **Decoder-only models**: they are pre-trained as **auto-regressive** models to **predict the next token**. They are great for **generating text**. An example is **GPT-2**.

## Fine-tuning transformers

It is possible to fine-tune the transformer architectures to learn specific tasks.
A recent approach involves fine-tuning a single model to perform multiple tasks: researchers have found that multi-task model often **outperformed** task specific models on their task of specialty. This is known as **instruction tuning**.

## Further uses

- **Sentence BERT** (**SBER**) allows to compute the relevance of a document for a given query by extracting the semantic of both and calculating their similarity.

- **Vector databases** index objects (texts or images) based on their embedding. They provide a **fast nearest neighbor search** in embedding space.

- **Contrastive Language-Image Pre-training** (**CLIP**) allows to align the embedding spaces generated from text and images, using contrastive learning.

## Zero, One and Few-shot Learning

Language models are **universal learners** that can be used **even without fine-tuning**. You just need to describe the task that the model needs to perform: this is known as **zero-shot learning**. In addition, you can provide a **few examples**: this is known as **few-shot learning**.
This is possible since the model has seen lots of examples of few-shot learning during pre-training.
