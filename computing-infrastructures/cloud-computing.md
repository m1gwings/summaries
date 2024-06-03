---
marp: true
theme: summary
math: mathjax
---
# Cloud computing

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Manuel Roveri_)

</div>

<style>
section {
    font-size: x-large;
}

.definition {
    padding-left: 0.5cm;
    padding-right: 0.5cm;
    background: var(--algorithms);
    border-radius: 0.5cm;
    border-style: solid;
    border-color: var(--text);
    border-width: 3pt;
    text-align: justify;
}
</style>

<div class="definition">

**Cloud Computing** is a coherent, large-scale, publicly accessible, collection of computing, storage, and networking resources.

</div>

It is available via Web service calls through the Internet. The access can be short-term or long-term on a pay-per-use basis.

One of the main reasons that motivated the transition to Cloud computing is the **over-provisioning** problem. This is caused by two facts:
1. it is hard to forecast the growth of the load of a software system;
2. upgrade of IT capacities has very coarse granularity: it takes some time to make the upgrade and usually it must be significative (_we cannot make "too small" upgrades_) to be economically sustainable despite the overheads.

Hence, what happens outside the cloud is that, either we increase too much IT capacities of our infrastructure to face the forecasted growth, which has been overestimated, ending in a waste of resources.

---

Or we can't react readily to an unpredicted growth, causing an under-supply of IT capacities.

In the Cloud world a very large number of applications runs on the same infrastructure, hence the fluctuations in the load are averaged, thus reducing the variance. This means that it is easier to predict the total load and exploit the IT resources to their full capabilities.

The main technology that allows to execute a large set of heterogeneous applications on quite homogeneous hardware is _virtualization_. This approach is known as **server consolidation**: different OS can run on the same hardware, leading to higher hardware utilization. Furthermore, it promotes application independency from the hardware.

Indeed, _without virtualization_:
- software is strongly linked with the hardware, moving or modifying an application is not easy;
- if the underlying hardware fails also the software running on it is doomed to fail.

_With virtualization_ it is possible to move VMs from one physical machine to another without interrupting the applications which are running inside (remember that the state of a VM can be written in a file).

---

This favors:
- **automatic scalability**: it is possible to automatically balance the workload by distributing the VMs on the physical machines according to the demand of the offered services;
- **high availability**: applications are protected against system failure. If a physical machine fails, we can migrate the VMs which were running on top of it to another machine.

## Cloud ontology

We can classify cloud systems as a stack of layers according to the composability criterion: one cloud layer is higher than another in the stack if its services can be composed from the services of the underlying layer. Each layer comprises one or more services.
In particular we can distinguish among 5 layers.
From top to bottom we have:
- **Cloud Application**: Software-as-a-Service (SaaS);
- **Cloud Software Environment**: Platform-as-a-Service (PaaS);
- **Cloud Software Infrastructure**: which comprises **Computational Resources** [Infrastructure-as-a-Service (IaaS)], **Storage** [Data-storage-as-a-Service (DaaS)]; **Communications** [Communication-as-a-Service (CaaS)];
- **Software Kernel**;
- **Firmware/Hardware**: Hardware-as-a-Service (HaaS).

---

### Cloud Application layer

The **Cloud Application layer** is the most visible layer to end-users of the cloud. Normally, the users access the services provided by this layer through web-portals, and are sometimes required to pay fees to use them.

Cloud applications can be developed on the Cloud Software Environment.

### Cloud Software Environment layer

The users of the **Cloud Software Environment layer** are _cloud applications' developers_, implementing their applications for and deploying them on the cloud.
Providers supply developers with a _programming-language-level_ environment with a well-defined API. This layer facilitates the interaction between the environment and the apps, accelerates the deployment, and supports scalability.

### Cloud Software Infrastructure layer

The cloud software infrastructure layer provides fundamental resources to other higher-level layers, which in turn can be used to construct new cloud software environments or cloud applications.
Note that cloud apps and SW environments might _bypass_ cloud SW infrastructure, however this would reduce simplicity and development efforts.

---

#### Infrastructure-as-a-Service

VMs are the most common form for providing computational resources to cloud users at this layer. Users get finer-granularity flexibility since they normally get super-user access to their VMs.

The issues of VMs are:
- **performance interference**: the behavior of one VM can affect the performance of another VM;
- inability to provide strong guarantees about SLAs.

#### Data-storage-as-a-Service

The second infrastructure resource is data storage, which allows users to store their data at remote disks and access them anytime from any place. Data storage systems are expected to meet several rigorous requirements for maintaining users' data reliability, performance, replication and data consistency.

#### Communication-as-a-Service

Communication is a vital component of the cloud infrastructure. Consequently, cloud systems are obliged to provide some communication capability that is service-oriented, configurable, schedulable, predictable, and reliable.

---

## Types of cloud

We can distinguish 4 types of clouds:
- **Private cloud**: it is used by a single organization and can be internally or externally hosted;
- **Community cloud**: it is shared by several organizations, typically is externally hosted, but may be internally hosted by one of the organizations;
- **Public cloud**: it is provisioned for open use for the public by a particular organization who also shots the service;
- **Hybrid**: it is the composition of two or more clouds that remain unique entities but are bound together offering the benefits of multiple deployment models. It can be both internally and externally hosted.

### Public clouds

Public clouds offer large scale infrastructures, available on a rental basis. Resources are granted via web services that customers can access through the internet.

### Private clouds

Private clouds run on internally managed WSCs. The organization sets up a _virtualization environment_ on its own servers. The key benefit is the total control on every aspect of the infrastructure.

---

### Community clouds

A Community cloud is a single cloud managed by several federated organizations. Combining together several organizations allows economy of scale. Resources can be shared and used by one organization, while the others are not using them.
Typically community clouds share infrastructures of the participants, however they can be hosted by a separate specific organization.

### Hybrid clouds

Hybrid clouds are the combination of any of the previous types. Usually this solution is adopted by companies that hold their private cloud and can be subjected to unpredictable peaks of load. In this case, such companies can rent resources from other types of cloud.

## From cloud to edge and fog computing

Cloud computing has _several advantages_:
- lower IT costs;
- improved performance;
- (almost) instant software updates;
- (virtually) unlimited storage capacity;
- increased reliability;

---

- universal document access;
- device independence.

But it suffers also different _disadvantages_:
- it requires a constant internet connection;
- does not work well with low-speed connections;
- the latency is too high for real time applications;
- stored data _might_ not be secure.

Furthermore, in the last years, the number of IoT devices is increasing more and more, thus producing larger and larger amount of data. Processing the data through cloud computing is usually infeasible: the bottleneck is due to sending and receiving the data to and from the WSC. Also, it is usually the case that IoT devices are employed in real time applications, where the latency of the cloud in unacceptable. A new computing paradigm has been proposed with the aim of solving these issues: **edge computing**. In edge computing the computation happens at the _edge_, that is, near where the data is generated.

## ML-as-a-Service

We can abstract the full stack of a ML solution (as for every other software solution) in 3 main layers:
1. **AI application**;
2. **AI platform**;
3. **AI hardware**.

---

Here we're going to focus on how to implement these abstract layers in the cloud computing paradigm (i.e. inside a WSC).
Indeed cloud computing simplifies the access to ML capabilities for:
- **designing a solution** (_without requiring a deep knowledge of ML_);
- **setting up a project** (_managing demand increases and IT solutions_).

There are cloud computing off-the-shelf components which offer entire **ML solutions**, **ML platforms**, or **ML infrastructures** (HW, and libraries).

Inside a WSC, the AI platform and AI hardware abstractions can be decomposed further in 4 layers:
1. **Machine/Deep Learning framework**;
2. **Computing framework**;
3. **Virtual Machine manager**;
4. **Computing cluster**.

### Computing cluster

The **computing cluster** is constituted by:
- **servers** equipped with general purpose CPUs, plus hardware accelerators like GPUs or TPUs;
- **storage devices** including DAS, NAS, and SAN;
- **network devices**.

---

### Virtual Machine manager

**Virtualization** is carried out through hypervisors (VMs) or containers.
The resources can be scaled elastically, as usual in cloud computing, by adding or reducing the number of VMs/containers instanced. Furthermore, users can design personalized software environments.

### Computing framework

**Computing Frameworks** are composed by several modules:
- cluster manager;
- data storage manager;
- data processing engine;
- graph computation engine;
- programming languages.

An application operating in a cluster is distributed among different computing (virtual) machines.

### Machine/Deep Learning framework

**Machine learning frameworks** cover a variety of learning methods for classification, regression, clustering, anomaly detection, and data preparation, and they may or may not include neural network methods.

---

**Deep learning frameworks** are specifically tailored for neural networks methods: they cover a variety of neural network topologies with many hidden layers.
