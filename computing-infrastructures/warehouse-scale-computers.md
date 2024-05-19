---
marp: true
theme: summary
math: mathjax
---
# Data-centers and Warehouse-scale computers

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

## Basic definitions

<div class="definition">

**Data-centers** are _buildings_ where multiple _servers_ and _communication units_ are _co-located_ because of their common environmental requirements, physical security needs, and ease of maintenance.

</div>

<br> 

<div class="definition">

**Warehouse-scale computers** (**WSC**s) (_like data-centers_) are _buildings_, of the size of a warehouse, where multiple _servers_ and _communication units_ are co-located; which _belong_ (usually) _to a single organization_, use a (relatively) _homogenous hardware and system software platform_, and share a _common system management layer_.

</div>

The software running on WSCs executes on clusters of hundreds to thousands of individual servers. The machine is itself this large cluster or aggregation of servers and needs to be considered as a single computing unit.

---

### The differences between the two

**Data-centers**:
- typically host a large number of _small-_ or _medium-sized applications_;
- each application runs on a _dedicated hardware infrastructure_ that is decoupled and protected from other systems in the same facility;
- _applications_ tend _NOT_ to _communicate with each other_;
- host _hardware and software_ for _multiple organizational units_ or even _different companies_.


**Warehouse-scale computers**:
- run a _small number_ of very _large applications/internet services_;
- have a _common resources management infrastructure_;
- _applications interact_ to implement _complex services_;
- host _homogeneous hardware_ controlled by a _single organization_.

## The shift in computing and storage

In the last few decades, computing and storage have moved **from PC-like clients** **to** smaller, often mobile, devices, combined with **large internet services** hosted in data-centers/warehouse-scale computers.

---

**Why?**
- _User experience improvement_ due to ubiquity of access to documents and ease of maintenance (no need for backups, ...).

- _Advantages to vendors_:
> - the software has to run on _few well-tested hardware configurations_;
> - _easier to dispatch changes_ (instead of having to update millions of devices);
> - faster _introduction of new hardware devices_ (e.g. accelerators).

- Some _workloads_ require _so much computing capability_ to be executed on a client device.

### From WSCs back to data-centers: public clouds

Initially designed for online data-intensive web workloads, _WSCs_ also _now power public clouds_ computing systems which _run many small-applications_, like a traditional data-center.
All of these applications rely on _virtual machines_ and they access large, **common services**, for _block or database storage_, _load balancing_, ..., _fitting well in the WSC model_.

---

## From one to many data-centers/WSCs

It is usual to have **multiple data-centers/WSCs** which offer the **same service**.
This allows to:
- _reduce_ user _latency_;
- _improve_ serving _throughput.
A _request_ is typically _fully processed_ in a _single data-center/WSC_.

### Where to place them: the hierarchical approach

The **hierarchical approach** consists in dividing the world, from _coarse- to fine-grain_, into:
1. **Geographical Areas** (**GA**s);
2. **Computing Regions** (**CR**s);
3. **Availability zones** (**AZ**s).

- **Geographical Areas** are defined by geo-political boundaries/country borders; they are determined mainly by data residency. In each GA there are at least two CRs.

- **Computing regions** are the finer-grain discretization that the customers can see. Their _perimeter_ is _defined by latency_: **2 ms** of round trip time (RTT, the time needed to send a packet and receive the answer) between any two nodes. Nodes in the same CR can be too far for synchronous applications, but ok for disaster recovery.

---

- **Availability zones** are finer grain locations within a single CR. They allow customers to run mission critical applications with high availability and fault-tolerance. This is due to application-level synchronous replication between different AZs; 3 is the usual necessary and sufficient number for quorum.

## Architectural overview of a WSC

The hardware implementation of different WSCs might significantly change, but the _architectural organization_ is usually _the same_.
We can split the architecture in 4 macro-areas:
- **Servers**;
- **Storage**;
- **Networking**;
- **Building** and **Infrastructure** (**Cooling systems**, **Power supply**, **Failure recovery**).

### Servers

They are like ordinary PCs, but with a form factor that allows to fit them into racks.
They may differ is:
- number of CPUs;
- available RAM;
- locally attached disks (HDD, SSD);
- other special purpose devices (GPU, TPU, ...).

---

### Storage

Disks and flash SSDs are the building blocks of WSCs' storage systems. These devices are connected to the data-center/WSC network and managed by sophisticated distributed systems.

### Networking

Communication equipment allows network interconnections among the devices.
