---
marp: true
theme: summary
math: mathjax
---
# Recurrent Neural Networks

<div class="author">

Cristiano Migali

</div>

- **Recurrent Neural Networks** (**RNNs**) are a _model with memory_ [_check the set of notes about sequential data problems_] where the function $f$ which computes the current hidden state given the current input and the previous state is implemented as a NN.

RNN describe dynamical systems with non-linear dynamics.

- **Theorem**: with enough neurons and time, RNNs can compute anything that can be computed by a computer.

Graphically, the recurrent relation described by $f$ is represented through recurrent connections between the neurons of the network.

## How to train RNNs

Given a dataset of input sequences $\{ \underline{x}^{(t)} \}_{t=1}^\tau$ and target output sequences $\{ \underline{y}^{(t)} \}_{t=1}^\tau$ we can train a RNN to learn the IO relationship under the usual supervised learning paradigm.
In particular, we can compare the predictions of the network with the ground truth outputs through a loss function which we minimize iteratively with SGD.
The only issue now is to understand how to compute the gradients w.r.t. the parameters of a RNN. This is done through a very slight variation of the back-propagation algorithm, known as **back-propagation through time**.
In particular, let $o$ be the function which, given the hidden state, computes the output of the network. The prediction of the network at time $t$ is defined by the following recurrent relationship:
$$
\begin{cases}
\hat{\underline{y}}^{(t)} = o(\underline{h}^{(t)}) \\
\underline{h}^{(t)} = f(\underline{x}^{(t)}, \underline{h}^{(t-1)})
\end{cases}.
$$
Once we fix the time step $t$, we can unroll the relationship as a function:
$$
\hat{\underline{y}}^{(t)} = g^{(t)}(\underline{x}^{(1)}, \ldots, \underline{x}^{(t)}).
$$
As usual, we can represent this function as a computational graph and then apply the usual back-propagation algorithm to compute the partial derivative w.r.t each parameter. What we just described is the _back-propagation through time_ algorithm.
Observe that, due to the unrolling, each parameter of the network will be connected to the output through many paths in the computational graph of $g^{(t)}$. As prescribed by the back-propagation equation, we have to sum the derivate obtained on each path. Usually we normalize this sum, scaling it by $\frac{1}{t}$. Observe that the scaling preserves the direction of the gradient.

---

## Issues with long term IO relationships

The back-propagation through time algorithm has issues when we want to learn long term IO relationships (i.e. the output at time $t$ depends on the input at time $t-k$ with $k \gg 1$) and $f$ is modeled as a standard FFNN.
The issue is related to vanishing gradient.

To better understand the problem let's consider a simpler model, with scalar input, scalar hidden state and scalar output.
In particular:
$$
\begin{cases}
h^{(t)} = a_s(v \cdot h^{(t-1)} + w \cdot x^{(t)}) \\
\hat{y}^{(t)} = a_o(u \cdot h^{(t)})
\end{cases}.
$$
To compute the derivatives on the different paths we assign a different variable to different replicas of the same weight in the computational graph. In particular we denote with $v_t, w_t$ the parameters in the replica of the network used to compute $h^{(t)}$ from $h^{(t-1)}$ and $x^{(t)}$.
Let $e$ be the error function for each sample. Then:
$$
\frac{\partial e(y^{(t)}, \hat{y}^{(t)})}{\partial w_{t-k}} = \frac{\partial e}{\partial \hat{y}} a_o'(u \cdot h^{(t)}) u \prod_{d=1}^{k} a_s'(v_{t-d+1} \cdot h^{(t-d)} + w_{t-d+1} \cdot x^{(t-d+1)}) v_{t-d+1}
$$
$$
\cdot a_s'(v_{t-k} \cdot h^{(t-k-1)} + w_{t-k} \cdot x^{(t)}) x^{(t)}.
$$
Observe that, if $a_s$ has gradients with magnitude less than $1$ (as it happens for hyperbolic tangent or sigmoid), then the term
$$
\prod_{d=1}^{k} a_s'(v_{t-d+1} \cdot h^{(t-d)} + w_{t-d+1} \cdot x^{(t-d+1)}) v_{t-d+1}
$$
goes to 0 as $k$ gets big.

An alternative activation could be the ReLU function. But it has null gradients for negative inputs, thus the gradient would not flow in time up to the first time step in which the pre-activation is negative.

Another approach is to use a linear activation for $a_s$. Here we do NOT have the vanishing gradient problem, but the behavior of the network would "simply" be to accumulate the input.

---

## Dealing with the vanishing gradient problem

### Long Short-Term Memories (LSTM)

**LSTMs** solve the problem of vanishing gradient designing a memory cell which allows to _write_, _keep_, and _read_ information. This implemented through logistic and linear units with multiplicative interactions.

A gating mechanism allows to determine the operations to execute on the memory.
- Information gets into the cell whenever its _write_ gate is on.
- Information stays in the cell as long as the _keep_ gate is on.
- Information is read from the cell by turning on its _read_ gate.

(_We're going to use a different notation w.r.t. what we used so far_). The hidden state of a LSTM is composed of two vectors: the **cell state** $C_t$ and the **output** $h_t$.

The **keep gate** is
$$
f_t = \sigma(W_f \text{stack}(h_{t-1}, x_t) + b_f)
$$
which takes value 1 for the part of the cell state that we have to keep, and 0 for the part of the cell state that we have to forget.
Indeed, the **cell state recursion** is
$$
C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t
$$
where $\tilde{C}_t$ is a proposal for the new cell state and $i_t$ is the **write gate**. In particular:
$$
i_t = \sigma(W_i \text{stack}(h_{t-1}, x_t) + b_i)
$$
and
$$
\tilde{C}_t = \tanh(W_C \text{stack}(h_{t-1}, x_t) + b_C).
$$
The expression for the output $h_t$ is controlled by the **read gate**
$$
o_t = \sigma(W_o \text{stack}(h_{t-1}, x_t) + b_o)
$$
and by the current state of the cell:
$$
h_t = o_t \odot \tanh(C_t).
$$

---

### Gated Recurrent Unit (GRU)

**GRU** is a slight variation of LSTM in which the keep and write gates are merged into a single update gate $z_t$ and the cell state and hidden state are merged in $h_t$. There are also some other modifications. The resulting equations are:
$$
\begin{cases}
z_t = \sigma(W_z \text{stack}(h_{t-1}, x_t)) \\
r_t = \sigma(W_r \text{stack}(h_{t-1}, x_t)) \\
\tilde{h}_t = \tanh(W \text{stack}(r_t \odot h_{t-1}, x_t)) \\
h_t = (1-z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t
\end{cases}.
$$

## Bidirectional RNNs

Due to the structure of the recurrence $\underline{h}^{(t)} = f(\underline{x}^{(t)}, \underline{h}^{(t-1)})$, RNNs learn IO relationships which are **causal**, i.e. the predicted output $\hat{\underline{y}}^{(t)}$ depends only on the values in the input sequence from time $1$ to time $t$. Sometimes we want to do predictions exploiting the information in the whole sequence (even future values). We can do so through bi-directional RNNs. We use two RNNs, one that runs "forward" and computes the hidden state $\underline{h}^{(t)} = f_1(\underline{x}^{(t)}, \underline{h}^{(t-1)})$ and the other which runs "backward" and computes the hidden state $\underline{g}^{(t)} = f_2(\underline{x}^{(t)}, \underline{g}^{(t+1)})$. At the end, the prediction at time $t$ depends on both $\underline{h}^{(t)}$ and $\underline{g}^{(t)}$:
$$
\hat{\underline{y}}^{(t)} = o(\underline{h}^{(t)}, \underline{g}^{(t)}).
$$

## Initialization

When initializing RNNs, we need to specify an initial state $\underline{h}^{(0)}$.
We could choose a fixed value as initialization like $\underline{h}^{(0)}$. However it is better to treat the initial state as a **learnable parameter vector** which we can optimize through back-propagation.

