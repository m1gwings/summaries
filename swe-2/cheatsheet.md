---
theme: cheatsheet
paginate: true
---
# SWE 2 Cheatsheet (A. Y. 2023/2024)

## Introduction

<div class="multiple-columns">
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
