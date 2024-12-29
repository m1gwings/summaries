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

## CNNs as FFNNs

We already remarked many times that convolution is a linear operation. For this reason **we can represent convolutional layers as dense layers** in a FFNN thanks to an appropriate choice of the weights. Before passing the input volume to the dense layer, we need to _flatten it_. The way in which we _do the flattening_ determines the _correspondence_ between the _weights in the filters of the convolutional layer_ and the _weights in the dense layer_.
Suppose that the flattening of a channel is done by putting its columns one below the other starting from the left-most, then the flattening of the whole volume is obtained by putting one below the other the 1D vectors we computed for each channel.
The final result is a 1D vector of $R \cdot C \cdot K$ entries where $R$ is the number of rows, $C$ is the number of columns, and $K$ is the number of channels of the input volume. Analogously the output of the dense layer will be a 1D vector of $R' \cdot C' \cdot K'$ entries where $R'$, $C'$, and $K'$ are respectively the number of rows, columns, and channels of the output volume.
Let's define the weight matrix $W \in \mathbb{R}^{R' \cdot C' \cdot K' \times R \cdot C \cdot K}$ and the bias vector $\underline{b} \in \mathbb{R}^{R' \cdot C' \cdot K'}$ of the dense layer which would make it equivalent to the convolutional layer.
Let $w_1, \ldots, w_{K'}$ be the filters of the convolutional layer, let $H$ and $W$ be the height and width of the neighborhood in the filters. For simplicity let's assume that the convolutional layer is in valid mode (then $R' = R-H+1$, $C' = C-W+1$). Remember that we always assumed that the coordinates in volume are indexed starting from 1.

---

Then, the **expression of the weight matrix** is:
$$
W = \begin{bmatrix}
\begin{matrix}\text{$1$st} \\ \text{out ch}\end{matrix}\left\{ \begin{matrix}
w_1(-\lfloor \frac{H}{2} \rfloor+1,-\lfloor \frac{W}{2} \rfloor+1, 1) & \cdots & w_1(\lfloor \frac{H}{2} \rfloor-1, \ldots) & \underbrace{\begin{matrix}0 & \cdots & 0\end{matrix}}_\text{$R-H$ zeroes} & w_1(\cdots,-\lfloor \frac{W}{2} \rfloor+2, 1) & \cdots & w_1(\ldots, K) \\
0 & \begin{matrix}\text{... the row} \\ \text{above shifted} \\ \text{by 1 on the} \\ \text{right ...}\end{matrix} \\
\vdots
\end{matrix} \right. \\
\vdots \\
\begin{matrix}\text{$K'$th} \\ \text{out ch}\end{matrix}\left\{ \begin{matrix}
w_K(-\lfloor \frac{H}{2} \rfloor+1,-\lfloor \frac{W}{2} \rfloor+1, 1) & \cdots & w_K(\lfloor \frac{H}{2} \rfloor-1, \ldots) & \underbrace{\begin{matrix}0 & \cdots & 0\end{matrix}}_\text{$R-H$ zeroes} & w_K(\cdots,-\lfloor \frac{W}{2} \rfloor+2, 1) & \cdots & w_K(\ldots, K) \\
0 & \begin{matrix}\text{... the row} \\ \text{above shifted} \\ \text{by 1 on the} \\ \text{right ...}\end{matrix} \\
\vdots
\end{matrix} \right. \\
\end{bmatrix}.
$$
- The matrix is **sparse**: only a few input neurons contribute to define each output (since convolution is local). Thus most of the entries are zero. The circular structure of the matrix reflects convolution spanning all the channels of the input.
- There are a lot of **shared weights**: the same filter is used to compute the output of an entire output channel. The same entries are applied shifted on the following rows.

The **expression of the bias vector** is very simple to derive:
$$
\underline{b} = \begin{bmatrix}
\text{$R' \cdot C'$ entries} \left\{ \begin{matrix} b_1 \\ \vdots \\ b_1 \end{matrix} \right. \\
\vdots \\
\text{$R' \cdot C'$ entries} \left\{ \begin{matrix} b_{K'} \\ \vdots \\ b_{K'} \end{matrix} \right.
\end{bmatrix}.
$$

The weight sharing reduces tremendously the amount of "true" parameters of a convolutional layer w.r.t. dense ones. As we remarked before, weight sharing is due to the spatial invariance of convolution. The rational is that if oen feature is useful to compute at some spatial position $(r_1, c_1)$, then it should also be useful to compute at a different position $(r_2, c_2)$.

## The receptive field

- Due to **sparse connectivity**, unlike in FFNNs where the value of each output depends on the entire input, in CNNs each output only depends on a specific region in the input.
This region in the input is the **receptive field** for that output.

---

The deeper you go, the wider the receptive field is: max-pooling and convolutions increase the receptive field.
Usually, the receptive field refers to the final output unit of the network in relation to the network input, but the same definition holds for intermediate volumes.

**Important observation**.
- Each convolution increases the spatial extent of the receptive field by $H-1$ rows and $W-1$ columns where $H$ and $W$ are respectively the height and the width of the filter.
- Each pooling layer increases the spatial extent of the receptive field by multiplying the number of rows and columns with the corresponding number of strides.

Remember that in the traditional CNN architecture, as we move deeper in layers, spatial resolution is reduced while the number of channels is increased. Now we can understand the rationale behind this choice: we search for higher-level patterns, and don't care too much about their exact location.
In particular we try to build output units with receptive fields as large as possible, ideally the whole input, encharged each of identifying a specific high level pattern.

## Details of the training of CNNs

CNNs can be trained exactly as FFNNs using gradient descent and automatic differentiation.
Care has to be taken when we back-propagate the gradient through max-pooling layers.
Indeed, max-pooling isn't an everywhere-differentiable operation. We deal with this issue similarly to what we do for ReLU: the derivative is 1 w.r.t. the entry which attains the maximum, 0 otherwise.

## Dealing with data scarcity

Deep learning models are very data hungry. In this section we will discuss some techniques which can help when we have to train a deep learning model with few training images.

### Data augmentation

- **Data augmentation** is a technique which allows to synthetically increase the size of the training set by means of a set of transformations applied to the original images.

In particular, the kind of applied transformations are:
- **geometric transformations**: shifts, rotations, perspective distortions, shear, scaling, and flip;
- **photometric transformations**: adding noise, modifying average intensity, superimposing other images, modifying the image contrast.

---

One **fundamental assumption** behind data augmentation is that the transformations should NOT change the category to which the image belongs. For example, if size/orientation is a key information to determine the output target, it is likely that we should not apply scaling/rotation as transformations.

Augmentation is meant to **promote network invariance** w.r.t. transformations used for augmentation.

Observe that data augmentation might not be enough to capture the inter-class variability of images.

Training including augmentation **reduces the risk of overfitting**, as it significantly increases the training set size. As usual it also introduces some bias due to the choice of the applied transformations.
Furthermore, data augmentation can be used to compensate for class imbalance in the training set, by **creating more realistic examples from the minority class**.

In general, transformations used in augmentation can also be class-specific, in order to preserve the image label.

#### Mixup augmentation

- **Mixup** is a **domain-agnostic** data augmentation technique. In particular, mixup creates _virtual samples_ that are **convex combinations of pairs of examples and their labels**.

Given a pair of training samples $(I_i, y_i)$, and $(I_j, y_j)$ drawn at random, belonging to different classes, we define a new virtual sample:
$$
\tilde{I} = \lambda I_i + (1-\lambda) I_j,
$$
$$
\tilde{y} = \lambda y_i + (1-\lambda) y_j
$$
> where $\lambda \in (0, 1)$. Observe that, in the classification setting, the transformation is well-defined for **one-hot encoded labels**.

The advantage of mixup (which makes it domain agnostic) is that we do NOT need to know which label-preserving transformations to use.

#### Test Time Augmentation (TTA)

Even if the CNN is trained using augmentation, it won't achieve perfect invariance w.r.t. considered transformations.
**Test Time Augmentation** (**TTA**) consists in performing augmentation also at inference time to improve the prediction accuracy. In particular, we perform a few random augmentations of the input $I$, obtaining $\{ A_l(I) \}_l$.
Then we classify all the augmented images and save the posterior vectors: $\underline{p}_l = \text{CNN}(A_l(I))$. 

---

The final prediction is obtained by aggregating the posterior vectors $\{ \underline{p}_l \}_l$, that is: $\text{avg}(\{ \underline{p}_l \}_l)$.

## Transfer learning

As we've already remarked, at an high level we can consider a CNN as a stack of two components: a **feature extractor** which takes as input an image and produces relevant features learned from data, and a **classifier** which uses the features produced by the feature extractor to make the classification.
Feature extractors trained on large datasets happen to learn features which are very useful and also general, i.e. they are relevant for many tasks.
The idea behind **transfer learning** is to re-cycle these feature extractors on different tasks.
In particular, given a dataset for a new task, we can train only the classifier of the CNN on the new data to make good classifications using the feature provided by the feature extractor which is kept freezed.
We can summarize the process in 5 steps:
1. take a powerful pre-trained CNN;
2. remove the Fully Connected (FC) layers;
3. design new FC layers to match the new problem (in particular the number of output neurons must match the number of categories of the new task), then plug it after the Feature Extractor (FE);
4. "freeze" the weights of the FE;
5. train only the FC layers on the new data set.

Transfer learning is extremely useful when we have few data at our disposal. Indeed the variance of the feature extractor is much higher than that of the classifier.

### Transfer learning vs fine-tuning

An alternative to transfer learning is **fine tuning**. In **fine tuning** the whole CNN is retrained, but the convolutional layers are initialized to the pre-trained model. Fine tuning requires more training data to be effective w.r.t. transfer learning.
Typically, for the same optimizer, lower learning rates are used when performing fine tuning than when training from scratch. This is due to the fact that we don't want to perturbate the pre-trained weights too much.

## Image retrieval from the latent space

- The feature space defined by feature extractors inside deep learning models is known as **latent space**.

The quality of the features learned from data is usually such that the distance between elements in the latent space is highly correlated with the perceptual similarity of the corresponding inputs.

---

For this reason we can use pre-trained feature extractor to build an image search engine which, given an image, provides all the similar ones. This works simply by returning the $k$ nearest neighbors of the input image in the latent space.
