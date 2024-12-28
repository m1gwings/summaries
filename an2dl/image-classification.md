---
marp: true
theme: summary
math: mathjax
---
# Image classification

<div class="author">

Cristiano Migali

</div>

## The problem

- **Image classification** is the problem of assigning to an input image $I \in \{ 0, \ldots, 255 \}^{R \times C \times 3}$ a label $y$ from a fixed set of categories $\Lambda$. We name **classifier** a function which maps the input image to the label corresponding to the predicted category.
More in general, we're often interested into assigning to each image a vector of scores with one entry per category, which corresponds to the estimated degree of membership of the image to the category.
Thus we can generalize the definition of classifier to a function  $\mathcal{K} : \mathbb{R}^{R \times C \times 3} \rightarrow \mathbb{R}^{|\Lambda|}$. We denote the $i$-th output component as
$$
s_i = [\mathcal{K}(I)]_i.
$$
> The predicted label is the one associated with the highest score:
$$
\hat{y} = \arg \max_{y \in \Lambda} s_{i(y)}
$$
> where $i(\cdot)$ maps a label to the corresponding index in $\{ 1, \ldots, |\Lambda| \}$.
Often the scores form a probability vector, in this case each score is the predicted probability that the input image belongs to the corresponding category.

A **good classifier** associates the largest score to the correct class.

## Possible approaches

### A 1-layer NN to classify images

The easiest attempt to deal with image classification with NNs is to use a very simple NN with just an input and an output layer. The output layer has one neuron for each class in $\Lambda$; these neurons are activated with softmax. Images are fed to the network by flattening the tensor: the result of this operation is a 1D vector with $R \cdot C \cdot 3$ entries which must match the number of neurons in the input layer.
The model we're using is simply a linear classifier: indeed, since there is no hidden layer; the relationship between the input and the score of each class (before the softmax) is linear. The softmax activation does not change the predicted class, the only advantage is that we can interpret the output as a probability distribution.

Observe that **dimensionality** prevents us from using in a straightforward manner deeper NNs.

---

Indeed, suppose we were to add an hidden layer having half of the neurons of the input layer. This would already explode the number of parameters in the network for images of reasonable size.

The functional form of the linear classifier we just described can be easily represented as follows:
$$
\mathcal{K}(I) = W \ \text{flatten}(I) + b
$$
where $W \in \mathbb{R}^{|\Lambda| \times (R \cdot C \cdot 3)}$, $b \in \mathbb{R}^{|\Lambda|}$.
The sores of $i$-th class is given by the inner product between the matrix rows $W[i, :]$ and $\text{flatten}(I)$:
$$
s_i = W[i, :] \ \text{flatten}(I) + b_i.
$$
This means that the score of a class is <u>weighted sum</u> of all the image pixels.
Indeed we can associate each weight in $W[i, :]$ to a channel value of a pixel of $I$. We can explicit this relationship through the $\text{unflatten}(\cdot)$ operation, which allows to interpret each row of the weight matrix as an image.

We can train the linear classifier treating it as the simple NN we described, using the iterative methods discussed in previous set of notes. In particular, by minimizing the CCE loss we would get exactly _logistic regression_ [see ML notes].

#### Geometric interpretation

AS it is usual for linear classifier, we can associate to each row $W[i(y), :]$ and corresponding bias $b_{i(y)}$ an hyperplane in $\mathbb{R}^{R \cdot C \cdot 3}$; this hyper-plane roughly tries to separate the samples which belong to class $y$ on one side, from the others.

#### Template matching interpretation

Another possible interpretation for the behavior of the trained classifier is **template matching**. Indeed, we know by the Cauchy-Schwarz inequality that, after fixing the norm, the vector which maximizes the inner-product with $W[i(y), :]$, and thus the score $s_{i(y)}$, has the same direction of $W[i(y), :]$. Thus $W[i(y), :]$ is a template which we're comparing with the input image looking for similarity; the more $W[i(y), :]$ and the input image $I$ are similar, the more likely it is that we assign to $I$ the label $y$.

## Challenges of image classification

- The **first challenge** of image classification is **dimensionality**: images are very high-dimensional image data.
- The **second challenge** is **label ambiguity**: a label might not uniquely identify the image. The classical examples is an image depicting several objects associated to different labels.

---

- The **third challenge** is **transformation**: there are many transformations that can change the RGB tensor associated to the image dramatically without changing its label. For example: _changes in the illumination conditions_, _deformations_, _view point changes_, and many others ... .
- The **fourth challenge** is **inter-class variability**: there is a broad range of objects associated to the same class.
- The **fifth challenge** is **perceptual similarity**: perceptual similarity in images is not related to pixel-similarity. This is related to the third challenge. Indeed perceptual similarity differs significantly from pixel similarity: there are images at the same "pixel distance" (i.e. $L^2$ distance in $R^{R \cdot C \cdot 3}$) which differs significantly. This explains why KNN classifiers are very bad in image classification when we use pixel distance.
