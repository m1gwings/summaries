---
theme: cheatsheet
paginate: true
---
# SWE 2 Cheatsheet (A. Y. 2023/2024)

## Introduction

<div class="multiple-columns with-title">
<div class="column">

**Software engineering** is a field of computer science dealing with software systems: large and complex, built by teams, that exist in many versions, that last many years, and undergo changes.

The **goal** of software engineering is to develop **software products**. They are different from traditional products being intangible (difficult to describe and evaluate), malleable, and human intensive (do not involve any trivial manifacturing process).

According to **ISO/IEC 25010**, the software product qualities are:
- functional suitability (functional completeness, functional correctness, functional appropriateness);
- performance efficiency (time behaviour, resource utilization, capacity);
- compatibility (co-existence, interoperability);
- usability (appropriateness recognizability, learnability, operability, user error protection, user interface aesthetics, accessibility),
- reliability (maturity, availability, fault tolerance, recoverability),
- security (confidentiality, integrity, non-repudation, authenticity, accountability),
- maintainability (modularity, reusability, analysability, modificability, testability),
- portability (adaptability, installability, replaceability).

In order to standardize the way in which we develop software, several **software lifecycles** have been proposed over the years. The traditional one is the **waterfall model** which treats software development as manufacturing.
Due to its lack of flexibility it is not the best choice nowadays, but it is still relevant since it identifies the main phases of the software development process.

</div>
<div class="column">

We distinguish between:
- **high phases**:
    - feasbility study;
    - requirement analysis & specification;
    - design;
- and **low phases**:
    - coding & unit test;
    - integration & system test;
    - deployment;
    - maintenance.

### Feasibility study

In this phase we perform the **cost/benefit** analysis. The objective is to determine whether the project should be started, which are the needed resources, evaluating possible alternatives.

The **outcome** is the **Feasibility Study Document**.

### Requirement analysis and specification

In this phase we analyze the domain in which the application takes place, identify the requirements and derive specifications for the software.

The **outcome** is the **Requirement Analysis and Specification Document (RASD)**.

### Design

During this phase we design the **software architecture** in terms of components, and relations and interactions among them.

The **outcome** is the **Design Document (DD)**.

</div>
<div class="column">

### Coding & unit test

During this phase each module is implemented and tested in isolation.

### Integration & system test

In this phase modules are integrated into (sub)systems which are then tested.

### Maintenance

We distinguish 4 types of maintenance:
- **corrective**: deals with the repair of faults or defects found;
- **adaptive**: consists of adapting software to changes in the environment;
- **prefective**: deals with accomodating to new changed user requirements;
- **preventive**: concerns activities aimed at increasing the system's maintainability.

The latter 3 types are regarded as **evolutionary maintenance**.
The distinction between corrective and evolutionary maintenance can unclear, because specifications are often incomplete and ambiguous.

</div>
</div>

---

## Requirements Engineering (RE)

<div class="multiple-columns">
<div class="column">

Software systems **RE** is the process of **discovering** the **purpose of the software system-to-be**, by identifying stakeholdes and their needs, and documenting these in a form that is amenable to analysis, communication, and subsequent implementation.

We distinguish between:
- **functional** requirements: which describe the **interactions** (independent from implementation) between the **system** and the **environment**;
- **non-functional** requirements: which are constraints on **how functionality must be provided** to the end user;
- **constraints** (or **technical** requirements): which are imposed by the customer or by the environment in which the system operates (e. g. the implementation language must be Java).

Requirements **should**:
- have a **single concern**;
- **not** be **ambiguous**;
- **be varifiable** and **testable**;
- **be achievable** by the sosftware system (that is, the software system can enforce them).

### The World and the Machine

The **World and the Machine** is a **framework** adopted in RE to identify the requirements of the system-to-be.
The two main elements are:
- the **machine**: the portion of the system to be developed (typically, software-to-be + hardware);
- the **world**: the portion of the real-world (environment) affected by the machine.

The **purpose** of the machine is **always in the world**.

</div>
<div class="column">

From this perspective, we can characterize the phenomena of interest for the system-to-be as:
- **world phenomena**: phenomena occurring in the world which the machine **cannot directly observe**;
- **machine phenomena**: phenomena occurring inside the machine (which aren't directly visible in the world);
- **shared phenomena**: phenomena which "_involve_" both the machine and actors in the world; they can be:
    - **machine controlled** (if the machine controls the interaction), or
    - **world controlled** (viceversa).

Then we can express the properties of the system-to-be through predicates regarding these phenomena.

In particular we can state:
- **goals**: which are **prescriptive** assertions formulated in terms of world phenomena (not necessarily shared) and allow us to declare the purpose of the system-to-be;
- **domain assumptions**: which are **descriptive** assertions **assumed to hold** in the world;
- **requirements**: which are **prescriptive** assertions formulated in terms of **shared** phenomena.

Given the set of requirements $R$, goals $G$ and domain assumptions $D$, we say that $R$ is **complete** iff
- $R$ ensures the satisfaction of $G$ in the context of domain assumptions $D$: $R \land D \models G$;
- $G$ captures the stakeholders' needs;
- $D$ represents valid properties/assumptions about the world.

</div>
<div class="column">

### Requirements elicitation

**Requirements elicitation** is the activity which allows to discover the requirements of the system-to-be.

The **first step** in requirements elicitation is to identify **scenarios**: that are a narrative description of what people do and experience as they try to make use of computer systems and applications. They must be **concrete**, **focused**, and **informal**.

#### Heuristics for finding scenarios

Ask yourself:
- Which user groups are supported by the system to perform their work?
- What are the primary tasks that the system needs to perform?
- What data will the actor create, store, change, remove or add in the system?
- What external changes does the system need to know about?
- What changes or events will the actor of the system need to be informed about?

#### Use cases

**After the scenarios** are formulated, we need to generalize them into **use cases**.

A use case is **defined by** specifying:
- a **name** (usually a verb);
- **partecipating actors** (the system is never specified explicitly as an actor);
- the **entry condition**: what is assumed to be true **before** the _flow of events_ (_see below_) has happened;
- the **flow of events**: the sequence of interactions between the actors (and the system) assuming no exceptional behaviors (_see exceptions_);

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

- the **exit condition**: what is assumed to be true **after** the _flow of events_ has happened;
- **exceptions**: the sequence of interactions between the actors (and the system) in case something exceptional happens, they are usually expressed as a list of "if <_something unexpected_> then <_sequence of interactions_>";
- **special requirements**: constraints, non-functional requirements.

Each use case may lead to one or more requirements; in turn, from the requirements, new, more detailed use cases could be derived describing how the requirements are fulfilled.

### Modeling for RE

After having identified the phenomena of interest for the system-to-be, the use cases, and the requirements; we need to produce artifacts that represent them and their interaction: that is we need to build models.

Which **tools** can we use **for modeling**?
- **natural language**: it is simple to use, but has a high level of ambiguity, and it is easy to forget to include relevant information;
- a **formal language**: it allows to use some tool to support analysis and validation and forces the specification of all relevant details, but it requires an expert in the use of the language;
- a **semi-formal language**: that is a language with a precise syntax but with no defined semantics (like UML) which is simpler than a formal language, imposes some kind of structure in the models, but is not amenable for automated analysis and has some level of ambiguity;
- finally we can also adopt a **mixed approach**.

#### UML for RE

As anticipated, we can use **UML** to model many elements of interest in RE.

</div>
<div class="column">

In particular UML allows to carry out:
- **dynamic modeling**: where we model interactions between actors and evolution over time of a system, through:
    - **sequence diagrams**;
    - **collaboration diagrams**;
    - **state machine diagrams**;
    - **activity diagrams**;
- **static modeling**: where we model objects of interest and their relationships, through:
    - **use case diagrams**;
    - **class diagrams**;
    - object diagrams;
    - component diagrams;
    - deployment diagrams.

##### UML Use Case diagram

It allows to represent the set of **all use cases** and, for each one, the **actors involved**; specifying the complete functionality of the system.

- We can represent **use cases** through **ellipses** with inside the use case name:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/use-case-diagrams/use-case.svg" width="150mm" />
</p>

- We can represent **actors** through _stick figures_ with the actor name below:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/use-case-diagrams/actor.svg"
    width="100mm" />
</p>

Once we have drawn all the use cases and actors, we can link them in several ways.

</div>
<div class="column">

The most important **types of associations between use cases** are:
- **include**: a use case uses another use case:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/use-case-diagrams/include.svg"
    width="300mm" />
</p>

- **extend**: a use case extends another use case:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/use-case-diagrams/extend.svg"
    width="300mm" />
</p>

- **generalize**: an abstract use case has several different specializations:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/use-case-diagrams/generalization.svg"
    width="300mm" />
</p>

The **types of associations between an actor and a use case** are:
- **initiate**: the use case is initiated by the actor:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/use-case-diagrams/initiate.svg"
    width="300mm" />
</p>

- **partecipate**: the actor partecipates to the use case:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/use-case-diagrams/partecipate.svg"
    width="300mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

##### Requirements-level class diagrams

These **class diagrams** have a different semantics w.r.t. those used in OO software design models. In particular, in RE we use class diagrams as **conceptual models for the application domain** which may include entities that will not be represented in the software-to-be.

Each **class represents an entity**:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/class-diagrams/entity.svg"
    width="250mm" />
</p>

Usually entities have **no operations** (methods), an **exception** to this rule are **entities** which are **part of the system** or the system itself.

We can **link entities** through:
- **association** (_undirected_ or _directed_): it represents a relationship between the two entities:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/class-diagrams/association.svg"
    width="300mm" />
</p>

- **generalization**: it indicates that one entity is considered to be a specialized form of the other:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/class-diagrams/generalization.svg"
    width="250mm" />
</p>

- **aggregation**: it indicates that one entity "_has_" the other:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/class-diagrams/aggregation.svg"
    width="250mm" />
</p>

</div>
<div class="column">

- **composition**: it is a stronger form of aggregation where the aggregated elements exist only as a part of the aggregate:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/class-diagrams/composition.svg"
    width="250mm" />
</p>

(_It is possible to specify the cardinalities also for aggregation and composition relationships_).

- Sometime we can use _stick figures_ to represent some actors, like users:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/class-diagrams/user.svg"
    width="200mm" />
</p>

How to **derive a class diagram for a domain**? Usually:
- **nouns** represent domain entities (classes), specializations (subclasses), and fields (attributes);
- **verbs** represent operations and relationships between classes.

##### Sequence diagrams

**Sequence diagrams** are graphical description of objects partecipating in a use case or scenario using a DAG notation.

How can we represent the **flow of events of a use case as a sequence diagram**?

- Every event has a **sender** and a **receiver** which are actors of the use case, we can represent them through life lines:

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/swe-2/static/sequence-diagrams/lifeline.svg"
    width="200mm" />
</p>

(_It is common to use stick figures to represent human actors_).

- An event is represented as a **message** from the sender to the receiver; the **occurrence** of the event is represented as a rectangle on the lifelines of both actors involved, a **synchronous message arrow** starts from the occurrence of the event in the lifeline of the sender and reaches the occurrence of the event in the lifeline of the receiver; the converse happens for the **return message arrow**:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/sequence-diagrams/sync-message.svg"
    width="200mm" />
</p>

- Messages can also be asynchronous when the **sender doesn't wait for a response**:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/sequence-diagrams/async-message.svg"
    width="150mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

Furthermore, sequence diagrams provide various constructs to modify the flow of the interactions:

- **alt** allows alternative behaviors based on the value of a condition:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/sequence-diagrams/alt.png"
    width="150mm" />
</p>

- **opt** allows to specify optional interactions which happen only when a condition is satisfied:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/sequence-diagrams/opt.png"
    width="150mm" />
</p>

- **loop** allows to interate a sequence of interactions while a condition is satisfied:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/sequence-diagrams/loop.png"
    width="150mm" />
</p>

- **break** allows to break out of a loop if a condition is satisfied:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/sequence-diagrams/break.png"
    width="100mm" />
</p>

</div>
<div class="column">

##### State machine diagrams

**State machine** diagrams capture the behavior of objects that are instances of a certain class.

The example below showcases part of the syntax, we won't delve deeper:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/state-machine-diagram.png"
    width="300mm" />
</p>

##### Activity diagrams

The examples below showcase part of the syntax, we won't delve deeper:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/activity-diagrams/diagram-1.svg"
    width="150mm" />
</p>

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/swe-2/static/activity-diagrams/diagram-2.svg"
    width="300mm" />
</p>

### RASD

The **Requirements Analysis and Specification Document** (RASD) has several **purposes**:
- it explains both the application domain and the system to be developed;
- it may have contractual value and be legally binding;
- it is the baseline for other activities such as project planning, software V&V, ... .

The **audience** of a RASD are:
- customers and users;
- systems analysts, requirements analysts;
- developers, programmers;
- quality assurance teams;
- project managers.

---

<div class="multiple-columns without-title">
<div class="column">

The **IEEE standard** for RASDs provides a possible structure:

1. **Introuction**

> 1.1 Purpose $\leftarrow$ _**reasons** motivating the existence of the product_
> 1.2 Scope $\leftarrow$ _indentifies the **product** and application **domain**_
> 1.3 Product overview

>> 1.3.1 Product perspective $\leftarrow$ _defines system's relationship to other products; describes **external interfaces**: system, user, hardware, software_
>> 1.3.2 Product functions $\leftarrow$ _summary of **major functions**_
>> 1.3.3 User characteristics $\leftarrow$ _general **characteristics** of the intended **groups of users**, including those that may influence usability (e. g., disabilities, experties))_
>> 1.3.4 Limitations $\leftarrow$ _**anything that will limit the developer's options** (e. g. regulations, reliability, criticality, hardware limitations, interfaces, etc.)_

> 1.4 Definitions

2. **References**

3. **Requirements** $\leftarrow$ _**all the requirements** go here; the standard provides different strategies for the organization_

> 3.1 Functions
> 3.2 Performance requirements
> 3.3 Usability requirements
> 3.4 Interface requriements
> 3.5 Logical database requirements
> 3.6 Design constraints
> 3.7 Software system attirbutes
> 3.8 Supporting information

4. **Verification** $\leftarrow$ _**verification methods** planned to qualify the software_

> (parallel to subsections in Section 3)

5. **Appendices**

> 5.1 Assumptions and dependencies $\leftarrow$ _**factors** not under the control of the software that may affect requirements_
> 5.2 Acronyms and abbreviations

</div>
<div class="column">

Let's analyze some sections more in depth:
- **3.1 Functions**: comprises the functional requirements of the system to be. Functional requirements can be organized by mode, user class, feature, ... . Furthermore, functional requirements can be hierarchically partitioned into sub-requirements.
- **3.2 Performance requirements**, **3.3 Usability requirements**, **...**: comprise all the non-functional requirements we consider high priority for our system, grouped by type.
- **3.6 Design constraints**: comprises contraints on design decisions imposed by domain-specific standards, regulatory documents or other project limitations.
- **3.7 Software system attributes**: includes the required quality attributes of the product: reliability, availability, ... .
- **3.9 Supporting information**: comprises additional supporting information to be considered, as, for example, sample input/output formats, background information that can help the readers, description of the problem(s) to be sovled.

We want a RASD to have the following **target qualities**:
- **completeness** w.r.t. goals (that is $R \land D \models G$ (_see before_)), w.r.t. inputs (that is, the requied behavior is specified for all posible types of inputs), w.r.t. strucutre (that is, the document does not contains To Be Defined (TBD) sections);
- **precision**: requirements should have a level of detail sufficient for software design, developement, and verification of the software release;
- **pertinence**: each requirements or domain assumption is needed for the satisfaction of some goal, each goal is truly neeeded by stakeholders;
- **consistency**: no contradiction in formulation of goals, requirements, and assumptions;
- **unambiguity**: unambiguous vocabulary, assertions, and responsibility;
- **feasibility**: the goals and the requirements must be technicaclly realizable within the assigned budget and schedules;
- **comprehensibility**: must be comprehensible by all in the target audience;
- **good structuring**;
- **modifiability**: must be easy to adapt, extend or contract through local modifications;
- **traceability**: must link requirements and assumptions to underlying foals, facilitates referencing of requirements in future documentation.

</div>
</div>

---

## Alloy

<div class="multiple-columns">
<div class="column">

**Alloy** is a **formal notation** for specifying models of systems and software; it comes with a supporting tool to **simulate** specifications and perform **formal verification** of properties (through _bounded model checking_).

Alloy is used for abstractions and conceptual modeling in a **declarative manner**.

In **RE** Alloy can be used to **formally describe the domain and its properties**, or the **operations** that the machine must provide. In **software design** it allows to formally model **components and their interactions**.


### Language

What follows has been inspired and adapted from `https://alloy.readthedocs.io/en/`.

As we've already seen (_for example when discussing about class diagrams for RE_) in order to model a domain we must define some **entities**, the **relationships among them**, and finally some **properties** (regarding the entities and their relationships) which are assumed to hold.

In Alloy **the type of an entity** is represented by a **signature**. To define a signature we can use the following syntax:
```
sig A { }
```
As anticipated, Alloy is not only a formal language, but also allows, through the supporting tool, to generate instances for the models that we've described. We will deal with the main commands for interacting with the tool later, for now we are going to introduce just the `run` command without delving too much into the syntax: it tells the tool to generate an **instance** for the model _with certain properties_.

</div>
<div class="column">

**Providing an instance for a model** requires to assign to every signature (which represents a set of entities of the same "_type_") a set of _so-called_ **atoms** (the individual entities of the type specified by the signature).

In particular, by executing:
```
run { } for exactly 3 A
```
for the simple model defined before, the tool provides the following instance:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/alloy/single-signature.png"
    width="150mm" />
</p>

Indeed we asked for an instance with exactly three atoms for the signature `A`, then the tool assigned to it the set `A = { A0, A1, A2 }`.

Now that we know how to define entities, we want a way to link them; that is, we want to define relationships between entites. For a given instance of an Alloy model, the relationships between its atoms are represented by **mathematical relations**, which are also sets. As it will be even more clear later, instances of Alloy models are just "_a bunch of sets_": some represent the set of atoms for a signature, others are relations between these atoms. For this reason it makes sense to list (_some of_) the **operations on sets** supported by the language before anything else.

#### Operations on sets

**When writing Alloy expressions, signatures are treated as sets**, indeed, as we've discussed before, for a given instance of a model, a set is assigned to each signature, and so we can easily evaluate expressions of this type.

Consider the model:

</div>
<div class="column">

```
sig A { }
sig B { }
```

In the following we will treat `A` and `B` as finite sets: `A = { A1, ..., AN }`, `B = { B1, ..., BM }`.

Then we can perform the following operations:
- **union**: `A + B`;
- **difference**: `A - B`;
- **intersection**: `A & B`;
- **cartesian product**: `A -> B`.

Finally:
- **`#A`** returns `N`, that is, the **number of elements in `A`**;
- **`none`** is the **empty set**.

#### Signatures

Now that we know how to perform basic manipulations on sets, we can deal with the general syntax for the definition of a **signature** (_filling the curly braces_):
```
sig A {
    field1: Set1,
    ...,
    fieldN: SetN
}
```
where `SetI` is either a signature or an expression that, for a given instance, evaluates to a set; that is, we can combine signatures through all the operators of the previous paragraph except for `#` (since it doesn't evaluate to a set).
**An instance for the model above requires** not only to assign a set of atoms to the signature `A`, but **also a relation** (in the mathematical sense) **for every `fieldI`**.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

**These relations are those which allow to express relationships between entities**.
In particular the relation assigned to `fieldI` will be a subset of the cartesian product between the set assigned to `A` and the set to which `SetI` evaluates (remember that in general `SetI` is an expression). But that's not all: in Alloy every relation has a **multiplicity** which implicitly is assumed to be `one`, that is, in `fieldI`, to every element of `A` corresponds exactly one element of `SetI` (_clearly different elements of `A` could be in relation with the same element of `SetI`_).

In order to specify **different multiplicities** we can use the following syntax:

- `fieldI: lone SetI`: to one element of `A` correspond 0 or 1 elements of `SetI`;
- `fieldI: set SetI`: there is no restriction on the number of elements of `SetI` which correspond to an element of `A`, that is, it is a standard mathematical relation;
- `fieldI: some SetI`: to one element of `A` correspond 1 or more elements of `SetI`;
- `fieldI: one SetI`: it is the default case described before.

##### Multirelations

Signatures **can have multirelations** as fields, for example:
```
sig Door { }
sig Card { }

sig Person {
    access: Card -> Door
}
```
For a given instance of this model, `access` is a ternary relation subset of the cartesian product between (_the sets assigned to_) `Person`, `Card` and `Door`.

</div>
<div class="column">

**Multirelations have a special kind of multiplicity**: `r: Set1I m -> n Set2I`.
This says that (_fixed an element of the signature in which the field `r` is defined_) each member of `Set1I` is mapped to `n` elements of `Set2I`, and `m` elements of `Set1I` map to each element of `Set2I`. **If not specified, the multiplicites are assubed to be `set`**.

##### Signature multiplicity

In addition to having multiplicity in relations, we can put multiplicities on the signatures themselves:
```
one sig Foo { }
some sig Bar { }
```

By default signatures have multiplicity `set`, that is, for a given instance of the model, the set associated to the signature has no restrictions. By making the signature `one`, in every instance such set will contain exactly one atom. We get analogous behavior with `some` and `lone`.

##### Subtypes

- **`extends`**

Writing `sig Child extends Parent { ... }` creates a **subtype**, that is, for a given instance, **the set assigned to `Child` is a subset of the set assigned to `Parent`** (so every atom of `Child` is an atom of `Parent`), furthermore, if more extensions are defied as in:
```
sig Parent { }
sig Child1 extends Parent
sig Child2 extends Parent
```
then, for a given instance, any atom of parent can only match **up to one** extension, that is, **the intersection between the set assigned to `Child1` and the one assigned to `Child2` is empty**. **If we don't want this constraint, we can use `in` instead of `extends`**.

</div>
<div class="column">

- **`abstract`**

If you make a signature `abstract`, then all atoms of the signature will belong to extensions: there will be no atoms that are just the supertype and not any of the subtypes. That is, for a given instance, **the union of the sets assigned to the children is equal to the set assigned to the parent** (the sets assigned to the children form a partition of the set assigned to the parent).

**Remark**: we can add fields to subtypes:
```
sig Child extends Parent { field: Set }
```
The semantics is straightforward: the relation assigned to `field` will associate atoms of `Child` to elements of `Set`; the atoms of `Parent` which aren't atoms of `Child` won't appear in (_the relation asssigned to_) `field`.

##### Enums

Enums are special signatures which are assigned the same set in every instance. 
We can define enums with the following syntax:
```
enum A { Elem1, Elem2, Elem3 }
```
In this case `A` will have 3 atoms in every instance. When we use them in expressions, we can interpret `Elem1`, `Elem2`, and `Elem3` as **singletons** containing only the corresponding atom; in this way we can apply all the usual operators which are defined for sets.
We can also define enums without the special syntax above through:
```
abstract sig A { }
one sig Elem1, Elem2, Elem3 extends A
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### Operations on relations

In this paragraph we will introduce some operators that are useful if we want to manipulate relations.

##### The `.` operator

Let `rel1 = A1 -> A2 -> ... -> A(N-1) -> C` and `rel2 = C -> B2 -> ... -> BM` then `rel1.rel2` is the set of all tuples `(a_1, ..., a_(n-1), b_2, ..., b_m)` such that, for some `c` in `C`, `(a_1, ..., a_(n-1), c)` belongs to `rel1` and `(c, b_2, ..., b_m)` belongs to `rel2`.

**Remark**: the behavior of the operator can be naturally extended to tha case in which either `rel1` or `rel2` is a "_simple_" set, that is, a relation of arity 1.

##### `iden`

`iden` is the relation which maps every atom in an instance of a model to itself.

##### Operations on binary relations

The following operators are defined only for binary relations:
- `~rel` returns the **converse** of `rel`;
- `^rel` returns the **transitive closure** of `rel`;
- `*rel` returns `^rel + iden`;

##### Advanced operations

- `<:` is **domain restriction**: `Set <: rel` is all of the elements in `rel` that **start** with an element in `Set`;
- `:>` is **range restriction**: `rel :> Set` is all the elements of `rel` that **end** with an element in `Set`;
- `rel1 ++ rel2` is the **union of the two relations**, with **one exception**: if there is an element `(k, a_1, ..., a_(n-1))` in `rel1` and an element `(k, b_1, ..., b_(m-1))` in `rel2` for some `k`, then `(k, a_1, ..., a_(n-1))` won't be added to `rel1 ++ rel2`.

</div>
<div class="column">

#### Constraints

Now that we know how to define entities and their relationships it's time to state some properties for our model that constrain the possible instances.
We can do so through operators that are applied to sets and return boolean values:
- `A = B` has the usual semantics;
- `A in B` is true iff `A` is a **subset** of `B`;
- `no A` is true iff `A` is **empty**;
- `some A` is true iff `A` has **at least one element**;
- `one A` is true iff `A` has **exactly one element**;
- `lone A` is true iff `A` is **either empty or has exactly one element**;
- `disj[A, B]` is true iff `A` and `B` are **disjoint**.

Furthermore (_as anticipated_), Alloy supports **first order logic quantifiers**:
- `some x: A | expr` is true iff `expr` is true for **at least one element** of `A`;
- `all x: A | expr` is true iff `expr` is true for **every element** of `A`;
- `no x: A | expr` is true iff `expr` is false for **every element** of `A`;
- `one x: A | expr` is true iff `expr` is true for **exactly one element** of `A`;
- `lone x: A | expr` is true iff `expr` is true for **zero or one elements** of `A`.

It is also possible to quantify over multiple elements, for example with: `some x, y, ...: A | expr` or `some x: A, y: B, ... | expr`.


#### Boolean expressions

Once we have expressions which evaluate to boolean values, we can combine them to build complex constraints through the following operators:
- `expr1 and expr2` (_or equivalently `expr1 && expr2`_) is true iff both `expr1` and `expr2` are true;

</div>
<div class="column">

- `expr1 or expr2` (_or equivalently `expr1 || expr2`_) is true iff at least one between `expr1` and `expr2` is true;
- `not expr1` (_or equivalently `!expr1`_) is true iff `expr1` is false;
- `expr1 implies expr2` (_or equivalently `expr1 => expr2`_) is true iff `expr1` is false or both `expr1` and `expr2` are true;
- `expr1 iff expr2` (_or equivalently `expr1 <==> expr2`_) is true iff `expr1` and `expr2` are both false or `expr1` and `expr2` are both true.

Furthermore Alloy provides some **syntactic sugar** like:
- **`let`**: `let` defines a local value for the purposes of the subexpression. For example:
```
let x = A + B, y = C + D | x + y
```
> `let` is mostly used to simplify complex expressions and give meaningful names to intermediate computations. **If writing a boolean expression, you may use `{ ... }` instead of `|`**.

- **`implies`-`else`**: when used in conjuction with `else`, `implies` acts as a conditional. `p implies A else B` returns `A` if `p` is `true` and `B` if `p` is `false`. `p` must be a boolean expression. (**`A` and `B` can also be non-boolean expressions**).

- **paragraph expressions**: if multiple constraints are surrounded with braces, they are all `and`-ed together. The following two are equivalent:
```
expr1 or {
    expr2
    expr3
    ...
}

expr1 or (expr2 and expr3 and ...)
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### Predicates and functions

**Predicates** and **functions** allow to reuse (_usually complex_) expressions in several parts of the model. In particular **predicates** return **boolean values**, while **functions** return **sets**.

##### Predicates

Predicates take the form:
```
pred name {
    constraint
}
```
where constraint is built through the operators discussed before.
Once defined, predicates can be used as part of boolean expressions, The following is a valid spec:
```
sig A {}

pread at_least_one_a {
    some A
}

pred more_than_one_a {
    at_least_one_a and not one A
}
```
Predicates can also take arguments:
```
pred foo[a: Set1, b: Set2, ...] {
    expr
}
```
The predicate **is called with `foo[x, y]`, using brackets, not parens**. In the body of the predicate, `a` and `b` would have the corresponding values. `a` must be an atom of `Set1`, while `b` must be an atom of `Set2`, or, more precisely,

</div>
<div class="column">

singleton sets containing that atom (_as we remarked before, in Alloy, the operators are defined only for sets_).

##### Functions

Alloy functions have the same structure as predicates but also return a value:
```
fun name[a: Set1, b: Set2]: output_type {
    expression
}
```

**Important remark**: as usual we can specify **multiplicities** also for **predicates and functions** arguments, as in:
```
fun name[a: some Set1, b: some Set2]:
    some output_type { expression
}
```
The **default** is **`one`** (_that's why we said before that the arguments of a predicate must be atoms of the corresponding set specified in the definition_).

When defining functions that return sets, it may be useful the **set comprehension** syntax: `{x: Set1, y: Set2, ... | expr}`.

#### Facts

Now that we know how to write complex constraint it's time to understand how to enforce them: we can use **facts**.
The syntax is the following:
```
fact name { constraint }
```
When facts are added to a model, in order to provide a **valid** instance, we not only need to assign a set to every signature and a relation to every field;

</div>
<div class="column">

these sets and relations must also satisfy all the constraints imposed by the facts.

##### Implicit facts

You can write a fact as part of a signature. The implicit fact goes after the signature definition and relations. Inside of an implicit fact, you can get the current atom with `this`. **Fields are automatically expanded in the implicit fact to `this.field`**. For example:
```
sig Node { edge: set Node } {
    this not in edge
}
```
(_The syntax `this not in edge` is a syntactic sugar for `not (this in edge)`_).

#### Commands

A **command** is what actually runs the analyzer. It can either find instances for the model that you have specified, or counterexamples to given properties.

##### `run`

- **`run`** tells the analyzer to find an instance for the model;
- **`run pred`** tells the analyzer to find an instance for the model where `pred` is `true`;
- **`run { constraint }`** tells the analyzer to find an instance for the model which satisfies `constraint`.

##### `check`

**`check`** tells the Analyzer to find a _counterexample_ to a given constraint.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

**Unlike with `run` command, `check` uses assertions**:
```
assert no_self_loops {
    no n: Node | self_loop[n] }
check no_self_loops
```

**Assertions may be used in `check` commands but not `run` commands. Assertions may not be called by other predicates or assertions**.

You can call `check` also with an ad-hoc constraint:
```
check { constraint }
```

##### Scopes

**All alloy models are bounded: they must have a maximum possible size**. If not specified, the analyzer will assume that there may be up to three of each top-level signature and any number of relations. This is called the **scope**, and can be changed for each command.

Given the following model:
```
sig A { }
sig B { }
```
we can write the following scopes:
- `run {} for 5`: the analyzer will look for models with up to five instances of each `A` and `B`;
- `run {} for 5 but 2 A`: the analyzer will look for models with up to two instances of `A`;
- `run {} for 5 but exactly 2 A`: the analyzer will only look for models with _exactly two_ `A`, the exact scope _may_ be higher than the general scope;
- `run {} for 5 but 2 A, 3 B`: places scopes on `A` and `B`.

(_The last command can be written as `run {} for 2 A, 3 B`_).

</div>
<div class="column">

#### Time

Alloy 6 added **temporal operators** to Alloy, making it easier to model dynamic systems.

Now **signatures** or **fields** can be declared **mutable**.

This is done through the `var` keyword:
```
sig A { }
var sig B { }
sig C {
    var field: lone B
}
```

This forces us to redefine **what an instance for a model is**:
- every instance has a certain number of **steps** which we can interpret as discrete time instants;
- **for every step**, we need to assign **a set to every signature** and a **relation to every field** accordingly (that is, for a given step, the relation must be a subset of the cartesian product of the sets assigned to the corresponding signatures **in that step**);
- **if signatures and fields are defined as usual**, then these sets and relations will stay the same in every step (and so we can adopt the usual interpretation);
- **otherwise if we use the `var` keyword as shown before**, these sets and relations could change at every step.

Clearly we need some operators to specify how the sets and relations can mutate from a step to the next.

**Important remark**: when dealing with mutable signatures and fields, **the evaluation of an expression happens for a given step which by default is the first one** (_of course we can have different values if we evaluate the same expression at different steps_).
**In particular, if we don't use temporal operators, all predicates and facts only hold for the _initial_ step**.

</div>
<div class="column">

From now on assume that we're evaluating the expressions at the generic step `s`; we will see in a moment that, through some operators, `s` won't always be the _initial_ step. Furthermore, for a predicate `P`, we will use `P(s)` to highlight that `P` is evaluated at step `s` and `s+1` for the step that follows `s`; **this is not valid syntax**.

Alloy operators include both _future_ and _past_ operators. Let `P` be a predicate, the **future operators** are:
- **`always`**: `always P` is equivalent to `P(s) and P(s + 1) and ...` (_it is true if `P` is always true from `s` onwards_);
- **`eventually`**: `eventually P` is equivalent to `P(s) or P(s + 1) or ...` (_it is true if `P` is currently true or will be true for some step_);
- **`after`**: `after P` is equivalent to `P(s + 1)`;
- **`;`**: `P ; Q` is a **shortand for `P and after Q`**;
- **`releases`**: `Q releases P` is `true` iff `P` is `true` until `Q` is `true`, then `P` _may_ become `false`;
- **`until`**: `P until Q` is equivalent to `(Q releases P) and eventually Q`.

##### The ' operator

The **`'`** operator is the correct syntax for what we have written as `P(s + 1)`; **it not only works with predicates, but also with expressions of any kind**. in general `expr'` is simply **the value of `expr` in the next step**.

For every future operator there is an **equivalent past operator**: `historically` is equivalent to `always`; `once` is equivalent to `eventually` (_the predicate after `once` doesn't need to have been true exactly once, but at least once_); `before` is equivalent ot `after`; `triggered` is equivalent to `releases`; `since` is equivalent to `until`.

**We can set the scope also for the steps of an instance**: the number of steps is specified as `for m..n steps`, where `m` is the minimum number of steps and `n` is the maximum. Writing `for n steps` is equivalent to `for 1..n steps`. If no steps count is given, the number defaults to 10.

</div>
</div>

---

## Software Architecture

<div class="multiple-columns">
<div class="column">

The **Software Architecture** (SA) of a system is the **set of structures** needed to reason about the system. These structures comprise **software elements**, the **relations among them**, and **properties** of both.
In particular the **set of structures relevant to software** are:
- **component-and-connector** structures;
- **module** structures;
- **allocation** structures.

### Component-and-connector structures

**Component-and-connector** structures describe how the system is structured as a **set of elements** that have **runtime behavior** (**components**) and **interactions** (**connectors**).

Component-and-connector structures allow us to answer questions such as:
- What are the major executing components and how do they interact at runtime?
- What are the major shared data stores?
- Which parts of the system are replicated?
- How does data progress through the system?
- Which parts of the system can run in parallel?
- How does the system's structure evolve during execution?

Furthermore, they allow us to study runtime properties such as availability and performance.

#### Representing component-and-connector structures in UML

We can represent a **simple component** as follows:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/component-and-connector-diagrams/component.svg"
    width="150mm" />
</p>

</div>
<div class="column">

Each component can **provide and require interfaces**:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/component-and-connector-diagrams/interfaces.svg"
    width="250mm" />
</p>

(_We can also write the name of the provided interface next to the ball_).

We can build **connectors** by "_matching_" a provided interface with a required interface:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/component-and-connector-diagrams/connector.svg"
    width="150mm" />
</p>

We can **connect several components** into a **subsystem**:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/component-and-connector-diagrams/subsystem.svg"
    width="250mm" />
</p>

</div>
<div class="column">

Finally, we can **connet subsystems' interfaces** through **dependency arrows**:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/component-and-connector-diagrams/connecting-subsystems.svg"
    width="250mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

We can represent the **interaction between components and other components** or **human actors and components** through sequence diagrams, using the following representation:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/component-and-connector-diagrams/sequence-diagram.svg"
    width="190mm" />
</p>

### Module structures

**Module structures** show how a system is structured as **a set of code or data units** that have to be procured or constructed, **together with their relations**.
Examples of modules are: packages, classes, functions, libraries, layers, database tables.

Modules **consitute implementation units** that can be used as the basis for work splitting. Typical **relationships among modules are**: uses, is-a (generalization), is-part-of.

An example of modular structure is the **layered architecture** where:
- layers are organized according to use relationships;
- a layer can use the layer below and can be used by the layer above.

A layered architecture has been used for example in the "Reference IoT Layered architecture" (RILA).

<p align="center">
    <img src="http://localhost:8080/swe-2/static/module-structures-diagrams/RILA.webp"
    width="230mm" />
</p>

</div>
<div class="column">

#### Representing modular structures in UML

We can use:
- **composite structure diagrams**

<p align="center">
    <img src="http://localhost:8080/swe-2/static/composite-structure-diagram.png"
    width="500mm" />
</p>

- **class diagrams**

<p align="center">
    <img src="http://localhost:8080/swe-2/static/class-diagrams/modular-structures.png"
    width="270mm" />
</p>

</div>

---

<div class="multiple-columns without-title">
<div class="column">

- **package diagrams**


<p align="center">
    <img src="http://localhost:8080/swe-2/static/package-diagram.png"
    width="500mm" />
</p>

Module structures allow us to answer questions such as:
- What is the primary functional responsibility assigned to each module?
- What other software elements is a module allowed to use?
- What other software does it actually use and depend on?
- What modules are related to other modules by generalization or specialization (that is, inheritance) relationships?

### Allocation structures

**Allocation structures define how the elements** from component-and-connector or module structures **map onto things that are not software**.
Examples of such things are:
- hardware (possibly virtualized);
- file systems;
- teams.

Typical allocation structures are:
- **deployment structures**;

</div>
<div class="column">

- implementation structures;
- work assignment structures.

#### Representing deployment structures in UML

- An example can be:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/deployment-diagrams/diagram-1.png"
    width="500mm" />
</p>

- or:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/deployment-diagrams/diagram-2.png"
    width="500mm" />
</p>

**Deployment structures** captures the topology of a system's hardware. It is built as part of architectural specification. The purpose is: specify the distribution of components, and identify performance bottlenecks.
Deployment structures are developed by architects, networking engineers, and system engineers.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Software Design Description (SDD)

A **software design description** specifies the manner in which architectural descriptions of systems are organized and expressed.

The required contents of an SDD according to the IEEE standard are:
- identification of the SDD (date, authors, organization);
- description of design stakeholders;
- selected design viewpoints;
- design views;
- design overlays;
- design rationale.

### Design principles

The main design principles for software architectures are:
- **divide and conquer**;

- **keep the level of abstraction as high as possible**: abstractions allow you to understand the essence of a subsystem without having to know unnecessary details;

- **increase cohesion where possible**;

- **reduce coupling where possible**;

- **design for reusability**: design the various aspects of your system so that they can be used again in other contexts (generalize your design as much as possible, simplify your design as much as possible, follow the preceding all other design principles, design your system to be extensible);

- **reuse existing designs and code**: design with reuse is complementary to design for reusability (take advantage of the investment you or others have made in reusable components);

</div>
<div class="column">

- **design for flexibility**: actively anticipate changes that a design may have to undergo in the future, and prepare for them (reduce coupling and increase cohesion, create abstractions, use reusable code and make code reusable, do not hard-code anything);

- **anticipate obsolescence**: plan for changes in the technology or environment so the software will continue to run or can be easily changed;

- **design for portability**: have the software run on as many platforms as possible;

- **design for testability**: take steps to make testing easier, for example design a program to automatically test the software, ensure that all the functionalities of the code can be driven by an external program, bypassing a graphical user interface;

- **design defensively**: be careful when you trust how others will try to use a component you are designing (handle all cases where other code might attempt to use your component inappropriately, check that all of the inputs to your component are valid, that is, satisfy the preconditions).

### Interface design

An **interface** is a **boundary** across which components interact. The **proper definition** of interfaces is an acrchitectural concern: it impacts maintainability, usability, testability, performance, and integrability. There are two important **guiding principles** to apply when defining interfaces: **information hiding** and **low coupling**.

The following aspect have to be considered during interface design:
- **contract principle**: any resource added to an interface implies a commitment to maintaining it;

</div>
<div class="column">

- **least surprise principle**: interfaces should behave consistently with expectations;
- **small interfaces principle**: interfaces should limit the exposed resources to the minimum.

Important **elements to be defined** are:
- the **interaction style** (for example: sockets, RPC, REST (_see later_));
- the **representation and structure** of exchanged data;
- **error handling**.

#### Interaction style

- **Sockets**: after connection establishment, communication is bidirectional. Both parties must agree on the same protocol;

- **RPC/RMI**: resembles procedure/method call in a centralized setting; stubs and skeletons are needed to transform procedure/method calls in messages and vice versa;

- **REpresentational State Transfer** (**REST**): it is a specific standardized architectual style for Application Programming Interfaces (APIs), it realizes clear separation between distributed, heterogeneous systems/components.

##### REST APIs

REST APIs are simple and **standardized**, developers do not have to worry about:
- the **communication protocol** (which is **HTTP**);
- how to **format the data** (in **JSON**);

Furthermore, they are **stateless**: they do not keep track of states across server and all clients; this approach is **scalable** and supports **caching**.

REST APIs are employed when we have to manage a set of resources (of whatever nature).

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

Indeed, the set of supported operations is abbreviated with **CRUD**, which stands for:
- **Create**: creation of a new resource through **POST** HTTP method;
- **Read**: retrieval of an existing resource through **GET** HTTP method;
- **Update**: update of an existing resource thorugh **PUT** HTTP method;
- **Delete**: deletion of an existing resource through **DELETE** HTTP method.

**REST APIs requests** are standard HTTP requests, made of 4 fields:
- an **header**;
- a **method** (among the ones that we've just discussed);
- an **endpoint**;
- **parameters/body**.

The same is true for **REST APIs responses** which are standard HTTP responses, made of 2 fields:
- a **status code**, that can be:
    - **2xx** for successful operations (for example 200 = Ok);
    - **4xx** for client errors (for example 400 = Bad request);
    - **5xx** for server errors (for example 500 = Internal server error, 503 = Service unabailable);
- **serialized data** which constitutes the body of the response and is usually in **JSON**.

One **utility** which allows to perform REST APIs request is **curl**, for example:
```
curl -X "GET" \
"https://petstore.swagger.io/v2
/pet/findByStatus?status='available'"
-H "accept:application/json"
```

</div>
<div class="column">

or
```
curl -X "POST"
"https://petstore.swagger.io/v2/pet" \
-H "accept:application/json" \
-H "Content-Type: application/json" \
-d "{ "id": 12300, ... }"
```

#### Representation and structure of exchange data

The **most used serialization formats** for interfaces are:
- **JSON**
```
{
    "guests": [
        { "firstName": "John", ... },
        ...
    ]
}
```
- **XML**
```
<guests>
    <guest>
        <firstName>John</firstName>
        <lastName>Doe</lastName>
    </guest>
    ...
</guests>
```
- and **Protobuffer**
```
message Guest {
    string firstName = 1;
    string lastName = 2;
}
message Guests {repeated Guest guests = 3;}
```

</div>
<div class="column">

#### Error handling

**Example of issues** that could arise when using an interface are:
- an operation is called with invalid parameters;
- the call does not return anything (for example because the component cannot handle the request in the current state; hardware/software errors prevent successful execution; misconfiguration issues).

**Possible reactions** are:
- raising an exception;
- returning an error code;
- log the problem.

#### Multiple interfaces and separation of concerns

A server can offer multiple interfaces at the same time. This enables: separation of concers; different levels of access rights; support to **interface evolution** (_see next_).

#### Interface evolution

Interfaces constitute the contract between servers and clients. Sometimes interfaces need to evolve (e. g., to support new requirements). The **strategies** to support continuity are: **deprecation** (declare well in advance that an interface version will be eliminated by a certain data); **versioning** (maintain multiple active versions of the interface); **extension** (a new version extends the previous one).

#### Documenting interfaces

Interface **documentation** explains how to use the interface, but should not include information about the internals of the component which provides such interface.
The **audience of an interface documentation** are: **developers offering the interface**, **developers using the interface**, **QA teams**,

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

and **software architects**.

##### OpenAPI specification

**OpenAPI specification defines** how to describe a REST API interface through an **OpenAPI definition**.
An **OpenAPI definition** is a (JSON or YAML) file which describes what a service offers through its interface.
Using OpenAPI specification has several benefits: it is a format standardized, public, and well-known; it is readable by humans (to understand and use the REST API), and machins (to automate tasks like testing or code generation).
**OpenAPI definition describes**: endpoints, resources, operations, parameters (including data types), authentication/authorization mechanism.
Furthermore it offers some **supporting tool** like: an **API validator** which checks the conformance to the standard; a **documentation** generator which produces clear and human readable description; a **SDK** generation which creates automatically client libraries in a programming language of choice.

### Architectural style

An **architectural style** determines the **vocabulary** of **components** and **connectors** that can be used in instances of that style, together with a set of **constraints** on how they can be combined. These can include topological constraints on architectural descriptions (for example, no cycles). Other constraints (for example having to do with execution semantics) might also be part of the style definition.

#### Client-server

In a **client-server** architectural style there are two **component roles**: a **client that issues requests**, and a **server that provides responses**.
It is common to use it when: **multiple users** need to access a single **resource**, there is a preexisting software we must **access remotely**,

</div>
<div class="column">

it is convenient to organize the system around a **shared piece of functionality** used by multiple components.

We can distribute parts of the software system (**GUI**, **application**, and **data**) onto a client-server architecture in different ways:
- **thin client**:
    - **distributed presentation**: the client handles part of the GUI, the server handles the other part of the GUI, the application, and the data;
    - **remote presentation**: the client handles the GUI, the server handles the application and the data;
- **fat client**:
    - **distributed logic**: the client handles the GUI and part of the application, the server handles the other part of the application and the data;
    - **remote data access**: the client handles the GUI and the application, the server handles the data;
    - **distributed storage**: the client handles the GUI, the application and part of the data, the server handles the other part of the data.

The main technical issues of the client-server architectural style are:
- **design** and **document** proper interfaces for our server;
- ensure the server is able to **handle multiple simultaneous requests**: the alternatives are forking vs thread pooling.

##### Forking

**Forking** is the simple approach used by **Apache Web Server** for **handling multiple simultaneous requests**: **one process** was created **per request** or **per client**.

It is a simple architecture which is also simple to program and gurantess isolation and protection given by the "one-connection-per-process" model, but has **scalability issues**.

</div>
<div class="column">

##### Thread pooling

Worker (or thread) pooling is an alternative approach adopted by **NGINX Web Server** designed for high concurrency which deals with the scalability issues.
NGINX dealt with these issues by introducing a new **architectural tactic**, that is, **a design decision that influences the control of one or more quality attributes**. It works as follows:
- the number of workers is fixed (so that we can't saturate the available resources);
- each worker has a queue;
- when queues are full the dispatcher drops the incoming requests to keep high performance;
- dispatcher balances the workload among available workers according to specific policies.

**Remark** architectural tactics introduce **quality attribute trade-offs**, in this case NGINX decided to **optimize scalability** and **performance** by **sacrificing availability (in some cases)**.

#### N-tiers architectures

In a **3-tiers architecture** we distribute the logical layers which constitute the software system (usually GUI, application, and data) over **3 physical tiers**.
**The most straightfoward way is to map each layer with a tier**.

This architecture can be generalized in the so-called **N-tiers** where the number of physical tiers isn't 3 anymore, but N in general.

#### Event-driven architecture

In an **event-driven** architecture, components can **register to**/**send events**. Events are **sent to all registered components**. There is **no explicit naming of target components**.
This architecture is often called **publish-subscribe** where **publish** refers to event generation, while **subscribe** refers to the declaration of interest.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

This approach is **very common in modern development practices**, it makes the **addition/deletion of components easy** (publishers/subscribers are decoupled), but it has **potential scalability problems** (the event dispatcher may become the bottleneck), and there is **no guaranteed ordering of events**.

Messages/events are **asynchronous**, the computation is **reactive**, the **destination** of messages is **determined by receiver**, not by the sender. Furthermore, event-driven architecturs make communication flexible: they allow one-to-many, many-to-one, and many-to-many forms of communication.

Relevant technologies to build event-driven architectures are: **Apache Kafka** and **RabbitMQ**.

##### Apache Kafka

**Kafka** is a **framework for the event-driven paradigm**: it includes primitives to create **event producers** and **consumers** and a runtime infrastructure to handle **event transfer** from producers to consumers, it **stores events durably and reliably**, and it allows consumers to **process events as they occur or retrospectively**.

There are 4 components' roles in Kafka's architecture: **producers**, **consumers**, **brokers**, and **ZooKeeper**.
Each **broekr handles** a set of **topics** and **topic partitions** which include sets of messages on the topic. Partitions are independent from each other and can be **replicated** on multiple brokers for fault tolerance. There is **one leading broker per partition**. The other brokers containing the same partition are **followers**. **Producers** know the available leading brokers and send messages to them. Messages in the same topic are organized in **batches** at the producers' side and sent to the broker when the batch size overcomes a certain threshold. Consumers adopt a **pull approach**. They receive in a single batch all messages belonging to a certain partition starting from a specified **offset**.

</div>
<div class="column">

Messages remain available at the brokers' side for a specified period and can be **read multiple times** in this perios. The leader keeps track of the **in-synch followers**. **ZooKeeper** is used to oversee the correct operation of the cluster. ALl brokers send heartbeat to ZooKeeper. ZooKeeper will replaace a failing broker by electing a new leader for all the partitions the failing broker was leading. It may also start/restart brokers.

**Message delivery** works as follows:
- the **producer** sends the message that it wants to publish to the corresponding leading broker;
- the **leading broker** commits messages by storing them in the corresponding partition, then it adds the message to **followers replicas** if available;
- finally the **leading broker** sends back a response to the **producer**, acknowledging that the message has been committed.

In case of failure the producer may not get the response. In this case the producer has to resend the message, kafka brokers can identify and eliminate duplicates.

An analogous failure can happen when performing synchronization with replicas: after sending the new message, the leading broker does not receive any acknowledging response from the follower. We can adopt:
- **exactly-once semantics** (the message will be commited exactly once on the replica): it is possible but has a long waiting time;
- **at-least-once semantics** (the message will be committed at least once on the replica): can be chosen by disabling duplicates' management on replicas;
- **at-most-once** (the message will be committed at most once on the replica): can be achieved simply by making the leading broker not to wait for a response from the follower (that is, by publishing the message asynchronously).

</div>
<div class="column">

When retrieving messages, each **consumer** can rely on a **persistent log** to keep track of the **offset** so that it is not lost in case of failure.
Even in this case, we can have:
- **at-lest-once semantics**: if the consumer fails after having elabolerated messages and before storing the new offset in the log, the same messages will be retreived again;
- **at-most-once semantics**: it is achieved by storing the new offset before the elaboration;
- **exactly-once semantics**: it can be achieved through transactional management.

**Kafka architectural tactics** are **scalability** (through multiple partitions and multiple brokers) and **fault tolerance** (through persistent storage, replication, and cluster management).

#### Microservices

The **microservice architectural style** is an approach to developing a single application as a suite of **small services**, each running in its own process and communicating with **lightweight mechanisms**, often an HTTP resrouce API.
When adopting a microservice architectural style, (preexisting) monolithic systems are decomposed into small specialized services and deal with a single **bounded context** in the target domain.

Microservices have **several advantages**:
- they enable **fine-grained scaling** strategies (in monolithic systems, selective replication is not possible, the entire system must be replicated as a whole, microservices enable flexible deployment and selective replication);
- they **reduce** the scale of **localized issues**, **improving resilience** (a single microservice can fail without making the whole system fail);

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

- they allow **better reuse** and **composability** (the functionality offered by a microservice can be used and reused in multiple contexts);
- they **reduce teams synchronization overhead** (each team has its own code artifact instead of having multiple teams working on the same);
- they allow organizations to have **small development teams** with well-defined areas of responsibility;
- the **technical implementation of each service is irrelevant** because the applications always communicate through **technology-neutral protocols** (like REST APIs);
- finally, **smaller codebases** are easier to debug, and cheaper to maintain.

##### Anatomy of a microservice

A **microservice is composed of 3 main elements**:
- the interface (usually a **REST API**): which exposes core operations of the service;
- the **application (or business) logic**: which implements the core operations executed upon requests;
- the **data storage**: each microservice typically has its own local data.

##### Routing patterns

When dealing with microservices, the **execution environment** has shared and not pre-allocated resources. It follows that the physical location of running services is potentially unkwnown: services need to be discovered.
**Service discovery** must be: **highly available** (we want to avoid single point of failure, this is usually achieved through replication), **load balanced** (service invocations are spread across all the service instances), **resilient** (if service discovery becomes temporarily unavailable, applications should still function and locate the services), **fault-tolerant** (it should monitor the health status of services and take action without human intervention).

</div>
<div class="column">

**Service discovery architecture** works as follows:
- when a service instance comes online, it **registers** its location (IP/port) to one discovery service instance. Instances of the same service are registered under the same service ID;
- a service location can be **looked up** by a logical name from the discovery nodes;
- service discovery nodes **share information** (location/health) among each other (propagation can use static lists, or P2P "gossip" protocols);
- service instances send periodic **heartbeat** to service discovery. If an instance dies, the discovery layer removes its location.

Finally, when a microservice client needs to locate another service:
- it **checks its local cache** for the location of service instances;
- it **sends direct requests** to service instances (clients decide how to spread requests to instances);
- the cached data is **periodically refreshed** by contacting the discovery engine (client cache is eventually consistent).

##### Resiliency patterns

Resiliency patterns answer the question "How do I make sure when there is a **problem** with a service, clients can avoid it before **recovery**?".
Service discovery provides some degree of resilience in the simple case in which a service instance dies (no heartbeat), but there are other subtle issues, for instance, remote resources could: throw errors (for example, temporary bursts of exceptions) or perform poorly.
The goal is to allow clients to "fail fast", avoiding useless resource consumption and ripple effects.

**Important remark**: the **ripple effect** is what happens when a service $A$, used by other services $B_i$,

</div>
<div class="column">

slows down: other services keep sending requests to $A$ making it harder for it to recover, furthermore, the number of open connections in services $B_i$ keep increasing, so they also slow down. This effect propagates and could make the whole system performing poorly.

In this setting we want a component that drops the requests from services $B_i$ to service $A$ until the latter has recovered, thus stopping the ripple effect. This component is known as **circuit breaker** (**CB**): it acts as a **proxy** for a remote service. When the remote service is called, the CB monitors the call. If CB detects too many failures, it inhibits future calls. Calls that take too long or return 5xx errors are treated as failures.

##### Security patterns

A **security pattern** which is often applied in practive is the usage of an **API gateway**: it acts a mediator, sitting between a service client and the service being invoked. Service clients talk only to the gateway. It is a gatekeeper for all traffic to microservices and allow to easily implement authentication/authorization mechanisms. It can be a single point of failur, but this is usually solved through replication.

##### Communication patterns

There are two possible **communication patterns**:
- **synchronous communication**: requires the two communicating parties to be ready to communicate at the same time;
- **asynchronous communication**: allows each counterpart to enter in the communication at its own pace.

We can implement **asynchronous communication** using an **event-driven framework**. TìIt can support **multiple communication styles**, like:
- **notification** (a service sends notifications to the other),

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

- **request/response**,
- **publish/subscribe**.

An asynchronous communication pattern has several advantages, like **loose coupling**, **higher flexibility**, **scalability**, and **availability**, but it is more complex to develop.

##### Spring

The **de-facto standard framework** for developing microservices in Java is **Spring**.
Spring offers explicit support for several key functionalities, like: **building RESTful APIs**, handling communication between microservices, user authentication, building an API gateway.

Let's see a **simple example** of service built with Spring: you are taasked with developing a service that will handle HTTP GET requests on `http://localhost:8080/greeting`. The service will provide a JSON representation of a greeting response: `{"id": 1, "content": "Hello, World!"}`.
You have the option to personalize the greeting by including an optional name parameter in the query string: `http://localhost:8080/greeting?name=User`. In this case the JSON will contain the following content: `{"id": 1, "content": "Hello, User!"}`. `id` is an integer number that keeps track of the number of times that we greeted a user.

The OpenAPI specification is:
```
openapi: "3.0.2"
info:
    title: A (very simple) RESTful web service
    description: RESTful web service.
    version: "1.0"
servers:
    - url: http://localhost:8080
components:
    schemas:
        Greeting:
            properties:
                id:
                    type: integer
                content:
                    type: string
                    pattern: "Hello, ^{.*?}!$"
```

</div>
<div class="column">

```
paths:
    /greeting/:
        summary: Greeting and increment counter
        parameters:
            - name: name
                in: query
                description: Name of who should be greeted
                required: false
                schema:
                    type: string
                    default: World
        get:
            operationId: greetNewUser
            responses:
                "200":
                    description: Successful greeting
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/Greeting"
```

First, let us create a very simple model that represents a new "Greeting". We use the Java "record" keyword: records are designed for scenarios in which a class is generated solely to function as a straightforward data transporter.
```
package com.example.restservice;

public record Greeting(long id, String content) { }
```
Now let's define the controller:
```
package com.example.restservice;

import java.util.concurrent.atomic.AtomicLong;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
@RestController
public class GreetingController {
    private static final String template = "Hello, %s";
    private final AtomicLong counter = new AtomicLong();

    @GetMapping("/greeting")
    public Greeting greeting(@RequestParam(value = "name",
    defaultValue = "World") String name) {
        return new Greeting(counter.incrementAndGet(),
        String.format(tempalte, name));
    }
}
```

- **`@RestController`** handles HTTP requests;
- **`@GetMapping(/greeting)`** handles HTTP GET requests for /greeting;
- The method `greeting` returns a new instance of the `Greeting` class.
- **`@RequestParam(value = "name", defaultValue = "World")`** `String name` specifies the input to the greeting method: `name` is a `String`, the value of this parameter is taken from `GET` request parameter `name`, we specify "World" as default value.
- The RESTful service populates a `Greeting` object, that will be directly written to the HTTP response as JSON.

Let's move to a **more intricated** example: we are going to build a RESTful service to manage the employees of a company. We model employees with the following data:
- **ID**: identifier of the employee. It should be unique for each employee;
- **Name**: the name of the employee;
- **Role**: a string describing the role of the employee within a company.

Our APIs should expose the following functionalities:
- **`getAllEmployees`**: retrieve the list of all the employees of the company;
- **`newEmployee`**: insert a new employee. The new employee is returned to the user of the API;
- **`findEmployeeById`**: retrieve data of a certain employee given the ID. In the case in which no employee is found, a 404 not found error is returned;
- **`replaceEmployee`**: given an employee ID and a new employee, replace the (eventual) existing employee with the new one. The new employee is returned to the user of the API;

</div>
<div class="column">

- **`deleteEmployee`**: delete an employee given the ID. In the case in which no employee is found, no error is returned to the user of the API.

The OpenAPI specification follows:
```
openapi: "3.0.2"
info:
    title: A (short) tutorial on RESTful web services
    description: RESTful web service.
    version: "1.0"
servers:
    - url: http://localhost:8080
components:
    schemas:
        Employee:
            properties:
                id:
                    type: integer
                name:
                    type: string
paths:
    /employees/:
        get:
            summary: Retrieve all Employees
            operationId: getAllEmployees
            responses:
                "200":
                    description: Successful operation
                    content:
                        application/json:
                            schema:
                                type: array
                                $ref: "#components/schemas/Employee"
        posts:
            summary: Add an Employee to the payroll application
            operationId: newEmployee
            requestBody:
                description: ...
                content:
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
                    application/json:
                        schema:
                            $ref: "#/components/schemas/Employee"
                required: true
            responses:
                "200":
                    description: Successful operation
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/Employee"
    /employees/{id}/:
        post:
            summary: Find Employee by ID
            operationId: getEmployeeById
            parameters:
                - name: id
                    in: path
                    description: ID of Employee to return
                    required: true
                    schema:
                        type: integer
            responses:
                "200":
                    description: Successful operation
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/Employee"
                "404":
                    description: Employee not found
        put:
            summary: Replace Employee with a new one
            description: ...
            operationId: replaceEmployee
            parameters:
                - name: id
                    in: path
```

</div>
<div class="column">

```
                    description: ...
                    required: true
                    schema:
                        type: integer
            requestBody:
                description: ...
                content:
                    application/json:
                        schema:
                            $ref: "#/components/schemas/Employee"
            responses:
                "200":
                    description: Successful operation
                    content:
                        application/json:
                            schema:
                                $ref: "#/components/schemas/Employee"
        delete:
            summary: Delete an Employee by id
            operationId: deleteEmployee
            parameters:
                - name: id
                    in; path
                    description: Employee ID to be remove
                    required: true
                    schema:
                        type: integer
            responses:
                "200":
                    description: Succesful operation
```

The mapping between the REST API and the methods is:
- **`getAllEmployees`** $\leftrightarrow$ `GET` method at `/employees/`,
- **`newEmployee`** $\leftrightarrow$ `POST` method at `/employees/`,
- **`findEmployeeByID`** $\leftrightarrow$ `GET` method at `/employees/{id}`,
- **`replaceEmployee`** $\leftrightarrow$ `PUT` method at `/employees/{id}`,
- **`deleteEmployee`** $\leftrightarrow$ `DELETE` method at `/employees/{id}`.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

We start by modeling employees (_we use JPA (Java Persistent API) annotations to make the object ready for storage_):

```
class Employee {
    private @Id @GeneratedValue long id;
    private String name;
    prviate String role;

    Employee() { }

    Employee(String name, String role) {
        this.name = name;
        this.role = role;
    }

    public Long getId() {
        return this.id;
    }
    public String getName() {
        return this.name
    }
    public String getRole() {
        return this.role;
    }
    public void setId(Long id) {
        this.id = id;
    }
    public void setName(String name) {
        this.name = name;
    }
    public void setRole(String role) {
        this.role = role;
    }
    @Override
    public boolean equals(Object o) {
        if (this == 0) return true;
        if (!(o instanceof Employee)) returnf alse;
        Employee employee = (Employee) o;
        return Objects.equals(this.id, employee.id) &&
            Objects.equals(this.name, employee.name) &&
```

</div>
<div class="column">

```
            Objects.equals(this.role, employee.role);
    }
    @Override
    public int hashCode() {
        return Object.hash(this.id, this.name, this.role);
    }
    @Override
    public String toString() {
        return "Employee{" + "id=" + this.id + ", name='" +
            this.name + '\'' + ", role='" + this.role + "'}";
    }
}
```
Spring Data **JPA repositories** are interfaces with methods supporting creating, reading, updating, and deleting records against a backend data store. We can declare the repository as follows:
```
import org.springframework.data.jpa.repository.JpaRepository;

interface EmployeeRepository extends JpaRepository<Employee,
    Long> { }
```
Let's define the **entry point** for the application:
```
@SpringBootApplication
public class PayrollApplication {
    public static void main(String.. args) {
        SpringApplication.run(PayrollApplication.class, args);
    }
}
```
Furthermore, we're going to implement a simple in-memory databse in which we preload some data:
```
@Configuration
class LoadDatabase {
```
</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
    private static final Logger log =
        LoggerFactory.getLogger(LoadDatabase.class);
    @Bean
    CommandLineRunner initDatabase(EmployeeRepository repository) {
        return args -> {
            log.info(...);
        };
    }
}
```

**Remark**: Spring Boot runs all **`CommandLineRunner`**s tagged with **`@Bean`** once the application starts. This runner needs a **copy** of the EntityRepository we created.

It is time to implement the **controller**.
```
@RestController
class EmployeeController {
    private final EmployeeRepository repository;
    EmployeeController(EmployeeRepository repository) {
        this.repository = repository;
    }
    @GetMapping("/employees")
    List<Employee> all() {
        return repository.findAll();
    }
    @PostMapping("/employees")
    Employee newEmployee(@RequestBody Employee newEmployee) {
        return repository.save(newEmployee);
    }
    @GetMapping("/employees/{id}")
    Employee one(@PathVariable Long id) {
        return repository.findById()
            .orElseThrow(() ->
            EmployeeNotFoundException());
    }
    @PutMapping("/employees/{id}")
    Employee replaceEmployee(@RequestBody Employee newEmployee,
        @PathVariable Long id) {
```

</div>
<div class="column">

```
        return repository.findById(id)
            .map(employee -> {
                employee.setName(newEmployee.getName());
                employee.setRole(newEmployee.getRole());
                return repository.save(employee);
            })
            .orElseGet(() -> {
                newEmployee.setId(id);
                return repository.save(newEmployee);
            });
    }
    @DeleteMapping("/employee/{id}")
    void deleteEMployee(@PathVariable Long id) {
        repository.deleteById(id);
    }
}
```

Finally, let's deal with **error handling**:
```
@ControllerAdvice
class EmployeeNotFoundAdvide {
    @ResponseBody
    @ExceptionHandler(ExmployeeNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    String employeeNotFoundHandler(EmployeeNotFoundException ex) {
        return ex.getMessage();
    }
}
```
The **advice** above is rendered straight into the response body, because of the **`@ResponseBody`** annotation. **`@ExceptionHandler`** configures the advice to only respond if an `EmployeeNotFoundException` is thrown. **`@ResponseStatus`** configures the advice to issue an HTTP 404 error code.

### Design Document (DD)

A **DD** has several **purposes**: it allows the **communication** between requirements analysts, architects, and developers; it is the **baseline** for implementation activities;

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

it constitutes a **mapping between requirements and components**; it the **baseline for integration and quality assurance**; it **refines the plan and previous estimations**.

The **reference structure of a DD** is:

1. Introduction

>> Scope $\leftarrow$ _reviews the domain and product, **summary of main architectural styes/choices**_
>> Definitions, acronyms, abbreviations
>> Reference documents
>> Overview $\leftarrow$ _describes contents and structure of the remainder of the DD_

2. Architectural Design

>> Overview: high-level components and interactions $\leftarrow$ _**informal view** (free style notation), major interfaces_
>> Component view $\leftarrow$ _components + interfaces: components diagrams, composite structure, class diagrams (detailed view)_
>> Deployment view $\leftarrow$ _infrastructure: deployment diagram(s) including non-logical elements_
>> Component interfaces $\leftarrow$ _details for each interface (name, signature, returned objects)_
>> Runtime view $\leftarrow$ _dynamics of the interactions: sequence diagrams (realization of use cases)_
>> Selected architectural styles and patterns
>> Other design decisions

3. User Interface Design $\leftarrow$ _overview of UIs, possibly mockups, may refine what's in the RASD (if present)_

4. Requirements traceability $\leftarrow$ _mapping between requirements and design elements_

5. Implementation, Integration and Test Plan $\leftarrow$ _order in which you plan to implement subsystems and components as well as plan of the integration and test of the integration_

6. Effort Spent

7. References

</div>
<div class="column">

### Software qualities and architectures

Several software qualities are directly influenced by architectural choices: we need **metrics** to quantify qualities and specific **methodologies to analyze** the quantitative impact of architectural choices on these qualities.

#### Availability

A service shall be **continuosly available** to the user, that is, it should have **little downtype** and **rapid** service **recovery**.
In order to measure the availability of a service we need to introduce some quantities of interest. In particular, **when a system fails**, we call:
- **time of occurrence** the time at which the user becomes aware of the failure;
- **detection time** the time at which operators become aware of the failure;
- **response time** the time required by operators to diagnose the issue and respond to users;
- **repair time** the time required to fix the service/components that caused the failure;
- **recovery time** the time required to restore the system (re-configuration, re-initialization, ...).

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/failure-recovery.svg"
    width="500mm" />
</p>

Furthermore, we call:
- **Mean Time To Repair** (**MTTR**) the average time between the occurrence of a failure and service recovery, also known as the **downtime**;
- **Mean Time To Failures** (**MTTF**) the average time between the recovery from one failure nad the occurrence of the next failur, also known as **uptime**;
- **Mean Time Between Failures** (**MTBF**) the average time between the occurrences of two consecutive failures.

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/time-between-failures.svg"
    width="500mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

Now that we've introduced **the quantities of intereset**, we are ready to define the **availability** of a service, that is, the **probability that a component is working propertly at time $t$**:

$$
A = \frac{MTTF}{MTBF} = \frac{MTTF}{MTTF + MTTR}
$$

Availability is typically specified in **"nines notation"**: 90% is 1-nine, 99% is 2-nines, 99.9% is 3-nines, ... .

Once we have computed the availability of a single component with the formula above, we are ready to compute the availability for the whole system where several components operate in **series** and in **parallel**. In particular:
- we say that **elements operate in series** if the failure of an element in the series leads to a failure of the whole combination;
- we say the **elements operate in parallel** if the failure of an element leads to other elements taking over the operations of the failed element.

System in **series** are represented as follows:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/series.svg"
    width="300mm" />
</p>

The **availability of the series is the product of the availabilities of the subsystems**:

$$
A_{series} = A_A \cdot A_B
$$

System in **parallel** are represented as follows:

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/parallel.svg"
    width="250mm" />
</p>

</div>
<div class="column">

The **availability of the parallel is**:

$$
A_{parallel} = 1 - (1 - A_A) \cdot (1 - A_B)
$$

**Important remark**: when computing the availability of a **complex system** where components are connected in series and in parallel, we can substitue a set of components in parallel with a single component with the equivalent availability, and the same applies for components in series. By iterating this substitutions we will get to a single component, whose availability is the one of the whole system.

##### Tactis for availability

The main tactics for availability are **replication** and **forward error recovery** (plus the **circuit breaker** that we've seen when talking about microservices).

- **Replication**

We have 4 **replication approaches**:

> - **hot spare**: C1 is leading, C2 is always ready to take over

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/hot-spare.svg"
    width="200mm" />
</p>

> - **warm spare**: C1 is leading and periodically updating C2. If C1 fails, some time might be needed to fully update C2

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/warm-spare.svg"
    width="200mm" />
</p>

</div>
<div class="column">

> - **cold spare**: C2 is dormant and started and updated only when needed

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/cold-spare.svg"
    width="300mm" />
</p>

> - **triple modular redundancy**: C1, C2, and C3 are all active. The produced result is the one produced by the majority

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/triple-modular-redundancy.svg"
    width="300mm" />
</p>

- **Forward error recovery**

When C1 is in the failure state, a recovery mechanism moves it to the degraded state. In the degraded state, C1 continues to be available even if not fully functional.

<p align="center">
    <img src="http://localhost:8080/swe-2/static/availability/forward-error-recovery.svg"
    width="300mm" />
</p>

</div>
</div>

---

## Verification & Validation

<div class="multiple-columns">
<div class="column">

**Verification** answers the question: "_Are we building the software right (w.r.t. a specification)?_".

**Validation** answers the qeustion: "_Are we building the right software (w.r.t. stakeholder needs)?_".

### Quality assurance (QA)

**Quality assurance** defines policies and processes to achieve **quality**.  In order to perform quality assurance, we need a way to assess **quality** a find **defects**.
But, first of all, we need to define what we mean with quality and defects:
- **quality** is a general term which may refer to: the absence of defects (or bugs), or the absence of other issues that prevent the fulfilment of non-functional requirements;
- **failure** refers to the termination of the ability of a product to perform a required function or its inability to perform it within previosuly specified limits; it can also refer to an event in which a system or system component does not perform a required function within specified limits;
- **fault** refers to the manifestation of a defect;
- a **defect** is an imperfection or deficiency in a program (for example a function should always return a positive value, but returns a negative value);
- an **error** is a human action that introduced an incorrect result.

### Verification

In other engineering disciplines we can "cover infinite cases" with a single test (for example if a bridge can handle $x$ tons, then it can handle also $0.99 x$ tons).
This is not the case for software engineering:
```
...
a = y / (x + 20)
...
```
the code above works for any value of `x` but `-20`.
For this reason we need to perfrom verification in severl phases during the entire development process.
A model which comprehends the various verification (and validation) stages that we have to perform is the V model.

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/swe-2/static/verification/v-model.png"
    width="500mm" />
</p>

The main approaches for verification in SWE are:
- **static analysis**: done on source code without execution (the analysis is static but properties are dynamic);
- **testing** (**dynamic analysis**): done by executing the sources (usually by sampling); it analyzes the actual behavior compared to the expected one.

#### Static analysis

The **core idea of static analysis** is the following: it analyzes the source code, each analyzer targets a fixed set of **hard-coded** (pre-defined, not custom) properties; it is completely **automatic**; at the end, the output reports **safe** if there are **no issues** or **unsafe** if there are potential issues.
The **checked properties** are often general safety properties, that is, the absence of certain conditions that may yield errors. For example: **no overflow** for integer variables, **no type errors**, ... .

We say **program behavior all possible executions** of a program, **as sequences of states**.
Static analysis **allows us to find possible erroneous states**, but **program behavior may not reach those states**. Thus, we say that **static analysis is pessimistic**.
Static analysis is based on **over-approximations** to be **sound**. The degree of precision is often traded-off against efficiency:
- **perfect precision** is often impossible due to undecidability;
- **high precision** may still be too computationally **expensive**;
- **low precision** is **cheaper** but leads to many **false positives** that must be verified manually.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

##### Control-Flow Graphs (CFG)

Many static analysis methods are based on **CFG**s. A **CFG** is a directed graph representing possible **execution paths**:
- a CFG **node** corresponds to a program **statement**;
- a CFG **edge** connects two **consecutive statements**;
- we **ignore declarations without assignment** since they do not affect the program state.

We can represent the control-flow constructs as follows:
- **sequence**
```
statement1
statement2
...
```

<p align="center">
    <img src="http://localhost:8080/swe-2/static/CFG/sequence.svg"
    width="120mm" />
</p>

- **if**

```
if (statement1) {
    statement2
} else {
    statement3
}
...
```

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/swe-2/static/CFG/if.svg"
    width="200mm" />
</p>

- **while**

```
while (statement1) {
    statement2
}
...
```

<p align="center">
    <img src="http://localhost:8080/swe-2/static/CFG/while.svg"
    width="160mm" />
</p>

- **for**

You just need to translate:
```
for (int i = 0; i < n; i++) {
    statement1
}
...
```
into

</div>
<div class="column">

```
int i = 0
while (i < n) {
    statement1
    i++
}
...
```
and then apply the transformation rules defined before.

##### Data-flow analysis

**Data-flow analysis** works on the CFG of a program. It extracts information about how the **data flows**: what values are read (used), and written (defined).
An example is **live variable analysis**.

- **Live variable analysis**

Given a CFG, a variable $v$ is **live at** the exit of **block** $b$ if there is some **path** (on the CFG) from block $b$ **to a use** $c$ of $v$ taht does not redefine $v$ (that is, there is no **intermediate block** ($b$ and $c$ are excluded) in the path that redefines $v$).

**Live variable analysis** determines, for each block, which variables **may be live** at the exit of that block. We say "**may**" since not every path on the CFG is a feasible path (that is, a path in the **program behavior**).
We use $LV(b)$ to represent the **set of live variables at block $b$**. So, because of what we just remarked, if $x \notin LV(k)$ then **definetely** $x$ is not live at $k$, if $x \in LV(k)$, **still**, $x$ **may not be live at $k$**.

Live variable analysis allows to perform **dead assignment elimintation**: if a variable is **not live after** it is **defined** by an assignment, the assignment is **useless** and can be **removed** without changing the program behavior.

**Important remark**: live variable analysis can be performed automatically through some standard algorithms.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

- **Reaching definitions**

Given a CFG, a **definition $(v, k)$** is an **assignment** to variable $v$ **occurring** at block $k$.
We say that a definition $(v, k)$ **reaches** block $r$ if there is **a path from $k$ to $r$** that does not redefine $v$.

The **goal** of **reaching definition analysis** is the following: for each block of the CFG we want to **determine which definitions may reach that block**.
We denote with $RD_{IN}(k)$ the **set of definitions reaching block $k$** and with $RD_{OUT}(k)$ the **set of definitions which exit from block $k$** (if block $k$ defines or redefines some variable, then $RD_{IN}(k) \neq RD_{OUT}(k)$).

In order to compute $RD_{IN}(k)$ and $RD_{OUT}(k)$ for every block $k$ we can exploit the following **equations**:
- $RD_{IN}(k)$ $=$ $\cup_{h \rightarrow k} (RD_{OUT}(h))$;
- $RD_{OUT}(k)$ $=$ $(RD_{IN}(k) \setminus kill_{RD}(k)) \cup gen_{RD}(k)$

where
- $h \rightarrow k$ means that block $h$ is a predecessor of block $k$ in the CFG;
- $kill_{RD}(k)$ is the set of definitions in $RD_{IN}(k)$ regarding **variables** which are **redefined at $k$**;
- $gen_{RD}(k)$ is the set of **definitions at $k$**.

In particular **we start by assigning $RD_{IN}(0) = \{\}$** where $0$ is the first block, then **we keep applying the formulas above to the blocks until convergence**.

**Important remark**: in principle, when performing **reaching definition analysis** on paper, we would have to write down a "$RD_{IN}$" and a "$RD_{OUT}$" set for each block; **it is worth observing that**:
- **if block $k$ does not define any variable**, then $RD_{IN}(k) = RD_{OUT}(k)$;
- **if block $k$ has only one predecessor $h$**, then $RD_{OUT}(h) = RD_{IN}(k)$;

</div>
<div class="column">

- **and of course holds the transitive property**.

So if sets $A, B, C, D, ...$ are equal, instead of writing down $A = \{ ... \}$, $B = \{ ... \}$, $C = \{ ... \}$, $D = \{ ... \}$, $...$, we can use the **compact notation instead**:
$$
A = B = C = D = ... = \{ ... \} \text{ .}
$$

- **`use-def`** and **`def-use` chains**

The information about which statements **define** values and which **use** them is useful for program optimization or to avoid potential errors. For this purpose we use:
- **`use-def`** (**UD**) **chains**: they are links from a **use** to **all the definitions** that may reach it;
- **`def-use`** (**DU**) **chains**: they are links from a **definition** to **all the uses that it may reach**.

In particular, we denote with $UD(v, k)$ the **set of blocks in which $v$ is defined**, and such that, the definition reaches the **use** $(v, k)$, that is:

$$

UD(v, k) = \begin{cases}
\{ q \mid (v, q) \in RD_{IN}(k) \} \text{ if } v \text{ is used in block } k \\
\{ \} \text{ otherwise}
\end{cases}

$$

Analogously, we denote with $DU(v, k)$ the **set of blocks in which $v$ is used**, and such that, the **definition** $(v, k)$ reaches that usage, that is:

$$
DU(v, k) = \begin{cases}
\{ q \mid k \in UD(v, q) \} \text{ if } v \text{ is defined in block } k \\
\{ \} \text{ otherwise}
\end{cases}
$$

Finally, from $UD$ and $DU$ we can compute **`use-def`** and **`def-use`** pairs, in particular, for a given variable $v$:
- a **`use-def` chain** is a couple $q \rightarrow k$ s. t. $(v, q)$ is a **use of $v$** and $k \in UD(v, q)$;
- a **`def-use` chain** is a couple $q \rightarrow k$ s. t. $(v, q)$ is a **definition of $v$** and $k \in DU(v, q)$.

</div>
<div class="column">

</div>
</div>