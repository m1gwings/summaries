---
marp: true
theme: summary
math: mathjax
---
# Sequence classifiers and labelers

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

Most of the approaches that we have tackled in the "_Text classification_" and "_Searching text_" summary completely disregard word order. $n$-grams can be used to capture word order information, but, as we already remarked, they don't scale well. **Word order** is super important for interpreting the meaning of the text and for classifying it. For this reason we need to study models which can handle inputs which are sequences of objects. In the particular case of text: sequences of words.
We focus on two **learning tasks**:
- **Sequence classification**: the input is an **ordered sequence** of tokens $(w_1, w_2, \dots, w_n)$ and the output is a single prediction $y$.
- **Sequence labelling**: the input is again an **ordered sequence** of tokens $(w_1, w_2, \dots, w_n)$ and the output is a sequence of predictions $(y_1, y_2, \dots, y_n)$. Observe that in general, the prediction $y_i$ depends on the **whole** input sequence, and not necessarily just on $w_i$ or $(w_1, w_2, \dots, w_i)$.

## Sequence labelling

Traditional methods for sequence labelling make use of either:
- **Hidden Markov Models** (HMMs) ($\approx$ Naive Bayes applied to sequences) in which there is a set of unobserved states of the system, in each state the system has a certain probability distribution over the observed words that it produces.
- **Conditional Random Fields** (CRFs) ($\approx$ Logistic Regression applied to sequences) in which transition and emission probabilities are replaced with **undirected potentials** $\phi(t_1, t_2)$ and $\phi(t_1, w_1)$.

Recent methods make use of **Recurrent Neural Networks** [_see AN2DL summaries_]. RNNs allow to **aggregate information** over a document while **not ignoring** word order. They provide a general way to **accumulate information** by combining the **embedding** of a current word with the **context** from the previous words. They are simply models which take 2 vectors as input (the current input and the previous state), and produce 2 vectors as output (the current output and the updated state). They can be used to process **arbitrarily long** input contexts.
**Long Short-Term Memory** (**LSTM**) are a clever implementation of RNNs [_see AN2DL summaries_].

---

## Applications of sequence classifiers and labellers

### Part-of-speech (POS) tagging

Each word in a sentence belongs to a certain **part of speech**: nouns, verbs, pronouns, prepositions, adverbs, conjunctions, participles, articles.
**POS tagging** is the task of assigning a part-of-speech label to each token in a sequence. This task is useful for developing features for certain tasks, it can reduce ambiguity in the bag-of-words representation by differentiating the words which are the same but belong to different parts of speech. It is also useful as an initial step for other NLP tasks.

### Named-Entity Recognition (NER)

**Named-Entity Recognition** is the task of identifying entities that are mentioned in a text. It can be treated as a sequence labelling task. It is often the first step in extracting knowledge from text. A **named entity** is an object in the real world. The most common tags are:
- **PER** (Person);
- **LOC** (Location);
- **ORG** (Organization);
- **GPE** (Geo-Political Entity).

Often, an entity is constituted of more than a word. The NER task is to find spans in text that constitute proper names and tag the type of entity.

Traditionally, NER is performed for:
- **Sentiment analysis**: identify sentiment towards particular company or person.
- **Information extraction**: extracting facts about entities from text.
- **Question answering**: answer questions about an entity.
- **De-identification**: remove references to individual from text to protect privacy.

NER can be hard because of:
- **Segmentation**: conversely to what happens in POS tagging where each word gets a tag, in NER entities can be phrases.
- **Type ambiguity**: the same word/phrase can have many types depending on the context.

The segmentation problem is solved through **BIO tagging**: we use a **B** tag for the token that **begins** a span, a **I** tag for a token inside a span, and a **O** tag for tokens outside a span. In particular, there is a different B and I tags for each kind of entity (e.g. B-PER, I-PER, B-LOC, I-LOC, ...).

---

### Entity linkage

Determining that a named-entity has been mentioned in text is only the first part of the problem. We still need to determine which **real-world entity** was referred to. For example, we may want to link a word/phrase representing a real-world entity to its Wikipedia page. In general we need a Knowledge Base with all the real-world entities we wish to link. This task is harder than it seems.

### Relation extraction

Once entity mentions have been linked to unique entities, **relationships between entities** can be mined and used to populate a knowledge graph. This is handled as a problem of predicting **missing links** ina graph. Entity embeddings can be leveraged for this purpose.

### Parse trees

**Parse trees** (also referred to as **syntax parse trees** or **dependency parse trees**) result from applying a **formal grammar** to analyze a sentence. Formal grammars define set of **rules** for **generating valid text**. Given a piece of text, we can reverse the process (i.e., **parse** the text) to determine which rules have been applied, and in which order, to create it. The recursive application of rules results in a tree structure for each sentence. Parse trees tell us how the words in a sentence **relate to one another**, from which we can try to **deduce the intended meaning**. In theory, there is no need of Machine Learning for parsing text, but in practice formal grammars are brittle and natural language can be ambiguous, so we need to use ML to extract parse tree.

### Co-reference resolution

**Co-reference resolution** is the problem of determining **who** or **what** is being referenced across (or sometimes within) sentences, e.g. through pronouns.
Most times the pronoun comes after the referent, but sometimes the opposite is true.
Resolving co-references to entities from earlier/later in the text helps understanding what is being said about those entities.

### Taxonomies and ontologies

A **taxonomy** is a hierarchy of concepts (e.g. types of products with is-a or part-of relationships). An **ontology** is a formal definition of concepts that does not depend on the language.
Most ontologies are composed of:
- **Classes**: a set of objects/a type.
- **Individuals**: an object.
- **Attributes**: a property with a primitive data type, allowing for restrictions on values.
- **Relationships**: the characterization of relationships among classes or individuals.
- **Logical rules**.

---

The relationships between concepts in an ontology form a graph.
