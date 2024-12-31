---
marp: true
theme: summary
math: mathjax
---
# Segmentation

<div class="author">

Cristiano Migali

</div>

- The **goal** of **image segmentation** is to separate images into coherent objects.
Being more formal, given an image $I \in \mathbb{R}^{R \times C \times 3}$, image segmentation consists in estimating a partition $\{ \mathcal{R}_i \}$ of $R \times C$ s.t. $I[\mathcal{R}_i]$ is a distinct object in $I$. 

There are two types of segmentation:
- **unsupervised segmentation** (which we do NOT address here);
- supervised (or **semantic**) **segmentation**.

In **semantic segmentation**, given an image $I$, we **associate to each pixel $(r, c)$ a label $y_i$** from a set of labels $\Lambda$.
The **result** is a grid $S \in \Lambda^{R \times C}$ of labels containing in each pixel the estimated class.

In **semantic segmentation** different instances of the same class of objects are grouped in the same partition; this does NOT happen in **instance segmentation**.

The dataset needed to carry out semantic segmentation has the usual supervised learning structure: $\mathcal{D} = \{ (I_i, {GT}_i) \}$ where ${GT}_i \in \Lambda^{R \times C}$ is a grid of ground truth labels (with the same spatial extent of the corresponding image) which have been annotated manually for each sample.
It is evident that datasets for semantic segmentation are very hard to build.

## Training semantic segmentation networks

When we train semantic segmentation networks, the categorical cross-entropy loss can be assessed in each and every pixel of the input. **The loss function becomes the sum of pixel-wise losses**:
$$
\hat{\theta} = \arg \min_{\theta} \sum_{r = 1}^R \sum_{c = 1}^C e(GT(r, c), S(r, c|\theta)).
$$

## Architectures for semantic segmentation

The most straightforward way to build a convolutional architecture which produces **segmentation maps** $S \in \Lambda^{R \times C}$ as output is the following: we define the network in such a way that the final volume has the same spatial extent of the initial image ($R \times C$) and a number of channels which equals the number of categories ($|Lambda|$). Then we can activate each "pixel" of the last volume depth-wise through softmax. Finally we take the argmax along the channel dimension to obtain the predicted labels.

---

### Semantic segmentation by convolutions only

The naive way of obtaining a final volume with the characteristic just described is to build a CNN with no pooling layers, just convolutions with padding same.

This approach turns out to be very inefficient due to the small receptive fields.
Indeed:
- on the one hand **we need to "go deep" to extract high level information** on the image;
- on the other hand **we want to stay local not to loose spatial resolution** in the predictions.

### Inherent tension in semantic segmentation

Semantic segmentation faces and inherent tension between semantics and location:
- **global information resolve "the what"** (i.e. allows to classify the objects correctly);
- while **local information resolves "the where"** (i.e. allows to identify with a certain precision the contours of the objects).

### Down-sampling + up-sampling

One way to merge global and local information is the following. We can build a two-stage network with a **contractive stage**, followed by an **expanding stage**.
The **contractive stage** is built as for usual CNNs for classification: we reduce gradually the spatial extent of the volumes through pooling layers and increase the depth. This first half of the network, as it happens for classification, extracts the semantic of the image relying on global information. The second half of the network is meant to up-sample the predictions to cover each pixel in the image. Increasing the image size is necessary to obtain sharp contours and spatially detailed class predictions.
We can also regard the two stages as an **encoder** and a **decoder**.

#### How to up-sample?

There are different techniques to perform up-sampling.

- **Nearest neighbor**: each pixel $I(r, c)$ becomes a grid of $H \times W$ pixels, all with the same value $I(r, c)$.

- **Bead of nails**: each pixel $I(r, c)$ becomes a grid of $H \times W$ pixels which are all 0 except the upper-left corner which takes the original value $I(r, c)$.

- **Max-un-pooling**: this technique can be used to revert the down-sampling performed by a previous max-pooling layer. In particular, during the max-pooling operation we keep track of the coordinates $(i, j) \in \{ 1, \ldots, H \} \times \{ 1, \ldots, W \}$ of the pixel which attained the max; when we up-sample, each pixel $I(r, c)$ becomes a grid of $H \times W$ pixels which are all 0 except the pixel in coordinates $(i, j)$ which is set to $I(r, c)$.

---

- **Transpose convolution**: in this technique we use a learnable filter with $H \times W$ parameters for up-sampling. The output is initialized to 0. The value of each input pixel is multiplied with the filter and added to the output in a certain location. This location is determined in this way: we start with the first input pixel in the upper left corner by adding the result to the upper-left corner of the output and then, every time we move by 1 in the rows or in the columns to process the next input pixel, we move the location where the result will be added by a number of strides which is an hyper-parameter of the layer.
Transpose convolution can by replaced by a pair of layers: up-sampling with bed of nails, followed by a convolutional layer.
Transpose convolution gives more degrees of freedom in the way we up-sample, since the **filters can be learned**.

### U-Net

**U-Net** is a famous architecture for semantic segmentation. Similarly to what we described before, the network is formed by:
- a **contracting path**,
- and **expansive path**.

In particular the network has a symmetric structure: the number of down-sampling stages matches the up-sampling stages.
At each down-sampling stage, the number of feature maps is doubled.
The main novelty is the addition of **skip connections**: each up-sample stage takes an input which is obtained by combining the output of the corresponding down-sample stage with the output of the previous up-sampling stage. Usually they are combined by channel-wise concatenation, but addition is also a reasonable option if we make sure that the dimensions of the two outputs match. These allows to improve the reconstruction by exploiting the local information in output from the down-sampling stage and the global information extracted by the encoder.

U-Net is trained with a custom loss which is defined in the domain of bio-medical image segmentation. In particular each pixel is weighted by:
$$
w(r, c) = w_c(r, c) + w_0 \exp\left( -\frac{(d_1(r, c) + d_2(r, c))^2}{2 \sigma^2} \right)
$$
where:
- $w_c$ is used to balance class proportions;
- $d_1$ is the distance to the border of the closest cell;
- $d_2$ is the distance to the border of the second closest cell.

In particular, the second term has very high value (close to $w_0$) for pixels in between the borders of two cells (i.e. pixels belonging to the separation boundary of the two cells), while it takes small values (close to 0) for other pixels where either $d_1$ or $d_2$ are big. This allows to improve the performance on the contours.
