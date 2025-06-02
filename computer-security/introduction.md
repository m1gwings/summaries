---
marp: true
theme: summary
math: mathjax
---
# Introduction to Computer Security

<div class="author">

Cristiano Migali

</div>

The basic **security requirements** are captured in the **CIA** paradigm for information security, which states 3 requirements:
- **Confidentiality**: the information can be accessed only by authorized entities;
- **Integrity**: the information can be modified only by authorized entities, and only in the way such entities are entitled to modify it;
- **Availability**: the information must be available to all the parties who have a right to access it, within specified time constraints.

## Security concepts

Let's list some important concepts to frame security problems.

### Vulnerability

A **vulnerability** is something that allows to violate one of the constraints of the CIA paradigm.
An example is: a software that fails to check the size of attachments.

### Exploit

An **exploit** is a _specific_ way to use one or more vulnerabilities to accomplish a specific objective that violates the constraints.
An example is: a large attachment sent to the software which doesn't check for size.

### Asset

An **asset** identifies what is valuable for an organization.
Examples of assets are:
- hardware (e.g. laptops, computers, phones),
- software (e.g. applications, operating system, db),
- data (e.g. data stored in a db),
- reputation.

---

### Threat

A **threat** is a circumstance potentially causing a CIA violation.
Examples of threats are:
- denial of service (e.g. software or hardware unavailable);
- identity theft (e.g. unauthorized access to software/data);
- data leak (e.g. unauthorized release of data).

### Attack

An **attack** is an <u>intentional</u> use of one or more exploits with the objective of compromising a system's CIA.
Examples of attacks are:
- attaching a "malicious" PDF file to an email.

### Threat Agent

A **threat agent** is whoever/whatever may cause an attack to occur.
Examples of threat agents are:
- malicious software or individual attaching a file.

### Attacker

An **attacker** is whoever/whatever performs the attack.

Observe that there is a difference between an attacker and an hacker. An **hacker** is someone with an _advanced understanding_ of computers and computer networks, and willingness to learn "everything".
**Black hats** is the term used to refer to malicious hacker. The security professionals instead are known as **white hats**.

### Risk

The **risk** is the statistical and economical evaluation of the exposure to damage because of the presence of vulnerabilities and threats.
$$
\text{risk} = \text{asset} \times \text{vulnerabilities} \times \text{threats}.
$$

Security experts need to deal with assets and vulnerabilities, which are the aspects under control.

---

### Trust and assumptions

When evaluating the security of a system, it is necessary to set boundaries. Part of the system need to be **assumed** secure. This is known as "trusted element".
