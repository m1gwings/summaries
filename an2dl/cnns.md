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

## Famous CNN architectures

In this section we will describe famous CNN architectures introduced after the traditional one (_LeNet-5_) we extensively treated.

### AlexNet

**AlexNet** is an architecture developed by Alex Krizhevsky at al. in 2012 and won the ImageNet competition. It is quite similar to LeNet-5: there are
- 5 convolutional layers (with rather large filter: $11 \times 11$, $5 \times 5$),
- 3 dense layers.

To counteract overfitting, they introduced:
- ReLU;
- dropout, weight decay and norm layers (not used anymore);
- max-pooling.

The first convolutional layer had 96 $11 \times 11$ filters, with stride $4$.
The output were **two** volumes of $55 \times 55 \times 48$ **separated over two GTX 580 GPUs**. The reason behind this choice is just to improve the parallelism on the available physical hardware. Most connections are among feature maps of the same GPU, which will be mixed at the last layer.

At the end they also trained an ensemble of 7 models to drop the error by $3 \%$.

### VGG

The **VGG16**, introduced in 2014 is a deeper variant of the AlexNet convolutional structure. Smaller filters are used and the network is deeper.
The paper presents a thorough study of the role of network depth.
Adding more convolutional layers is feasible due to the **use of very small ($3 \times 3$) convolution filters in all layers**.
The **idea** is that <u>multiple</u> $3 \times 3$ convolutions in a sequence achieve the same receptive field with less parameters and more non-linearities than larger filters in a single layer.
For example consider stacking 3 convolutional layers with $3 \times 3$ filters vs one single convolutional layer with $7 \times 7$ filters. The receptive field is of the same size, but the first option has less parameters and more non-linearities.

---

### Network in Network

The **Network in Network** paper introduced two new blocks, namely: **MLPconv layers** and **GAP**.

**MLPconv** stands for Multi-Layer Perceptron convolution (where Multi-Layer Perceptron is a term sometimes used as a synonym of FFNN). These are an alternative to convolutional layers. In particular they use a stack of FC layers followed by ReLU which are applied to the input volume in a **sliding manner**, trying to mimic the behavior of convolution. As convolution, they still preserve sparsity and weight sharing. Each layer features a **more powerful functional approximation** that a convolutional layer than a convolutional layer which is obtained by stacking a linear operation with ReLU. These kind of layers are not very much used nowadays.

**GAP** stands for **Global Average Pooling**.GAP layers try to substitute the FC layer at the end of the network. The **idea** is that, instead of feeding the last volume, after flattening, to an FC layer, we take the average of each channel and activate the resulting 1D vector through soft-max. Observe that we need to make sure that the number of channels in the last volume matches the number of categories of the problem (this is easily achieved by setting properly the number of filters of the last convolutional layer). Alternatively we can use an hidden layer to adjust feature dimension after the GAP.
Observe that a FC layer corresponds to a multiplication against a **trainable dense matrix**, while GAP corresponds to a multiplication (_of the flattened final volume_) against a **block diagonal**, **non trainable matrix**.

The rationale behind GAP is the following: FC layers are prone to overfitting since they have many parameters.
The summarize, the advantages of GAP are the following:
- there are no parameters to optimize, the network is lighter and thus less prone to overfitting;
- there is more interpretability since it creates a direct connection between channels and classes output;
- <u>the network can be used to classify images of different sizes</u>, indeed, the shape of the output is **independent from the spatial extent of the input**.

Another important advantage of GAP is that **it increases invariance to shifts**. Indeed, the features extracted by the convolutional part of the network are invariant to shift of the input image, but those computed by dense layers after flattening are not (different input neurons are connected by different weights).
Therefore, a CNN trained on centered images might not be able to correctly classify shifted ones. The GAP solves this problem: the shifted image will produce in the last channel the same features of the original image, just shifted, and average is invariant to the shift (unless part of the features gets "shifted outside the spatial extent of the last volume").

The whole Network in Network (NiN) architecture stacks MLPconv layers with max-pooling and a GAP layer with softmax at the end of the network.

---

#### Global pooling layers

We can generalize the idea of GAP to **Global Pooling Layers**: which are layers that perform a global operation on each channel, **along the spatial components**. They return one single value per channel. The usual pooling operations are average (for the GAP), or the maximum (for the GMP).

### InceptionNet

**InceptionNet** is a family of architectures which try to answer the following problem: **image features might appear at different scales**, and it is difficult to **define the right filter size**.
In particular, this is done through the introduction of a new block: the **inception module**. In an inception module multiple convolutions and pooling operations are run in parallel.
Different convolutions have different filter size, the final results are merged by depth-wise concatenation of the volumes.
All the blocks preserve the spatial dimension by zero padding for convolutions or by [**fractional stride**](https://www.tensorflow.org/api_docs/python/tf/nn/fractional_max_pool) for max-pooling. Observe that in this way the activation map grows much in depth.
A usual configuration is to have in parallel: $1 \times 1$ convolution, $3 \times 3$ convolution, $5 \times 5$ convolution, and $3 \times 3$ max-pooling.
Inception modules of this kind are very computationally expensive, and computational problems will get significantly worse when stacking multiple layers due to the increase of the depth of volumes.
What is usually done to alleviate the problem is to reduce the number of input channels thanks to $1 \times 1$ convolutional layers before the $3 \times 3$ and $5 \times 5$ convolutions. Using these $1 \times 1$ convolutional layers is referred to a **bottleneck layer**. Furthermore, adding $1 \times 1$ convolutional layers increases the number of non-linearities.

GoogLeNet is an architecture of the InceptionNet family developed in 2014. It is a stack of 27 layers considering pooling ones. At the beginning there are two blocks of convolution + pooling layers. Then, there is a stack of 9 inception modules. There is no fully connected layer at the end, just a GAP, then a linear classifier activated by softmax.
The network was so deep that the gradient w.r.t. parameters in the early stage would vanish. To solve the problem, two additional classification heads had been attached to the network at intermediate layers, and the corresponding losses where used during training. The rationale is that in this way we force intermediate layers to provide meaningful features for classification as well. Furthermore the magnitude of the gradient of the loss associated with classification heads closers to the input has a significative magnitude even when taken w.r.t. the parameters of the first layers.
These classification heads are of course removed at inference time.

---

### ResNet

**ResNet** architecture has been introduced after the following **empirical observation**: increasing network depth by stacking an increasingly number of layers, at some point, starts worsening the performance of the model, but this is NOT due to overfitting, since the same trend is shown both in training and validation error.
In principle adding more layers shouldn't be harmful since the unneeded layers at the end of the network can learn the identity mapping, and thus the network would become equivalent to a shallower one. The issue of deeper models is that they are harder to optimize: the additional layers fail to learn the identity mapping.
The **idea** behind ResNet is to try to solve the problem directly by making it easier for a layer to learn the identity mapping, This is achieved through **identity shortcut connections**. They work as follows: we add to the output $\tilde{O}$ of a "weight layer" (like convolutional layers), the value of the input $I$. The final result is $O = \tilde{O} + I$. In this way the weight layer has to learn the best residual $O - I$. The advantage is that the residual of the identity map is 0, which is easily obtained by setting the weights of the weight layer to 0.
Networks of this kind can still be trained through back-propagation.
Observe that, for the model to work, $I$ and $\tilde{O}$ must have the same size, this is usually achieved through additional $1 \times 1$ convolutional layers to adjust the number of channels in the volume.
In very deep architecture $1 \times 1$ convolutional layers are used to reduce the computational load as was done in InceptionNet: we reduce the number of channels with a $1 \times 1$ convolution, then we apply a convolutional layer with larger filters (like $3 \times 3$), and finally we restore the number of channels with a $1 \times 1$ convolution. 

### MobileNets

MobileNets are a family of architectures designed to reduce the number of parameters and of operations, to embed networks in mobile applications. The issue preventing the use of networks in mobile devices is that convolutional layers have (still) quite a few parameters, and are also quite computationally demanding.

The new addition is the **separable convolution**, which is a convolution made in two steps:
1. first we do **depth-wise convolution**, which is like 2D convolution on each channel of the input independently (we use a different 1-channel filter for each channel of the input);
2. then we do **point-wise convolution** which combines the output of depth-wise convolution (which has the same dimensions of the input) through $N_F$ filters that are $1 \times 1$.

Adopting the usual notation, the number of parameters in a separable convolution is:
$$_
K \cdot H \cdot W + N_F \cdot K
$$

---

The number of operations (products) in traditional convolution (with padding "same") is $N_F \cdot H \cdot W \cdot K \cdot R \cdot C$.
Separable convolutions instead require $K \cdot H \cdot W \cdot R \cdot C$ for depth-wise convolution, and $N_F \cdot K \cdot R \cdot C$ for point-wise convolution.

### Wide ResNet

In **Wide ResNet** we increase the number of filters in the blocks by scaling them by a factor $k$ and we reduce the number of layers.

### ResNeXt

In **ResNeXt** the **ResNet module** has been made wider by adding multiple pathways in parallel; the results are added together at the end.
It is similar to the inception module, but all the paths share the same topology.

### DenseNet

In each block of a **DenseNet**, **each convolutional layer takes as input the output of all the previous layers**: there are short connections between convolutional layers of the network; each layer is connected to every other in a feed-forward fashion.
This alleviates the vanishing gradient problem and promotes feature re-use since each feature is spread through the network.
