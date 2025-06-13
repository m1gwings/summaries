---
marp: true
theme: summary
math: mathjax
---
# Secure network architectures

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Prof. Michele Carminati's slides_)

</div>

## Firewalls

A **firewall** is a network access control system that verifies all the packets flowing through it. It main **functions** are usually IP packet filtering and **Network Address Translation** (**NAT**).

A firewall must be the single enforcement point between a screened network and outside networks. It checks all and only the firewall flowing through it. Thus it is powerless against insider attacks.

The firewall itself is a computer: it could have vulnerabilities and be violated. Most of the times it is a single purpose machine, an embedded appliance with just firmware, usually offering few or no services to reduce the attack surface.

Firewall filtering is implemented through **rules**. Policies must be built on a **default deny base**.

### Firewall taxonomy

We divide firewalls depending on their **packet inspection capability** (from low to high layers).
1. **Network layer firewalls** filter packets at the network and transport layer.
2. **Application layer firewalls** filter packets at application layer.

#### Packet filters

**Packet filters** are network layer firewalls. They decode the ICP (and part of the TCP heder):
- the source and destination IP;
- the source and destination port;
- the protocol type;
- the IP options.

They are **stateless**: they cannot track TCP connections and there is no full payload inspection.
The rules are built through predicates on the processed field which allow to determine if a packet is allowed or not.

---

Examples are:
- Block any incoming packet ("default deny"):
```
iptables -P INPUT DROP
```
- Allow incoming packets if going to 10.0.0.1:
```
iptables -A INPUT -d 10.0.0.1 -j ALLOW
```
- Block anything out except SMTP (port 25):
```
iptables -P OUTPUT DROP
iptables -A OUTPUT --dport 25 -j ALLOW
```
Regardless of the specific syntax. every network packet filter allow to express the following concept: if the packet matches a certain condition, then do this (e.g., block, allow, log, ...).

#### Stateful (or Dynamic) Packet Filters

**Stateful Packet Filters** are network packet filters that keep track of the **TCP state machine** (after SYN, SYN-ACK must follow). It allows to track connections and allow response packets only when they follow a previous corresponding request.

The disadvantage of this kind of firewalls is that performance is bounded on a **per-connection basis**, not on a **per-packet basis**. The **number of simultaneous connections** are just as important as packets per second.

Firewalls of this kind can be used to track connection and provide deeper content inspection. **Network Address Translation** (**NAT**) is offered as an embedded feature.
A fundamental concept for NAT to work is the session. A **session** is an atomic, transport-layer exchange of application data between 2 hosts. In TCP this corresponds roughly to a TCP connection. In UDP, there is no explicit concept of session.
Thus, if we need to add NAT on top of TCP, we simply add a new slot (if allowed) for each new TCP connection. Conversely, in UDP, the session must be inferred. This is done as follows: if a response packet is received withing a certain timeout (e.g., 2 minutes), it is considered "in the session".

Some protocols transmit network information data at application layer.
An example is FTP which has a PORT application command to specify the port on which the data is transferred. Stateful firewalls must take care of this.
The NAT should operate on this data transferred at application level.

In particular, a client-side firewall for FTP in **standard mode**:
1. Must open port 21 outbound.
2. Must dynamically open/close the (inbound) ports that the client specifies in the command.

---

A server-side firewall:
1. Must open port 21 inbound.
2. Must dynamically open/close the (outbound) ports that the client specifies in the command.

In **passive mode** both channels are initialized by the server. A client-side firewall:
1. Must open port 21 outbound.
2. Must dynamically open/close the (outbound) ports that the server specifies.

The server-side firewall:
1. Must open port 21 inbound.
2. Must dynamically open/close the (inbound) ports that the server specifies.

#### Circuit firewalls

**Circuit firewalls** are firewalls which rely on TCP connections.
The client connects to a specific TCP port on the firewall, which then connects to the address and port of the desired server. Essentially, it is a TCP-level proxy. Observe that it is not transparent to the client.

#### Application proxies

**Application proxies** are the same as circuit firewalls, but at application layer. They are almost never transparent. Each protocol needs its own proxy server which inspects, validates, and manipulates protocol application data.

An application proxy can authenticate users, apply specific filtering policies, perform advanced logging, content filtering, or scanning. It can be used to expose a subset of the protocol to defend clients, or to defend servers.

## Architectures for secure networks

### Dual- or Multi-zone architectures

In most cases, the perimeter defense works on the assumption that what is "good" is inside and what's outside should be kept outside if possible.
The **problem** is that, if we mix externally accessible servers with internal clients, we lower the security of the internal network.
The **solution** is to allow external access to the accessible servers, but not to the internal network. The general idea is to split the network by privilege levels.
In practice, we create a semi-public zone called DMZ (demilitarized zone). The DMZ will host public servers. On the DMZ there is no critical or irreplaceable data since it is almost as risky as the internet.
We put a first firewall between internet and the DMZ and a second firewall between the DMZ and the private network.

---

### Virtual Private Networks

**Virtual Private Networks** (**VPNs**) are needed when we have one of the following requirements:
- Remote employees need to work "as if" they were in the office, accessing resources on the private zone.
- Connecting remote sites without using dedicated lines.

In other words, we want to ensure CIA to data transmitted over a public network.

A VPN provides an encrypted overlay connection over a public network.

There are two VPN modes: **full tunnelling** and **split tunneling**.
In full tunneling every packet goes through the VPN tunnel. This approach could be inefficient. It is a single point of control and application of all security policies as if the client were in the corporate network.

In split tunneling the traffic to the corporate network goes through the VPN, the traffic to the internet goes directly to the ISP. It is more efficient, but with less control.

Examples of VPN technologies are **PPTP** (Point-to-Point Tunneling Protocol), which is a Microsoft proprietary protocol; VPN over pure TLS; SSH tunnel; OpenVP; IPSEC.
