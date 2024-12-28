---
marp: true
theme: summary
math: mathjax
---
# Convolutional Neural Networks

<div class="author">

Cristiano Migali

</div>

## The feature extraction perspective

Before introducing the new model this set of slides are about, i.e. convolutional neural networks, let's understand the reasons which led to its development.

Because of the challenges we discussed in the set of notes about image classification, we can't feed image directly to a classifier.
In particular, we need to extract features in order to _reduce dimensionality_ and _extract meaningful information_. A good set of features should map images belonging to the same category to the same region of the feature space.

The usual approach is to define an **"hand crafted" feature extraction** algorithm.
This approach has several **pro**s:
- it allows to exploit _expert information_;
- features are _intrinsically interpretable_;
- you can _adjust features_ to improve your performance;
- we introduce the bias of our model but we also reduce the variance, thus a limited amount of training data is needed.

But there are also some **con**s:
- it requires a lot of _design/programming efforts_;
- it is _not viable_ in many _visual recognition_ tasks (e.g. on natural images) which are easily performed by humans;
- there is a _risk of overfitting_ the training set used in the design;
- it is _NOT very general and "portable"_.

The alternative is provided by **data-driven features**. The idea is to learn also the right set of features from the data, as prescribed by the deep learning approach.
Convolutional neural networks allow to do so.

## The model

### Convolution

The basic building block of convolutional neural networks is the **convolution operation**. Convolution is a linear, spatially local transformation equivalent to correlation. The only difference between the two is the relationship between the weights in the filter and the entries of the input tensor. In particular, in convolution:
$$
(I \ast w)(r, c) = \sum_{(u, v) \in U} w(u, v) I(r-u, c-v).
$$

---

Convolution is defined up to the "filter flip" for the Fourier Theorem to apply.
From our perspective the two operations are exactly equivalent, indeed, as it's usual in ML, we will learn the set of weights in the filter from data, thus the only requirement is to be consistent at training and inference time.
Indeed in practice, in CNN arithmetic there is no flip!

#### Convolution output close to image boundaries

We haven't tackled yet the problem of computing convolution output close to image boundaries, in particular for output entries $(r, c)$ s.t. $(r+u, c+v) \not \in \text{indices}(I)$ for some $(u, v) \in U$.

We can solve the problem in 3 different ways, which are known as **valid**, **same**, and **full**.

- In the **valid** approach we simply reduce the dimensionality of the output in such a way that all the input regions used to compute output entries are fully inside the original image. In particular, let $U = \{ -\lfloor \frac{H}{2} \rfloor, -(\lfloor \frac{H}{2} \rfloor-1), \ldots, \lfloor \frac{H}{2} \rfloor-1, \lfloor \frac{H}{2} \rfloor \} \times \{ -\lfloor \frac{W}{2} \rfloor, \ldots, \lfloor \frac{W}{2} \rfloor \}$ for $H, W \in \{ 2n-1 \ | \ n \in \mathbb{Z}^+ \}$.
> Then:
$$
r+u \geq 1 \ \forall (u, \cdot) \in U \text{ iff } r \geq 1 + \lfloor \frac{W}{2} \rfloor;
$$
$$
r+u \leq R \ \forall (u, \cdot) \in U \text{ iff } r \leq R - \lfloor \frac{W}{2} \rfloor.
$$
> Thus the number of rows in output is $R - \lfloor \frac{W}{2} \rfloor - 1 - \lfloor \frac{W}{2} \rfloor + 1 = R - 2 \lfloor \frac{W}{2} \rfloor = R - W + 1$.
Analogously the number of columns in the output is $C - H + 1$.

- In the **same** approach the output has the same dimensionality of the input. This is achieved through **padding**, i.e. we assume that the image takes value 0 for coordinates outside of $\{ 1, \ldots, R \} \times \{ 1, \ldots, C \}$.

- In the **full** approach we use padding and compute all output entries for which the corresponding region in the input space intersects with the original image for at least one pixel. In particular, consider the same neighborhood we described for the valid approach. Then, we have to impose:
$$
\exists (u, \cdot) \in U \text{ s.t. } r+u \geq 1 \text{ iff } r \geq 1 - \lfloor \frac{W}{2} \rfloor;
$$
$$
\exists (u, \cdot) \in U \text{ s.t. } r+u \leq R \text{ iff } r \leq R + \lfloor \frac{W}{2} \rfloor.
$$
> Thus the number of rows in output is $R + \lfloor \frac{W}{2} \rfloor - 1 + \lfloor \frac{W}{2} \rfloor + 1 = R + W - 1$.

---

> Analogously, the number of columns in output is $C + H - 1$.

### The typical architecture of a CNN

CNNs are typically made of blocks that include:
- convolutional layers;
- non-linearities (activation functions);
- pooling layers (sub-sampling/max-pooling).

An image passing through a CNN is transformed in a sequence of volumes. In particular the depth of the volume is given by the number of channels of the 3D tensor; the number of rows $R$ and columns $C$ form what is known as the _spatial extent_.
Stage after stage the depth of the volume is increased, while the height and width of the volume decreases. Each layer takes a volume in input and returns one as output.

#### Convolutional layers

**Convolutional layers** return the convolution of the input volume with $N_F$ learnable filters: $w_1, \ldots, w_f$. In particular, each convolution with a filter produces a 2D tensor, all these tensors are stacked together forming a volume with depth $N_F$.
Each slice of the volume is adjusted by adding a bias term which is the same for all the entries of the slice.
In particular, let $I$ be the input volume with $K$ channels and $O$ the output volume, they're linked by the following relationship:
$$
O(r, c, l) = \sum_{k=1}^K \sum_{(u, v) \in U} w_l(u, v, k) \cdot I(r+u, c+v, k) + b_j.
$$
Each filter needs to have the same number of channels as the input for the convolution to be well defined. Furthermore all filters are defined over the same neighborhood $U$.
The neighborhood $U$ and the number of filters $N_F$ are hyper-parameters of the layer.

Let's count the number of parameters of a convolutional layer. Consider the usual neighborhood describing a rectangle with width $W$ and height $H$. Each filter has $W \cdot H \cdot K$ parameters, there $N_F$ filters and each output channel has an additional bias term. In total we have
$$
N_F \cdot W \cdot H \cdot K + N_F = N_F(W \cdot H \cdot K + 1)
$$
parameters.
Observe that, due to the dependence with $K$, layer with the same hyper-parameters ($U$ and $N_F$), can have a different number of parameters depending on where these are located in the network.

---

##### Strides

Another hyper-parameter of convolutional layers in CNNs is the **number of strides**.
In particular we need to specify the number of strides w.r.t. the rows and the columns, which we can represent as a couple $(s_r, s_c)$. The number of strides allows to select only a portion of the usual output, in particular, we keep only the rows with index 1 modulo $s_r$ and the columns with index 1 modulo $s_c$ (assuming we start counting from 1). Thus, if we set the number of strides to $(1, 1)$, we get the usual convolution.

#### Activation layers

**Activation layers** introduce non-linearities in the network, otherwise a CNN would be equivalent to a linear classifier.
As we've already seen, activation functions are scalar functions, namely they operate one ach single value of the volume. Thus, activations don't change volume size.

Activation functions often used in CNNs are ReLU and leaky ReLU while hyperbolic tanget or sigmoid are mostly popular in FFNNs architectures.

#### Pooling layers

**Pooling layers** reduce the spatial extent of the volume.
A pooling layer operates independently on every depth slice of the input volume and resizes it spatially.
In particular each output entry is obtained by applying an aggregating operation $\text{op}$ which takes as input a region surrounding the corresponding entry in the input volume and produces a single value. The shape of the region is defined by a neighborhood $U$ as in convolutions.
In particular, let $I$ be the input volume and $O$ the output one, we have:
$$
O(r, c, k) = \text{op}(\{ I(r+u, c+v, k) \ | \ (u, v) \in U \}).
$$
The usual operation is $\max$ and in this case, we talk about **max-pooling layers**.
The neighborhoods used in pooling layers have rectangular shapes as for convolutions. The spatial extent is reduced by using a number of strides which match the dimensions of the neighborhood.
The usual max-pooling layers have $(2, 2)$ strides, thus they half both the number of columns and rows of the volume.

#### Putting all together

The layers we've just described are stacked together in the following order: convolutional layer, activation layer, and max-pooling layer.
That is, an input volume is first processed by a convolutional layer, then it is activated by an activation layer, and finally its spatial extent is reduced by a pooling layer. Then the volume is fed to the next stage with convolution, activation, and pooling.

---

As we anticipated, usually the depth of the volume is increased during the process (this is achieved by increasing the number of filters in the convolution layers), while the spatial extent is reduced (this is achieved through pooling layers).
After a certain number of stages, the volume is flattened in a 1D tensor which is fed to a FFNN for classification.
For this reason, we can regard the convolution stages in the CNN as a feature extractor which learns the features needed by the classifier.

What we described so far is the architecture of one of the first CNNs: _LeNet-5_, designed by Yann LeCun. What happens in this kind of architectures is that most of the parameters ends up in the FFNN classifier.

## Latent representation in CNNs

The features learned by CNNs have been found empirically to be very good most of the times. For example, the distance in the feature space usually captures the perceptual similarity among images; conversely to what happens for pixel distance.
