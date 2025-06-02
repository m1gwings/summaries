---
marp: true
theme: summary
math: mathjax
---
# Introduction to NLP

<div class="author">

Cristiano Migali

</div>

The **goal** of **NLP** is to process natural (human) language.
Human language is:
-  **compositional**: it allows to express thoughts in sentences comprising **subjects**, **verbs**, and **objects**.
It has an endless capacity for generating new sentences;
- **referential**: it allows to express information about objects and their locations/actions;
- **temporal**: it allows to convey temporal information through tenses;
- **varied**: there are thousands of languages spoken around the world.

NLP mainly deals with text data.

Being able to process text is very powerful, since:
- text is **pervasive**: e.g. personal communications, news, finance, law, ... ;
- text is **important**: it can influence public opinion, ... .

Among the most popular tasks in NLP, we find:
- **translation**;
- **summarization**;
- **anonymization** and **synthetic data generation**;
- **question answering**;
- **explanations**.

NLP is **difficult**, since:
- human language is **extremely expressive**: one can quite literally say anything in natural language;
- even _nonsensical statements_ and _logical inconsistencies_ can be expressed in natural language;
- human language can be **highly ambiguous**, but thankfully it is also very **redundant**;
- even **prosody**, i.e. the way somebody pronounces and emphasizes text, can affect the meaning of a sentence.

## History of NLP

The field grew out of Linguistics, Computer Science, Speech Recognition & Psychology.

During the **40s** the development of formal language theory with finite state automata, probabilistic algorithms for speech, and information theory prepared the ground for the development of NLP.

---

From **1957** to **1970**, two **paradigms** were developed:
- the **symbolic** paradigm (_formal language theory_, _AI logic_, ...);
- the **stochastic** paradigm (_Bayesian methods_, ...).

Between **1970** and **1993** there has been the development of finite-state models through empirical approaches. 

Between **1994** and **1999** there has been the decline of the symbolic approach: new approaches relied on heavy use of data-driven methods and on new application areas (the Web).

From **2000** to **2010** empirical approaches became ever more significant, especially with the usage of Machine Learning techniques.

from **2010** to **2018**, ML became the de-facto standard for NLP.
Finally, in **2018**, **transformer architectures** revolutionized the field.

## Preprocessing text

In order to carry out NLP tasks, it is common to pre-process text by performing cleaning activities, such as:
- remove **mark-up** (non-content information);
- **lowercase** the text;
- remove **punctuation**.
And, after tokenization:
- remove **stopwords** (extremely high frequency words);
- remove **low frequency words**;
- perform **stemming** or **lemmatization** to reduce vocabulary size;
- perform **spelling correction**.

### Tokenizing text

Most NLP tasks require **tokenization**, i.e. **segmenting** text into sequences of characters called **tokens**. Usually, it involves splitting sentences into words, although sometimes tokenization happens at character-level. Tokenization often requires language-specific resources, e.g. for Chinese.
One of the simplest approaches is **space-based tokenization**: many languages use spaces between words and it is possible to segment text into tokens based on the white-space characters between words.
Depending on the application, one may want to split **hyphenated words**. Sometimes the converse also happens: the "unit of meaning" is spread over two **non-hyphenated words**. Some languages are highly **agglutinative**, and can build very long and specific content, which might be better to separate out. Furthermore, sometimes it is not possible to blindly remove punctuation (like in Ph.D., ...).

---

Many languages like Chinese, don't use spaces to separate words. It is harder to decide where the token boundaries should be.

An option, other than **white-space segmentation** or **single-character segmentation** is to **use the data** to understand how to tokenize.

With **sub-word tokenization**, words are split in tokens which can consist of more than one character.

### Word normalization

Preprocessing for text classification or retrieval often also requires some form of text normalization, like normalizing word formats or segmenting sentences.

### Case folding

Applications like **web search** often reduce all letters to lower case. This drastically reduces vocabulary size and increases recall. Furthermore, for classification problems, removing case reduces vocabulary and thus the number of parameters that must be learnt and helps the classifier to generalize well from far fewer examples.
Anyway, you can lose important information by removing cases. For example WHO (World Health Organization) vs who.

### Morphology, Lemmatization, and Stemming

The **morpheme** is the smallest linguistic unit that has semantic meaning. For example, unbelievably can be split in the morphemes: un-believe-able-ly.
Morphemes are divided into:
- **root**: the base form (_believe_);
- **affixes**: **prefix** (_un-_), **infix** (_-able-_), and **suffix** (_-ly_).

**Lemmatization** is the process of representing all words as their **lemma**, i.e. their shared **root**. For example:
- _am_, _are_, _is_ $\rightarrow$ _be_;
- _car_, _cars_, _car's_, _cars'_ $\rightarrow$ car.

It requires looking up each word in a **lexicon**. Thus, you need rules for mapping words according to the morphology of langauge, plus mappings for all the irregular words.

**Stemming** is a simple algorithm that reduces terms to stems by removing their affixes:
- no lexicon is needed;
- it is often used in text retrieval to reduce computational requirements.
An example is the Porter Stemming Algorithm (from 1980).

---

### Stopword removal

**Stopwords** are just the most frequent terms in a language.
Removing stopwords can sometimes boost the performance of retrieval/classification models. Most likely it will just reduce the computational/memory burden.

### Regular expressions

**Regular expressions** are **patterns** that allow to search within text documents. Throughout regular expressions, you can find out **whether patten exists** in documents and you can **extract information** from document wherever the pattern occurs.

The simplest pattern is an **exact match**: "abc".

The next simplest pattern is the **choice** between two sequences: "(abc|bdd)".

An important pattern involves a **wildcard symbol** ".": it matches any character (except for the newline character).

Another common pattern involves **square brackets**: it indicates a choice for a single character:
- "[abc]" = "(a|b|c)";
- "[a-z]" = "(a|b|...|z)";
- "[^abc]" = all characters expect those that match "[abc]".

Other special characters can be used in regular expressions:
- "\n" = the newline character;
- "\t" = the tab character;
- "\s" = any whitespace character;
- "\S" = any non-whitespace character;
- "\d" = "[0-9]";
- "\w" = "[a-zA-Z0-9]" = any "word" character.

The real power of regular expression comes from **repetition**. The following patterns, when added to a regular expression, tell us how many times the previous character (or pattern), must be repeated:
- \* = zero or more times,
- \+ = one or more times;
- ? = zero or one times;
- {n} = exactly n times;
- {n,m} = at least n, up to m times. 

---

Regular expressions provide a powerful language for writing rules to extract content from text documents. The advantages of regular-expression based text-extraction are in the simplicity of the approach, and the fact that rules can be made quite precise, to reduce the number of **false positives**.
The limitations are that:
- extraction rules must (usually) be written by hand, which can be difficult;
- some false positives are usually present (e.g. extract the product ID as a phone number);
- often there are many false negatives due to the fact that rules are not general enough;
- it is hard to integrate the knowledge of context. 
