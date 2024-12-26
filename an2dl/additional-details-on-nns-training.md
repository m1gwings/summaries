---
marp: true
theme: summary
math: mathjax
---
# Additional details on NNs training

<div class="author">

Cristiano Migali

</div>

## Limiting overfitting

### Early stopping

Consider a graph with the number of iterations of GD on the $x$-axis vs the training and validation error of the parameters at the given iteration, respectively $E_\text{train}(\theta^{(k)})$ and $E_\text{val}(\theta^{(k)})$, on the $y$-axis.
Overfitting networks show on this kind of graphs the following behavior: the <u>training error</u> decreases monotonically with the number of gradient descent iterations $k$ (we obtain the same behavior if we average multiple runs of SGD). At the beginning, also the <u>validation error</u> decreases with the number of iterations; but at some point the network "looses generalization". In particular there is an iteration after which the validation error starts increasing. At this point the additional training iterations are only worsening the performance of our model, since, as remarked many times, we're interested in generalization.
To alleviate the problem, we can adopt a technique known as **early stopping**. It works as follow: we keep track of the last iteration $k_\text{ES}$ in which we obtained a new minimum for the validation error; if we don't get a new minimum after a certain number of iterations (i.e. the validation error isn't decreasing), we stop the training and restore the parameters $\theta^{(k_\text{ES})}$.

### Weights regularization

Regularization is about constraining the model "freedom", based on a-priori assumptions. So far we've learned the parameters of our NNs by maximizing data likelihood:
$$
\theta_\text{MLE} = \arg \max_\theta p(\mathcal{D}|\theta).
$$
We can reduce model "freedom" by using a _Bayesian approach_ known as **Maximum A-Posteriori Estimation**:
$$
\theta_\text{MAP} = \arg \max_\theta p(\theta | \mathcal{D}) = \arg \max_\theta p(\mathcal{D}|\theta) \cdot p(\theta).
$$
The difference w.r.t. ML estimation is that we've introduced a prior $p(\theta)$ on the parameters, i.e. we've defined a-priori which parameters are likely and which are not. One usual assumption is that the weights of our models should be small. This is enforced as follows:
$$
p(\theta) = \mathcal{N}(\theta|0, \sigma_\theta^2).
$$

---

Let's see the impact on the loss function:
$$
\theta_\text{MAP} = \arg \max_\theta p(\mathcal{D}|\theta) p(\theta)
$$
$$
= \arg \max_\theta \prod_{i=1}^N \frac{1}{\sqrt{2 \pi} \sigma} \exp\left(-\frac{(t_i - \text{FFN}(x_i|\theta))}{2 \sigma^2}\right) \prod_{q=1}^Q \frac{1}{\sqrt{2 \pi} \sigma_\theta} \exp\left( -\frac{\theta_q^2}{2 \sigma^2_\theta} \right)
$$
$$
= \arg \min_\theta \left[ \sum_{i=1}^N \frac{(t_i - \text{FFNN}(x_i|\theta))^2}{2 \sigma^2} + \sum_{q=1}^Q \frac{\theta_q^2}{2 \sigma_\theta^2} \right]
$$
$$
= \arg \min_\theta \left[ \sum_{i=1}^N (t_i - \text{FFNN}(x_i|\theta))^2 + \gamma \sum_{q=1}^Q \theta_q^2 \right]
$$
where $\gamma = \frac{\sigma^2}{\sigma_\theta^2}$.
The _new term_ in the loss function:
$$
\gamma \sum_{q=1}^Q \theta_q^2
$$
is known as **regularization**. Observe that the larger is $\gamma$ the stronger is the regularization effect. This can be seen both by looking at the expression of the loss or by looking at the definition of $\gamma$.
The best value for $\gamma$ can be chosen through **hyper-parameters tuning**.

### Dropout

**Dropout** is a regularization technique which tries to approximate _bagging_ [check ML notes for bagging] in a computationally inexpensive manner. Indeed, for large NNs, it is not feasible to apply bagging to build a large ensemble.
In particular, dropout approximates an ensemble constituted of all the sub-networks which we can obtain by removing non-output units from an original topology.
The method works as follows: during each iteration of mini-batch SGD we sample independently one mask value from a Bernoulli distribution for each non-output unit. The success probability of the Bernoulli distribution is an hyper-parameter of the method and allows to tune the strength of the regularization. During the training iteration, the mask values are used to turn off the units for which we sampled a 0. If we organize the mask values inside vectors, one for each layer: $\underline{m}_1, \ldots, \underline{m}_L$, this is achieved by a simple element-wise product of the pre-activation of each layer with the corresponding mask:
$$
\underline{h}_{l+1} = g\left[ (W_{l+1} \underline{h}_l + \underline{b}_{l+1}) \odot \underline{m}_l \right].
$$
This also forces hidden units to learn independent features instead of relying on other units (a phenomenon known as **co-adaptation**).

---

At inference time the predictions of the models in the virtual ensemble are implicitly averaged. In particular we remove all the masks but we also scale the parameters by multiplying all of them by the success probability; this procedure is known as **weight scaling**. This ensure that the expected value of the pre-activation stays the same also at inference time.

## Better activation functions

Activation functions such as sigmoid or hyperbolic tangent suffers of a problem known as **vanishing gradient**. Indeed, their gradient is close to 0 when the input is big in absolute value. Of course having gradients close to 0 is an issue when we want to learn by iteratively minimizing a loss function through gradient descent, since the magnitude of the parameters update at each iteration would become so small to be barely noticeable.
If this wasn't enough, their gradient has value which is always smaller than 1. This is a problem since, as it is clear by the back-propagation equation, gradients are multiplied together as we go through the layers of the networks. Each time we multiply by a number with absolute value smaller than 1, we're reducing the magnitude of the partial product. Then, the gradients w.r.t. parameters that are faraway from the output vanish. This hinders learning in deep networks.
These problems can be solved by choosing different activation functions.

### Rectified Linear Unit

- The **Rectified Linear Unit** (**ReLU**) is defined as:
$$
g(a) = \max(0, a)
$$
> and its derivative is $g'(a) = \mathbb{1}[a > 0]$ for $a \neq 0$.

It has several **advantages** w.r.t. S-shaped activations:
- faster SGD converged (it has been empirically found to be roughly 6 times faster);
- leads to sparse activation (i.e. only some hidden units are activated);
- efficient gradient propagation (there is no vanishing or exploding gradient problems);
- very efficient to compute (we just need to threshold at 0);
- it is scale-invariant: $\max(0, ax) = a \max(0, x)$.

It has potential **disadvantages**:
- it is not-differentiable at zero, however it is differentiable everywhere else;
- it has non-zero centered output;
- it is unbounded (it could potentially blow up);
- it suffer the _dying neurons problem_: ReLU neurons can sometimes be pushed into states in which they become inactive for essentially all inputs. This can happen with very high learning rates. In this state, no gradient flows backward through the neuron, and so the neuron becomes stuck and "dies".

---

### Leaky ReLU

- **Leaky ReLU** tries to fix the "dying ReLU" problem. It was originally defined as:
$$
g(a) = \begin{cases}
a \text{ if } a \geq 0 \\
0.01 a \text{ otherwise}
\end{cases}.
$$

### ELU

- **ELU** tries to make mean activations closer to zero, which speeds up learning. It introduces an additional hyper-parameter $\alpha$ which has to be tuned by hand. In particular, it is defined as:
$$
g(a) = \begin{cases}
a \text{ if } a \geq 0 \\
\alpha (e^a-1) \text{ otherwise}
\end{cases}.
$$

## Weights initialization

The final result of GD is affected by weight initialization.
Let's consider different possible initialization:
- **all zeros**: this initialization doesn't work since all gradients would be zero and no learning would happen;
- **big numbers**: it is a bad idea since, if we're unlucky, it could take very long to converge;
- **sampling from a zero mean isotropic gaussian with small variance** ($\theta^{(0)} \sim \mathcal{N}(0, \sigma^2 = 0.01)$): this initialization is good for small networks, but might lead to problems in deeper NNs as we describe afterwards.

In deeper networks:
- if weights start too small, then gradient shrinks as it passes through each layer;
- if weights start too large, then gradient grows as it passes through each layer until it's too massive to be useful.

A proposal to solve this issue is **Xavier initialization**.

### Xavier initialization

Suppose we have an input $x$ with $I$ components and a linear neuron with random weights $\underline{w}$. Its output is:
$$
h = w_1 x_1 + \ldots + w_I x_I.
$$
Observe that, by applying the well known decomposition $\mathbb{V}\text{ar}[X] = \mathbb{E}[X^2] - \mathbb{E}^2[X]$, we can derive the following formula for independent random variable $X$ and $Y$:
$$
\mathbb{V}\text{ar}[X Y] = \mathbb{V}\text{ar}[X] \mathbb{V}\text{ar}[Y] + \mathbb{V}\text{ar}[X]\mathbb{E}^2[Y] + \mathbb{E}^2[X]\mathbb{V}\text{ar}[Y].
$$

---

If we apply this formula to the product $w_i x_i$ (which it is reasonable to model as the product of independent random variables), we get:
$$
\mathbb{V}\text{ar}[w_i x_i] = \mathbb{E}^2[x_i] \mathbb{V}\text{ar}[w_i] + \mathbb{E}^2[w_i]\mathbb{V}\text{ar}[x_i] + \mathbb{V}\text{ar}[w_i]\mathbb{V}\text{ar}[x_i].
$$
Now, if our inputs and weights both have mean 0, that simplifies to:
$$
\mathbb{V}\text{ar}[w_i x_i] = \mathbb{V}\text{ar}[w_i] \mathbb{V}\text{ar}[x_i].
$$
If we assume all the $w_i$ and all the $x_i$ to be i.i.d., we obtain:
$$
\mathbb{V}\text{ar}[h] = \mathbb{V}\text{ar}[w_1 x_1 + \ldots + w_I x_I] = I \mathbb{V}\text{ar}[w_1] \mathbb{V}\text{ar}[x_i].
$$
This means that the variance of the output equals the variance of the input scaled by $I \mathbb{V}\text{ar}[w]$. If we were to force the variance of the input and the output to be the same, we would set:
$$
I \mathbb{V}\text{ar}[w_1] = 1 \text{ iff } \mathbb{V}\text{ar}[w_1] = \frac{1}{I}.
$$ 
For this reason Xavier proposes the initialization: $w \sim \mathcal{N}(0, \frac{1}{I})$.

### Glorot & Bengio initialization

Performing similar reasoning for the gradient, Glorot & Bengio found the following equation:
$$
O \mathbb{V}\text{ar}[w_1] = 1
$$
where $O$ is the number of neurons in the layer "after" the weights.

To accommodate for both proposals, a usual initialization is:
$$
w \sim \mathcal{N}\left(0, \frac{2}{I+O}\right).
$$

### He initialization

More recently He proposed, for rectified linear units, $w \sim \mathcal{N}\left(0, \frac{2}{I}\right)$.

## Batch normalization

It has been found empirically that networks converge faster if inputs have been normalized and whitened, i.e. they have been transformed in such a way that their covariance matrix is diagonal. Normalization and whitening are beneficial also when applied to the inputs of layers other than the second one.
**Batch normalization** is a technique to cope with this.  

---

In particular it works as follows:
- first of all at the beginning of the training we need to force pre-activations to take values on a unit Gaussian;
- then we add a _batch normalization layer_ after fully connected layers (or convolutional layers), and before non-linearities.

Batch normalization layers work as follows: they take as input the values of the pre-activations in the mini-batch $\mathcal{B} = \{ z_1, \ldots, z_m \}$. They compute the average $\mu_\mathcal{B}$ and the variance $\sigma^2_\mathcal{B}$ of such values. Let $z$ be the input of the batch normalization layer. First of all it is normalized:
$$
\hat{z} = \frac{z - \mu_\mathcal{B}}{\sqrt{\sigma^2_\mathcal{B} + \varepsilon}},
$$
then the normalized value is shifted and rescaled through some learnable parameters:
$$
\text{BN}_{\gamma, \beta}(z) = \gamma \hat{z} + \beta.
$$
Observe that a batch normalization layer has 4 parameters (5 if we consider also the smoothing parameter $\varepsilon$): $\gamma$ and $\beta$ are learnable; $\mu_\mathcal{B}$ and $\sigma_\mathcal{B}^2$ are computed for each mini-batch during training. At inference time we use global statistics for the mean and the variance of each pre-activation as values for $\mu_\mathcal{B}$ and $\sigma_\mathcal{B}^2$. These are computed using training running averages.

The rationale behind the affine linear transformation after normalization is that in this way we allow the network to learn "how much normalization is needed". In particular, it is also possible to learn $\gamma = \sqrt{\mathbb{V}\text{ar}[z]}$ and $\beta = \mathbb{E}[z]$, making the batch normalization layer an identity mapping.

In practice, batch normalization has shown to:
- improve gradient flow through the network;
- allow using higher learning rates, and thus faster learning;
- reduce the strong dependence on weights initialization;
- act as a form of regularization wlightly reducing the need for dropout.

## More about GD

### Nesterov Accelerated Gradient

- **Nesterov Accelerated Gradient** is an alternative of Gradient Descent in which each iteration is split in two phase. First of all we take one "big step" in the direction of the gradient:
$$
\theta^{(k+\frac{1}{2})} = \theta^{(k)} - \alpha \frac{d E}{d \theta}(\theta^{(k)});
$$

---

> then we take a "smaller correction step":
$$
\theta^{(k+1)} = \theta^{(k+\frac{1}{2})} - \eta \frac{d E}{d \theta}(\theta^{(k+\frac{1}{2})}).
$$

### Adaptive Learning Rates

Up to know we use the same learning rate for all the parameters in the network, but gradient magnitudes vary significantly across layers, making different neurons learning at different rates. To account for these problems we can use adaptive learning rates, i.e. different learning rates for different parameters of the network.

Several algorithms of this kind have been propose during the years, like:
- Resilient propagation (Rprop);
- Adaptive Gradient (AdaGrad);
- RMSProp;
- AdaDelta;
- Adam;
- ... .
