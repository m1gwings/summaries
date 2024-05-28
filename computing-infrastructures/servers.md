---
marp: true
theme: summary
math: mathjax
---
# Servers

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

Servers hosted in individual shelves are the basic building blocks of WSCs. They are interconnected by hierarchies of networks, and supported by the shared power and cooling infrastructure.

They are _like ordinary PCs_, but with a **form factor** that _allows_ to _fit_ them _into the shelves_. They house the _motherboard_, the _chip-set_, plus additional _plug-in components_.

## Racks

<div class="definition">

The _special shelves_ which accommodate all the IT equipment, including servers, are known as **racks**.

</div>

Each rack houses several vertically stacked slots, with a standard height measured in _Us_: **1 U = 44.45 mm**. The advantage of a standard form factor is that it allows to stack together different electronic devices, even from different producers.

The rack is not only a container: it handles the shared power infrastructure, including power delivery, battery back-up, and power conversion.

---

The width and depth of a rack can vary across different WSCs. Usually they are 19 in wide and 48 in deep.

It is often convenient to connect the network cables at the top of the rack, such a rack-level switch is called **Top Of Rack** (**TOR**) switch for this reason.

### Form factors

Servers come with 3 main form factors (2 of which are standardized to make them fit into racks):
- **tower**;
- **rack**;
- **blade**.

#### Tower server

**Tower servers** do NOT have a standardized form factor: they look and feel like traditional tower PCs.

**Pros**:
- Easy to _upgrade and customize_.
- _Cost_-effectiveness: usually they are the cheapest of all kind of servers.
- Easy to _cool_ since they have low overall components density.

**Cons**:
- Consume _a lot of space_.

---

- _Low performance_.
- Suffer _complicated cable management_.

#### Rack server

**Rack servers** are designed to be positioned inside a single rack slot. They are vertically stacked along with other devices.

**Pros**:
- _Failure containment_: it takes very little effort to identify, remove, and replace a malfunctioning server with another.
- _Simplified cable management_.
- _Cost_-effectiveness.

**Cons**:
- _Power usage_: they need an additional cooling system due to the high components density, thus consuming more power.
- _Maintenance_: since multiple devices are placed in a rack together, maintaining them gets increasingly difficult with the number of racks.


#### Blade server

**Blade servers** are hybrid rack servers, in which servers are placed into _blade enclosures_, forming _blade systems_. 

---

Blade servers are the latest and most advanced type of servers in the market.

**Pros**:
- _Load balancing and failover_: thanks to their much simpler and slimmer infrastructure, load balancing among the servers and failover managements tend to be easier.
- _Centralized management_: in a blade system, you can connect all the blades through a single interface, making maintenance and monitoring easier.
- _Cabling_: blade servers don't involve the cumbersome task of setting up cabling.
- _Size and form-factor_: they are the smallest and most compact servers.

**Cons**:
- _Expensive configuration_: the initial configuration and setup of a blade server requires heavy effort in a complex environment;
- _HVAC_ (Heating, Ventilation and Air Conditioning): blade servers have very high component density; they need special accommodations to ensure that they don't overheat.
- _Vendor lock-in_: blade servers typically require the use of the manufacturer's specific blades and enclosures.

---

## Components

### The motherboard

The **motherboard** provides socket and plug-in slots to install CPUs, DIMMs (Dual In-line Memory Module a.k.a. _RAM sticks_), local storage (flash SSDs or HDDs), and NICs (Network Interface Card).

### Chip-set and additional components

A server's _motherboard_ supports:
- from 1 to 8 CPUs;
- from 2 to 192 DIMM slots;
- from 1 to 24 drive bays (which can be HDD and SSD with SAS or SATA connectors);
- from 1 to 20 GPUs or TPUs.

#### Graphical Processing Unit (GPU)

**GPUs** are processing units meant for _data-parallel computations_: the same program is executed on many functional units in parallel.

The usual _configuration_ for GPUs in a rack in the following: there is a _CPU host_ connected to a _PCIe_-attached accelerator tray with multiple GPUs. GPUs within the tray are connected using high-bandwidth interconnects such as _NVlink_.

---

#### Tensor Processing Unit (TPU)

While suited to ML, GPUs are still relatively _general purpose devices_. In recent years designers further specialized them to ML-specific hardware: **TPUs**.

TPUs are hardware accelerators designed for efficient computations with _tensors_. In the ML domain, a **tensor** is an $n$-dimensional matrix. Furthermore, it is the basic unit of operation of _TensorFlow_. For this reason TPUs are used both for _training_ and _inference_ of deep learning models.

Several TPU versions have been developed:
- _TPUv1_: it is an inference focused accelerator connected to the host CPU via a PCIe link.
- _TPUv2_: in this version, each tensor core has an array for matrix computations (_MXU_) and a connection to high bandwidth memory (_HBM_) to store parameters and intermediate values during computations.
Multiple TPUv2 accelerator boards can be connected in a rack through a custom high-bandwidth network which enables "fast parameter reconciliation" (_aggregation steps in back-propagation_). 
- _TPUv3_: it is the first _liquid cooled accelerator_ of this kind. It is 2.5x faster than TPUv2.
- _TPUv4_: it is 2.7x faster than TPUv3.

---

#### Field-Programmable Gate Array (FPGA)

An **FPGA** is an array of logic gates that can be programmed (configured) in the field, i.e. by the end user of the device as opposed to the manufacturers. It is composed of several interconnected digital sub-circuits that efficiently implement common functionalities, offering an high level of flexibility.
The digital sub-circuits are called **Configurable Logic Blocks** (**CLBs**).

The configuration of an FPGA is carried out through Hardware Description Languages (HDLs) (such as VHDL) which allow to declare the required components and how they are interconnected.
