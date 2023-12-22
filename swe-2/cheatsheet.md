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

**After the scenarios** are formulate, we need to generalize them into **use cases**.

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
- **special requirements**: constrains, non-functional requirements.

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

- **composition**: it is a stronger form of aggregation where the aggregate controls the lifecycle of the elements it aggregates:

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



</div>
<div class="column">

</div>
</div>