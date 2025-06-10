---
marp: true
theme: summary
math: mathjax
---
# Access control

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

**Access control** is the process of determining if an authenticated user can access or not to a certain resource in a certain way. It is a binary decision, what makes it complex is a problem of scale: you cannot explicitly list the answers for all the possible scenarios and, thus, you need to resort to _rules_.

The **component** of the kernel which enforces the **access control policies** is the **reference monitor**. A reference monitor has the following requirements:
- it should be tamper proof;
- it cannot be bypassed;
- it is small enough to be verified/tested extensively.

The reference monitor has to find and evaluate the security policy relevant for the given request. It verifies the identity of the principal making the request and decides whether the access is granted or denied. This is "easy" in centralized systems, but gets more difficult in distributed ones.

The **access control models** can be roughly divided in:
- **Discretionary Access Control** (**DAC**);
- **Mandatory Access Control** (**MAC**);
- **Role-Based Access Control** (**RBAC**).

The difference between DAC and MAC is in who assigns privileges. RBAC abstracts roles from identities.

## Discretionary Access Control

In **Discretionary Access Control**, the resource owner discretionarily decides its access privileges. All off-the-shelf OSs implement DAC.
For each resource (**object**), we need to specify who (**subject**) can access it in a specific way (**action**).
In UNIX:
- The **subjects** are: users and groups.
- The **objects** are files (_remember that in UNIX everything is a file_).
- The **actions** are: read, write, execute.

In WIndows:
- The **subjects** are: users and roles (multiple ownership is allowed).

---

- The **objects** are files and "other" resources.
- The **actions** are delete, change permissions, change ownership.

In UNIX, permissions are represented with permission **triads**.  
Each file has 3 triads of permission bits: one for the **owner**, one for the **group**, and one for **others**.  
These are shown as a 10-character string like `-rwxr-x--x`, where:
- The first character indicates the file type (`-` for regular file, `d` for directory, etc.).
- The next 9 characters are grouped in sets of 3: **read** (`r`), **write** (`w`), and **execute** (`x`), or `-` if that permission is not granted.

For example, `-rw-r--r--` means a regular file where:
- the owner can read and write,
- the group can read,
- others can also read.

In general, we can encode the information required by the DAC model (subjects, objects, and actions) in a **protections state**, which is a triple $(s, o, a)$ where $s$ is a subject, $o$ is an object, and $a$ is an action. We can arrange these triples in a matrix $A$ with a row for each subject and a column for each object. Each entry of the matrix $A[s, o]$ is the list of actions that subject $s$ can perform on object $o$.
This is known as the **HRU model**.
The basic operations on this data structure are:
- create (or destroy) a subject $s$;
- create (or destroy) an object $o$;
- add (or remove) an action from $A[s, o]$.

A sequence of basic operations can be casted into an atomic update through **transitions**.

Given an initial protection state and a set of basic operations, we need to ask ourselves the following: is there any sequence of transitions that leaks a certain right $r$ (for which the owner is removed) into the access matrix? If not, then the system is safe w.r.t. right $r$.
In a generic HRU model with infinite resources, this is an **undecidable** problem.

Common DAC implementations involve a reproduction of the HRU model. Observe that the access matrix is a sparse matrix.
Alternative implementations are:
- **Authorization tables**: they record non-null triples $(s, o, a)$.
- **Access Control Lists** (**ACLs**): they record by column (i.e., for each **object**, the list of subjects and authorizations).
- **Capability Lists** (**CLs**): they record by row (i.e., for each **subject**, the list of objects and authorizations).

---

ACLs are efficient with **per object** operations. This is the most common case. They don't allow multiple owners (even though this is partially achievable via groups).

CLs are efficient with **per subject** operations. Usually objects change and subjects stay, so they turn out being inefficient.

The general shortcomings of DAC systems is that:
- They cannot prove safety.
- They control the access to objects but not to the data inside the objects (i.e., we have a problem of granularity).
- They have problems of scalability and management.

## Mandatory Access Control

The idea behind **Mandatory Access Control** is to do not let owners assign privileges.
Privileges are set by a security **administrator**, who defines a **classification** of subjects (_clearance_) and objects (_sensitivity_).
The classification is composed of:
- A strictly ordered set of **secrecy levels**.
- A set of **labels**.

An example of secrecy levels used in the US is: _top secret_ > _secret_ > _for official use only (FOUO)_ > _unclassified_.
Example of labels are: _policy_, _energy_, _finance_, _ATOMAL_, _NOFORN_.

The secrecy levels together with the labels form a lattice. Indeed, the classification induces a partial order relationship:
$$
\{ C_1, L_1\} \geq \{ C_2, L_2 \} \ \iff \ C_1 \geq C_2 \text{ and } L_2 \subseteq L_1.
$$

The **Bell-LaPadula Model** (**BLP**) defines two <u>MAC rules</u>:
- **Rule 1**: **no read up** (a.k.a., _simple security property_). A subject $s$ at a given secrecy level **cannot read** an object $o$ at an **higher** secrecy level.
- **Rule 2**: **no write down** (a.k.a., _star property_). A subject $s$ at a given secrecy level **cannot write** an object $o$ at a **lower** secrecy level.

The model also defined one <u>DAC rule</u>:
- **Rule 3** (a.k.a., _Discretionary Security Property_). It states the uses of an access matrix to specify the discretionary access control.

The BLP model enjoys the **tranquillity property**: the secrecy levels of objects cannot change dynamically. As a result there is a monotonic flow of information toward higher secrecy levels. This implies a need of **trusted subjects** who can declassify or sanitize documents.
The limitation of this approach is that it does not address integrity.
