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

- A **CSPRNG** is a deterministic function $\text{PRNG} : \{ 0, 1 \}^\lambda \rightarrow \{ 0, 1 \}^{\lambda + l}$ whose output cannot be distinguished from uniform sampling of $\{ 0, 1 \}^{\lambda + l}$ in $\Theta(\text{poly}(\lambda))$. $l$ is known as the **stretch**.

In practice we have only candidate CSPRNG. Indeed we have no proof that a PRNG exists, proving such a thing would imply $P \neq NP$.

CSPRNG are usually realized starting from another building block: **PseudoRandom Permutations** (**PRPs**), in turn defined starting from **PseudoRandom Functions** (**PRFs**).
Consider the set of functions $\mathbf{F} = \{ f : \{ 0, 1 \}^{\text{in}} \rightarrow \{ 0, 1 \}^{\text{out}} \}$. A uniformly samples function $f \sim \mathbf{F}$ can be encoded in a $2^{\text{in}}$ entries table, each entry _out_ bit wide. Then: $|\mathbf{F}| = 2^{\text{out} \cdot 2^{\text{in}}}$.

- A **PseudoRandom Function** (PRF) is a function $\text{prf}_{\text{seed}} : \{ 0,1 \}^{\text{in}} \rightarrow \{ 0, 1 \}^{\text{out}}$ which is parameterized by a $\lambda$ bit seed. The entire function is described by the value of the seed. It cannot be told apart from a random function $f \sim \mathbf{F}$ in $\text{poly}(\lambda)$.

- A **PseudoRandom Permutation** is a bijective PRF which produces outputs of the same dimension of the inputs: $\text{prf}_{\text{seed}} : \{ 0, 1 \}^{\text{len}} \rightarrow \{ 0, 1 \}^{\text{len}}$.

Observe that such function can be represented as a sequence with $2^{\text{len}}$ elements, each one being a string of $\text{len}$ bits. Thus, such a function, is a permutation of the sequence with all the strings of $\text{len}$ bits.
Operatively speaking, these functions act on a block of bits in input and produce a block of bits in output of the same size which looks unrelated from the input. Furthermore, the behavior of such functions is fully identified by the seed.

---

No formally proven PRP exists. Again, its existence would imply $P \neq NP$.
PRPs are typically constructed as follows.
1. Compute a small bijective boolean function $f$ of the input and the key (_here with bijective we mean that fixing the key and trying all possible inputs we get all possible outputs, no matter the fixed key_).
2. Compute $f$ again between the previous output and the key.
3. Repeat $2$ until you're satisfied.

Concrete PRPs go by the historical name of **block ciphers**. They are considered broken if, with less than $2^\lambda$ operations, they can be told apart from a PRP, e.g. via:
- Deriving the input corresponding to an output without the key.
- Deriving the key identifying the PRP or reducing the amount of plausible ones.
- Identifying non-uniformities in their outputs.

The key length $\lambda$ is chosen to be large enough so that computing $2^\lambda$ guesses is not **practically feasible**.
The following are numbers of operations which provide practically acceptable unfeasibility, according to different standards.
- **Legacy level security**: at least $2^{80}$ boolean operations.
- **5 to 10 years security**: at least $2^{256}$ boolean operations.
- **Long term security**: at least $2^{256}$ boolean operations.

Now we list some **widespread block ciphers**.
- **Advanced Encryption Standard** (**AES**): it work on 128 bit blocks. There are 3 key lengths: 128, 192, and 256 bits.
- **Data Encryption Algorithm** (**DEA**, a.k.a. DES): it is the legacy standard by NIST. The key is too short (just 56 bits). It is patches via triple encryption, which has $\lambda = 112$ equivalent security. This is still found in some legacy systems, and officially deprecated.

#### Electronic CodeBook (ECB) mode

One of the simplest way to use a block cipher for encryption is the **Electronic CodeBook** (**ECB**) **mode**. If the plaintext has lees bits than the block size, we simply pad it and pass it in input to the block cipher. Conversely, we split the input in blocks with the right number of bytes and encode each block with the same key.
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

One standard mechanism to provide <u>**integrity**</u> are **Message Authentication Codes** (**MACs**). The idea is to add a small piece of information (tag) to the encrypted message that allows to test for message integrity.
**Important**: MACs do NOT provide data authentication.

- A **MAC** is constituted by a pair of functions:
> - COMPUTE_TAG(string, key): returns the tag for the input string;
> - VERIFY_TAG(string, tag, key): returns true or false.

Observe that this method does not provide authentication **since** both the sender and the receiver can craft valid tags.

---

Resume from CBC (Cipher Block Chaining) MAC.