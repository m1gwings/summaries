---
marp: true
theme: summary
math: mathjax
---
# Clustering text

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

**Text clustering** allows to create coherent groups of documents based on some **distance function** or **similarity measure**. Examples of documents groupings are:
- same **topic**;
- same **emotion**;
- same **problem** to be fixed;
- same **complaint/praise**;
- same **author**;
- same **text generator**;
- same **source document**.

## Document similarity

A usual similarity metric used for documents is **cosine similarity** between **TF-IDF vectors**.

## Clustering techniques

### k-Means

k-Means is one of the simplest clustering techniques. It produces $k$ clusters. The algorithm is the following.
1. Initialize $k$ centroids randomly;
2. Assign each data point ot the closest centroid;
3. Recompute centroid by averaging data points in cluster;
4. Repeat step (2) and (3) until convergence, when centroids stop moving.

The potential problems with $k$-means is that choosing the "right" value for $k$ is critical. Furthermore, the algorithm can converge on a **local minimum**.

### k-Medoids

In the k-Medodis algorithm we represent each cluster by its **medoid** rather than its centroid. A **medoid** is one of the datapoints from the dataset. In particular it is the point with the smallest average distance to all other points in the same cluster.
The algorithm is analogous to k-Means. The advantage of this approach is that it can be used with other metrics than Euclidean distance. Furthermore a medoid, being a real document, provides a realistic representation of the cluster.
The disadvantage is that the algorithm has much higher computational complexity with respect to k-Means.

---

### DBScan

The **DBScan** algorithm (which stands for **Density-Based Spatial Clustering of Applications with Noise**) is a density-based clustering algorithm. With this algorithm, you don't need to specify the number of clusters in advance.

## Topic modeling

**Topic models** are **soft clusters** of documents: documents can belong to multiple clusters. Each cluster is referred to as a **topic**.
A **topic vector** is a probability distribution over words, while a **document vector** is a probability distribution over topics.

Topic modeling is a form of matrix decomposition: it decomposes the terms $\times$ documents count matrix into two smaller matrices. terms $\times$ topics and topics $\times$ documents.

The most famous technique for Topic Modeling is **Latent Dirichlet Allocation** (LDA). It has this name because it uses a Dirichlet prior when estimating the parameters.

Topic modeling allows to make document representations more dense & useful, furthermore it allows to calculate more meaningful distances between documents.
It deals with problems of polysemy, synonymy, short documents. Sometimes it is useful for visualizing collections.
