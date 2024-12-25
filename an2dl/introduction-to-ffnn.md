---
marp: true
theme: summary
math: mathjax
---
# Introduction to Feed Forward Neural Networks

<div class="author">

Cristiano Migali

</div>

## The Perceptron

- The **perceptron** is a parametric model for classification which tries to mimic in a simplified manner the behavior of a biological neuron in the brain. In particular, the model has the following functional form:
$$
\text{perceptron}(\underline{x} | \underline{w}, b) = g\left(\begin{bmatrix} \underline{w}^T & -b \end{bmatrix} \begin{bmatrix} \underline{x} \\ 1 \end{bmatrix}\right)
$$
> where $g$ is a _non-linear function_ called activation. In the original perceptron model $g = \text{sign}$. $\underline{w}$ are known as **weights**, while $b$ is the **bias**. An input $\underline{x}$ is predicted as belonging to the positive class $+1$ iff $\begin{bmatrix} \underline{w}^T & -b \end{bmatrix} \begin{bmatrix} \underline{x} \\ 1 \end{bmatrix} > 0$.

Let's understand better the relationship between the perceptron and biological neurons. Each neuron is connected to others through _dendrites_. We model this connection with the set of weights $\underline{w}$ which represent the strength of the connections with the other neurons, modeled as inputs. Dendrites collect charges from _synapses_, both _inhibitory_ and _excitatory_ (this is modeled through the sign of the entries in the input vector). The cumulated charge (modeled through the sum of the weighted inputs) is released (this is modeled as the output of the perceptron being $+1$) once a threshold $b$ is passed.

Historically, there are several contributions which led to the development of the perceptron.
- In 1943, Warren McCullog and Walter Harry Pitts proposed the Threshold Logic Unit or Linear Unit: the activation function was a threshold unit equivalent ot the Heaviside step function.
- In 1957, Frank Rosemblatt developed the first perceptron. Weights were encoded in potentiometers, and weight updates during learning were performed by electric motors.
- In 1960, Bernard Widrow introduced the idea of representing the threshold value as a bias term in the ADALINE (Adaptive Linear Neuron or later Adaptive Linear Element).

### Hebbian learning

Up to now we've only described the structure of the perceptron. Of course, to make it capable of solving a classification task, we need to describe a process to find the appropriate values for the weight vector $\underline{w}$ and the bias $b$.

---

It is here that the learning happens and we exploit a dataset of examples.
As for the structure of the model, this process is motivated by a biological analogy: **Hebbian learning**. During his research, Donald Hebb observed that "the stength of a synapse increases according to the simultaneous activation of the relative input and the desired target". Remembering the relationship between the weights and the connections, we can translate Hebbian learning into equations as follows:
$$
w_i^{(k+1)} = w_i^{(k)} + \eta \cdot x_i^{(k)} \cdot t^{(k)}
$$
where $w_i^{(k)}$ is the estimated value for the $i$-th entry of the weight vector at the $k$-th step of the learning process, $x_i^{(k)}$ is the $i$-th entry of the considered input sample, and $t^{(k)}$ is the corresponding target. Finally $\eta$ is known as **learning rate** and regulates the impact of each iteration of the learning process on the values of the weight vector. This hyper-parameter turns out to be irrelevant in this setting, but, as we will see, plays a major role in Feed Forward Neural Networks training. Of course we apply the same update rule for the bias $b$, which we can consider as part of the weight vector if we extend the input by appending an entry with constant value $1$. In particular, we can write the update rule in vectorial form:
$$
\underline{w}_\text{ext}^{(k+1)} = \underline{w}_\text{ext}^{(k)} + \eta \cdot t^{(k)} \cdot \underline{x}_\text{ext} \text{.}
$$
During each step of the process, we apply the update rule considering a miss-predicted sample $(\underline{x}^{(k)}, t^{(k)})$, i.e. a sample for which $\text{perceptron}(\underline{x}^{(k)}|\underline{w}^{(k)}, b^{(k)}) \neq t^{(k)}$. The process ends when all the samples in the dataset are correctly classified.

It is possible to show that, if there is an extended weight vector $\underline{w}^*_\text{ext}$ which correctly classify all the samples, then the procedure will converge. We've NO guarantee of converging always to the same set of weights, indeed there could be multiple "optimal" weight vectors.
Furthermore, such an $\underline{w}_\text{ext}^*$ exists iff the classes in the dataset are linearly separable, i.e. there is at least one hyperplane which induces an half-space that contains all and only the samples of one of the two classes (this implies that the symmetric half-space contains all and only the samples of the other class).

The result we just stated in the greatest weakness of the perceptron: it does not work anymore if the dataset isn't linearly separable; and this happens very often in practice.

#### Formal derivation of the Hebbian learning rule

[Read ML notes: "Linear classification", p. 5.](http://localhost:8080/ml/linear-classification.md#5)

---

## Feed Forward Neural Networks

As we remarked, the inability of the perceptron to handle non-linear datasets is due to the fact that it is a linear classifier. Indeed, the score which determines how a sample will be classified, i.e. the scalar product on which we apply the $\text{sign}$ function, is linear w.r.t. the features of the input. **Feed Forward Neural Networks** try to solve this issue by introducing non-linearities in this relationship.

- In particular a **Feed Forward Neural Network** (**FFNN**) is a layered model in which each layer takes a vector as input and produces one vector with size $s_l$ as output.

> The input of the first layer is the input of the model $\underline{x}$, while the output of the last layer $\underline{h}_L$ is the output of the model. Each layer performs the following computation:
$$
\underline{h}_{l+1} = g\left( \begin{bmatrix} \underline{w}_{l+1, 1}^T \underline{h}_l  \\ \vdots \\ \underline{w}_{l+1,s_{l+1}}^T \underline{h}_l \end{bmatrix} + \begin{bmatrix} b_{l+1,1} \\ \vdots \\ b_{l+1,s_{l+1}} \end{bmatrix} \right)
$$
> where $g : \mathbb{R} \rightarrow \mathbb{R}$ is a non-linear activation function which we apply element-wise. We can  imagine each layer as $s_l$ perceptrons stacked together, each taking as input the output of the previous layer.

FFNNs are usually represented graphically as follows:
<p align="center">
    <img src="static/ffnn.svg"
    width="400mm" />
</p>

Observe that each layer (after the fist) has the following number of parameters:
$$
s_{l-1} \cdot s_l + s_l = (s_{l-1} + 1) s_l \text{;}
$$
for the number of parameters in the first layer we've to substitute $s_{l-1}$ with $I$ which is the dimensionality of the input.

---

### Activation functions

There are several activation functions which we can choose for each layer of the network depending on our needs.

#### Linear activation

- The **linear activation** function is $g(a) = a$; its _derivative_ is $g'(a) = 1$.

This activation is used in the last layer when we're facing a regression task since its range is the whole $\mathbb{R}$.

This activation is almost never used for intermediate layers since it's possible to show that the composition of linear functions is still linear, hence, the additional intermediate layer employing this activation function would not add expressive power to the model.

#### Sigmoid activation

- The **sigmoid activation** function is
$$
g(a) = \frac{1}{1+\exp(-a)}
$$
> and its derivative is $g'(a) = g(a)(1 - g(a))$.

This function has range $(0, 1)$, for this reason it is used for binary classification problems where the positive class is associated with $1$, while the negative is associated with $0$. When the input is $0$, $g(0) = \frac{1}{2}$. Furthermore it is differentiable; we will see that this property is essential for the training process to work.

#### Hyperbolic tangent activation

- The **hyperbolic tangent activation** function is:
$$
g(a) = \frac{\exp(a) - \exp(-a)}{\exp(a) + \exp(-a)}
$$
> and its derivative is $g'(a) = 1 - g^2(a)$.

This activation has very similar properties w.r.t. the sigmoid. It differs for the range which is $(-1, 1)$ and, for this reason, it is used for binary classification problems where the positive class is associated with $1$, while the negative class is associated with $-1$.

---

#### Softmax activation

- The **softmax activation** function takes as input a vector (which is the "pre-activation" of the last layer) and produces a vector as output. In particular, the $k$-th output is:
$$
h_k = \frac{\exp(z_k)}{\sum_{j=1}^s \exp(z_j)}.
$$

Each entry in the output produced by this activation takes value in $(0, 1)$. Furthermore the sum of the entries is always $1$. For this reason the results of this activation are interpreted as probability vectors. In particular, we use the softmax activation when we're dealing with a multi-class classification problem in which the targets are one-hot encoded.

### Approximation properties of FFNNs

There is a theoretical result which guarantees the expressiveness of FFNNs. It takes the name of Universal Approximation Theorem (for FFNNs), or UAT for short.
In particular, it states the following: "a single hidden layer FFNN with S shaped activation functions (like sigmoid or hyperbolic tangent) can approximate any measurable function to any desired degree of accuracy on a compact set".
In short, regardless the function we are learning, a FFNN with a single hidden layer can represent it.
**Important**:
- it doesn't mean that a learning algorithm can find the right weights which approximate the desired function;
- the relationship between the inverse of the approximation error and the number of neurons in the hidden layer could be exponential or worse, furthermore we do NOT know a priori how many neurons are sufficient for the task at hand.

### Training of FFNNs

As for the perceptron, given a dataset of examples $\mathcal{D} = \{ (x_1, t_1), \ldots, (x_N, t_N) \} \subseteq \mathcal{X} \times \mathcal{T}$, we need to describe a process to find (_learn_) the right set of weights and biases which allow the given FFNN topology to carry out the desired task.

#### Statistical motivations

The training process in the supervised learning setting is motivated under the following statistical assumptions.

##### Regression

In the regression setting we assume that:
$$
t_i|x_i \sim \mathcal{N}(\text{FFNN}(x_i|\theta^*), \sigma^2) \text{,}
$$

---

that is, there exists a set of "_true_" parameters $\theta^*$ s.t. the conditional distribution of the target given the input is gaussian with mean corresponding to the output of the network and variance $\sigma^2$.

To estimate (learn) the parameters $\theta^*$ we can rely on the usual maximum likelihood estimation framework. In particular, the likelihood function is:
$$
L(\theta, \sigma^2) = \prod_{i=1}^N \mathcal{N}(t_i | \text{FFNN}(x_i|\theta), \sigma^2).
$$

Then:
$$
\log L(\theta, \sigma^2) = - \frac{1}{2 \sigma^2} \sum_{i=1}^N (t_i - \text{FFNN}(x_i | \theta))^2 + N \log\left( \frac{1}{\sqrt{2 \pi} \sigma} \right).
$$

Observe that maximizing the log-likelihood w.r.t. $\theta$ is equivalent to minimizing the following **loss function**:
$$
E(\theta) = \text{SSE}(\theta) = \sum_{i=1}^N (t_i - \text{FFNN}(x_i|\theta))^2.
$$
This is known as **Sum of Squares Error** (**SSE**).
The learning process consists "simply" in minimizing the above loss. Before describing how this is done, let's tackle the loss function for classification problems.

##### Classification

The assumptions for the classification problem are similar, in particular, for binary classification we have:
$$
t_i|x_i \sim \text{Be}(\text{FFNN}(x_i|\theta^*)).
$$
Observe that the expression above is well defined if the FFNN has a single neuron in output with sigmoid activation.

In this case:
$$
L(\theta) = \prod_{i=1}^N \text{Be}(t_i | \text{FFNN}(x_i | \theta)) = \prod_{i=1}^N \text{FFNN}(x_i|\theta)^{t_i} (1 - \text{FFNN}(x_i|\theta))^{1-t_i}.
$$
Then:
$$
\log L(\theta) = \sum_{i=1}^N \left[ t_i \log \text{FFNN}(x_i|\theta) + (1-t_i)\log (1-\text{FFNN}(x_i|\theta))\right].
$$

---

Observe that maximizing the log-likelihood w.r.t. $\theta$ is equivalent ot minimizing the following **loss function**:
$$
E(\theta) = \text{CCE}(\theta) = - \sum_{i=1}^N \left[ t_i \log \text{FFNN}(x_i|\theta) + (1-t_i)\log (1-\text{FFNN}(x_i|\theta))\right].
$$
This is known as **Categorical Cross-Entropy**.

#### Minimizing the loss function

As we've seen, training FFNNs consists in minimizing loss functions of the form:
$$
E(\theta) = \sum_{i=1}^N e(t_i, \text{FFNN}(x_i|\theta))
$$
where $e(t, p) : \mathbb{R}^{s_L} \times \mathbb{R}^{s_L} \rightarrow \mathbb{R}^+_0$ computes the error of the prediction $p$ knowing the ground truth target $t$.
In particular, we carry out such minimization iteratively, through **gradient descent** (**GD**). The update rule is:
$$
\theta^{(k+1)} = \theta^{(k)} - \eta \cdot \frac{d E(\theta)}{d \theta} (\theta^{(k)}) = \theta^{(k)} - \eta \cdot \sum_{i=1}^N \frac{d}{d \theta} \left[ e(t_i, \text{FFNN}(x_i | \theta)) \right](\theta^{(k)}).
$$
This approach introduces some new problems that we have to handle, namely: **initialization** (i.e. the choice of the initial set of parameters $\theta^{(0)}$), **stopping condition** (i.e. a criterion which tells us when we can stop applying the iterative rule), and, the most important, **computing the required derivatives**.

In the general GD setting, _initialization_ is done by random sampling. As we will see, for the special case of NNs training, some care has to be taken.
The same holds for the _stopping condition_: in the usual GD setting we fix a certain number of iterations a-priori. This can be done also for NNs training, but additional conditions are often considered to improve the quality of the obtained model.
We will provide the missing details in a separated set of notes, namely "Additional details on NNs training".

##### Computing derivatives

The computation of derivatives is carried out through a set of techniques which take the name of **automatic differentiation** (**AD**). [_For more details check the NAML summaries_].
Automatic differentiation allows to compute the exact value of the derivative of a function w.r.t. one of its input variables, evaluated at a certain point. The "only" requirement of AD techniques is the knowledge of the _computational graph_ of the function, which is a representation of the function as a DAG in which each node represents an intermediate result of the computation obtained by applying an _elementary function_, i.e. a function for which we know the analytical expression for all its partial derivatives, to the intermediate results associated with its predecessors.

---

The nodes with no predecessors represent the inputs of the function, while the nodes with no successors represent the outputs of the function.
Let $v_1$ and $v_2$ be the intermediate results associated to two nodes in the computational graph, then, it follows (not directly) from the chain rule that:
$$
\frac{\partial v_1}{\partial v_2} = \sum_{P \text{ path from } v_2 \text{ to } v_1} \ \prod_{(u, w) \in P} \frac{\partial w}{\partial u}.
$$
$\frac{\partial w}{\partial u}$ takes the name of **derivative on the edge**, indeed we can associate each edge on the DAG with one such derivative, and it's also useful to write its expression directly on top of the corresponding edge in the DAG. This makes it easier to find the overall expression stated before.
Usually, the value of derivatives on the edge depend on intermediate values used in the computation of the function. For this reason we carry out automatic differentiation in the following way.
- In the **forward step** we compute all the intermediate results till the outputs.
- In the **backward step** we cumulate by multiplying together the values of the derivatives on the edge (which we can now compute having all the intermediate results) starting from the output and reaching the desired node w.r.t. which we want to differentiate. This is done for each path from the output to the desired node; the results for different paths are summed together, as prescribed by the previous expression.

This process is what is nowadays called **back-propagation**. Observe that back-propagation rules were originally derived starting from a very different setting. Nevertheless it has been found a-posteriori that the original process was equivalent to iterative minimization with gradient descent in which derivatives are computed by AD (as we just described).

Finally, observe that the usual representation of FFNNs (which we depicted previously) is very similar to a computational graph. The main difference is that, since we want to differentiate w.r.t. weights and biases, these should appear as nodes since they would corresponds to inputs of the function. Luckily this is a minor issue, indeed, when we are differentiating w.r.t. a certain weight, we can treat all the others as fixed constants. The only thing that we have to keep in mind is that, in the last step of the process, i.e. when we reach the edge corresponding to the weight w.r.t. we are differentiating during the backward step, the derivative on the edge is w.r.t. that weight, instead of being w.r.t. the variable associated with the predecessor node.

---

##### GD variations

Gradient descent is rarely implemented exactly as we described it before.

- **Momentum**: one common variation is _momentum_, which allows to avoid some local minima. The update rule becomes:
$$
\theta^{(k+1)} = \theta^{(k)} - \eta \cdot \frac{d E}{d \theta}(\theta^{(k)}) - \alpha \cdot \frac{d E}{d \theta}(\theta^{(k-1)}).
$$
> In this way we keep some inertia in parameters update.

- **SGD**: another variation which is always adopted is _Stochastic Gradient Descent_. For large datasets (i.e. $N \gg 1$), the computation of $\frac{d E}{d \theta}$ becomes prohibitively expensive since it scales linearly with $N$.

> This problem is alleviated as follows: instead of considering all the samples of the dataset when computing the loss, we randomly select a subset of them at each iteration. In particular, if the subset has size $1$ we get the original SGD, if the subset has a size greater than $1$, but smaller than $N$, we name it **mini-batch gradient descent**.
In analogy with these conventions, the original gradient descent is also known as **Batch gradient descent**.
