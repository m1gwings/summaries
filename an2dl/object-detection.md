---
marp: true
theme: summary
math: mathjax
---
# Object detection

<div class="author">

Cristiano Migali

</div>

- In the **object detection task** we're given a fixed set of categories and an input image which contains an unknown and varying number of instances of objects belonging to the aforementioned categories.
We're required to draw a bounding box on each object instance and associate a label which represents the category to which the object belongs.

A training set for object detection consists in annotated images with labels and bounding boxes for each object. Observe that each image requires **a varying number of outputs**. In particular, we assign to an input image $I \in \mathbb{R}^{R \times C \times 3}$:
- **multiple labels** $\{ l_i \}$ from a fixed set of categories $\Lambda$, each corresponding to **an instance of that category**;
- the coordinates $\{ (r, c, h, w)_i \}$ of the bounding box enclosing **each** object.

That is:
$$
I \mapsto \{ (x, y, h, w, l)_1, \ldots, (x, y, h, w, l)_N \}.
$$

## How to asses performance in object detection?

We need a scalar metric to quantitatively assess the network performance over each and every image in the test set. One metric is the so-called **Intersection over Union** (**IoU**). In particular, given a predicted bounding box and the ground truth we compute the ratio between the area of the intersection of the two bounding boxes and the are of the union. If the two bounding boxes overlap and have the same shape, the IoU is 1. If the two bounding boxes are completely non-overlapping, the IoU is 0. If the two bounding boxes do NOT fully overlap or if they have different shapes or size, the IoU is between 0 and 1.

## Excursus: multi-label classification

So far, all the models we have seen provide a fixed-sized output. CNNs (like other NNs) can be modified to return **multiple classification outputs** by **replacing softmax activation in the output layer** with **sigmoid activation** in each of the $L$ neurons. The $i$-th neuron will predict the probability $p_i \in [0, 1]$ of class membership for the input in a non-exclusive manner. The model must be trained with the binary cross-entropy loss function.
This approach differs from the usual one in the fact that the output probabilities do NOT sum to 1. An input image might belong to multiple categories, depending on the content.

---

## Approaches for object detection

### The straightforward solution: sliding window

This approach is very similar to the sliding window for semantic segmentation. Suppose we're given a pre-trained model which is meant to process images of a fixed size. We slide on the input image producing patches of that size and classify each of them. Observe that, for this approach to work, we need to **include a background class** since we will have to classify also regions which do NOT contain any object.

This approach has many **cons**.
- It is **very inefficient** since it does NOT re-use features that are "shared" among overlapping patches.

- It is difficult to detect objects at different scales.

But it has also one **pro**:
- You don't need to retrain the CNN.

### Region proposal
#### R-CNN

A more effective approach relies on **region proposal**. Region proposal algorithms (and networks) are meant to **identify bounding boxes** that correspond to a **candidate object** in the image.
Algorithms with **very high recall** (but low precision) were there before the deep learning advent. The idea is to:
- apply a region proposal algorithm;
- classify by a CNN the image inside each proposal regions.

This approach takes the name of **R-CNN**.

Region proposal algorithms can identify regions with different sizes and shapes but the original R-CNN approach works with a CNN that requires a fixed input size. Thus the identified regions are warped to the fixed input size before being fed to the CNN.

In the original R-CNN approach, the classification happens through a SVM trained on the latent space produced by the CNN. The CNN is fine-tuned with a dense layer and a classification head which is then removed (and replaced with the SVM).
Furthermore, the regions identified by region proposal algorithms are **refined** by a regression network.

---

R-CNN has many limitations.
- **There is no end-to-end training**: we fine-tune the network with a softmax classifier before training the SVM, then we train post-hoc the SVM, finally we train post-hoc bounding-box regressions.
- **Region proposals are from a different algorithm** which can't be optimized for the detection by CNN.
- **Training is slow** and takes a lost of disk space to store the features.
- **Inference is slow** since the CNN has to be executed on each proposed region.

**Remark**: efficiency in object detection networks is key! Otherwise you might want to train a segmentation network instead!

#### Fast R-CNN

**Fast R-CNN** improves the efficiency of **R-CNN** by computing convolutional features only once.
1. In particular, we feed the whole image to the CNN that extracts the final volume (a.k.a. the features in the latent space) before flattening.
2. A **region proposal** algorithms identifies the regions on the image, these are then projected onto the feature space. Regions are directly cropped from the feature maps, instead from the image: it is in this way that we re-use convolutional computation.
3. At the end of the CNN there is still a FC layer which requires a fixed size activation. Thus, a **ROI pooling layer** (**ROI** stands for **Region Of Interest**) extracts from the proposed region mapped onto the latent space an activation with the required spatial extent by splitting the region in a $H \times W$ grid and applying max-pooling in each cell of the grid (the result is a $H \times W$ activation where $H \times W$ is the fixed size required by the FC layer).
4. The FC layers estimate both classes and BB location. We use a multi-task learning approach to optimize the model.

Observe that now training is performed in an **end-to-end manner** and the convolutional part is executed only once.

This approach becomes incredibly faster than R-CNN during testing. Now that convolutions are NOT repeated on overlapping areas, the **vast majority of test time is spent on ROI extraction**.

#### Faster R-CNN

In **Faster R-CNN** the ROI extraction algorithm has been replaced by a **Region Proposal Network** (**RPN**). The **RPN** operates on the same features used for classification. Its goal is to associate to each **spatial location** in the feature space, $k$ **anchor boxes** which are ROIs having different scales and ratios (for example $k = 9$, where we have all the combinations of anchors given $3$ sizes of anchor width and $3$ height/width ratios).

---

If the feature maps have spatial dimension $R' \times C'$, the network outputs $R' \times C' \times k$ **candidate** anchors and **estimates _objectiveness scores_** for each anchor. The RPN is divided in two sub-modules: the **cls** (classification) **network** and the **reg** (regression) **network**. The classification network is trained to predict the **object probability**, i.e. the probability for an anchor to contain an object. The result are $k$ estimated probability pairs $(\hat{p}, 1-\tilde{p})$ **for each spatial location** and expresses the probability for the anchor in the spatial location to contain _any object_.
The regression network is trained to adjust each of the $k$ anchors in each spatial location to better match the object ground truth box. In particular, this networks provides $k$ tuples of 4 elements each for spatial location. The 4 elements are the delta by which we have to adjust the bounding box of the corresponding anchor.
At the end we select $n_\text{prop}$ ROIs from the outputs of the classification and regression networks in the RPN.
Proposals are selected analyzing: non-maximum suppression based on the objectiveness score and the IoU between the anchors and the corrected boxes. There is also a fixed threshold on the objectiveness score.
The proposals are classified as in the standard Fast R-CNN architecture. In particular the detection head returns for each ROI feature vector $L$ classification scores and $4 \times (L-1)$ bounding box correction (the "$L-1$" is due to the fact that among the $L$ classes there is the background for which we do NOT compute bounding box corrections).

In principle, in RPN you can adopt anchors having non-rectangular shapes. However it can be difficult to compute IoU, which is instead extremely easy and fast in the case of boxes.

**Training** now involves 4 losses, in a weighted sum, which regard: the classification network inside the RPN, the regression network inside the RPN, the final classification score, and the final bounding box coordinates.

The training happens in the following steps:
1. we train the RPN keeping the backbone network frozen and training only RPN layers (this ignores object classes);
2. we train Fast R-CNN using the proposals form the RPN trained before and fine tune the whole Fast R-CNN including the backbone;
3. we fine tune the RPN in cascade of the new backbone;
4. we freeze the backbone and the RPN and fine-tune only the last layers of the Faster R-CNN.

### You Only Look Once (YOLO)

All the detection architectures we described so far are pipelines of multiple steps.
In particular, **region-based methods make it necessary to have two steps** during inference. This can be slow to run and hard to optimize, because each individual component must be trained separately.
The goal of **YOLO architecture** is to reframe object detection as a single regression problem, straight from image pixels to bounding box coordinates and class probabilities, and solve there regression problem all at once.

---

In particular YOLO works as follows:
1. we divide the image in a coarse gride (e.g. $7 \times 7$);
2. each grid cell is associated to $B$ anchors (which are base bounding box shapes) placed at the center of the cell;
3. for each cell and anchor we predict the **offset of the base bounding box** to better match the object as a tuple $(dx, dy, dh, dw, \text{objectiveness\_score})$ and the **classification score of the base-bounding box** over the considered categories $\Lambda$ (including background). So the output of the network has dimension $7 \times 7 \times B \times (5 + C)$.

The whole prediction is performed in a single forward pass over the image, by a single convolutional network.
Typically, networks based on region-proposals are more accurate, single shot detectors are faster but less accurate.
