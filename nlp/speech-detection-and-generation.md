---
marp: true
theme: summary
math: mathjax
---
# Speech detection and generation

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Mark Carman's slides_)

</div>

## Human speech

**Human speech** consists of:
- **vowels**, which are sounds pronounced without restricting the vocal tract;
- **consonants**, which are sounds made by partial or complete closing of the vocal tract.

Different sounds that make up words are referred to as phones/**phonemes**.

HUman phonation can be modeled as follows:
- the larynx/glottis produces pulses, acting as a **source**;
- the vocal tract shapes such pulses, acting as a **filter**.

The source is not very important for speech recognition, since the filter carries the most information.
As it is clear from the phonation model, speech is just a sound wave, i.e. a time series of pressure values over time.

We can distinguish specific types of sounds in speech:
- **vowels**: periodic signals;
- **fricatives**: consonants produced by forcing the air through a narrow channel,
- **glides**: smooth transitions;
- **bursts**: rapid transitions.

To distinguish different types of sounds, we can view them in the frequency domain using the Fourier transform.

Since an audio signal consists of a sequence of sounds, we can compute the frequency representation of consecutive sounds in sequence and arrange them in a tridimensional graph whose axes are frequency, time, and amplitude: this is called a **spectrogram**
In order to compute such representation, we can employ the **Short-time Fourier Transform** (**STFT**). We divide the signal into chunks and perform a Fast Fourier Transform in each chunk. The chunks overlap to reduce border effects.
Each chunk is pre-processed with a "windowing function" which further reduce the border effects by reducing the amplitude of the signal at the two ends of the chunk.
A special kind of spectrogram is the **Mel spectrogram**, which limits frequency range to a maximum of $8\ \text{kHz}$ and represents frequencies and amplitudes on logarithmic scale.

---

Usually, before running the STFT, the signal is pre-processed by applying a **pre-emphasis** filter to **amplify high frequencies**. This is useful for balancing the spectrum since high frequencies usually have smaller amplitudes, avoiding numerical problems when calculating the Fourier transform and possibly improving the signal-to-noise ratio.

Humans hear frequencies in the range $20\ \text{Hz}$ to $20\ \text{kHz}$. We distinguish noises based on their relative pitch.

## Speech recognition

**Speech recognition** is the problem of converting an audio-signal to text. Up until relatively recently, it was tackled using features extracted from the Mel spectrogram and Hidden Markov Models with Gaussian Mixture Models.
Now, it is more common to adopt a deep learning approach, using **Convolutional Neural Networks** (CNN) to detect phonemes either directly on the input waveform or on the Mel Spectrogram. The issue with this approach is that the classifier produces a prediction over a **fixed window**. We need to work out **how many windows** correspond to the **same phoneme**/latter.
This can be frame as a seq2seq problem. By using a special additional token which corresponds to the nil output, we can have such model to produce an output which isn't the same length of the input.

Powerful recent **transformer-based** architecture work with **raw audio** in time series representation, using a Convolutional Neural Network to produce the initial embeddings, followed by a Transformer to process them. This approach takes the name of **wav2vec**.

Even more recent Transformer-based systems with state-of-the-art performance make use of the **Mel spectrogram** as input representation. This approach, which takes the name of **Whisper**, is similar to a Vision transformer.

### Evaluating speech-to-text systemss

There are two metric to evaluate speech-to-text systems:
- The **Word Error Rate** (**WER**) in a string which penalizes detected words which are different from the ground truth, based on the edit distance:
$$
\text{W} = 100 \cdot \frac{\text{Insertions} + \text{Substitutions} + \text{Deletions}}{\text{Total words in correct transcript}}.
$$
- The **Sentence Error Rate** (**SER**) which is the percentage of sentences which had at least one error:
$$
\text{SER} = 100 \cdot \frac{\text{\# of sentences with at least one error}}{\text{Total number of sentences}}.
$$

---

## Speech synthesis

The aim of **speech synthesis** (a.k.a. text-to-speech) is to convert a **text string into an audio waveform**. It is often implemented as a 3-stage system:
1. conversion of **text** into **phonemes**;
2. conversion of **phonemes** into a **mel spectrogram**;
3. conversion of the **mel spectrogram** into an **audio signal**.

Usually, the text produced by text-to-speech systems need also to be normalized. We can train another seq2seq model to this end.

A problem in text-to-speech is **homograph disambiguation**: the English word contains words that are **written** in the **same way**, but **pronounced** in **different ways**. The correct pronunciation needs to be determined from the context.

An example of text-to-speech architecture is **Tacotron2**: it uses an LSTM-based encoder-decoder to generate a Mel spectrogram. **WaveNet** is the **vocoder** of Tacotron2: it converts the Mel spectrogram into an audio signal. 

### Evaluation of text-to-speech

The evaluation of text-to-speech systems requires **human testers**, checking **intelligibility** and **quality** (naturalness, fluency).

### Older approaches

The older approaches of transforming a text string into a waveform involve a 2 stages process:
1. **text analysis**: the conversion from a text string to a phonetic representation;
2. **waveform synthesis**: the conversion from the phonetic representation to the waveform.

The main approaches for **waveform synthesis** are:
- **Formant synthesis**: the use of an acoustic model and additive synthesis, it results in "robotic" voice.
- **Articulatory synthesis**: simulate movements of articulators and acoustics of the vocal tract (it is complex).
- **Concatenative synthesis**: concatenate small pre-recorded wave units (this is the most used approach).

The _traditional approach_ to **phonetic analysis** involves converting **words** into **list of phonemes**, using various approaches:
- **Dictionary-based conversion**: it relies on a dictionary which maps each word to its phonetic representation.

---

- **Grapheme-to-phoneme** (**g2p**) **conversion**: it trains a classifier for handling names and other unknown words.

Phonetic analysis is not enough. We need to determine also the right **prosody**, i.e. the intonation, stress, and rhythm of the sentence. There are some rules which were traditionally used to determine the prosody from the context. Nowadays the Machine Learning approach is the prominent one.

**Waveform synthesis** requires to solve two subproblems:
- **diphone synthesis**;
- **unit selection synthesis**.

A **diphone** is a phoneme-like unit from the middle of one phoneme to the middle of the next. Due to the coarticulation phenomenon, each phoneme differs slightly, depending on the preceding and following ones. Diphone synthesis can be implemented through a **diphone database**.

A **unit** is any piece of speech that can be concatentaed: diphones, syllables, ... .
