---
marp: true
theme: summary
math: mathjax
---
# Computing infrastructures

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

A **computing infrastructure** is a _technological infrastructure_ that _provides <u>hardware</u> and <u>software</u>_ for _<u>computation</u>_ to other systems and services.

</div>

Some _macro-classes_ of computing infrastructures are:
- **data centers**, which comprise:
    - servers for _processing_;
    - servers for _storage_;
    - servers for _communication_;
- **edge computing systems**;
- **embedded PCs**;
- **IoT** (Internet of Things).

Let's analyze each one of them.

## Data centers

### Pros

1. _Lower_ IT _costs_;
2. _High performance_;
3. _Instant_ software _updates_;

---

4. _"Unlimited" storage_ capacity;
5. Increased _data reliability_;
6. _Universal document access_;
7. _Device independence_.

### Cons

1. _Require_ a constant _internet connection_;
2. Do _NOT work_ well with _low-speed connections_;
3. _Hardware features_ might be _limited_;
4. _Privacy_ and _security_ issues;
5. High _power consumption_;
6. _Latency_.

#### Energy consumption partitioning

The energy consumed by a data center is roughly partitioned as follows:

- ~45 % - _Servers_ (CPU, memory, disk);
- ~25 % - _Infrastructure_ (UPS, cooling, power distribution); 
- ~15 % - _Power draw_ (Electrical utility costs);
- ~15 % - _Network_ (Switches, links, transit).

That is: the **majority of energy** is **NOT employed** for **computation**.

---

## Edge (a.k.a fog) computing systems

<div class="definition">

**Edge computing** is a distributed computing model that brings computation and data storage closer to the sources of data.

</div>

### Pros

1. High _computational capacity_;
2. _Distributed computing_;
3. _Privacy_ and _security_;
4. _Reduced latency_.

### Cons

1. Require _power connection_;
2. Require _connection_ to the _cloud_.

## Embedded PCs

Examples are:
- _Raspberry Pi_;
- _Google Coral_;
- ... .

---

### Pros

1. _Pervasive computing_;
2. _High performance units_;
3. _Availability of development boards_;
4. _Programmed as PCs_;
5. _Large community_.

### Cons

1. (Pretty) _High power consumption_;
2. (Some) _HW design_ has to be done.

## IoT

### Pros

1. Highly _pervasive_;
2. _Wireless connection_;
3. _Battery powered_;
4. _Low costs_;
5. Supports _sensing and actuating_.

### Cons

1. _Low computing_ ability;
2. _Constraints_ on _energy_;
3. _Constraints_ on _memory_ (RAM).