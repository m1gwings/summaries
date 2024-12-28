---
marp: true
theme: summary
math: mathjax
---
# Introduction to computer vision and digital images

<div class="author">

Cristiano Migali

</div>

## What is Computer Vision?

- **Computer vision** (**CV**) is an interdisciplinary scientific field that deals with how computers can gain high-level understanding from digital images or videos.

In the latest years there has been a dramatic change in CV:
- once, most of techniques and algorithms were _built upon a mathematical/statistical description of images_;
- nowadays, machine learning methods are much more popular.

## Digital images

In order to be able of understanding how any CV algorithm works, we need first to understand how digital images are represented inside computers. The most common encoding for digital images is **RGB** which stands for **Red**, **Green**, **Blue**.
Each **RGB image** is a tensor $I \in \{ 0, \ldots, 255 \}^{R \times C \times 3}$. In particular, images are displayed as a grid of pixels. Each pixel is a colored square. The grid has $R$ rows and $C$ columns. The color of each pixel is encoded through 3 values which represent respectively the intensity of the red, green, and blue. For this reason we refer to $R = I[:, :, 1]$, $G = I[:, :, 2]$, and $B = I[:, :, 3]$ as the red, green, and blue channels respectively. Observe that $R, G, B \in \{ 0, \ldots, 255 \}^{R \times C}$. Since a number in the range $\{ 0, \ldots, 255 \}$ can be stored in memory using $8$ bits, each pixel occupies 3 bytes.
Analogously, gray-scale images have just one channel which encodes the intensity of white of the corresponding pixels, and one pixel requires just 1 byte of storage.
For this reason, storing images with the raw RGB format requires a lot of space. Indeed, it is usual to apply compression algorithms; this is done for example in formats like JPEG.

## Digital videos

In analogy to what we've explained so far, it's easy to understand how to encode videos. **Videos** are sequences of images (_frames_). If a frame is:
$$
I \in \mathbb{R}^{R \times C \times 3};
$$
a video of $T$ frames is:
$$
V \in \mathbb{R}^{R \times C \times 3 \times T}.
$$

---

If storing raw RGB images could result in high disk space consumption, it becomes basically unfeasible for videos.  Indeed, without compression, 1 frame in full HD ($R = 1080, C = 1920$) occupies $\approx 6 \text{MB}$; then 1 second in full HD (at 24 fps) occupies $\approx 150 \text{MB}$.
Fortunately, visual data are very redundant, thus compressible.
This has to be _taken into account when you design a machine learning algorithm_ for images or videos. For example, when we train a neural network, this information is not compressed.

## The most important operation in image processing: correlation

- An image transformation is said to be (**spatially**) **local** if each pixel in the output depends only on a restricted region surrounding the corresponding pixel in the input. In particular, consider a gray-scale input image $I$; given a neighborhood $U(r, c)$ which we can model as a set of displacements, the output pixel at row $r$ and column $c$: $G(r, c)$, depends only on the following values of the input image: $\{ I(r+u, c+v) | (u, v) \in U(r, c) \}$. We can represent the transformation as follows:
$$
G(r, c) = T_{U(r, c)}[I](r, c).
$$

- In particular, a transformation is said to be **space invariant** if the shape of the neighborhood of input pixels used to compute output pixels has constant shape. In formulas, this becomes: $U(r, c) = U \ \forall r, c$.

Local transformation can be both linear or non-linear. We can represent all **linear**, **space invariant**, **local transformations** as:
$$
T[I](r, c) = \sum_{(u, v) \in U} w(u, v) \cdot I(r+u, c+v).
$$

We can consider weights $w = \{ w(u, v) | (u, v) \in U \}$ as an image, or **a filter**. The filter $w$ entirely defines the operation. Indeed, the transformation above is usually known as **correlation** and can be also denoted as:
$$
(I \otimes w)(r, c) = \sum_{(u, v) \in U} w(u, v) \cdot I(r+u, c+v).
$$
We can easily extend the operation to RGB images by introducing weight coefficients for each channel:
$$
T[I](r, c) = \sum_i \sum_{(u, v) \in U} w(u, v, i) \cdot I(r+u, c+v, i).
$$
