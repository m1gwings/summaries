---
marp: true
theme: summary
math: mathjax
---
# Authentication

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

- **Identification** is the process through which an entity declares its identifier (e.g. "I am `foobar`").
- **Authentication** is the process through which an entity provides a _proof_ that verify its identity (e.g. "Here is `foobar`'s ID card").

Authentication can be:
- **Unidirectional**: when only one of the entities involved in the communication, communicates to the other its identity together with a proof to verify it.
- **Bidirectional** (or **mutual**): when both the entities in the communication authenticate themselves.

Authentication can happen between any entity (e.g. human to human, human to computer, computer to computer).

There are three **factors** of authentication:
1. Something that the entity **knows** (e.g. a password, PIN, ...).
2. Something that the entity **has** (e.g. a door key, a smart card, ...).
3. Something that the entity **is** (e.g. face, voice, fingerprints).

For humans (3) is more used than (2) which is more used than (1).
For machines, (1) is more used than (2) which is more used than (3).

**Multi-factor** authentication uses two or three factors.

## The "to know" factor

The **advantages** of this factor are:
- low cost;
- ease of deployment;
- low technical barrier.

The **disadvantages** are that secrets can be stolen/snooped, guessed, or cracked.
Possible **countermeasures** (which are costs) involve enforcing passwords that:
- change/expire frequently;
- are long and have a rich character set;
- are not related to the user.

---

Countermeasures are costs since humans are not machines. They are inherently unable to keep secrets and it is hard to _remember_ complex passwords.
For this reason it is important to choose the right countermeasure depending on the most likely attack in the scenario under study.
Against **snooping**, complexity is unimportant, change is important, being related to the user or not is unimportant.
Against **cracking**, complexity is important, change may help, being related to the user or not is unimportant.
Against **guessing**, complexity may help, change may help, not being related to the user is important.

It is important when using the "to know" factor of authentication to ensure the secure **exchange** of the **secret**. In particular, we can minimize the risk that secrets get stoles through _mutual authentication_ if possible and using a _challenge-response_ or _zero knowledge proof_ scheme.
Authentication involves also **storing** the **secret**. Again, to minimize the risk that secrets get stolen, never store passwords in clear: use hashing and salting to mitigate dictionary attacks, use access control policies, never disclose secrets in password-recovery schemes.

## The "to have" factor

The **advantages** of this factor are that:
- it is a human factor (it is less likely to hand out a key);
- it has relatively low cost;
- it has a good level of security.

The **disadvantages** are that:
- it is hard to deploy;
- the something that the user must prove to possess can be lost or stolen.

The **countermeasure** to the second disadvantage is to use a "to have" factor as a second factor.

Example of classic technologies are:
- The **one-time password generators**: they use a secret key and a counter synchronized with the host. A MAC-compute function is used to compute a MAC with the counter and the key. The host verifies the MAC through the MAC-verify function.
- The **smart cards**: they are CPUs with non-volatile RAM with a private key. The smart card authenticates itself to the host via a **challenge response** protocol. It uses the private key to sign the challenge. The private key does not leave the device. They are tamper proof to some extent.
- **Static OTP lists**: they are known to both the client and the host. The host chooses a challenge (e.g. it points out an entry of the list that the client must provide). The client transmits the response. The host should not keep the list in clear.

---

- **Yubikeys**: it can be inserted into a USB port. You can ta the Yubikey when prompted. It generates a secure code: the device sends a **one-time password** or **cryptographic key for authentication**.

## The "to be" factor

The **advantages** of this factor are that:
- it has a high level of security and robustness;
- it requires no extra hardware to carry around.

The **disadvantages** are that:
- it is hard to deploy;
- it involves probabilistic matching;
- measurements could be invasive;
- some features can be cloned;
- bio-characteristics change (**countermeasure**: re-measure often);
- privacy sensitivity (**countermeasure**: secure the process);
- users with disabilities (**countermeasure**: provide alternatives).

### Fingerprint

An example of a "to be" authentication factor is the **fingerprint**.
TO carry out the _enrollment_, we need a reference sample of the user's fingerprint, acquired by a fingerprint readers. The features are derived from the sample. For higher accuracy, you can record the features for more than one finger and different positions.
The feature vectors are stored ina secure database. When the user logs on, a new reading of the fingerprint is taken; features are compared against the reference features. The user is accepted if the match is above a pre-defined threshold.
The main issue of this approach are _false positives_ and _false negatives_.

## Novel and experimental factors of authentication

Some _novel_ and _experimental_ factors of authentication are:
- The **social** factor: the user must prove they know someone.
- The **single sign on** tries to solve the following problem: managing and remembering multiple passwords is complex. Users re-use passwords over multiple sites. A solution is to elect a trusted host, users authenticated on the trusted host, then other hosts ask the trusted host if a user is authenticated. This approach has a single point of _trust_: the trusted server. If it is compromised, then all sites are compromised. The password reset scheme must be bulletproof. Furthermore, it is difficult to get it right for the developers since the flow is complex to implement and, even though libraries exists, they can be bugged.

---

## Password managers

**Password managers** ease the problem of managing and remembering multiple password. You select a trusted password managed. You then authenticate on the password manager with a <u>master password</u> and generate/copy a password for each service.

The **advantages** are that:
- There is no need to remember all passwords.
- It allows generating robust passwords different for each service.
- It improves usability.

The **disadvantages** are that:
- It is a single point of trust and failure.
- It extends the attack surface.
