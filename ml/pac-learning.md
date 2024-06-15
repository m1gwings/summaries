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
\leq \sum_{h \in H_\text{bad}} \mathbb{P}_{\mathcal{D}_\text{train}}(L_\text{train}(h) = 0) = \sum_{h \in H_\text{bad}} \prod_{n=1}^N \mathbb{P}_{\mathcal{D}_\text{train}}(c(x_{\text{train},1}) = h(x_{\text{train},1})) = \sum_{h \in H_\text{bad}} (1-L_\text{true}(h))^N \leq
$$

$$
\leq \sum_{h \in H_\text{bad}} (1-\epsilon)^N = |H_\text{bad}|(1-\epsilon)^N \leq |H|(1-\epsilon)^N \leq |H|e^{-\epsilon N}.
$$
> The last inequality follows from the fact that $1-x \leq e^{-x} \forall x \geq 0$, it is easy to verify by studying $e^{-x} - (1-x)$ which has value $0$ in $x=0$ and increases for $x \geq 0$ (check the derivative).

Now, if we assume that, for every training set $\mathcal{D}_\text{train}$, $\hat{h}_{\mathcal{D}_\text{train}} \in \text{VS}_{H,\mathcal{D}_\text{train}}$, then:
$$
\mathbb{P}_{\mathcal{D}_\text{train}}(L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}) \geq \epsilon) \leq \mathbb{P}_{\mathcal{D}_\text{train}}(\exists h \in \text{VS}_{H,\mathcal{D}_\text{train}} | L_\text{true}(h) \geq \epsilon) \leq |H|e^{-\epsilon N}.
$$
Observe that this assumption is very strong combined with the fact that $H$ is finite.

Anyway, we can derive a **Probably Approximately Correct** (**PAC**) bound on the true loss of the learned hypothesis.
We can enforce $\mathbb{P}_{\mathcal{D}_\text{train}}(L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}) \geq \epsilon) \leq \delta$ by setting $|H|e^{-\epsilon N} \leq \delta$. The last inequality can be rearranged.
- Pick $\epsilon$ and $\delta$, and compute $N$:
$$
N \geq \frac{1}{\epsilon}(\ln |H| + \ln(\frac{1}{\delta}));
$$
- Pick $N$ and $\delta$, and compute $\epsilon$:
$$
\epsilon \geq \frac{1}{N} (\ln |H| + \ln(\frac{1}{\delta})).
$$

Observe that the number of $M$-ary boolean functions is $2^{2^M}$ (_this comes from the fact that over a set of N elements we can define 2^N binary functions, and the set of assignments to $M$ propositional symbols has size $2^M$_). So the bounds have an **exponential** dependency on the number of features $M$.

Let's consider an example. Suppose that $H$ contains **conjunctions of constraints** on _up to_ $M$ boolean attributes. Then $|H| = 3^M$ (each attribute can be either taken positive, taken negative, or not taken, independently from the others). How many examples are sufficient to ensure with probability at least $1-\delta$ that every $h$ in $\text{VS}_{H,\mathcal{D}_\text{train}}$ satisfies $L_\text{true}(h) \leq \epsilon$?
$$
N \geq \frac{1}{\epsilon}\left(\ln 3^M + \ln\left(\frac{1}{\delta}\right)\right) =  \frac{1}{\epsilon}\left( M \ln 3 + \ln\left(\frac{1}{\delta}\right) \right).
$$

Let's formalize the definition of **PAC learning**.

- Consider a class $C$ of possible target concepts defined over a set of instances $X$ of length $n$, and learner $L$ using hypothesis space $H$.
$C$ is **PAC-learnable** if there exists an algorithm $L$ such that for every $c \in C$, for any distribution $\mathcal{P}$, for any $\epsilon$ such that $0 \leq \epsilon \leq \frac{1}{2}$, and $\delta$ such that $0 \leq \delta \leq \frac{1}{2}$,

---

> algorithm $L$, with probability at least $1-\delta$, outputs a concept $h$ such that $L_\text{true}(h) \leq \epsilon$ using a number of samples that is polynomial in $\frac{1}{\epsilon}$ and $\frac{1}{\delta}$.

- (_We use the same notation of the previous definition_). $C$ is **efficiently PAC-learnable** by $L$ using $H$ iff for all $c \in C$, distribution $\mathcal{P}$ over $X$, $\epsilon$ s.t. $0 < \epsilon < \frac{1}{2}$, and $\delta$ s.t. $0 < \delta < \frac{1}{2}$, learner $L$ will with probability at least $1-\delta$ output an hypothesis $h \in H$ such that $L_\text{true}(h) \leq \epsilon$, in time that is **polynomial** in $\frac{1}{\epsilon}$, $\frac{1}{\delta}$, $M$, and $\text{size}(c)$.

Observe that if $C$ is _efficiently PAC-learnable_, then it is $PAC-learnable$, since we assume that "_each sample has to be seen at least once_".

## Agnostic learning

Usually the train error is **not equal to zero**: the Version Space is **empty**!
We can still bound (_with a certain probability_) the quantity $L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}) - L_\text{train}(\hat{h}_{\mathcal{D}_\text{train}})$.
We will use the following result.
- **Hoeffding bound**: for $N$ i.i.d. random variables $X_1, \ldots, X_N$ where $X_i \in [0, L]$ and $0 < \epsilon < 1$, we define the empirical mean $\overline{X} = \frac{1}{N}(X_1 + \ldots + X_N)$, obtaining the following bound:
$$
\mathbb{P}(\mathbb{E}[\overline{X}] - \overline{X} > \epsilon) < e^\frac{-2N\epsilon^2}{L^2}.
$$

- **Theorem**: if the hypothesis space $H$ is finite, the training set $\mathcal{D}_\text{train}$ consists of $N$ i.i.d. samples, and $0 < \epsilon < 1$:
$$
\mathbb{P}_{\mathcal{D}_\text{train}}(\exists h \in H | L_\text{true}(h) - L_\text{train}(h) > \epsilon) \leq |H|e^{-2N\epsilon^2}.
$$

> **Proof**: we proceed analogously to the consistent case and, at some point, we use the Hoeffding bound:

$$
\mathbb{P}_{\mathcal{D}_\text{train}}(\exists h \in H | L_\text{true}(h) - L_\text{train}(h) > \epsilon) = \mathbb{P}_{\mathcal{D}_\text{train}}(L_\text{true}(h_1) - L_\text{train}(h_1) > \epsilon \lor \ldots
$$
$$
\ldots \lor L_\text{true}(h_{|H|}) - L_\text{train}(h_{|H|}) > \epsilon) \leq \sum_{h \in H} \mathbb{P}_{\mathcal{D}_\text{train}}(L_\text{true}(h) - L_\text{train}(h) > \epsilon) =
$$
$$
= \sum_{h \in H} \mathbb{P}_{\mathcal{D}_\text{train}}(\mathbb{E}_{\mathcal{D}_\text{train}}[L_\text{train}(h)] - L_\text{train}(h) > \epsilon) < \sum_{h \in H} e^{-2N\epsilon^2} = |H|e^{-2N\epsilon^2}.
$$

Finally, since $\hat{h}_{\mathcal{D}_\text{train}} \in H$,
$$
\mathbb{P}_{\mathcal{D}_\text{train}}(L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}) - L_\text{train}(\hat{h}_{\mathcal{D}_\text{train}}) > \epsilon) \leq \mathbb{P}_{\mathcal{D}_\text{train}}(\exists h \in H | L_\text{true}(h) - L_\text{train}(h) > \epsilon) \leq |H|e^{-2N\epsilon^2}.
$$

Now, let's set:
$$
|H| e^{-2N\epsilon^2} = \delta \text{ iff } \epsilon = \sqrt{\frac{\ln |H| + \ln \frac{1}{\delta}}{2N}}.
$$

---

Then, with probability at least $1-\delta$:
$$
L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}) < L_\text{train}(\hat{h}_{\mathcal{D}_\text{train}}) + \epsilon = L_\text{train}(\hat{h}_{\mathcal{D}_\text{train}}) + \sqrt{\frac{\ln |H| + \ln \frac{1}{\delta}}{2N}}.
$$

The shape of the expression above is coherent with the bias-variance decomposition.
For large $|H|$ we have low bias (assuming we can find a good $\hat{h}_{\mathcal{D}_\text{train}}$) we have high variance.
For small $|H|$ we have high bias (is there a good $h$?) but low variance.

Given $\delta$, $\epsilon$, how large should $N$ be?
$$
N \geq \frac{1}{2\epsilon^2}\left( \ln|H| + \ln\frac{1}{\delta} \right).
$$

Observe that we can exploit Hoeffding bound also to get a confidence interval on the test estimate of the true loss.
In particular, for fixed $\mathcal{D}_\text{train}$:
$$
\mathbb{P}_{\mathcal{D}_\text{test}}(L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}) - L_\text{test}(\hat{h}_{\mathcal{D}_\text{train}}) > \epsilon) = \mathbb{P}_{\mathcal{D}_\text{test}}(\mathbb{E}_{\mathcal{D}_\text{test}}[L_\text{test}(\hat{h}_{\mathcal{D}_\text{train}})] - L_\text{test}(\hat{h}_{\mathcal{D}_\text{train}}) > \epsilon) < e^{-2 J \epsilon^2}
$$
where $J = |\mathcal{D}_\text{test}|$.  From this we can derive the usual bounds in probability as we did previously.
Observe that, since $\mathcal{D}_\text{test}$ is independent from $\mathcal{D}_\text{train}$, $L_\text{test}$ is an unbiased estimator of the true loss, hence we don't have the $|H|$ term in the bound.

## Continuous hypothesis spaces

What about **continuous hypothesis spaces** where $|H| = + \infty$? Can we get some bounds in this case? Yes! But we need additional machinery.

- A **dichotomy** of a set $S$ is a partition of $S$ into two disjoint subsets (_equivalently, it is a binary function over $S$_).

- A set of instances $S$ is **shattered** by the hypothesis space $H$ if and only if for every dichotomy of $S$ there exists some hypothesis in $H$ consistent with this dichotomy.

- The **Vapnik-Chervonenkis dimension** $\text{VC}(H)$ of hypothesis space $H$ defined over the instance space $X$ is the **size of the largest finite subset** of $X$ shattered by $H$. If arbitrarily large finite sets of $X$ can be **shattered** by $H$, then $\text{VC}(H) \equiv +\infty$.
> (_Size of $X$_ -> _Subset $S$ of $X$_ -> _Dichotomy of $S$_ -> _Consistent hypothesis_).

- A linear boundary classifier in $M$-D has VS dimension of $M+1$ (_the number of parameters_).

---

- **Rule of thumb**: the number of parameters in the model often matches the VC dimension. But in general, it can be completely **different**! There are problems where the **number of parameters is infinite** and the $\text{VS}$ dimension if **finite**! There can also e a hypothesis space with **1 parameter** and **infinite VC-dimension** ($1$-NN).

In general it holds that:
$$
L_\text{true}(\hat{h}_{\mathcal{D}_\text{train}}) \leq L_\text{train}(\hat{h}_{\mathcal{D}_\text{train}}) + \sqrt{\frac{\text{VC}(H)(\ln \frac{2N}{\text{VC}(H)}+ 1) + \ln \frac{4}{\delta}}{N}}.
$$

In **Structural Risk Minimization** we choose the hypothesis space $H$ to minimize the above bound on the true error.

- **Theorem**: the VC dimension of an hypothesis space $|H| < +\infty$ is bounded from above:
$$
\text{VC}(H) \leq \log_2(|H|).
$$

> **Proof**: if $\text{VC}(H) = d$, then there exist at least $2^d$ functions in $H$ (if $|S| = d$, then $S$ has $2^d$ dichotomies), hence $|H| \geq 2^d$, which proves the desired inequality.

- **Theorem**: a concept class $C$ with $\text{VC}(C) = + \infty$ is not PAC-learnable.
