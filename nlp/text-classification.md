---
marp: true
theme: summary
math: mathjax
---
# Text classification

<div class="author">

Cristiano Migali

</div>

**Text classification** is the process of _training a model_ to classify _textual_ documents into categories. Text classification is extensively used. Examples of applications are:
- **spam/phishing detection**;
- **authorship identification**;
- **sentiment analysis**;
- ... .

## Text features

When working with classical models, which assume their inputs to live in finite-dimensional vector space, it is necessary to extract **features** from documents which, in principle, can be arbitrarily long. The _features_ are **signals** in the documents that are useful for the classification.

A naive approach, which doesn't rely on meaningful features, would be to cut the documents at fixed lengths and treat them as categorical variables. This approach is of course un-effective due to the sparseness of the samples in the input space, given the average training data size.

The most common classes of features are:
- **syntax-based features**: e.g. the number of capitalized words;
- **part-of-speech based features**: e.g. the number of verbs versus proper nouns,
- **reading-difficulty** based features: e.g. average length of words/sentences;
- **bag-of-words**: represent documents as vectors of words counts.

### Bag-of-words model

The motivation behind the bag-of-words model is that much of the **useful information** for classifying documents is present in the **vocabulary** of the document.
This set of features _throws away all word order information_ but retains critical vocabulary information.

---

## Word frequency
### Statistical laws for term frequencies

There are different _statistical law_ about the frequency of occurrence of terms in documents.

- **Heap's law**: vocabulary grows with approximately the square root of document/collection length:
$$
V(l) \propto l^\beta \text{ with } \beta \approx 0.5.
$$

- **Zip's law**: token's frequency is approximately proportional to the inverse of its rank:
$$
\text{ctf}_{t} \propto 1/\text{rank}(t)^s \text{ with } s \approx 1
$$
> where the **rank** is the position of the term in the ordered list from the most frequent to the least.

Both these laws can be explained with the **random typing model**.
