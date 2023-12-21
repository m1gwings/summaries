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

</div>
</div>
