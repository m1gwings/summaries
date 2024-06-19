---
marp: true
theme: summary
math: mathjax
---
# Markov Decision Processes

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Marcello Restelli_)

</div>

**Markov Decision Processes** (**MDPs**) are a special family of probabilistic models for **Sequential Decision Problems**. Before introducing the model, let's discuss the problems we wish to solve.

## Sequential Decision Making

The **goal** in a sequential decision making problem is to select actions as to maximize a cumulative reward. Actions may have **long-term** consequences. The reward may be **delayed**. It may be better to **sacrifice** immediate reward to gain more long-term reward.

Usually we model the _Agent-Environment interface_ as follows: at each step $t$, the agent executes the action $a_t$, receives observation $o_t$ and a scalar reward $r_t$.
The environment receives action $a_t$, emits observation $o_t$ and a scalar reward $r_t$.

- We define **history** the sequence of observations, actions, and rewards:
$$
h_t = a_1, o_1, r_1, \ldots, a_t, o_t, r_t.
$$

What "happens next" (_the action chosen by the agent, and the observation and reward chosen by the environment_) depends on the history.

- In particular, we define **state** the information used to determine what happens next. Formally, the state is a function of the history:
$$
s_t = f(a_1, o_1, r_1, \ldots, a_t, o_t, r_t).
$$

The environment state $s_t^e$ is the environment's private representation which it uses to produce the next observation/reward.
The environment state is **NOT usually visible** to the agent. Even if $s_t^e$ is visible, it may contain **irrelevant** information.

The agent state is the agent's internal representation which it used to select the next action. It can be any function of the history: $s_t^a = f(h_t)$.

under the **full observability** assumption the agent **directly** observes the environment state:
$$
o_r = s_t^a = s_t^e.
$$
Formally, this is a **Markov Decision Process** (MDP).

---

We classify sequential decision making problems along the following axes:
- **state space**: _finite_ vs _infinite_;
- **action space**: _finite_ vs _infinite_;
- **transitions**: _deterministic_ vs _stochastic_;
- **dynamics**: _stationary_ vs _non-stationary_;
- **observability**: _fully-observable_ vs _partially-observable_;
- **number of agents**: _single agent_ vs _multi-agent_.

## Discrete-time finite Markov Decision Processes

MDP rely on a fundamental assumption: the **Markov assumption**, which can be phrased as "_the future is independent of the past given the present_".

- A stochastic process $X_t$ is said to be **Markovian** if and only if
$$
\mathbb{P}(X_{t+1} = j \ | \ X_t = i, X_{t-1} = k_{t-1}, \ldots, X_1 = k_1, X_0 = k_0) = \mathbb{P}(X_{t+1} = j \ | \ X_t = i).
$$ 

This assumption has several consequences. The state **captures all the information** from history. Once the state is known, the history may be **thrown away**. The state is a **sufficient statistic** for the future. The conditional probabilities are **transition probabilities**.

If the probabilities are **stationary** (_time invariant_), we can write:
$$
p_{ij} = \mathbb{P}(X_{t+1} = j | X_t = i) = \mathbb{P}(X_1 = j | X_0 = i).
$$

- A **discrete-time finite Markov Decision Process** is a Markov reward process with **decisions**. It models an environment in which all states are Markovian and time is divided into stages. Formally, a **Markov Process** is a tuple $(\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu)$:
> - $\mathcal{S}$ is a _finite_ **set of states**;
> - $\mathcal{A}$ is a _finite_ **set of actions**;
> - $P$ is a state transition probability matrix, $P(s' | s, a)$;
> - $R$ is a reward function: $R(s, a) = \mathbb{E}[r|s,a]$;
> - $\gamma$ is a discount factor, $\gamma \in [0, 1]$;
> - $\mu$ is a set of initial probabilities $\mu_i = P(X_0 = i)$ for all $i \in \mathcal{S}$.

We can ask ourselves: "is a scalar reward an adequate notion of a goal?".
The **Sutton hypothesis** assumes: "That all of what we mean by goals and purposes can be well though as the maximization of the cumulative sum of a received scalar signal (reward)". Probably it is ultimately wrong, but it is so **simple** and **flexible** we have to disprove it before considering anything more complicated.

A goal should specify **what** we want to achieve, not **how** we want to achieve it.
The same goal can be specified by (infinite) **different reward functions**.
A goal must be outside of agent's direct control: thus outside the agent.
The agent must be able to measure success **explicitly** and **frequently** during its lifespan.

---

We need to define _how the reward is cumulated_. In particular, we need to understand which is the time horizon of our problem, it can be:
- **finite**: the problem has a _finite and fixed_ number of steps;
- **indefinite**: the agent will eventually stop, reaching an absorbing state, but the number of steps required to stop can different from episode to episode (_with episode we mean the interactions between the agent and the environment from the initial state until it reaches an absorbing state_);
- **infinite**: the agent never stops.

Analogously we can cumulate the reward in many ways:
- **total reward**: $V = \sum_{t=1}^{+\infty} r_t$ (_it can diverge in the infinite horizon case_);
- **average reward**: $V = \lim_{n \rightarrow + \infty} \frac{r_1 + \ldots + r_n}{n}$;
- **discounted reward**: $V = \sum_{t=1}^{+\infty} \gamma^{t-1} r_t$;
- **mean-variance reward**.

Observe that the **discounted reward** is _always convergent_ if $r_i \in [R_\min, R_\max]$.
In particular:
$$
V= \sum_{t=1}^{+\infty} \gamma^{t-1} r_t = \sum_{t=1}^{+\infty} \gamma^{t-1} (r_t - R_\min + R_\min) = \sum_{t=1}^{+\infty} \gamma^{t-1} (r_t - R_\min) + \frac{R-\min}{1-\gamma}.
$$
Now, $r_t - R_\min \geq 0$, then:
$$
\sum_{t=1}^N \gamma^{t-1}(r_t - R_\min) \text{ is non-decreasing}.
$$
Furthermore it is bounded by $\frac{R_\max - R_\min}{1-\gamma}$, hence $V$ is always convergent (since non-decreasing, bounded sequences in $\mathbb{R}$ are convergent).

An analogous reasoning can be applied to the average reward.

- We define **return** $v_t$ the total discounted reward from time-step $t$:
$$
v_t = r_{t+1} + \gamma r_{t+2} + \ldots = \sum_{k=0}^{+\infty} \gamma^k r_{t+k+1}.
$$

The discount $\gamma \in [0, 1)$ is the present value of future rewards.
The value of receiving reward $r$ after $k+1$ time-steps is $\gamma^k r$.

$\gamma$ close to 0 leads to a "**myopic**" evaluation, $\gamma$ close to 1 leads to a "**far-sighted**" evaluation.

**Important remark**: $\gamma$ can be also interpreted as the **probability** that the process will **go on**. We can interpret every discounted problem as an un-discounted by adding to any state a transition with probability $1-\gamma$ which leads to an absorbing state.

---

Most Markov reward (and decision) processes are discounted, why?
- **Mathematically** it is convenient to discount rewards;
- **Avoids infinite returns** in cyclic Markov processes;
- **Uncertainty** about the future may not be fully represented;
- If the reward is **financial**, immediate rewards may earn more interest than delayed rewards;
- **Animal/human behavior** shows preference for immediate reward;
- It is sometimes possible to use **un-discounted** Markov reward processes (i.e. $\gamma = 1$), e.g. if all sequences **terminate**.

### Policies

A **policy**, at any given point in time, _decides_ which action the agent selects. A policy fully defines the **behavior** of an agent.

Policies can be:
- **Markovian**: the _choice of the action depends only on the current state_ $\subseteq$ **History-dependent**:  the _choice of the action depends on the history_;
- **Deterministic**: in the same state or history we select always the same action $\subseteq$ **Stochastic**: in the same state or history we sample an action according to a distribution;
- **Stationary**: does not depend on time $\subseteq$ **Non-stationary**: depends on time.

- Formally, a policy $\pi$ is a **distribution over actions** given the state:
$$
\pi(a|s) = \mathbb{P}[a|s].
$$

MDP policies depend on the **current state** (_not the history_), i.e. MDP policies are stationary (_time-independent_).

Given an MDP $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma, \mu)$ and a policy $\pi$:
- the state sequence $s_1, s_2, \ldots$ is a **Markov process** $(\mathcal{S}, P^\pi, \mu)$;
- the state and reward sequence $s_1, r_2, s_2, \ldots$ is a **Markov reward process** $(S, P^\pi, R^\pi, \gamma, \mu)$ where:
$$
P^\pi(s'|s) = \sum_{a \in \mathcal{A}} \pi(a|s) P(s'|s, a);
$$
$$
R^\pi(s) = \mathbb{E}_{a \sim \pi}[R(s, a)] = \sum_{a \in \mathcal{A}} \pi(a|s)R(s,a).
$$

---

We can arrange $P^\pi$ in an $|\mathcal{S}| \times |\mathcal{S}|$ (_right, i.e. <u>rows</u> sum to 1_) stochastic matrix:
$$
P^\pi = \begin{bmatrix}
\mathbb{P}(X_{t+1} = s_1 | X_t = s_1) & \cdots & \mathbb{P}(X_{t+1} = s_{|\mathcal{S}|} | X_t = s_1) \\
\vdots & \ddots & \cdots \\
\mathbb{P}(X_{t+1} = s_1 | X_t = s_{|\mathcal{S}|}) & \cdots & \mathbb{P}(X_{t+1} = s_{|\mathcal{S}|} | X_t = s_{|\mathcal{S}|})
\end{bmatrix}.
$$

Then:
$$
{P^\pi}^2 = \begin{bmatrix}
\sum_{k=1}^{|\mathcal{S}|} \mathbb{P}(X_{t+1} = s_k | X_t = s_1) \mathbb{P}(X_{t+1} = s_1 | X_t = s_k) & \cdots & \sum_{k=1}^{|\mathcal{S}|} \mathbb{P}(X_{t+1} = s_k | X_t = s_1) \mathbb{P}(X_{t+1} = s_{|\mathcal{S}|} | X_t = s_k) \\
\vdots & \ddots & \vdots \\
\sum_{k=1}^{|\mathcal{S}|} \mathbb{P}(X_{t+1} = s_k | X_t = s_{|\mathcal{S}|}) \mathbb{P}(X_{t+1} = s_1 | X_t = s_k) & \cdots & \sum_{k=1}^{|\mathcal{S}|} \mathbb{P}(X_{t+1} = s_k | X_t = s_{|\mathcal{S}|}) \mathbb{P}(X_{t+1} = s_{|\mathcal{S}|} | X_t = s_k)
\end{bmatrix}.
$$
Now observe that:
$$
\sum_{k=1}^{|\mathcal{S}|} \mathbb{P}(X_{t+1} = s_k | X_t = s_i) \mathbb{P}(X_{t+1} = s_j | X_t = s_k) =
$$
$$
\stackrel{\text{stationarity + consequence of Markov property}}{=} \sum_{k=1}^{|\mathcal{S}|} \mathbb{P}(X_{t+1} = s_k | X_t = s_i) \mathbb{P}(X_{t+2}=s_j | X_{t+1} = s_k, X_t = s_i) =
$$
$$
\stackrel{\text{chain rule with bookkeeping}}{=} \sum_{k=1}^{|\mathcal{S}|} \mathbb{P}(X_{t+2} = s_j, X_{t+1} = s_k | X_t = s_i) \stackrel{\text{marginalization with bookkeeping}}{=} \mathbb{P}(X_{t+2} = s_j|X_t = s_i).
$$

Then:
$$
{P^\pi}^2 = \begin{bmatrix}
\mathbb{P}(X_{t+2} = s_1 | X_t = s_1) & \cdots & \mathbb{P}(X_{t+2} = s_{|\mathcal{S}|}|X_t = s_1) \\
\vdots & \ddots & \vdots \\
\mathbb{P}(X_{t+2} = s_1 | X_t = s_{|\mathcal{S}|}) & \cdots & \mathbb{P}(X_{t+2} = s_{|\mathcal{S}|}|X_t = s_{|\mathcal{S}|})
\end{bmatrix}.
$$
The reasoning can be easily generalized to ${P^\pi}^k$ through induction.

### Value functions

Given a policy $\pi$, it is possible to define the **utility** at each state. This process is known as **Policy Evaluation**.

- The **state-value function** $V^\pi(s)$ of an MDP is the expected return starting from state $s$, and then following policy $\pi$:
$$
V^\pi(s) = \mathbb{E}_\pi[v_t | s_t = s].
$$

For **control purposes**, rather than the value of each state, it is easier to consider the **value of each action** in each state.

---

- The **action-value function** $Q^\pi(s, a)$ is the expected return starting from state $s$, taking action $a$, and then following policy $\pi$:
$$
Q^\pi(s, a) = \mathbb{E}_\pi[v_t | s_t = s, a_t = a].
$$

#### Bellman expectation equations

The **state-value function** can again be **decomposed** into immediate reward plus discounted value of successor state:
$$
V^\pi(s) = \mathbb{E}_\pi[v_t | s_t = s] = \mathbb{E}_\pi[r_{t+1} + \gamma v_{t+1}|s_t = s] = \mathbb{E}_\pi[r_{t+1}|s_t = s] + \gamma \mathbb{E}_\pi[v_{t+1} | s_t = s] =
$$
$$
\stackrel{\text{law of total expectation}}{=} \mathbb{E}_\pi[r_{t+1}|s_t = s] + \gamma \mathbb{E}_\pi[\mathbb{E}_\pi[r_{t+1}|s_{t+1}, s_t = s]|s_t = s] =
$$
$$
\stackrel{\text{markov property}}{=} \mathbb{E}_\pi[r_{t+1}|s_t = s] + \gamma \mathbb{E}_\pi[\mathbb{E}_\pi[r_{t+1}|s_{t+1}]|s_t = s] =
$$
$$
\stackrel{\text{def. of } V^\pi \text{ and stationarity}}{=} \mathbb{E}_\pi[r_{t+1}|s_t = s] + \gamma \mathbb{E}_\pi[V^\pi(s_{t+1})|s_t = s] = \mathbb{E}_\pi[r_{t+1} + \gamma V^\pi(s_{t+1})|s_t = s] =
$$
$$
= \sum_{a \in \mathcal{A}(s)} \pi(a|s) \left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V^\pi(s') \right].
$$

The **action-value function** can similarly be decomposed:
$$
Q^\pi(s, a) = \mathbb{E}_\pi[r_{t+1} + \gamma v_{t+1}|s_t = s, a_t = a] =
$$
$$
= \mathbb{E}_\pi[r_{t+1}|s_t = s, a_t = a] + \gamma \mathbb{E}_\pi[\mathbb{E}_\pi[v_{t+1}|s_{t+1}, a_{t+1}, s_t = s, a_t = a]|s_t = s, a_t = a] =
$$
$$
= \mathbb{E}_\pi[r_{t+1}|s_t = s, a_t = a] + \gamma \mathbb{E}_\pi[\mathbb{E}_\pi[v_{t+1}|s_{t+1}, a_{t+1}]|s_t = s, a_t = a] = 
$$
$$
= \mathbb{E}_\pi[r_{t+1}|s_t = s, a_t = a] + \gamma \mathbb{E}_\pi[Q^\pi(s_{t+1}, a_{t+1})|s_t = s, a_t = a] =
$$
$$
= \mathbb{E}_\pi[r_{t+1} + \gamma Q^\pi(s_{t+1}, a_{t+1})|s_t = s, a_t = a] =
$$
$$
= R(s, a) + \gamma \sum_{s' \in S} P(s'|s,a) \sum_{a' \in \mathcal{A}(s')} \pi(a'|s') Q^\pi(s', a').
$$

The Bellman expectation equation can be expressed concisely in matrix notation:
$$
V^\pi = R^\pi + \gamma P^\pi V^\pi.
$$

Observe that:
$$
\det[I - \gamma P^\pi - \lambda I] = \det[(1-\lambda)I - \gamma P^\pi] = (-1)^{n} \gamma^n \det[P^\pi - \frac{1-\lambda}{\gamma}I].
$$
Then $\lambda$ is an eigenvalue of $I - \gamma P^\pi$ iff $\frac{1-\lambda}{\gamma}$ is an eigenvalue of $P^\pi$.
Because of the properties of stochastic matrices, $\lambda_i(P^\pi) \in [-1, 1]$ for all $i$.
Then:
$$
-1 \leq \frac{1-\lambda}{\gamma} \leq 1 \text{ iff } 0 < 1-\gamma \leq \lambda \leq 1+\gamma \text{ if } \gamma < 1.
$$

---

We just proved that, if $\gamma < 1$, then $I-\gamma P^\pi$ is invertible (since all its eigenvalues are strictly positive).

Then we can compute the value function for the chosen policy $\pi$ in closed form:
$$
V^\pi = (I-\gamma P^\pi)^{-1}R^\pi.
$$

The formula could be also derived by observing that (_remember the remark on the value of ${P^\pi}^k$_):
$$
V^\pi = \sum_{k=1}^{+\infty} (\gamma P^\pi)^{k-1} R^\pi = (I-\gamma P^\pi)^{-1} R^\pi
$$
because of the formula which generalizes the geometric series to matrices.

- The **Bellman operator for $V^\pi$** is defined as $T^\pi : \mathbb{R}^{|\mathcal{S}|} \rightarrow \mathbb{R}^{|\mathcal{S}|}$ (maps value functions to value functions):
$$
(T^\pi V^\pi)(s) = \sum_{a \in \mathcal{A}(s)} \pi(a|s)\left[R(s,a) + \gamma \sum_{s' \in S} P(s'|s,a) V^\pi(s')\right].
$$

Using Bellman operator, Bellman expectation equation can be **compactly** written as (_observe that in matrix notation $T^\pi V^\pi = R^\pi + \gamma P^\pi \underline{v}$_):
$$
T^\pi V^\pi = V^\pi.
$$
$V^\pi$ is a **fixed point** of the Bellman operator $T^\pi$. This is a **linear equation** in $V^\pi$ and $T^\pi$.
If $0 < \gamma < 1$ then $T^\pi$ is a **contraction** w.r.t. the maximum norm.

Hence, starting from any initial vector $\underline{v}^{(0)} \in \mathbb{R}^{|\mathcal{S}|}$ we can build a sequence which converges to $V^\pi$ by simply iterating the application of the Bellman operator:
$$
||T^\pi \underline{v}^{0} - V^\pi||_\infty = ||T^\pi \underline{v}^{0} - T^\pi V^\pi||_\infty \leq \gamma ||\underline{v}^{(0)} - V^\pi||.
$$
Hence, by induction:
$$
||\underline{v}^{(k)} - V^\pi||_\infty = ||{T^\pi}^k \underline{v}^{(0)} - V^\pi||_\infty \leq \gamma^k ||\underline{v}_0 - V^\pi||_\infty \stackrel{k \rightarrow +\infty}{\rightarrow} 0 \text{ iff } \underline{v}^{(k)} \stackrel{k \rightarrow +\infty}{\rightarrow} V^\pi
$$
because of the properties of norms (_the norm of a vector is 0 iff the vector is the zero vector + norms are continuous_).

- The **Bellman operator for $Q^\pi$** is defined as $T^\pi : \mathbb{R}^{|\mathcal{S}| \times |\mathcal{A}|} \rightarrow \mathbb{R}^{|\mathcal{S}| \times |\mathcal{A}|}$ (maps action-value functions to action-value functions):
$$
(T^\pi Q^\pi)(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) \sum_{a' \in \mathcal{A}} \pi(a'|s') Q^\pi(s', a').
$$

Using Bellman operator, Bellman expectation equation can be compactly written as:
$$
T^\pi Q^\pi = Q^\pi.
$$

---

$Q^\pi$ is a fixed point of the Bellman operator $T^\pi$.
If $0 < \gamma < 1$ then $T^\pi$ is a contraction w.r.t. the maximum norm.

#### Optimal value functions

- The **optimal state-value function** $V^*(s)$ is the maximum value function over all policies:
$$
V^*(s) = \max_\pi V^\pi(s).
$$

- The **optimal action-value function** $Q^*(s,a)$ is the maximum action-value function over all policies
$$
Q^*(s, a) = \max_\pi Q^\pi(s, a).
$$

The optimal value function specifies the **best** possible performance in the MDP. An MDP is "**solved**" when we know the optimal value function.

Value functions define a partial ordering over policies:
$$
\pi \geq \pi' \text{ iff } V^\pi(s) \geq V^{\pi'}(s) \ \forall s \in \mathcal{S}.
$$

- **Theorem**: for any MDP:
> - there exists an **optimal policy $\pi^*$** that is better than or equal to all other policies $\pi^* \geq \pi \ \forall \pi$;
> - **all** optimal policies achieve the **optimal value function** $V^{\pi^*}(s) = V^*(s)$;
> - **all** optimal policies achieve the **optimal action-value function** $Q^{\pi^*}(s, a) = Q^*(s, a)$;
> - there is always a **deterministic optimal policy** for any MDP.

A deterministic optimal policy can be found by maximizing over $Q^*(s, a)$:
$$
\pi^*_\text{det}(a|s) = \begin{cases}
1 \text{ if } a = \arg \max_{a \in \mathcal{A}(s)} A^*(s, a) \\
0 \text{ otherwise}
\end{cases}.
$$

We can also compute $\pi^*$ from $V^*$ (_we will the lighter notation for deterministic policies_):
$$
\pi^*(s) = \arg \max_{a \in \mathcal{A}(s)}\left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V^*(s') \right].
$$

##### Policy improvement theorem

In this section we will present and prove an important theorem: the **policy improvement theorem**. But, before doing so, we need some intermediate result.

- **Lemma (1)**: $Q^\pi(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) V^\pi(s')$.

---

> **Proof**:
$$
Q^\pi(s, a) = \mathbb{E}_\pi[r_{t+1} + \gamma v_{t+1}|s_t = s, a_t = a] =
$$
$$
= \mathbb{E}_\pi[r_{t+1}|s_t = s, a_t = a] + \gamma \mathbb{E}_\pi[\mathbb{E}_\pi[v_{t+1}|s_{t+1}, s_t = s, a_t = a]|s_t = s, a_t = a] =
$$
$$
= \mathbb{E}_\pi[r_{t+1}|s_t = s, a_t = a] + \gamma \mathbb{E}_\pi[V^\pi(s_{t+1})|s_t = s, a_t = a] =
$$
$$
= R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V^\pi(s').
$$

- For any policies $\pi, \pi'$, we identify:
$$
Q^\pi(s, \pi'(s)) = \sum_{a \in \mathcal{A}(s)} \pi'(a|s) Q^\pi(s, a).
$$
> Observe that, if $\pi'$ is deterministic, the expression has the natural meaning (_remember the lighter notation for deterministic policies and the standard one_).

- **Lemma (2)**: let $\pi$, $\pi'$ be any pair of policies such that
$$
Q^\pi(s, \pi'(s)) \geq V^\pi(s) \ \forall s \in \mathcal{S}.
$$
> Then $V^\pi(s) \leq \mathbb{E}_{\pi'}[r_{t+1} + \gamma r_{t+2} + \ldots + \gamma^{N-1} r_{t+N} + \gamma^N V^\pi(s_{t+N})|s_t = s]$ for all $s \in \mathcal{S}, N \in \mathbb{N}^+$.

> **Proof**: we will proceed by induction.
Base case ($N = 1$):
$$
V^\pi(s) \stackrel{\text{hp.}}{\leq} Q^\pi(s, \pi'(s)) = \sum_{a \in \mathcal{A}(s)} \pi'(a|s) Q^\pi(s, a) =
$$
$$
\stackrel{\text{lemma (1)}}{=} \sum_{a \in \mathcal{A}(s)} \pi'(a|s) \left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) V^\pi(s') \right] = \mathbb{E}_{\pi'}[r_{t+1} + \gamma V^\pi(s_{t+1})|s_t = s].
$$

> Inductive step ($N > 1$):
$$
V^\pi(s) \stackrel{\text{ind. hp.}}{\leq} \mathbb{E}_{\pi'}[r_{t+1} + \gamma r_{t+2} + \ldots + \gamma^{N-2} r_{t+N-1} + \gamma^{N-1} V^\pi(s_{t+{N-1}})|s_t = s] \leq
$$
$$
\stackrel{\text{base case}}{\leq} \mathbb{E}_{\pi'}[r_{t+1} + \gamma r_{t+2} + \ldots + \gamma^{N-2} r_{t+N-1} + \gamma^{N-1} \mathbb{E}_{\pi'}[r_{t+N}+\gamma V^\pi(s_{t+N})|s_{t+N-1}]|s_t = s] =
$$
$$
\stackrel{\text{markov property}}{=} \mathbb{E}_{\pi'}[r_{t+1} + \gamma r_{t+2} + \ldots + \gamma^{N-2} r_{t+N-1} + \gamma^{N-1} r_{t+N} + \gamma^N \mathbb{E}_{\pi'}[ V^\pi(s_{t+N})|s_{t+N-1}, s_t = s]|s_t = s] =
$$
$$
\stackrel{\text{linearity + law of total expectation}}{=} \mathbb{E}_{\pi'}[r_{t+1} + \gamma r_{t+2} + \ldots + \gamma^{N-1} r_{t+N} + \gamma^N V^\pi(s_{t+N})|s_t = s].
$$

Now we're ready to introduce the theorem.

---

- **Policy improvement theorem**: let $\pi$, $\pi'$ be any pair of policies such that
$$
Q^\pi(s, \pi'(s)) \geq V^\pi(s) \ \forall s \in \mathcal{S}.
$$
> Then the policy $\pi'$ must be as good as, or better than $\pi$:
$$
V^{\pi'}(s) \geq V^\pi(s).
$$

> **Proof**: because of lemma (2)
$$
V^\pi(s) \leq \mathbb{E}_{\pi'}[r_{t+1} + \gamma r_{t+2} + \ldots + \gamma^{N-1} r_{t+N} + \gamma^N V^\pi(s_{t+N})|s_t = s] =
$$
$$
= \mathbb{E}_{\pi'}[r_{t+1} + \gamma r_{t+2} + \ldots + \gamma^{N-1} r_{t+N}|s_t = s] + \gamma^N \mathbb{E}_{\pi'}[V^\pi(s_{t+N})|s_t = s].
$$
> Now, as we proved when talking about the _discounted reward_, $V^\pi(s)$ is bounded for any $s \in \mathcal{S}$, hence the same holds for $\mathbb{E}_{\pi'}[V^\pi(s_{t+N})|s_t = s]$ (_we're averaging, according to a certain distribution, all the values of $V^\pi$_).
Hence, if we take the limit for $N \rightarrow +\infty$ (_we bring the limit inside the expected value without further questioning (:-D), one day I'll be able of being more formal [I need Lebesgue theory of integration with all its nice theorems]_), the right side converges to $V^{\pi'}(s) + 0$ (since $0 < \gamma < 1$). Then, by the comparison theorem for limits:
$$
V^\pi(s) \leq V^{\pi'}(s)
$$
> as we wanted to prove.

**Very important remark**: if, <u>in addition</u>, $Q^\pi(\hat{s}, \pi'(\hat{s})) > V^\pi(\hat{s})$ for some $\hat{s} \in \mathcal{S}$, then:
$$
V^{\pi'}(\hat{s}) \stackrel{\text{bellman equation}}{=} \sum_{a \in \mathcal{A}(\hat{s})} \pi'(a|\hat{s})\left[ R(\hat{s}, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|\hat{s},a) V^{\pi'}(s') \right] \geq
$$
$$
\stackrel{\text{policy improvement theorem}}{\geq} \sum_{a \in \mathcal{A}(\hat{s})} \pi'(a|\hat{s})\left[ R(\hat{s}, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|\hat{s},a) V^\pi(s') \right] =
$$
$$
\stackrel{\text{lemma (1)}}{=} \sum_{a \in \mathcal{A}(\hat{s})} \pi'(a|\hat{s}) Q^\pi(\hat{s}, a) = Q^\pi(\hat{s}, \pi'(\hat{s})) \stackrel{\text{hp.}}{>} V^\pi(\hat{s}).
$$

Then, $\pi'$ is strictly better than $\pi$.

##### Bellman optimality equation

- **Lemma (3)**: $V^\pi(s) = \sum_{a \in \mathcal{A}(s)} \pi(a|s) Q^\pi(s, a)$.

> **Proof**:
$$
V^\pi(s) = \mathbb{E}_\pi[v_t|s_t = s] = \mathbb{E}_\pi[\mathbb{E}_\pi[v_t|a_t, s_t = s]|s_t = s] =
$$

---

$$
= \mathbb{E}_\pi[Q^\pi(s, a_t)|s_t = s] = \sum_{a \in \mathcal{A}(s)} \pi(a|s) Q^\pi(s, a) \text{ as we wanted to prove}.
$$

The **Bellman optimality equation** is an equation satisfied by all the optimal policies. Let $\pi^*$ be an optimal policy.
Then:
$$
V^{\pi^*}(s) \stackrel{\text{lemma (3)}}{=} \sum_{a \in \mathcal{A}(s)} \pi^*(a|s) Q^{\pi^*}(s, a) \leq \max_{a \in \mathcal{A}(s)} Q^{\pi^*}(s, a)
$$
where the last inequality follows from the fact that the sum on the left is a convex combination.
Furthermore, it can't be $V^{\pi^*}(s) < Q^{\pi^*}(s, \hat{a})$ for some $\hat{a} \in \mathcal{A}(s)$, otherwise $V^{\pi^*}$ would not be optimal because of the _very important remark after the policy improvement theorem_.
Hence, it must be:
$$
V^{\pi^*}(s) = \max_{a \in \mathcal{A}(s)} Q^{\pi^*}(s, a).
$$

This is the so-called **Bellman optimality equation** which is usually expressed either as dependent only on $V^*$ or only on $Q^*$ (_remember that $V^{\pi^*} = V^*$ and $Q^{\pi^*} = Q^*$_). 

- **Bellman Optimality Equation for $V^*$**:
$$
V^*(s) = \max_{a \in \mathcal{A}(s)} Q^*(s, a) =
$$
$$
\stackrel{\text{lemma (1)}}{=} \max_{a \in \mathcal{A}(s)}\left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V^*(s') \right].
$$

- **Bellman Optimality Equation for $Q^*$**:
$$
Q^*(s, a) \stackrel{\text{lemma (1)}}{=} R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V^*(s') =
$$
$$
= R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s,a) \max_{a' \in \mathcal{A}(s')} Q^*(s', a').
$$

Analogously to what we did before, we can define the operator corresponding to each of the equations above.

- The **Bellman optimality operator** for $V^*$ is defined as $T^* : \mathbb{R}^{|\mathcal{S}|} \rightarrow \mathbb{R}^{|\mathcal{S}|}$ (maps value functions to value functions):
$$
(T^* V^*)(s) = \max_{a \in \mathcal{A}} \left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V^*(s') \right].
$$

---

- The **Bellman optimality operator** for $Q^*$ is defined as $T^* : \mathbb{R}^{|\mathcal{S}| \times |\mathcal{A}|} \rightarrow \mathbb{R}^{|\mathcal{S}| \times |\mathcal{A}|}$ (maps action-value functions to action value functions):
$$
(T^* Q^*)(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) \max_{a' \in \mathcal{A}(s')} Q^*(s', a').
$$

#### Properties of the Bellman Operators

Bellman Operators enjoy the following properties:
- **monotonicity**: if $\underline{v}_1 \leq \underline{v}_2$, then:
$$
T^\pi \underline{v}_1 \leq T^\pi \underline{v}_2 \text{ and } T^* \underline{v}_1 \leq T^* \underline{v}_2;
$$
- **max-norm contraction**:
$$
||T^\pi \underline{v}_1 - T^\pi \underline{v}_2||_\infty \leq \gamma ||\underline{v}_1 - \underline{v}_2||_\infty \text{ and}
$$
$$
||T^* \underline{v}_1 - T^* \underline{v}_2||_\infty \leq \gamma ||\underline{v}_1 - \underline{v}_2||_\infty;
$$
- **fixed points**: $V^\pi$ is the unique fixed point of $T^\pi$ and $V^*$ is the unique fixed point of $T^*$;
- **convergent iteration**:
$$
\lim_{k \rightarrow +\infty} (T^\pi)^k \underline{v}_1 = V^\pi \text{ and } \lim_{k \rightarrow +\infty} (T^*)^k \underline{v}_1 = V^*.
$$

**Very important remark**: observe that, since $T^*$ has a unique fixed point, all the policies which satisfy the Bellman optimality equation have the same value function. Furthermore, we know that there exists at least an optimal policy, and such policy must satisfy the Bellman optimality equation (which we showed being a necessary condition for optimality). Hence all the policies which satisfy the Bellman optimality equation have the same value function of an optimal policy and thus they are optimal. In other words, the Bellman optimality equation in this setting is not only necessary, but also sufficient for a policy to be optimal.

## Solving MDPs

Solving an MDP means finding an **optimal policy**. 
A **naive approach** consists of:
1. **enumerating** all the deterministic Markov policies;
2. **evaluate** each policy;
3. **return** the best one.

Unfortunately, the number of deterministic policies (_we know from the theory that there must be at least one optimal deterministic policy_) is exponential in the number of state: $|\mathcal{A}|^{\mathcal{S}}$.

We need a more intelligent way to look for the optimal policy.

---

### Dynamic Programming

**Dynamic Programming** (**DP**) is a family of techniques which can be used to solve certain optimization problems. In particular, the term **dynamic** refers to the fact that the problem has a sequential/temporal component; the term **programming** means that we're optimizing a "program" (i.e. a policy) (_like in linear programming_).
In particular, in Dynamic Programming we break down a problem into simpler sub-problems, whose solutions can be combined to produce a solution for the original problem. The property that we just described is called **optimal substructure**.
Another property which DP relies on is the **overlapping sub-problems** property: sub-problems **recur** many times and solutions can be **cached** and **reused**.

We can use DP in a MDP both for **prediction** (computing the value function of a given policy) and **control** (finding the optimal policy).

#### Finite-horizon DP

There is a really convenient way of applying DP to a finite horizon MDP.
Assume that every interaction between the environment and the agent lasts $N$ steps.
Hence, in a given interaction, the agent can be in a certain state for at most $N+1$ times (counting also the initial state).
The **principle of optimality** in a problem of this kind is that an optimal policy for all the $N$ steps must be optimal for the last $N-1$ steps (easy proof by contradiction).
Hence, we can build an $(N+1) \times |\mathcal{S}|$ table which stores the value of being in state $\mathcal{S}$ at step $t$: **observe that finite-horizon problems are non-stationary**.

In the last step we know that, no matter the policy, the value of being in any state is $0$: we cannot interact with the environment any more. Hence we can fill the last row with zeroes.

At each step $t$, the value of playing an action $a$ in a certain sate $s$ is:
$$
Q(s, a, t) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V(s', t+1);
$$ 
if we fill the table stating from the last row, we can assume that $V(s', t+1)$ is known.
Hence, we can compute the optimal value function by choosing the best action at every step:
$$
V^*(s, t) = \max_{a \in \mathcal{A}(s)} Q^*(s, a, t) = \max_{a \in \mathcal{A}(s)} \left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V^*(s', t+1) \right].
$$
This process is known as **backward induction**. The equation above is known as **backward recursion** and allows us to fill the table. The cost is $O(N |\mathcal{S}| |\mathcal{A}|)$.
Once we have filled the table, at each stable we can choose the action with highest value in the given state, remembering that:
$$
Q^*(s, a, t) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V^*(s',t+1).
$$

---

#### Policy evaluation

We know that, given a policy $\pi$, we have two ways of computing the corresponding value function $V^\pi$.
We can either solve the Bellman expectation equation:
$$
V^\pi = (I - \gamma P^\pi)^{-1}R^\pi
$$
or apply the Bellman expectation operator iteratively (_we know that this procedure converges in the limit to the value function_). In particular, in this last approach, we update the estimated value function with the following backup operation:
$$
V_{k+1}(s) \gets \sum_{a \in \mathcal{A}(s)} \pi(a|s) \left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V_k(s') \right].
$$
- A **sweep** consists of applying a backup operation to each state. Using **synchronous** backups, at each iteration $k+1$, for all states $s \in \mathcal{S}$, we update $V_{k+1}(s)$ from $V_k(s')$.

#### Policy iteration

Consider a **deterministic policy** $\pi$. We ask ourselves "for a given state $s$, would it be **better** to do an action $a \neq \pi(s)$". It is possible to answer the question by noticing that we can improve a policy by acting greedily. Let:
$$
\pi'(s) = \arg \max_{a \in \mathcal{A}(s)} Q^\pi(s, a).
$$
Then:
$$
Q^\pi(s, \pi'(s)) \stackrel{\text{definition of } \pi'}{=} \max_{a \in \mathcal{A}(s)} Q^\pi(s, a) \geq Q^\pi(s, \pi(s)) \stackrel{\text{lemma (3)}}{=} V^\pi(s).
$$
Hence, $\pi'$ is at least as good as $\pi$ <u>because of the policy improvement theorem</u>.

In particular, if $Q^\pi(s, \pi'(s)) > V^\pi(s)$ for some $s \in \mathcal{S}$ we know that $\pi'$ is <u>strictly better</u> than $\pi$.
Conversely, if $V^\pi(s) = \max_{a \in \mathcal{A}(s)} Q^\pi(s, a)$, then $\pi$ satisfies the Bellman optimality equation and is thus optimal.
These two observations describe the **policy improvement** algorithm.
At every step we evaluate a deterministic policy $\pi$ and then compute the greedy policy $\pi'$ (which is also deterministic) until the value function of $\pi$ does not satisfy the Bellman optimality equation.

**Remark**: the algorithm terminates in finite time since at every step we strictly improve the policy and the deterministic policies are in finite number.

---

The algorithm can be generalized by relaxing the constraint of computing the exact value function of policy $\pi$.
In particular, we can do **iterative policy evaluation** of $V^\pi$ for few steps, and then compute the greedy policy $\pi'$. There are convergence guarantees also for this algorithm.

The cost of policy iteration is the cost of policy evaluation + the cost of policy improvement.
- Policy evaluation has a complexity of:
> - $O(|\mathcal{S}|^3)$ or $O(|\mathcal{S}|^{2.373})$ if we compute the closed form solution to Bellman optimality equations;
> - $O\left( |\mathcal{S}|^2 \frac{\log(\frac{1}{\epsilon})}{\log(\frac{1}{\gamma})} \right)$ if we apply the iterative approach.

- Policy improvement has recently been proven to be $O\left( \frac{|\mathcal{A}|}{1-\gamma} \log\left(\frac{|\mathcal{S}|}{1-\gamma}\right) \right)$.

#### Value iteration

The **value iteration** algorithm consists of finding the optimal policy for an MDP by iterative application of the Bellman optimality operator.

Remember that this approach converges in the limit. Anyway we have some theoretical guarantees which provide termination conditions.
- **Theorem**:
$$
||V_{i+1} - V_i||_\infty < \epsilon \implies ||V_{i+1} - V^*||_\infty < \frac{2\epsilon \gamma}{1-\gamma}
$$

Observe that applying the Bellman optimality operator to get a full update has a complexity of $O(|\mathcal{S}|^2 |\mathcal{A}|)$.

#### Efficiency of DP

To find an optimal policy, DP is polynomial in the number of states...
But the number of states is often astronomical, e.g. often growing exponentially with the number of state variables.
In practice, classical DP can be applied to problems with a few millions states.
**Asynchronous DP** can be applied to larger problems, and is appropriate for parallel computation.
It is **surprisingly** easy to come up with MDPs for which the methods are not practical.

**Comparison between PI and VI**: each iteration of PI is computationally **more expensive** than each iteration of VI, but PI typically requires fewer iterations to converge than VI.

---

### Infinite Horizon Linear programming

In this section we will derive an LP formulation of the problem of finding an optimal policy in a MDP.
Let $V \in \mathbb{R}^{|\mathcal{S}|}$ s.t. $V \geq T^*(V)$.
Because of the monotonicity of the Bellman optimality operator:
$$
T^*(V) \geq {T^*}^2(V),
$$
hence $V \geq T^*(V) \geq {T^*}^2(V)$. By induction $V \geq {T^*}^k (V)$.
Then, since limits preserve inequalities and ${T^*}^k(V) \stackrel{k \rightarrow + \infty}{\rightarrow} V^*$, it holds that $V \geq V^*$.
Observe that, if $V > T^*(V)$, by analogous reasoning, $V > V^*$ (_you take the limit of $T^*(V) \geq {T^*}^k(V)$ and then you apply $V > T^*(V)$_).

Fix $\underline{\mu} \in \mathbb{R}^{|\mathcal{S}|}$, $\underline{\mu} > \underline{0}$.
Then: $\underline{\mu}^T V \geq \underline{\mu}^T V^*$ if $V \geq V^*$ and, in particular, $\underline{\mu}^T V > \underline{\mu}^T V^*$ if $V > V^*$

We're ready to define the LP:
$$
\min_V \underline{\mu}^T V
$$
$$
\text{s.t}
$$
$$
V \geq T^*(V).
$$

First of all observe that $V^* = T^*(V^*)$ by Bellman optimality equation, hence it is feasible for the problem above. Furthermore, we proved that if $V \geq T^*(V^*)$ then $V \geq V^*$ and so $\underline{\mu}^T V \geq \underline{\mu}^T V^*$, hence $V^*$ is also optimal for the LP.
Now suppose that $V > T^*(V)$, then $V > T^*(V) = V^*$, and so $\underline{\mu}^T V > \underline{\mu}^T V^*$, or, in other words, $V$ is not optimal.
Hence, to be optimal, $V$ must satisfy $V = T^*(V)$, that is, it must be optimal for the MDP because of Bellman optimality equations.

We proved that the optimal value functions for the MDP are all and only the optimal solutions to the above LP.

Let's find the dual of the above optimization problem.
Observe that $V \geq T^*(V)$ can be expanded as:
$$
V(s) \geq \max_{a \in \mathcal{A}(s)} \left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V(s') \right] \ \forall s \in \mathcal{S}.
$$
This is equivalent to imposing:
$$
V(s) \geq R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s'|s, a) V(s') \ \forall a \in \mathcal{A}, s \in \mathcal{S}.
$$

---

Observe that if we fix column $s'$, the coefficient of $V(s')$ at row $s, a$ is:
$$
\begin{cases}
1-\gamma P(s'|s, a) \text{ if } s = s' \\
-\gamma P(s'|s, a) \text{ otherwise}.
\end{cases}
$$
While the constant term is $R(s, a)$ for each row.

Let $\lambda(s, a)$ be the variables of the dual problem.
Then the dual problem is:
$$
\max_\lambda \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} \lambda(s, a) R(s, a)
$$
$$
\text{s.t.}
$$
$$
\sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} \mathbb{1}[s = s'] \lambda(s, a) = \mu_s + \gamma \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} P(s'|s, a) \lambda(s, a) \ \forall s' \in \mathcal{S}
$$
$$
\lambda(s, a) \geq 0 \ \forall s \in \mathcal{S}, a \in \mathcal{A}.
$$
Finally, we can rewrite it as:
$$
\max_\lambda \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} \lambda(s, a) R(s, a)
$$
$$
\text{s.t.}
$$
$$
\sum_{a \in \mathcal{A}} \lambda(s', a) = \mu_s + \gamma \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} P(s'|s, a) \lambda(s, a) \ \forall s' \in \mathcal{S}
$$
$$
\lambda(s, a) \geq 0 \ \forall s \in \mathcal{S}, a \in \mathcal{A}.
$$

$\lambda(s, a)$ can be interpreted as:
$$
\lambda(s, a) = \sum_{t=0}^\infty \gamma^t \mathbb{P}(s_t = s, a_t = a).
$$
Indeed:
$$
\sum_{a \in \mathcal{A}} \sum_{t=0}^\infty \gamma^t \mathbb{P}(s_t = s', a_t = a) = \sum_{t=0}^\infty \gamma^t \mathbb{P}(s_t = s') = \sum_{t=0}^\infty \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} \gamma^t P(s'|s,a) \mathbb{P}(s_{t-1} = s, a_{t-1} = a) =
$$
$$
 = \gamma \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} P(s'|s,a) \sum_{t=0}^\infty \gamma^{t-1} \mathbb{P}(s_{t-1} = s, a_{t-1} = a).
$$
[_This just show that such interpretation "solves" (ignoring the constant shift $\mu_s$) the constraint above, we should also show that the converse is true but I don't know how; maybe the associated operator is a contraction and thus admits a unique fixed point_].

[_What follows will be super informal ( :-( )_]
Furthermore, by the law of total expectation, we can write $\mathbb{E}[r_{t+1}] = \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} R(s, a) \mathbb{P}(s_t = s, a_t = a)$.

---

Hence, since the return is $v = \sum_{t=0}^\infty \gamma^t r_{t+1}$, then:
$$
\mathbb{E}[v] = \sum_{t=0}^\infty \gamma^t \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} R(s, a) \mathbb{P}(s_t = s, a_t = a) = \sum_{s \in \mathcal{S}} \sum_{a \in \mathcal{A}} \lambda(s, a) R(s, a),
$$
which is exactly the objective function which we're maximizing.

Then the corresponding optimal policy is:
$$
\pi^*(s) = \arg \max_{a \in \mathcal{A}} \lambda(s, a)
$$
_[I don't know why]_.

LP **worst-case** convergence guarantees are better than those of DP methods, but LP methods become **impractical** at a much smaller number of states than DP methods do.
