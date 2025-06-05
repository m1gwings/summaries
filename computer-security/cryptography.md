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

Cryptography was born in ancient society, when writing became more common, and hidden writing became a need. In particular it was born for commercial (e.g. the recipe for lacquer on clay tablets) or military uses. It was designed by humans, for human computers: algorithms were computed by hand ì, with pen and paper.

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

In 1955 Nash argues that **computationally secure** ciphers are ok. The rationale is the following. Consider a cipher with a finite, $\lambda$ bit long, key. Assume that the attacker effort to break the cipher is $\Theta(2^\lambda)$, while the owner of the key takes $\Theta(\lambda^2)$ to compute the cipher. The computational gap gets unsurmountable for large values of $\lambda$.

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
- Any symmetric cipher $(\mathbf{P}, \mathbf{K}, \mathbf{C}, \mathbb{E}, \mathbb{D})$ with $|\mathbf{P}| = |\mathbf{K}| = |\mathbf{C}|$ is perfectly secure if and only if:
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
