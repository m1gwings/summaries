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

The **Bellman optimality equation** is an equation satisfied by all and only the optimal policies. Let $\pi^*$ be an optimal policy.
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

_[It is also sufficient because it admits a unique solution]_.