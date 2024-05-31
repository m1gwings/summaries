---
marp: true
theme: summary
math: mathjax
---
# Networking

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Guido Maier_)

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

## Stages of enterprise infrastructures

### Monolithic app

The earliest stage of enterprise infrastructures is the monolithic architecture in which applications were run on a mainframe and did not communicate together. Clearly, this architecture had minimal network demands.

### Client server

The second stage, in chronological order, is the client-server architecture which initially involved only applications used **inside of the enterprise**. In this setting, a computer, said _server_, runs the applications, providing services which can be accessed by other computers, said _clients_, by sending requests _through the network_.
This infrastructure produced high network demand _inside the enterprise_. The communication happened both through TCP/IP and proprietary protocols.

---

### Web applications

With the rise of the web, client-server applications were accessed not only inside the enterprise, but from clients coming from anywhere. As a consequence the network demand both inside and outside of the enterprise increased a lot. The communication protocol used is for the great majority TCP/IP.

### Microservices

In the current stage, the applications running onto servers are split into smaller ones which execute very specific functionalities, known as **microservices**. Furthermore, the deployment of these microservices moved to the cloud.
This clearly increased the server-to-server traffic: several microservices running (potentially) on different servers need to cooperate to carry out the required operation.

---

## Effective networking in WSCs

The considerations made about the current enterprise infrastructure (_microservices_), and the shift to the cloud, motivates the study of efficient networking solutions to connect the huge number of servers in WSCs. Furthermore, as the performance of servers increases over time, the demand for inter-server bandwidth naturally increases as well.

Observe that making the networking scale is not as easy as for computation or storage, where we can simply increase the number of servers/storage devices respectively (_horizontal scaling_).
Indeed doubling the _leaf bandwidth_ is easy: with twice as many servers, we'll have twice as many network ports and thus twice as much bandwidth. But, if we assume that every server needs to talk with every other server, doubling the leaf bandwidth is not enough to communicate efficiently, we need to deal with the _bisection bandwidth_ (_defined below_).

<div class="definition">

In computer networking, if the network is bisected into two equal-sized partitions, the **bisection bandwidth** of a _network topology_ is the bandwidth available between the two partitions. Bisection should be done in such a way that the bandwidth between two partitions is minimum.

</div>

---

In this setting, bisection bandwidth is a good characterization of the actual network capacity.

The networks used in WSCs can be classified into three main categories:
- **Switch-centric** architecture: uses switches to perform packet forwarding;
- **Server-centric** architecture: uses servers with multiple Network Interface Cards (NICs) to act as switches in addition to performing other computational functions;
- **Hybrid** architecture: combines switches can servers for packet forwarding.

We classify the **traffic** inside a WSC network into:
- **North-south traffic**: it refers to communications with devices external from the WSC (_through the internet_); for example all the requests and responses exchanged with external clients.
- **East-west traffic**: it refers to communications between the servers in the WSC. Think about storage replication, VM migration, etc. . Observe that _east-west traffic is usually significantly larger than north-south traffic_.
We can further classify east-west traffic into:
> - **Unicast**: point-to-point communication between two servers;
> - **Multicast**: one-to-many communication (e.g. when dispatching software updates);

---

> - **Incast**: many-to-one communication (e.g. the reduce phase in MapReduce).

### Switch-centric architectures

#### Three-tier network

**Three-tier network** is a "_classical_" switch-centric network architecture for WSCs. In particular the switches in the network topology are classified into three levels: **access**, **aggregation**, and **core**. Servers are connected to the WSC network through access switches. Each access switch is connected to at least two aggregation level switches. Aggregation switches are connected to core switches (_a.k.a. gateways_).

For a given access switch we denote with $N$ the number of ports connected to other switches, with $B$ their bandwidth, with $n$ the number of ports connected to servers, and, finally, with $b$ their bandwidth. We can now distinguish between a three-tier network **without oversubscription**: $N B = n b$, or **with oversubscription**: $N B < n b$.

Another distinction is among **Top-of-Rack** (**ToR**) and **End-of-Row** (**EoR**) architecture.
In the **ToR architecture** each server is connected to a ToR access switch in its rack. Aggregation switches are in dedicated racks or in shared racks. In this architecture the number of cables is limited as the number of ports per switch (_reducing the cost_),

---

but it suffers of limited scalability due to the higher complexity for switch management simply caused by the high number of switches.

In the **EoR architecture**, aggregation switches are positioned one per corridor, at the end of a line of rack. _Servers in a rack are connected directly to the aggregation switch in another rack_. Aggregation switches must have a larger number of ports, and more complex cabling is required (_increasing the cost_). Anyway the switch management is simpler since the switches are less.

In this architecture the bandwidth can be increased by increasing the switches at the core and aggregation layers, and by using routing protocols such as **Equal Cost Multiple Path** (**ECMP**) that equally shares the traffic among different routes.

This solution is very simple, but can be very expensive in large data-centers since:
- upper layers require faster network equipments;
- each layer is implemented by switches of a different kind;
- the cost in term of acquisition, management, spare-part stocks and energy consumption can be very high.

#### Clos topology a.k.a. Leaf-Spine

In a Leaf-Spine network we can distinguish between two levels of switches: **leaf** and **spine**.

---

Leaf switches are connected to servers (_access switches_), while spine switches serve as aggregation switches. In particular, in a WSC, ToR switches form the leaf layer.

The Spin-Lead topology is borrowed from the telephone world (_with circuit switching_), in particular it is inspired by Clos networks.

A **non-folded Clos network** has the topology depicted below:

<p align="center">
    <img src="static/non-folded-clos-network.svg"
    width="500mm" />
</p>

In particular there are three stages of switches: an **input stage**, a **middle stage**, and an **output stage**. Each switch of one stage is connected to all the switches of the following state (_and vice-versa_). Let $k$ be the number of middle stage switches. Let $n$ be the number of input and outputs switches of side stages. 

---

The following results hold.
- If $k \geq n$ there is always a way to **rearrange** communications to free a path between any pair of idle input/output ports. In particular, the term _Clos topology_ usually denotes the special case $k = n$.
- If $k \geq 2n-1$ there is always a **free path** between any pair of idle input/output ports.

Notice that $t$ is a free design parameter: the total number of input/output ports $N t$ can scale freely (_by increasing the number of ports of middle-stage switches_).

Observe that in Clos topology each switching module is unidirectional: there is a pre-defined input and output stage. Anyway it is easy to modify it, making it bidirectional.

<p align="center">
    <img src="static/bidirectional-clos-topology.svg"
    width="350mm" />
</p>

---

In particular the previous picture depicts the case $n = k$. Each switching module is bidirectional. There are $t$ leaf switching modules with $2k$ bidirectional ports each, and $k$ spine switching modules with $t$ bidirectional ports each: a Leaf-Spine architecture.
Each path between two I/O ports traverses either 1 (if the servers which are communicating are connected to the same leaf switch) or 3 modules.

An **interesting case** is the one in which _every switch_ has $2k$ ports. In particular, since this holds also for spine switches, which in the general case have $t$ ports, it must be that $t = 2 k$. Then we have $2 k$ leaf switches. Each leaf switch has $k$ I/O ports and $k$ ports towards the $k$ spine switches. Hence, we have a total of $2k^2$ I/O ports.

Clos design has several advantages, like the use of homogeneous equipments, ease in routing, the number of hops is the same for any pair of nodes, etc. .

##### Multi-tier clos networks

Can we scale the Leaf-Spine network to a multi-tier design? The answer is yes, by using a PoD based model.
In general a **Point of Delivery** (**PoD**) is a module or group of network, compute, storage and application components that work together to deliver a network service, and, most important, a PoD constitutes a _repeatable pattern_.
In our case we want to transform each Leaf-Spine group into a PoD.

---

In particular we can build a PoD with $2k$ switches with $2k$ ports each: $k^2$ towards the servers and $k^2$ towards the WSC network (plus $2k^2$ for the full connection of the two stages).

<p align="center">
    <img src="static/single-pod-multi-tier-clos.svg"
    width="200mm" />
</p>

The PoD is replicated $P$ times, allowing for the connection of a total of $k^2P$ servers. The PoDs are interconnected through $k^2$ switches with $P$ ports each.

<p align="center">
    <img src="static/multi-tier-clos-network.svg"
    width="270mm" />
</p>

---

Observe that the connectivity between aggregation switches and core switches is partial.

A special instance of this topology is the **Fat-tree**, where $P = 2k$. It allows to connect $P k^2 = 2 k^3$ servers thanks to $P 2 k + k^2 = 4k^2 + k^2 = 5k^2$ switches, with $2k = P$ ports each.

Another important instance is **VL2 network**. It is a cost-effective WSC network with high bisection bandwidth. It uses three types of switches: _intermediate_, _aggregation_, and _ToR_ switches. In particular there are $\frac{D_A}{2}$ intermediate switches, $D_I$ aggregation switches and $\frac{D_A D_I}{2}$ ToR switches, and it allows to connect a total of $5 D_A D_I$ servers. It uses a load balancing technique called Variant Load Balancing (VLB).

### Server centric architectures

**CamCube** is an example of server-centric architecture proposed for building container-sized data centers. It may reduce implementation and maintenance costs by using only servers to build the network infrastructure. It uses a 3D-torus topology to interconnect the servers directly. As a torus-based architecture, it exploits network locality to increase communication efficiency. The drawbacks are that CamCube requires servers with multiple NICs to assemble the 3D-torus network. Furthermore, it is characterized by long paths, and high routing complexity.

---

### Addressing and routing in WSC networks

In the context of WSC networks, addressing and routing can be very challenging. Standard schemes do not provide efficient solutions: techniques specific for WSC networks have been developed. 
In particular at layer 2 we have to overcome classical ethernet-based spanning tree-based routing to exploit equal-cost multi-paths. At layer 3 we need to overcome the complexity of classical Interior Gateway routing protocols and support VM migration.
