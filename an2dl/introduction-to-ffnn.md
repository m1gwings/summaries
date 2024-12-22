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
\text{perceptron}(\underline{x} | \underline{w}, b) = h\left(\begin{bmatrix} \underline{w}^T & -b \end{bmatrix} \begin{bmatrix} \underline{x} \\ 1 \end{bmatrix}\right)
$$
> where $h$ is a _non-linear function_ called activation. In the original perceptron model $h = \text{sign}$. $\underline{w}$ are known as **weights**, while $b$ is the **bias**. An input $\underline{x}$ is predicted as belonging to the positive class $+1$ iff $\begin{bmatrix} \underline{w}^T & -b \end{bmatrix} \begin{bmatrix} \underline{x} \\ 1 \end{bmatrix} > 0$.

Let's understand better the relationship between the perceptron and biological neurons. Each neuron is connected to others through _dendrites_. We model this connection with the set of weights $\underline{w}$ which represent the strength of the connections with the other neurons, modeled as inputs. Dendrites collect charges from _synapses_, both _inhibitory_ and _excitatory_ (this is modeled through the sign of the entries in the input vector). The cumulated charge (modeled through the sum of the weighted inputs) is released (this is modeled as the output of the perceptron being $+1$) once a threshold $b$ is passed.

Historically, there are several contributions which led to the behavior of the perceptron.
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
where $w_i^{(k)}$ is the estimated value for the $i$-th entry of the weight vector at the $k$-th step of the learning process, $x_i^{(k)}$ is the $i$-th entry of the considered input sample, and $t^{(k)}$ is the corresponding target. Finally $\eta$ is known as **learning rate** and regulates the impact of each iteration of the learning process on the values of the weight vector. This hyper-parameter turns out to be irrelevant in this setting, but, as we will see, plays a major role in Feed Forward Neural Networks training. Of course we apply the same update rule for the bias $b$, which we can consider as part of the weight vector if we extend the input by append an entry with constant value $1$. In particular, we can write the update rule in vectorial form:
$$
\underline{w}_\text{ext}^{(k+1)} = \underline{w}_\text{ext}^{(k)} + \eta \cdot t^{(k)} \cdot \underline{x}_\text{ext} \text{.}
$$
During each step of the process we apply the update rule considering a miss-predicted sample $(\underline{x}^{(k)}, t^{(k)})$, i.e. a sample for which $\text{perceptron}(\underline{x}^{(k)}|\underline{w}^{(k)}, b^{(k)}) \neq t^{(k)}$. The process ends when all the samples in the dataset are correctly classified.

It is possible to show that, if there is an extended weight vector $\underline{w}^*_\text{ext}$ which correctly classify all the samples, then the procedure will converge. We've NO guarantee of converging always to the same set of weights, indeed there could be multiple "optimal" weight vectors.
Furthermore, such an $\underline{w}_\text{ext}^*$ exists iff the classes in the dataset are linearly separable, i.e. there is at least one hyperplane which induces an half-space that contains all and only the samples of one of the two classes (this implies that the symmetric half-space contains all and only the samples of the other class).

The result we just stated in the greatest weakness of the perceptron: it down not work anymore if the dataset isn't linearly separable; and this happens very often in practice.

## Feed Forward Neural Networks

As we remarked, the inability of the perceptron to handle non-linear datasets is due to the fact that it is a linear classifier. Indeed, the score which determines how a sample will be classified, i.e. the scalar product on which we apply the $\text{sign}$ function, is linear w.r.t. the features of the input. **Feed Forward Neural Networks** try to solve this issue by introducing non-linearities in this relationship.

- In particular a **Feed Forward Neural Network** (**FFNN**) is a layered model in which each layer takes a vector as input and produces one with size $s_l$ as output.

---

> The input of the first layer is the input of the model $\underline{x}$, while the output of the last layer $\underline{h}_L$ is the output of the model. Each layer performs the following computation:
$$
\underline{h}_{l+1} = g\left( \begin{bmatrix} \underline{w}_{l+1, 1}^T \underline{h}_l  \\ \vdots \\ \underline{w}_{l+1,s_{l+1}}^T \underline{h}_l \end{bmatrix} + \begin{bmatrix} b_{l+1,1} \\ \vdots \\ b_{l+1,s_{l+1}} \end{bmatrix} \right)
$$
> where $g : \mathbb{R} \rightarrow \mathbb{R}$ is a non-linear activation function. We can  imagine each layer as $s_l$ perceptrons stacked together, each taking as input the output of the previous layer.

FFNNs are usually represented graphically as follows:
<p align="center">
    <img src="static/ffnn.svg"
    width="400mm" />
</p>

Observe that each layer (after the fist) has the following number of parameters:
$$
s_{l-1} \cdot s_l + s_l = (s_{l-1} + 1) s_l \text{;}
$$
for the number of parameters in the first layer we've to substitute $s_{l-1}$ with $I$ which is the cardinality of the input.

### Activation functions

There are several activation functions which we can choose for each layer of the network depending on our needs.

#### Linear activation

- The **linear activation** function is $g(a) = a$; its _derivative_ is $g'(a) = 1$.

This activation is used in the last layer when we're facing a regression task since its range is the whole $\mathbb{R}$.

---

This activation is almost never used for intermediate layers since it's possible to show that the composition of linear functions is still linear, hence, the additional intermediate layer employing this activation function would not add expressive power to the model.

#### Sigmoid activation

- The **sigmoid activation** function is
$$
g(a) = \frac{1}{1+\exp(-a)}
$$
> and its derivative is $g'(a) = g(a)(1 - g(a))$.

This function has range $(0, 1)$, for this reason is for binary classification problems where the positive class is associated with $1$, while the negative is associated with $0$. When the input is $0$, $g(0) = \frac{1}{2}$. Furthermore it is differentiable; we will see that this property is essential for the training process to work.

#### Hyperbolic tangent activation

- The **hyperbolic tangent activation** function is:
$$
g(a) = \frac{\exp(a) - \exp(-a)}{\exp(a) + \exp(-a)}
$$
> and its derivative is $g'(a) = 1 - g^2(a)$.

This activation are very similar properties w.r.t. the sigmoid. It differs for the range which is $(-1, 1)$ and, for this reason, it is used for binary classification problems where the positive class is associated with $1$, while the negative class is associated with $0$.

#### Softmax activation

- The **softmax activation** function takes as input a vector (which is the "pre-activation" of the last layer) and produces a vector as output. In particular, the $k$-th output is:
$$
h_k = \frac{\exp(z_k)}{\sum_{j=1}^s \exp(z_j)}.
$$

Each entry in the output produced by this activation takes value in $(0, 1)$. Furthermore the sum of the entries is always $1$. For this reason the results of this activation are interpreted as probability vectors. In particular, we use the softmax activation when we're dealing with a multi-class classification problem in which the targets are one-hot encoded.

---

### Approximation properties of FFNNs

There is a theoretical result which guarantees the expressiveness of FFNNs. It takes the name of Universal Approximation Theorem (for FFNNs), or UAT for short.
In particular, it states the following: "a single hidden layer FFNN with S shaped activation functions (like sigmoid or hyperbolic tangent) can approximate any measurable function to any desired degree of accuracy on a compact set".
In short, regardless the function we are learning, a FFNN with a single hidden layer can represent it.
**Important**:
- it doesn't mean that a learning algorithm can find the right weights which approximates the desired function;
- the relationship between the inverse of the approximation error and the number of neurons in the hidden layer could be exponential or more, furthermore we do NOT know a priori how many neurons are sufficient for the task at hand.
