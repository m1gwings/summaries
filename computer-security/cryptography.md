---
marp: true
theme: summary
math: mathjax
---
# Introduction to Cryptography

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

**Cryptography** tries to solve the following problem: how to communicate a secret message over an untrusted channel. Indeed, the etymology is "art of secret writing".

## History of cryptography

Cryptography was born in ancient society, when writing became more common, and hidden writing became a need. In particular it was born for commercial (e.g. the recipe for lacquer on clay tablets) or military uses. It was designed by humans, for human computers: algorithms were computed by hand, with pen and paper.

In 1553, for the first time Bellaso separates the encryption method from the key.

In 1883, Kerchoff stated six principles for a good cipher:
1. It must be practically, if not mathematically, unbreakable.
2. It should be possible to make it public, even to the enemy.
3. The key must be communicable without written notes and changeable whenever the correspondents want.
4. It must be applicable to telegraphic communication.
5. It must be portable, and should be operable by a single person.
6. Finally, given the operating environment, it should be easy to use, it shouldn't impose excessive mental load, nor require a large set of rules to be known.

In the 20th century, mechanical computation changed cryptography. First rotor machine was developed in 1917 by Ed Hebern. The design was popularized in WWII by the german Enigma. During WWII, Alan Turing et al. worked at Betchley Park to break the Enigma cipher. 

In 1949 Shannon proved that a **mathematically unbreakable** cipher exists.

In 1955 Nash argues that **computationally secure** ciphers are ok. The rationale is the following. Consider a cipher with a finite, $\lambda$ bit long, key. Assume that the attacker effort to break the cipher is $\Theta(2^\lambda)$, while the owner of the key takes $\Theta(\lambda^2)$ to compute the ciphertext. The computational gap gets unsurmountable for large values of $\lambda$.

---

## Key concepts in cryptography

- A **cryptosystem** is a system that takes in input a message (known as **plaintext**) and transforms it into a **ciphertext** with a reversible function that usually takes a **key** as a further input.

- The **Kerckhoffs' Principle** states that the security of a cryptosystem relies only on the secrecy of the key, and never on the secrecy of the algorithm.

This means that in a secure cyptosystem we cannot retrieve the plaintext from the ciphertext without the key. Also, we cannot retrieve the key from analyzing ciphertext-plaintext pairs. Finally, algorithms must always be assumed known to the attacker.

- The **plaintext space $\mathbf{P}$** is the set of possible plaintext messages (e.g., $\{0, 1\}^l$).
- The **ciphertext space $\mathbf{C}$** is the set of possible ciphertexts (again, usually $\{ 0, 1 \}^{l'}$).
- The **keyspace $\mathbf{K}$** is the set of possible keys ($\{ 0, 1 \}^\lambda$).

- An **encryption function** is a function $\mathbb{E} : \mathbf{P} \times \mathbf{K} \rightarrow \mathbf{C}$. A **decryption function** is a function $\mathbb{D} : \mathbf{C} \times \mathbf{K} \rightarrow \mathbf{P}$. Such functions must satisfy a _correctness property_: for all $\text{ptx} \in \mathbf{P}$ there exist $k, k' \in \mathbf{K}$ s.t. $\text{ptx} = \mathbb{D}(\mathbb{E}(\text{ptx}, k), k')$.

In order to provide **confidentiality**, we want to prevent anyone not authorized from being able to understand the data.

We consider the following **attacker models**.
- **Ciphertext only**: the attacker simply eavesdrops.
- **Known plaintext attack**: the attacker knows both the plaintext and the corresponding ciphertext.
- **Chosen plaintext attack**: the attacker choses the plaintext to encrypt.
- The attacker may tamper with the data and observe the reactions of a decryption-capable entity. In the limit case, the attacker sees the actual decrypted value.

## Symmetric encryption

The basic idea behind symmetric encryption is to use the same key in both the encryption and decryption function. This approach has some issues: how to agree on the key? We cannot send the key on the same channel of the messages, since such channel is untrusted. Thus an off-band transmission mechanism is needed. This poses some scalability problems.

A symmetric algorithm is composed of the following building blocks.

- **Substitution**: replacing a byte with another according to a certain map. An example is the Caesar cipher, in which we replace each letter in a sentence with the one following it by $K$ positions in the alphabet. This is of course a naive approach, the keyspace is too small.

---

- **Transposition**: it means swapping the values of some bits. A toy example could involve arranging the plaintext in a matrix, writing by rows and reading by columns. The key would be the pair: number of rows, number of columns. The keyspace is still relatively small, but now **repetitions** and **structure** are gone.

Let's introduce the definition of perfect cypher.
- In a **perfect cipher**, for all $\text{ptx} \in \mathbf{P}$ and $\text{ctx} \in \mathbf{C}$, we have that:
$$
\mathbb{P}[\text{ptx sent} = \text{ptx}] = \mathbb{P}[\text{ptx sent} = \text{ptx} \ | \ \text{ctx sent} = \text{ctx}].
$$
In other words, seeing the ciphertext gives us _no information_ on what the corresponding plaintext could be. The definition is not constructive, so it makes sense to ask if a perfect cipher exists.
The answer is given by the following theorem due to Shannon.
- **Theorem**: any symmetric cipher $(\mathbf{P}, \mathbf{K}, \mathbf{C}, \mathbb{E}, \mathbb{D})$ with $|\mathbf{P}| = |\mathbf{K}| = |\mathbf{C}|$ is perfectly secure if and only if:
> - every key is used with probability $\frac{1}{|\mathbf{K}|}$;
> - a unique key maps a given plaintext into a given ciphertext: for all $(\text{ptx}, \text{ctx}) \in \mathbf{P} \times \mathbf{C}$ there exists a unique $k \in \mathbf{K}$ s.t. $\mathbb{E}(\text{ptx}, k) = \text{ctx})$;
> - each key must be at least as long as the plaintext.

A **simple working example** which satisfies the above properties is the following. Assume $\mathbf{P}$, $\mathbf{K}$, $\mathbf{C}$ to be the set of binary strings. The encryption function draws a _uniformly random_, fresh key $k$ our of $\mathbf{K}$ each time it is called and computes $\text{ctx} = \text{ptx} \oplus k$ (where $\oplus$ is the bitwise XOR).

Vernam patented a telegraphic machine implementing $\text{ptx} \oplus k$ in 1919. Mauborgne suggested the use of a random tape containing the key $k$. Using Vernam's encrypting machine with Mauborgne's suggestion implements a perfect cipher.
This cipher is known as **One Time Pad** (OTP).
It is not viable in practice since it is too difficult to generate, share and store the key.

Real-world algorithms are not perfect ($|\mathbf{K}| < |\mathbf{P}|$), and so can be broken. Each ciphertext-plaintext pair leaks a small amount of information, since the key is re-used. For this reason, brute forcing is possible for real world ciphers: we try all possible keys, until one produces an output that is "more likely". Conversely, perfect ciphers are not vulnerable to brute force, because trying all the (random) keys will yield all the possible plaintexts, which are all equally likely.

- A real (non perfect) cryptosystem is **broken** if there is a way to break it that is **faster** than brute forcing.

Real cryptosystems rely on the **computational security assumption**. The idea is to design a cipher so that a successful attack would imply being able to solve  a hard computational problem efficiently (which is assumed not possible since the common belief is that $P \neq NP$).

---

Now we list some computationally hard problems.
A first example is **factor large integers**. If $p$ and $q$ are two **large primes**, computing $n = p q$ is easy, but retrieving $p$ and $q$ from $n$ is slow (you need to use the quadratic sieve field: you try all primes until you get the smaller between $p$ and $q$).
Another example is the **discrete logarithm**. Given $x$, $a$, $p$, it is easy to compute $y = a^x \mod p$, but knowing $y$, it is **difficult** to compute $x$.

In order to prove that a cryptosystem is computational secure, we need to carry out the following steps:
1. Define the ideal attacker behavior.
2. Assume a given computational problem is hard.
3. Prove that any non ideal attacker solves the hard problem.

### Cryptographically safe pseudorandom number generators

In order to build a cipher which resemble an OTP, preserving practicality, we may want to expand a finite-length key. Now we define an object which can achieve such objective.

- A **CSPRNG** is a deterministic function $\text{PRNG} : \{ 0, 1 \}^\lambda \rightarrow \{ 0, 1 \}^{\lambda + l}$ whose output cannot be distinguished from uniform sampling of $\{ 0, 1 \}^{\lambda + l}$ in $O(\text{poly}(\lambda))$. $l$ is known as the **stretch**.

In practice we have only candidate CSPRNG. Indeed we have no proof that a PRNG exists, proving such a thing would imply $P \neq NP$.

CSPRNG are usually realized starting from another building block: **PseudoRandom Permutations** (**PRPs**), in turn defined starting from **PseudoRandom Functions** (**PRFs**).
Consider the set of functions $\mathbf{F} = \{ f : \{ 0, 1 \}^{\text{in}} \rightarrow \{ 0, 1 \}^{\text{out}} \}$. A uniformly sampled function $f \sim \mathbf{F}$ can be encoded in a $2^{\text{in}}$ entries table, each entry _out_ bit wide. Then: $|\mathbf{F}| = 2^{\text{out} \cdot 2^{\text{in}}}$.

- A **PseudoRandom Function** (PRF) is a function $\text{prf}_{\text{seed}} : \{ 0,1 \}^{\text{in}} \rightarrow \{ 0, 1 \}^{\text{out}}$ which is parameterized by a $\lambda$ bit seed. The entire function is described by the value of the seed. It cannot be told apart from a random function $f \sim \mathbf{F}$ in $O(\text{poly}(\lambda))$.

- A **PseudoRandom Permutation** is a _bijective_ (in the sense that, for each fixed $\text{seed}$, the resulting function is bijective) PRF which produces outputs of the same dimension of the inputs: $\text{prf}_{\text{seed}} : \{ 0, 1 \}^{\text{len}} \rightarrow \{ 0, 1 \}^{\text{len}}$.

Observe that, fixed a $\text{seed}$, the resulting function can be represented as a sequence with $2^{\text{len}}$ elements, each one being a string of $\text{len}$ bits. Thus, such a function, is a permutation of the sequence with all the strings of $\text{len}$ bits.
Operatively speaking, these functions act on a block of bits in input and produce a block of bits in output of the same size which looks unrelated from the input. Furthermore, the behavior of such functions is fully identified by the seed.

---

No formally proven PRP exists. Again, its existence would imply $P \neq NP$.
PRPs are typically constructed as follows.
1. Compute a small bijective boolean function $f$ of the input and the key (_here, again, with bijective we mean that fixing the key and trying all possible inputs we get all possible outputs, no matter the fixed key_).
2. Compute $f$ again between the previous output and the key.
3. Repeat $2$ until you're satisfied.

Concrete PRPs go by the historical name of **block ciphers**. They are considered broken if, with less than $\Theta(2^\lambda)$ operations, they can be told apart from a PRP, e.g. via:
- Deriving the input corresponding to an output without the key.
- Deriving the key identifying the PRP or reducing the amount of plausible ones.
- Identifying non-uniformities in their outputs.

The key length $\lambda$ is chosen to be large enough so that computing $2^\lambda$ guesses is not **practically feasible**.
The following are numbers of operations which provide practically acceptable unfeasibility, according to different standards.
- **Legacy level security**: at least $2^{80}$ boolean operations.
- **5 to 10 years security**: at least $2^{128}$ boolean operations.
- **Long term security**: at least $2^{256}$ boolean operations.

Now we list some **widespread block ciphers**.
- **Advanced Encryption Standard** (**AES**): it work on 128 bit blocks. There are 3 key lengths: 128, 192, and 256 bits.
- **Data Encryption Algorithm** (**DEA**, a.k.a. DES): it is the legacy standard by NIST. The key is too short (just 56 bits). It is patches via triple encryption, which has $\lambda = 112$ equivalent security. This is still found in some legacy systems, and officially deprecated.

#### Electronic CodeBook (ECB) mode

One of the simplest way to use a block cipher for encryption is the **Electronic CodeBook** (**ECB**) **mode**. If the plaintext has less bits than the block size, we simply pad it and pass it in input to the block cipher. Conversely, we split the input in blocks with the right number of bytes and encode each block with the same key.
In this approach we use the same key for each block, leaking information. Furthermore we preserve the structure of the plaintext: two blocks in the plaintext with the same value, will have the same value also in the ciphertext.

#### Counter (CTR) mode

One way of solving the issues of ECB mode is to use **Counter** (**CTR**) **mode**.

---

In counter mode we use the block cipher to encrypt the values of a counter which starts from 0 and increases by 1 for each block in the plaintext, using still each time the same key. The output is a PRNG assuming that the block cipher is a PRP.
The output of such mechanism is combined in XOR with the plaintext, simulating an OTP where the key is pseudo-random instead of being random. Observe that there is nothing special in the starting point of the counter, but it must be agreed between who encrypts and who decrypts.

This cipher is sufficient to guarantee confidentiality against **ciphertext-only attacks**. Unfortunately the CTR mode of operation is <u>insecure against **chosen-plaintext attacks**</u> since the encryption is deterministic: the same plaintext is always mapped to the same ciphertext.

To solve the issue, there are 3 different approaches.
- **Rekying**: change the key for each block with a ratchet (_see later_).
- **Randomize** the encryption by add removable randomness to the encryption changing the mode of employing the PRP.
- **Numbers used ONCE** (**NONCEs**): pick a NONCE as the counter starting point. The NONCE is public.

#### Symmetric ratcheting

This mechanism takes the name from its mechanical counterpart: it is not possible to roll-back the procedure. The idea is to start with a $\lambda$ bit seed and use a PRNG with $2 \lambda$ stretch to generate a sequence of keys. The first $\lambda$ bits in output from the PRNG are the $i$-th key. The second $\lambda$ bits are used as seed to generate the next key and the next seed. The first input to the PRNG is the original seed. Thus, each block is encrypted with a different key.

### Malleability and active attackers

With the ciphers that we have seen so far, making changes to the ciphertext (not knowing the key) maps to predictable changes in the decrypted plaintext. This fact can be creatively abused to build decryption attacks. We want to avoid this fact, adding a mechanism to ensure **data integrity**.

#### Message Authentication Codes

One standard mechanism to provide <u>**integrity**</u> are **Message Authentication Codes** (**MACs**). The idea is to add a small piece of information (tag) <u>to the encrypted message</u> that allows to test for message integrity.
**Important**: MACs do NOT provide data authentication.

- A **MAC** is constituted by a pair of functions:
> - COMPUTE_TAG(string, key): returns the tag for the input string;
> - VERIFY_TAG(string, tag, key): returns true or false.

---

Observe that this method does not provide authentication **since** both the sender and the receiver can craft valid tags.

One possible way of implementing a MAC is the **Cipher Block Chaining MAC** (**CBC-MAC**). It is realized as follows. We encrypt the first block in the plaintext with the block cipher using our key. Then we compute the XOR of such output with the second block of the plaintext and encrypt the result again with the key. We iterate the process until the last block of the plaintext. It can be proved that the approach described so far is secure only for **prefix free** messages (i.e., we don't have two messages which are one the prefix of the other). Encrypting the result once more provably fixes the issue.

#### Hash functions

- An **hash function** is a function $H()$ which maps an arbitrary-length input $x$ on a fixed-length output $h$, known as _digest_. It needs to be **fast**.

Hash function provide a fast way to verify data integrity: comparing the digests.
The issue with hash functions is that they suffer from the **collision** problem: the codomain is "smaller" than the domain, thus the function can't be 1-to-1.

Given a proper hash function, it should be **computationally infeasible** to find:
- an input $x$ such that, for a given digest $h$, $H(x) = h$ (this is known as **pre-image attack resistance**);
- an input $y$ such that, for a given different input $x \neq y$, $H(y) = H(x)$ (this is known as **second pre-image attack resistance**);
- a pair of inputs $x, y$ such that $H(x) = H(y)$ (this is known as **collision resistance**).

An hash function may be **broken** if, <u>faster than brute-forcing</u>, an attacker is able to find an input (or pair of inputs) satisfying one of the properties above.
With an $n$-sized function, we can find a pre-image faster than brute-forcing, if we take less than $2^{n-1}$ trials (with $2^{n-1}$ trials you have $50 \%$ chance of finding a pre-image since you're trying half of the $2^n$ $n$-bit longs strings).
While, we are able to find a collision faster than brute-forcing if we try less than $2^{\frac{n}{2}}$ pairs (again, with $2^{\frac{n}{2}}$ pairs, we have $50 \%$ chance of finding a collision because of the birthday paradox).

Some candidate hash functions are the following:
- SHA-2 was privately designed by NSA and has a digest of 256, 384, or 512 bits.
- SHA-3 followed a public design contest (similar to AES) and has again the same digest size of SHA-2.

They are both currently unbroken and widely standardized.

Example of hash function which <u>should not be used</u> are the following:
- SHA-1 has a digest of 160 bits, it si collision-broken (obtainable in $\approx$ $2^{61}$ ops).

---

- MD-5 is horribly broken: it is possible to find collisions in $\approx 2^{11}$ operations and to carry out a second pre-image attack in $\approx 2^{40}$ operations.

Hash function can be used to:
- store/compare hashes instead of values;
- to build MACs: generate tag hashing using together the message and a secret string and verify the tag recomputing the same hash (this approach is known as **HMAC**);
- write down only the hash of the disk image you obtained in official documents for forensic use.

## Asymmetric crypto-systems

There are still some features we would like which are not provided by symmetric crypto-system:
- agreeing on a short secret over a public channel;
- confidentially sharing a message over a public authenticated channel without sharing a secret with the recipient;
- actual data authentication.

Before 1976, the solution was to rely on human carriers/physical signatures. The invention of **asymmetric crypto-systems** revolutionized the scenario.

### Diffie-Hellman key agreement

The goal of the **Diffie-Hellman key agreement** is to make two parties agree on a secret value w/ only public messages.

The procedure relies on the so-called **Computational Diffie-Hellman assumption** (**CDH**).
- **CDH Assumption**: let $(\mathbf{G}, \cdot) \equiv \langle g \rangle$ be a finite cyclic group, and two numbers $a, b$ sampled uniformly from $\{ 0, \dots, |\mathbf{G}|-1 \}$. Then, given $g^a$ and $g^b$, finding $g^{ab}$ costs more than $\text{poly}(\log|\mathbf{G}|)$. The best current attack approach is to find either $b$ or $a$ (a discrete logarithm problem).

The attacker model is the following:
- it can eavesdrop anything, but not tamper;
- the CDH assumption holds.

Now we introduce some definitions needed to outline the procedure.
- Let $p$ be a prime number. We say that a number $a$ is a **primitive root** of $p$ if raising $a$ to any number between $1$ and $p-1$, $\mod p$, we obtain each number between $1$ and $p-1$.

---

The Diffie-Hellman key agreement works as follows.
1. Pick a prime $p$ and a primitive root $a$ of $p$ and make both public.
2. Pick a secret number $X$ in $\{ 1, \dots, p-1 \}$. Each party should pick a secret number. Assuming that Alice and Bob are the parties of the communication, Alice will pick the secret $X_A$ and Bob will pick the secret $X_B$.
3. Compute $Y = a^X \mod p$ (hence $Y_A = a^{X_A}\mod p$, $Y_B = a^{X_B}\mod p$).
4. Share $Y$ with the other parties (Alice sends $Y_A$ to Bob and Bob sends $Y_B$ to Alice).
5. Compute the secret $K = Y_{\text{received}}^X$ (i.e. $K = Y_B^{X_A} = Y_A^{X_B}$).

Due to the CDH assumption, it is hard for someone who eavesdrops on the public channel to compute the secret $K$ knowing just $Y_A$ and $Y_B$.

Let $\lambda = \log |\mathbf{G}|$, breaking the CDH assumption requires using less than $\theta(2^\frac{\lambda}{2})$ operations.

### Public key encryption

The main concept behind public key encryption is the following: the cipher uses two keys key1 and key2. What is encrypted with key1 can be decrypted only with key2 (and not with key1 itself), and vice-versa. One of the two keys is kept **private** by the subject, and the other can be **publicly** disclosed. This solves the problem of key exchange.
The employed approaches are such that it should be easy to compute the public key from the private key, but the private key "cannot" be retrieved from the public key.

Assuming that the attacker cannot tamper messages, we can achieve **confidentiality** on an untrusted channel as follows. The two parties share the public key on the untrusted channel. Each party encrypts the message they want to send with the public key of the other party. Then the other party is the only one who can decrypt the message, assuming the confidentiality of their private key.

Asymmetric crypto-system tend to be significantly more computationally intensive than symmetric ones. Thus, they are often used to share a secret key between two parties which is then used to communicate through symmetric encryption.

#### RSA algorithm

The **RSA algorithm** is an algorithm for public key encryption. It relies on the hard problem of factorization. The key sizes used in RSA are often of 2048 or 4096 bits. 1024 bit long keys are also usually safe.
**Important**: even though asymmetric encryption algorithms also have their key length, this is not by itself a metric of security (conversely to what happens for symmetric algorithms). What we should compare is the number of operations required for a brute-force attack.

---

### Authenticating the data

To build a secure hybrid encryption scheme, we need to be sure that the public key that the sender uses is the one of the recipient. That is, we would like to be able to verify the authenticity of a piece of data without a pre-shared secret.

**Digital signatures** solve the problem and much more. Proper signatures cannot be repudiated by the user. They rely on asymmetric cryptographic algorithms.
In particular they provide authentication and integrity in the following way. A party computes the digest of the message they want to send and then encrypts it with their private key. The other party can use the public key of the sender to decrypt the encrypted digest and compare it against the digest of the received message. Assuming that the private key is kept secret, we are sure of the identity of the sender being the only one with access to their private key, obtaining authentication. Furthermore, by comparing the digest of the message with the decrypted digest, we also get authenticity.

The following are widespread signature schemes:
- **RSA** (with different order than operations);
- **Digital Signature Standard** (**DSA**).

### Public key binding problem

We still have an issue: the exchange of public keys **must be secured**. In particular, each public key must be bound to the correct user identity.
If public keys are not authentic, a Man-In-The-Middle attack is possible on asymmetric encryption and anyone can produce a signature on behalf of anyone else.

A **Public Key Infrastructure** (**PKI**) is what associates keys with identity on a wide scale. A PKI uses a trusted third party authority called a **Certification Authority** (**CA**). The CA **digitally signs** files called **digital certificates**, which bind an identity (a **Distinguished Name** (**DN**)) to a public key.
In particular, the CA produces a document with the identity of an actor (a DN) and its public key, which is then digitally signed with the secret key of the CA. Then the CA provides the digitally signed certificate to anyone who wants to communicate with the actor. The certificate can be validated through the public key of the CA (as it is usually done with digital signatures). Now we have the same problem of before, we need a secure way to gather the public key of the CA.
A CA could have its certificate signed by another CA to whom we could ask. Of course this process cannot regress to the infinite. We need a trusted element: a **root of trust**. These are known as **top-level CA**. Their certificate is self-signed. The public keys of such CAs are directly stored in the devices instead of being gathered from the internet. This approach is known as **Software Trusted Storage**.

What we described produces the so-called **certification authorities hierarchy**, in which we distinguish **root CAs** and **subsidiary CAs**.

---

#### Certificate revocation issues

Signatures cannot be revoked, but certificates need to be revoked at times. To do so there exist **Certificate Revocation Lists** (**CRLs**) and, as an alternative, the **Online Certificate Status Protocol** (OCSP) which provides real-time certificate verification, improving efficiency over traditional CRLs.

The sequence of verifications required to check the validity of a certificate is the following.

1. Does the signature validate the document?
2. Is the public key the one on the certificate?
3. Is the certificate the one of the subject?
4. Is the certificate validated by the CA?
5. Is the root certificate trusted?
6. Is the certificate in a CRL?

## Fundamentals of information theory

_Shannon_'s information theory is a way to mathematically frame communication. It provides a way to quantify information.
A communication takes place between two **endpoints**:
- a _sender_: made of an information source and an encoder;
- a _receiver_: made of an information destination and a decoder.

Information is carried by a channel in the form of a sequence of **symbols** of a **finite alphabet**.
The receiver gets information only through the channel.
It will be uncertain on what the next symbol is, until the symbol arrives. Thus we model the sender as a **random variable**. Acquiring information is modeled as getting to know an outcome of a random variable $X$. The amount of information depends on the distribution of $X$. Intuitively, the closer is $X$ to a uniform distribution, the higher the amount of information I get from knowing an outcome.
Encoding maps each outcome as a finite sequence of symbols. More symbols should be needed when more information is sent.

We need a way to measure uncertainty with the following desirable properties:
- it should be a non-negative measure;
- "combining uncertainties" should result in addition of the corresponding measures.

- Let $X$ be a discrete random variable with $n$ outcomes in $\{ x_0, \dots, x_{n-1} \}$ with $p_i = \mathbb{P}[X = x_i]$. The **entropy** of $X$ is $H(X) = -\sum_{i=0}^{n-1} p_i \log_b p_i$. The measurement unit of entropy depends on the base $b$ of the logarithm: typical case for $b=2$ is bits.

---

- **Shannon's noiseless coding theorem**: it is possible to encode the outcomes of $n$ i.i.d. variables, each one with entropy $H(X)$, into no less than $nH(X)$ bits. If $< nH(X)$ bits are used, some information will be lost.

A consequence of this theorem is that arbitrarily compression of bit strings is impossible without loss. Cryptographic hashes must discard some information.
Another consequence is that guessing a piece of information (i.e., one outcome of $X$) is at least as hard as guessing a $H(X)$ bit long bit string.

- The **min-entropy** of $X$ is defined as $H_\infty(X) = -\log(\max_{i=1}^{n-1} p_i)$. Intuitively, it is the probability of random variable with uniform distribution, where the probability of each outcome is $\max_{i=1}^{n-1} p_i$. Guessing the most common outcome of $X$ is at least as hard as guessing a $H_\infty(X)$ bit long bit string.
