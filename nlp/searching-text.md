---
marp: true
theme: summary
math: mathjax
---
# Searching text

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

## Information retrieval

**Information retrieval** is the _task_ of **finding content**, which could be documents, images, videos, etc., that is useful (i.e. relevant) to user's **information need**.
In order to do so, a usual approach involves extracting **query keywords** from **information needs** and then look for documents containing those keywords.
Anyway, it can happen for example that **no document** contains all query terms or **many documents** contain all of them. The problem is addressed by _assigning score_ to keyboards based on how discriminative they are or by _expanding document representation_ to include more information (e.g. page importance) and train a **ML model**.

### Retrieval as text classification

A naive approach would be to treat retrieval as text classification. We train a model which takes in input the bag-of-words of the document and the query and predicts the probability that the document is relevant to the given query. Of course such model should be non-linear since we need to consider the interaction between the query and the document. An example could be a non-linear model that includes pairwise interactions between query and document terms. The issue is that, in this way, the number of parameters explode very quickly.

### Retrieval as term weighting

#### TF-IDF

A popular approach in information retrieval is **Inverse Document Frequency** (**IDF**) weighting. It ranks documents according to the inverse probability that they contain the query terms by chance. In particular, consider the query $\mathbf{q} = \{ t_1, \dots, t_Q \}$. Let $\text{df}_t$ be the number of documents in the corpus which contain term $t$. Then, assuming independent terms, the probability that a document $\mathbf{d}$ contains a subset of the terms in the query $\mathbf{s} = \{ t_{i_1}, \dots, t_{i_S} \} \subseteq \mathbf{q}$ with $1 \leq S \leq Q$, $1 \leq i_1 < \dots < i_S \leq Q$ by chance is:
$$
\mathbb{P}[\mathbf{s} \subseteq \mathbf{d}] = \prod_{j=1}^S \mathbb{P}[t_{i_j} \in \mathbf{d}] = \prod_{j=1}^S \frac{\text{df}_{t_{i_j}}}{N}
$$
where $N$ is the number of documents in the corpus.
Finally we take minus the logarithm of such quantity, to make the score additive:

---

$$
\text{score}(\mathbf{d}) = - \log \prod_{j=1}^S \frac{\text{df}_{t_{i_j}}}{N} = \sum_{j=1}^S \log \frac{N}{\text{df}_{t_{i_j}}}
$$
where we choose $\mathbf{s} = \mathbf{q} \cap \mathbf{d}$.

Minus the logarithm of the probability is a standard information theory measure for the information gained from observing a term. Intuitively, the amount of information should be proportional to the surprise at observing a term.

Instead of the probability, sometimes the **odds** of observing a term are used:
$$
\text{odds}(t) = \frac{\mathbb{P}(t)}{1-\mathbb{P}(t)} = \frac{\text{df}_t}{N} \frac{N}{N-\text{df}_t} = \frac{\text{df}_t}{N-\text{df}_t}.
$$
The resulting document score (with the addition of smoothing of $0.5$ to prevent terms with small frequencies from dominating the ranking):
$$
\text{score}(d) = \sum_{t \in \mathbf{q} \cap \mathbf{s}} \log \frac{N-\text{df}_t+\frac{1}{2}}{\text{df}_t + \frac{1}{2}}.
$$

Using just IDF as a score disregards the number of times a term appears in a document. This information could be useful to understand the relevance of the document to the query. This problem is solved with the **TF-IDF** score. Let $\text{tf}_{t,\mathbf{d}}$ be the number of times term $t$ appears in document $\mathbf{d}$. The new score is:
$$
\text{score}(\mathbf{q}, \mathbf{d}) = \sum_{t \in \mathbf{q} \cap \mathbf{d}} \text{tf}_{t,\mathbf{d}} \log \frac{N}{\text{df}_t}.
$$

TF-IDF works well in practice, but it has the issue that the score increases linearly with the number of occurrences of a term. Researchers have questioned this property. Common alternatives (with little theoretical justification :( ) are:
- $\log(1+\text{tf}_{t,\mathbf{d}})$;
- $\max(0, 1+\log(\text{tf}_{t, \mathbf{d}}))$.

#### Length normalization

Longer documents have a larger vocabulary, so it is more likely that they contain the query terms, but they could be not useful to the searcher. For this reason shorter documents with the same term count should be preferred.
To account for this problem it is possible to normalize for the length.

The Vector Space Model treats TF-IDF values for all terms in a document as a vector representation:
$$
\mathbf{d} = (\text{tf}_{1,\mathbf{d}} \cdot \text{idf}_1, \dots, \text{tf}_{n,\mathbf{d}} \cdot \text{idf}_n).
$$

---

The **similarity** between the query and the document is computed based on the **angle between vectors**. Actually, the cosine of the angle is used (since it gives similarity in the range $[0, 1]$):
$$
\text{sim}(\mathbf{q}, \mathbf{d}) = \frac{\mathbf{q} \cdot \mathbf{d}}{||\mathbf{q}|| ||\mathbf{d}||}.
$$

Other kinds of length normalization have been studied.
An example is **Pivoted Length Normalization** (**PLN**). The idea is that generally longer documents do contain more information than shorter ones, but normalizing loses all length information. So instead you can parameterize the $L_1$ normalization around the average document length:
$$
\frac{\text{tf}_{t, \mathbf{d}}}{L_\mathbf{d}} \rightarrow \frac{\text{tf}_{t,\mathbf{d}}}{b L_\mathbf{d} + (1-b) L_{\text{ave}}}
$$
where:
- $L_\mathbf{d} = \sum_t \text{tf}_{t, \mathbf{d}}$ (_this is simply the length of the document_);
- $L_{\text{ave}} = \frac{1}{N} \sum_{\mathbf{d}} L_{\mathbf{d}}$;
- $0 \leq b \leq 1$.

Pivoted Length Normalization leads to the famous **Okapi BM25 ranking formula**:
$$
\text{RSV}_{\mathbf{d}} = \sum_{t \in \mathbf{q}} \log \left[ \frac{N}{\text{df}_t} \right] \cdot \frac{(k_1+1) \text{tf}_{t, \mathbf{d}}}{k_1 ((1-b) + b (L_{\mathbf{d}}/L_{\text{ave}})) + \text{tf}_{t, \mathbf{d}}}
$$
where $k_1$ and $b$ are parameters to be set (the default values are $k_1 \in [1.2, 2]$ and $b = 0.75$, but often these are tuned on a validation set).

## Index Structures

Retrieval measures must be calculated fast, since delay affects attention. Search engines need to respond in tenths of a second and have been engineered to be as fast as possible.

**Inverted Indices** are the building blocks of search engines. THey are made up of **posting lists** mapping term IDs to document IDs. They use integer compression algorithms that allow for fast decompression to reduce space requirement.

Calculating the retrieval function involves computing joins over posting lists. Documents in posting lists are sorted by term count to allow for early termination of results list computation. Index pruning techniques are used to get rid of documents that would never be retrieved for a certain query.

### Positional indices

Documents are more likely to be relevant if query terms appear close together. Most indices record locations of terms in a document and allow for proximity between keywords to be calculated.

---

## Re-ranking

The idea behind **re-ranking** is the following: once an initial set of potentially relevant documents has been, found, why not re-rank them based on all available information in order to improve the overall quality of search results?

For **web search**, many indicative features include:
- multiple **retrieval functions** (BM25, Embedding-based, BERT, ...);
- different **document parts/views** (titles, anchor-text, bookmarks, ...);
- **query-independent** features (PageRank, HITS, spam scores, ...);
- **personalized** information (user click history, ...);
- **context** features (location, time, previous query in session, ...).

Search engines like Google combine **hundreds of signals** together.

**Rank learning** provides an automated and coherent method for combining diverse signals into a single retrieval score while optimizing a **measure users care about**.
In order to do rank learning, we need ground truth data regarding the relevance of a document for a search. Search engines employ people to annotate search results with relevance information. Of course it is not possible to train models directly from click data, since it would create a feedback loop. The latest approaches include using an LLM to judge relevance.

The problem can be framed as a **simple regression problem**: predict the relevance label of the document based on feature values. It is usual to employ list wise losses which consider the predicted order for the documents more than the predicted labels by themselves.

---

## Evaluating search results

The traditional measures to evaluate search results include:
- **precision at depth $k$**: $P @ k = \# \{ \text{relevant docs in top } k \}/k$;
- **recall at depth $k$**: $R @ k = \# \{ \text{relevant docs in top } k \}/\# \{ \text{relevant docs} \}$;
- **$F$-measure at depth $k$**: the harmonic mean of the two previous quantities.

More recent metrics include:
- **Mean Average Position** (**MAP**) (_see Recommender Systems notes_):
$$
\text{AveP} = \frac{\sum_{k=1}^n P@k \times \text{rel}(k)}{\# \{ \text{relevant documents} \}};
$$
- **Normalized Discounted Cumulative Gain** (**NDCG@$k$**):
$$
\text{NDCG}(Q, k) = \frac{1}{|Q|} \sum_{j=1}^{|Q|} Z_{kj} \sum_{m=1}^k \frac{2^{R(j,m)}-1}{\log_2(1+m)}.
$$
