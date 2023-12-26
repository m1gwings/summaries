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

What follows has been inspired and (_partially_) adapted from `https://alloy.readthedocs.io/en/latest/index.html`.

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

</div>
<div class="column">

Consider the model:
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
- **`#A`** returns `N`, that is, the **number of elements in `A`**.

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
then, for a given instance, any atom of parent can only match **up to one** extension, that is, **the intersection between the set assigned to `Child1` and the one assigned to `Child2` is empty**.

</div>
<div class="column">

- **`abstract`**

If you make a signature `abstract`, then all atoms of the signature will belong to extensions: there will be no atoms that are just the supertype and not any of the subtypes. That is, for a given isntance, **the union of the sets assigned to the children is equal to the set assigned to the parent** (the sets assigned to the children form a partition of the set assigned to the parent).

**Remark**: we can add fields to subtypes:
```
sig Child extends Parent {
    field: Set
}
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
fun name[a: some Set1, b: some Set2]: some output_type {
    expression
}
```
The **default** is **`one`** (_that's why we said before that the arguments of a predicate must be atoms of the corresponding set specified in the definition_).

#### Facts

Now that we know how to write complex constraint it's time to understand how to enforce them: we can use **facts**.
The syntax is the following:
```
fact name {
    constraint
}
```
When facts are added to a model, in order to provide a **valid** instance, we not only need to assign a set to every signature and a relation to every field; these sets and relations must also satisfy all the constraints imposed by the facts.

</div>
<div class="column">

##### Implicit facts

You can write a fact as part of a signature. The implicit fact goes after the signature definition and relations. Inside of an implicit fact, you can get the current atom with `this`. **Fields are automatically expanded in the implicit fact to `this.field`**. For example:
```
sig Node {
    edge: set Node
} {
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

**`check`** tells the Analyzer to find a _counterexample_ to a given constraint. **Unlike with `run` command, `check` uses assertions**:
```
assert no_self_loops {
    no n: Node | self_loop[n]
}
check no_self_loops
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

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

#### Time

Alloy 6 added **temporal operators** to Alloy, making it easier to model dynamic systems.

Now **signatures** or **fields** can be declared **mutable**.

</div>
<div class="column">

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

From now on assume that we're evaluating the expressions at the generic step `s`; we will see in a moment that, through some operators, `s` won't always be the _initial_ step. Furthermore, for a predicate `P`, we will use `P(s)` to highlight that `P` is evaluated at step `s` and `s+1`

</div>
<div class="column">

for the step that follows `s`; **this is not valid syntax**.

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