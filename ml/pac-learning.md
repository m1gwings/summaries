---
marp: true
theme: summary
math: mathjax
---
# PAC learning

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Marcello Restelli_)

</div>

Let's (_re-_)state two remarks that will allow us to introduce the following chapter.
- Over-fitting happens because the training error is a **bad estimate** of the generalization error.
- Since over-fitting is linked to the variance of the model, we know that we can alleviate the problem by increasing the number of samples.

These observations lead to two natural questions:
- Can we infer something about the generalization error from the training error?
- Can we estimate how many samples are enough to achieve a "small" generalization error?

We will try to answer in a simplified setting: "noiseless" binary classification (the results can be generalized).
Let:
- $X$ be the set of **instances** (_the objects in our world which we want to classify_);
- $H$ be the set of **hypotheses**;
- $C \subseteq \{ 0, 1 \}^X$ the set of possible **concepts** to learn;
- $\mathcal{P}$ be the unknown probability distribution defined over $X$ which describes the sampling process;
- $c \in C$ be the **true concept** that we want to learn;
- $\mathcal{D} = \{ (x_1, c(x_1)), \ldots, (x_N, c(x_N)) \}$ where $x_1, \ldots, x_N \sim_\text{i.i.d} \mathcal{P}$ be a **dataset** (_we assume that $N$ is fixed_).

The "teacher" provides a dataset $\mathcal{D}_\text{train} = \{ (x_{\text{train},1}, c(x_{\text{train},1})), \ldots, (x_{\text{train},N}, c(x_{\text{train},N})) \}$. Observe that there is no noise in the target, we know the true class of each sample.
The learner must output an hypothesis $\hat{h}_{\mathcal{D}_\text{train}} \in H$ which estimates $c$.
$\hat{h}_{\mathcal{D}_\text{train}}$ is **evaluated** by its performance on **subsequent instances** drawn according to $\mathcal{P}$. In particular, we define:
$$
L_\text{true}(h) = \mathbb{P}_{x \sim \mathcal{P}}[c(x) \neq h(x)]
$$
for every $h \in H$.
While:
$$
L_\mathcal{D}(h) = \frac{1}{N} \sum_{n=1}^N \mathbb{1}[c(x_n) \neq h(x_n)]
$$
for every $h \in H$,  dataset $\mathcal{D}$.

---

Observe that, <u>if $h$ doesn't depend on $\mathcal{D}$</u>, then $L_\mathcal{D}$ is an unbiased estimate of the true loss:
$$
\mathbb{E}_\mathcal{D}[L_\mathcal{D}(h)] = \mathbb{E}_\mathcal{D}\left[\frac{1}{N} \sum_{n=1}^N \mathbb{1}[c(x_n) \neq h(x_n)] \right] = \frac{1}{N} \sum_{n=1}^N \mathbb{E}_\mathcal{D}\left[ \mathbb{1}[c(x_n) \neq h(x_n)] \right] =
$$
$$
= \frac{1}{N} \sum_{n=1}^N \left[ 1 \cdot \mathbb{P}_{x \sim \mathcal{P}}(c(x) \neq h(x)) + 0 \cdot \mathbb{P}_{x \sim \mathcal{P}}(c(x) = h(x)) \right] = L_\text{true}(h).
$$

Unfortunately, our learner produces the hypothesis $\hat{h}_{\mathcal{D}_\text{train}}$ by minimizing $L_\text{train} = L_{\mathcal{D}_\text{train}}$ (_which implies that $\hat{h}_{\mathcal{D}_\text{train}}$ depends on $\mathcal{D}_\text{train}$_), hence it **DOESN'T HOLD ANYMORE IN GENERAL** that:
$$
\mathbb{E}_{\mathcal{D}_\text{train}} \left[ \mathbb{1}[c(x_{\text{train},n}) \neq \hat{h}_{\mathcal{D}_\text{train}}(x_{\text{train},n})] \right] = 1 \cdot \mathbb{P}_{x \sim \mathcal{P}}(c(x) \neq \hat{h}_{\mathcal{D}_\text{train}}(x)) + 0 \cdot \mathbb{P}_{x \sim \mathcal{P}}(c(x) = \hat{h}_{\mathcal{D}_\text{train}}(x))
$$
since the value of $\mathbb{1}[c(x_{\text{train},n}) \neq \hat{h}_{\mathcal{D}_\text{train}}(x_{\text{train},n})]$ depends on the whole training set $\mathcal{D}_\text{train}$, instead of depending just on the $n$-th sample of the dataset as it happened before.

Never the less, if we have test set $\mathcal{D}_\text{test}$ independent from $\mathcal{D}_\text{train}$, then, as we already remarked many times, $L_\text{test}(\hat{h}_{\mathcal{D}_\text{train}}) = L_{\mathcal{D}_\text{test}}(\hat{h}_{\mathcal{D}_\text{train}})$ is an unbiased estimate of $L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}})$. That is, if we fix $\mathcal{D}_\text{train}$:
$$
\mathbb{E}_{\mathcal{D}_\text{test}}[L_\text{test}(\hat{h}_{\mathcal{D}_\text{train}})] = L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}).
$$

Answering the first of our questions consists in finding an upper bound to:
$$
L_\text{true}[\hat{h}_{\mathcal{D}_\text{train}}] - L_\text{train}[\hat{h}_{\mathcal{D}_\text{train}}].
$$

We will answer first in a special case.

- We call **version space** the set of **consistent hypotheses**, that is:
$$
\text{VS}_{H,\mathcal{D}_\text{train}} = \{ h \in H | L_\text{train}(h) = 0 \}
.$$

- **Theorem**: if the hypothesis space $H$ is finite ($|H| < +\infty$) and $\mathcal{D}_\text{train}$ is a sequence of $N \geq 1$ independent random example sof some target concept $c$, then for any $0 \leq \epsilon \leq 1$, the probability that $\text{VS}_{H,\mathcal{D}_\text{train}}$ contains a hypothesis error greater than $\epsilon$ is less than $|H|e^{-\epsilon N}$:
$$
\mathbb{P}_{\mathcal{D}_\text{train}}(\exists h \in \text{VS}_{H,\mathcal{D}_\text{train}} | L_\text{true}(h) \geq \epsilon) \leq |H|e^{-\epsilon N}.
$$

> **Proof**:
> Let $H_\text{bad} = \{ h_{\text{bad},1}, \ldots, h_{\text{bad},|H_\text{bad}|} \} = \{ h \in H | L_\text{true}(h) \geq \epsilon \}$. Observe that $L_\text{true}(h) \geq \epsilon$ is either true or false, independently from $\mathcal{D}_\text{train}$. Then:
$$
\mathbb{P}_{\mathcal{D}_\text{train}}(\exists h \in \text{VS}_{H,\mathcal{D}_\text{train}} | L_\text{true}(h) \geq \epsilon) = \mathbb{P}_{\mathcal{D}_\text{train}}((L_\text{train}(h_1) = 0 \land L_\text{true}(h_1) \geq \epsilon) \lor \ldots
$$

$$
\ldots \lor (L_\text{train}(h_|H|) = 0 \land L_\text{true}(h_|H|) \geq \epsilon))  =  \mathbb{P}_{\mathcal{D}_\text{train}}(L_\text{train}(h_{\text{bad},1}) = 0 \lor \ldots \lor L_\text{train}(h_{\text{bad},|H_\text{bad}|}) = 0) \leq
$$

---

$$
\leq 
$$