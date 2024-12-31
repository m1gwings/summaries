---
marp: true
theme: summary
math: mathjax
---
# Explainability of CNNs

<div class="author">

Cristiano Migali

</div>

## CNN visualization

### Visualizing filters

The first approach towards explainability of CNNs it the visualization of CNN filters. Filters with 3 channels can be visualized as RGB images; filters with 1 channel can be visualized as gray-scale images.
Unfortunately it is difficult to interpret filters with many channels which we can find at deeper layers. We can plot each channel as a gray-scale image but we won't be able in understanding the overall behavior.

### Visualizing maximally activating patches

Another approach consists in visualizing the so-called **maximally activating patches**. The process works as follows:
1. first we **select a neuron** in a deep layer of a pre-trained CNN;
2. we compute the activation of the neuron for each input image in the dataset;
3. we select the images yielding the highest activations;
4. finally we show the regions corresponding to the receptive field of the neuron in the images selected in the previous step.

This process is iterated for many neurons.

This approach is very computationally intensive since it requires to do inference on the whole dataset and it is also restricted to patches belonging to the data-set.

An **alternative** is to compute the input which maximally activates a neuron by considering the neuron activation as an objective function to be maximized iteratively via gradient ascent with back-propagation. Usually some form of regularization is added to steer the input to look more like a natural image.

We can adopt this approach also for the neurons in the very last layer of the classifier, which correspond each to a class.

### Grad-CAM

**CAM**s are not only very useful for weakly supervised localization, they are also an important tool for explainability since they allow to identify the region of the image which led to the decision of the network. **Grad-CAM** tries to improve the resolution of the heat-maps provided by CAM through image augmentation.

---

We consider the augmentation operator $\mathcal{A}_l : \mathbb{R}^{N \times M} \rightarrow \mathbb{R}^{N \times M}$ which performs, among the other things, random rotations and translations of the input image.
All the CAMs $\{ g_l \}$ that the CNN generates when fed with multiple augmented versions of the same input image, are very informative for reconstructing the high-resolution heat-map.
The entire pipeline from the augmented image to the generation of a low-resolution saliency map is seen as the result of the same linear down-sampling operator $\mathcal{D}$ applied to different perturbed variants of the same high-resolution map.
Then, heatmap super-resolution consists in solving an inverse problem:
$$
\arg \min_h \frac{1}{2} \sum_{l=1}^L || \mathcal{D}(\mathcal{A}_l(h)) - g_l ||_2^2 + \lambda {TV}_{l_1}(h) + \frac{\mu}{2} ||h||_2^2
$$
where ${TV}_{l_1}$ is the _anisotropic total variation regularization_ used to preserve the edges in the target heat-map.
This is solved through sub-gradient descent since the function is convex and non-smooth.
