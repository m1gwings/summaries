---
marp: true
theme: summary
math: mathjax
---
# Localization

<div class="author">

Cristiano Migali

</div>

- In the **classification and localization task** the input image contains a single relevant object to be classified in a fixed set of categories. In particular, we need to assign the object class to the image and locate the object in the image by its **bounding box**.

To perform classification and localization we need a training set of annotated images with a label and a bounding box around the object. The localization problem can be generalized involving regressions over more complicated geometries (like the human skeleton).

We can univocally determine a bounding box by the coordinates of the upper-left corner and the height and width, this results in a tuple $(r, c, h, w)$. Indeed, **bounding box estimation is a regression problem**.

Classification and localization belongs to the family of **multi-task learning** in which we build models which can perform multiple tasks. In this case the network should predict both the bounding box and the label. The output is a tuple $(r, c, h, w, l)$ where $(r, c, h, w)$ describe the bounding box and $l$ is the predicted label.
We can train model of this kind by **merging two losses**:
$$
E(\theta) = \alpha E_\text{task 1}(\theta) + (1-\alpha) E_\text{task 2}(\theta)
$$
where $\alpha \in [0, 1]$ is an hyper-parameter to tune. In particular, to tune $\alpha$ we need to do cross-validation using a metric different from the training loss.

## Human pose estimation

- **Pose estimation** is formulated as a CNN-regression problem towards body joints. It is a kind of localization task. In particular, a **pose** is defined as a **vector** of $k$ **joint locations** for the human body, possibly normalized w.r.t. the bounding box enclosing the human. Each joint location requires 2 coordinates, thus the output of the network has $2k$ entries.

## Weakly-supervised learning for localization

As we already remarked, in **supervised learning**, a model $\mathcal{M}$ performing inference in $\mathcal{T}$ is a function:
$$
\mathcal{M} : \mathcal{X} \rightarrow \mathcal{T}
$$
and requires a training set $\mathcal{D} \subseteq \mathcal{X} \times \mathcal{T}$, namely training couples are of the same type as classifier input-output.
For some tasks (for example segmentation), these type of annotations are very expensive to gather.

---

- In **weak supervised learning** we build a model $\mathcal{M}$ able to solve a task which requires to predict targets in $\mathcal{T}$, but is trained using labels in a different domain $\mathcal{K} \neq \mathcal{T}$ which are easier to gather.

### Class Activation Mapping

We can apply the weak supervised learning paradigm to classification. In particular we want to perform localization without having annotated bounding boxes for training images. The training set is typically annotated only for classification: $\mathcal{D} \subseteq \mathcal{X} \times \Lambda$.

This can be done through **Class Activation Mapping** (**CAM**). This technique can be applied to CNNs which end with a GAP followed by a dense layer whose output is activated through softmax. The advantages of GAP extend beyond simply acting as a structural regularizer that prevents overfitting. By a simple tweak it is possible to identify the discriminative image regions leading to a prediction and from those infer a bounding box.

Let's see in detail how to compute a CAM. Assume that the last volume of the CNN before GAP is $V$ and has dimension $R' \times C' \times K'$.
The GAP transforms it in a vector
$$
\text{GAP}(V)[k] = \frac{1}{R' C'} \sum_{r=1}^{R'} \sum_{c=1}^{C'} V[r, c, k] \text{ for $k \in \{ 1, \ldots, K' \}$}.
$$
This 1D tensor is processed by a dense-layer; the result (before soft-max activation), is a set of scores:
$$
S_y = \sum_{k=1}^{K'} w_{y,k} \text{GAP}(V)[k] \text{ for $y \in \{ 1, \ldots, |\Lambda| \}$ }.
$$
These scores determine the predicted class. Observe that the scores depend linearly on the volume $V$. Through a simple tweak we can write each score $S_y$ as an average of a channel with spatial extent $R' \times C'$. This channel is the CAM $M_y$:
$$
S_y = \sum_{k=1}^{K'} w_{y,k} \text{GAP}(V)[k] = \sum_{k=1}^{K'} w_{y,k} \frac{1}{R' C'} \sum_{r=1}^{R'} \sum_{c=1}^{C'} V[r, c, k]
$$
$$
= \frac{1}{R'C'} \sum_{r=1}^{R'} \sum_{c=1}^{C'} \sum_{k=1}^{K'} w_{y,k} V[r, c, k] = \frac{1}{R'C'} \sum_{r=1}^{R'} \sum_{c=1}^{C'} M_y(r, c).
$$
$M_y(r, c)$ directly indicates the importance of the activations in $V$ at $(r, c)$ in the prediction of class $y$.
Usually $R' < R, C' < C$, thus the CAMs have to be up-sampled to match the input-image dimension. This is usually done through bilinear interpolation.
From CAM we can build bounding box by enclosing the values which are above the $20 \%$ of the maximum value in $M_y$.
