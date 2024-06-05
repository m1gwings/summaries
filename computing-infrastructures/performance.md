---
marp: true
theme: summary
math: mathjax
---
# Performance

<div class="author">

Cristiano Migali
(_adapted from the slides of Prof. Danilo Ardagna_)

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

We define **computer performance** as the _total effectiveness_ of a computer system, including throughput, individual response time, and availability.

It can also be characterized by the amount of useful work accomplished by a computer system or computer network compared to the time and resources used.

</div>

System quality is a central issue of computer systems. It is common practice to validate these system against the functional requirements rather than against quality ones. Indeed, quality validation requires different, and often not available, skills.
Little information related to quality is usually available early in the system lifecycle, but its understanding is of **great importance** from the **cost and performance point of view**.

How can we evaluate system quality?
We can do it in different ways.
- **Use of intuition and trend extrapolation**: it is rapid and flexible, but not very accurate.

---

> Unfortunately those who possess these qualities in sufficient quantity are rare.

- **Experimental evaluation of alternatives**: experimentation is always valuable, often required, and sometimes the approach of choice. It is also expensive, often prohibitively so. A further drawback is that an experiment is likely to yield accurate knowledge of system behavior under one set of assumptions, but not any insight that would allow generalization.

- **Model-based approach**: we build a representation of a system that is _simpler_ than the actual system, _captures_ the essential characteristics, and can be evaluated to make **predictions**. In particular we can distinguish 3 different classes of model-based approaches.
> - **Analytical and numerical techniques** are based on the application of mathematical techniques, which usually exploit results coming from the **theory of probability and stochastic processes**. They are the most efficient and the most precise, but are available only in very limited cases.

> - **Simulation techniques** are based on the reproduction of traces of the model. They are the most general, but might also be the less accurate, especially when considering cases in which rare events can occur. The solution time can also become really large when high accuracy is desired.

---

> - **Hybrid techniques** combine analytical/numerical methods with simulation.

## Queueing theory

We're going to adopt the model of **queueing network** to estimate the performance of a system. In particular, **queueing theory** is the theory behind what happens when you have a lot of jobs, scarce resources, and so long queue and delays.
**Queueing network modelling** is a particular approach to computer system modelling in which the computer system is represented as a network of queues.
A **network of queues** is a collection of **service centers**, which represent system **resources**, and customers, which represent **users** or **transactions**.

In particular, queueing theory applies whenever queues come up.
Queues come up often in computer systems:
- CPU uses a time-sharing scheduler;
- Disk serves a queue of requests waiting to read or write blocks;
- ... .

The success of queueing networks is due to the fact that low-level details of a system are largely irrelevant to its high-level performance characteristics.

---

### Single queue

The basic scenario for a single queue is that customers, who belong to some population, arrive at the service facility. The service facility has one or more servers which can perform the service required by customers. If a customer cannot gain access to a server, it must join a queue, ina  buffer, until a server is available. When service is complete, the customer departs, and the server selects the next customer from the buffer according to the service discipline (_queueing policy_).
Hence, there are different aspects that characterize queueing models:
- **arrival**;
- **service**;
- **queue**;
- **population**.

#### Arrival of customers

**Arrivals** represents jobs entering the system: they specify how fast, how often, and which types of jobs does the station service. We are interested in the average arrival rate $\lambda \ \left[ \frac{\text{requests}}{s} \right]$.
Arrival can come:
- from an external source;
- from another queue;
- from the same queue, through a loop-back arc.

---

#### Service

The **service** part represents the time a hob spends being served. As with the inter-arrival time, the important characteristics of this time will be its **average duration** (or, for a more advanced analysis, the **distribution function**).
If the average duration of a service interaction between a server and a customer is $\frac{1}{\mu}$, then $\mu$ is the **maximum service rate**.

#### Number of servers

We distinguish between:
- a **single server**: the service facility has the capability to serve one customer at a time, waiting customers will stay in the buffer until chosen for service; how the next customer is chosen will depend on the service discipline.

- an **infinite server**: there are always at least as many servers as there are customers, so that each customer can have a dedicated server as soon as it arrives in the facility. There is no queueing, (and no buffer) in such facilities.

- **multiple server**: it is between the two previous extrema. There are a fixed number of $c$ servers, each of which can service a customer at any time. If the number of customers in the facility is **less than or equal to $c$**, there will be **no queueing**.

---

> Instead, if there are **more than $c$ customers**, the additional customers will have to wait in the buffer.

#### Queue

If jobs exceed the capacity of parallel processing of the system, they are forced to wait queueing in a buffer.
If the buffer **has finite capacity**, there are two alternatives for when the buffer becomes **full**:
- the fact that the facility is full is passed back to the arrival process and **arrivals are suspended** until the facility has spare capacity, i.e. a customer leaves;
- or, arrivals continue and arriving **customers are lost** (turned away) until the facility has spare capacity again.

If the buffer capacity is so large that it never affects the behavior of the customers, it is assumed to be **infinite**.

When one of the jobs currently in service leaves the system, one of the jobs in the queue can enter the now free service center. **Service discipline** determines which of the jobs in the queue will be selected to start its service.

#### Service discipline

When more than one customer is waiting for service, we need a rule for selecting which of the waiting customers will be the next one to gain access to a server.

---

The **most commonly used service disciplines** are:
- **First-Come-First-Serve** (**FCFS**) (a.k.a. First-In-First-Out (FIFO));
- **Last-Come-First-Serve** (**LCFS**) (a.k.a. Last-In-First-Out (LIFO));
- **Random-Selection-for-Service** (**RSS**);
- **PRIority** (**PRIs**): the assignment of different priorities to elements of a population is one way in which classes are formed.

#### Population

The characteristic of the population which we are interested in is usually the **size**. Clearly, if the size of the population is **fixed**, at some value $N$, no more than $N$ customers will ever be requiring service at any time.
When the population is finite, the arrival rate of customers will be affected by the number who are already in the service facility (e.g. zero arrivals when all $N$ customers are already in the facility).
When the size of the population is so large that there is no perceptible impact on the arrival process, we assume that the population is **infinite**.

Ideally, members of the population are indistinguishable from each other. When this is not the case, we divide the population into **classes** whose members all exhibit the same behavior. Different classes **differ** in one or more characteristics, for example, arrival rate, service demand, etc. .

---

Identifying different classes is a **workload characterization** task.

### Queueing networks

For many systems we can adopt a view of the system as a collection of resources and devices with customers or jobs circulating between them.
We can associate a service center with each resource in the system and then route customers among the service centers. After service at one service center, a customer may progress to other service centers, following some previously defined pattern of behavior, corresponding ot the customer's requirements.

A queueing network can be represented as a graph where nodes represent the service centers $k$ and arcs the possible transitions of users from one service center to another. Nodes and arcs together define the network topology.

A network may be:
- **open**: customers may arrive from, or depart to, some external environment;
- **closed**: a fixed population of customers remain within the system;
- **mixed**: there are classes of customers within the system exhibiting open and closed pattern of behavior respectively.

---

_Open models_ are characterized by _arrivals_ and _departures_ from the system.
In _closed models_ we have a parameter $N$ that accounts for the fixed population of jobs that continuously circulate inside the system.

Whenever a job, after finishing service at a station has possible alternative routs, an appropriate selection policy must be defined. The policy that describes how the next destination is selected is called routing. Routing specification is required only in all the points where jobs exiting a stations can have more than one destination.

The main routing algorithms that _we will consider_ are:
- **probabilistic**: each path has assigned a probability of being chosen by the job that left the considered station;
- **round robin**: the destination chosen by the job rotates among all the possible exits;
- **join the shortest queue**: jobs can query the queue length of the possible destinations, and choose to move to the one with the smallest number of jobs waiting to be served.

### Operational laws

**Operational laws** are simple equations which may be used as an abstract representation or model of the **average** behavior of **almost any** system.

---

The laws are very **general** and make almost **no assumptions** about the behavior of the random variables characterizing the system. Another advantage is their **simplicity**: they can be applied quickly and easily.

Operational laws are based on observable variables, values which we could derive from watching a system over a finite period of time.
We assume that the system receives **requests** from its environment.
Each request generates a **job** or **customer** within the system.
When the job has been processed, the system responds to the environment with the completion of the corresponding request.

If we observed such an abstract system, we might measure the following quantities:
- $T$: the length of **time** we observe the system;
- $A$: the number of request **arrivals** we observe;
- $C$: the number of request **completions** we observe;
- $B$: the total amount of time during which the system is **busy** ($B \leq T$);
- $N$: the average **number of jobs** in the system.

From these observed values, we can derive the following four important quantities:
- $\lambda = \frac{A}{T}$: the **arrival** rate;
- $X = \frac{C}{T}$: the **throughput** or **completion rate**;

---

- $U = \frac{B}{T}$: the **utilization**;
- $S = \frac{B}{C}$: the **mean service time** per completed job.

We will assume that the system is job flow balanced. This means that the number of arrivals is equal to the number of completions during an observation period, i.e., $A = C$.
This is a testable assumption because an analyst can always test whether the assumption holds. It can be strictly satisfied by careful choice of measurement interval.

Note that if the system is job flow balanced, the arrival rate will be the same as the throughput, that is:
$$
\lambda = X.
$$

A **system** may be regarded as being made up of a number of devices or **resources**. Each of these may be treated as a **system** in its own right from the perspective of operational laws.
An **external request** generates a job within the system: this **job** may then **circulate** between the resources until all necessary processing has been done; as it arrives at each resource it is treated as a request, generating a hob internal to that resource.

We can redefine the observed quantities, differentiating between each subsystem:
- $T$: the length of **time** we observe the system (same for all subsystems);
- $A_k$: the number of request **arrivals** we observe for resource $k$;

---

- $C_k$: the number of request **completions** we observe at resource $k$;
- $B_k$: the total amount of time during which the resource $k$ is **busy** ($B_k \leq T$);
- $N_k$: the average **number of jobs** in the resource $k$ (queueing or being served).

From these observed values we can derive the following four important quantities for resource $k$:
- $\lambda_k = \frac{A_k}{T}$ is the **arrival rate** at resource $k$;
- $X_k = \frac{C_k}{T}$ is the **throughput** or **completion rate** of resource $k$;
- $U_k = \frac{B_k}{T}$ is the **utilization** of resource $k$;
- $S_k = \frac{B_k}{C_k}$ is the **mean service time** per completed job of resource $k$.

#### Utilization law

**Utilization law** links together the throughput, the utilization, and the service time of a resource.
In particular:
$$
U_k = \frac{B_k}{T} = \frac{C_k}{T} \frac{B_k}{C_k} = X_k S_k.
$$

#### Little's law

**Little's law** links together the throughput, the average number of requests in the system, and the response time:
$$
N = X R.
$$

---

If the system throughput is $X \left[ \frac{\text{requests}}{s} \right]$, and each **request remains in the system on average for $R$ seconds**, then for each unit of time, we can observe on average $X R$ requests in the system.

Let's derive it. Consider a plane with the time on the $x$-axis, subdivided in $T$ slots, and the number of jobs on the $y$-axis, subdivided in $C$ slots. On this plane we can plot the **total arrivals** $A(t)$ over time, and the **total completions** $C(t)$ over time.
Of course $C(t) \leq A(t)$ for all $t \in \{ 1, \ldots, T \}$. $C(T) = C$, $A(T) = A$ (_and $A = C$ because of the job flow balance assumption_).
Observe that $A(t) - C(t)$ is the number of requests that the system is processing in time slot $t$. Now let $W$ be the are between $A(t)$ and $C(t)$.
That is:
$$
W = \sum_{t=1}^T (A(t) - C(t)) \Delta t.
$$
$W$ denotes the accumulated time in the system, measured in $\text{requests} \cdot s$.
$\frac{W}{T} = \frac{\sum_{t=1}^T (A(t) - C(t)) \Delta t}{\sum_{t=1}^T \Delta t}$ is the sample mean of the number of requests in each time slot, that is:
$$
N = \frac{W}{T}.
$$

---

$\frac{W}{C}$ coincides with the sample mean of the residence time of each request (remember that $C = A$ is the number of requests), that is:
$$
R = \frac{W}{C}.
$$

Finally, it follows, that:
$$
N = \frac{W}{T} = \frac{C}{T} \frac{W}{C} = X R.
$$

We can apply Little's law to every subsystem and to the whole system.

#### Interactive Response Time law

**Interactive Response Time law** applies to a special class of closed model, known as interactive systems. In an interactive system we distinguish between the users, modeled as infinite servers (we will explain in a moment why) and the actual computer system used by them.
We assume that the users, after performing a request, they wait to receive and process the response before submitting another request. Hence, incoming responses to the users have never to queue, this is why we can model them as infinite servers.

On average the users take $Z$, known as the **think time**, to process a request.

---

In this context, we denote with **response time $R$**, the time that a user has to wait before receiving a response.
Then, the actual residence time of a request in the system (which comprises both the users and the actual computer system) is $R + Z$: this is the one that we must use in Little's law. That is:
$$
N = X(R+Z)
$$
where $N$ is the number of users, and $X$ is the throughput of the system.
This is the **Interactive Response Time law**, usually expressed as:
$$
R = \frac{N}{X} - Z.
$$

#### Visits and forced flow law

In an observation interval, we can count not only completions external to the system, but also the number of completions at each resource within the system.
Let $C_k$ be the number of completions at resource $k$. We define the **visit count** $V_k$ of the $k$-th resource to be the ratio of the number of completions at that resource to the number of system completions:
$$
V_k = \frac{C_k}{C}.
$$

---

Note that:
- If $C_k > C$, resource $k$ is visited several times (on average) during each system level request. This happens when there are loops in the model.
- If $C_k < C$, resource $k$ might not be visited during each system level request. This can happen if there are alternatives.
- If $C_k = C$, resource $k$ is visited (on average) exactly once every request.

The **forced flow** law captures the relationship between the different components within a system. It states that the throughputs or flows, in all parts of a syste must be proportional to one another:
$$
X_k = \frac{C_k}{T} = \frac{C_k}{C} \frac{C}{T} = V_k X.
$$
The throughput at the $k$-th resource is equal to the product of the throughput of the system and the visit count at that resource.

#### Demand and utilization law

The total amount of service that a system job generates at the $k$-th resource is called the **service demand $D_k$**:
$$
D_k = S_k V_k.
$$

We can use this quantity to compute the utilization of the resource $k$.

---

In particular, this provides another version of the utilization law:
$$
U_k = \frac{B_k}{T} = \frac{C_k}{C} \frac{B_k}{C_k} \frac{C}{T} = V_k S_k X = D_k X.
$$

**Remark**:
- The average service time $S_k$ accounts for the average time that a job spends in station $k$ when it is served.
- The average service demand $D_k$ accounts for the average time a job spends in station $k$ during its staying in the system. As seen for the visits, depending on the way in which the jobs move in the system, the demand can be less than, greater than, or equal to the average service time of station $k$.

#### Response and Residence time

When considering nodes characterized by visits different from one, we can define two permanence times:
- response time $\tilde{R}_k$;
- residence time $R_k$.

The **response time** $\tilde{R}_k$ accounts for the average time spent in station $k$ <u>for the single interaction</u>.
The **residence time** $R_k$ accounts instead for the **average time spent by a job at station $k$ during the staying** in the system: it can be greater or smaller than the response time depending on the number of visits.

---

Note that there is the same relation between residence time and response time as the one between demand and service time:
$$
R_k = V_k \tilde{R}_k.
$$

Also observe that for single queue open system, or tandem models, $V_k = 1$ for every $k$. This is implies that the average service time and service demand are equal, and the same holds for response time and residence time.

#### General response time law

One method of computing the mean response time per job in a system is to apply Little's law to the system as a whole.
However, if the mean number of jobs in the system, $N$, or the system level throughput, $X$, are not known, an alternative method can be used.

Applying Little's law to the $k$-th resource we see that $N_k = X_k \tilde{R}_k$, where $N_k$ is the mean number of jobs at the resource and $\tilde{R}_k$ is the average time spent at the resource for a single interaction (usual Little's law).

From the Forced Flow Law we know that $X_k = X V_k$. Thus.
$$
\frac{N_k}{X} = \frac{X_k \tilde{R}_k}{X} = V_k \tilde{R}_k = R_k.
$$

---

The total number of jobs in the system is clearly the sum of the number of jobs at each resource, i.e.: $N = N_1 + \ldots + N_K$ if there are $K$ resources.
From Little's law, $R = \frac{N}{X}$.
Hence:
$$
R = \frac{N}{X} = \sum_{k=1}^K \frac{N_k}{X} = \sum_{k=1}^K R_k.
$$
This is known as **General Response Time law**.

The average response time of a job in the system is the sum of the resources residence time.

### Performance bounds

**Performance bound** provide valuable insights into the **primary factors** affecting the performance of computer systems. Can be computed **quickly** and **easily** therefore serve as a first cut modelling technique.
They allows to treat several alternatives together.

In particular we will do **bounding analysis**. We will consider single class systems only, and determine **asymptotic bounds** which are **upper** and **lower bounds** on the system's performance indices $X$ and $R$. In our case, we will treat the bounds on $X$ and $R$ as a function of the **number of users** $N$ or the **arrival rate** $\lambda$.
Bounding analysis can highlight and quantify the critical influence of the system **bottleneck**.

---

The resource within a system which has the greatest service demand is known as the bottleneck resource or **bottleneck** device, and its service demand is $D_\max = \max_k \{ D_k \}$.
The bottleneck resource is important because it limits the possible performance of the system. This will be the resource which has the highest utilization in the system.
Indeed, from utilization law:
$$
U_k = X D_k \leq 1 \text{ iff } X \leq \frac{1}{D_k} \text{ for all } k
$$
hence, $X \leq \frac{1}{D_\max}$.

The bounding analysis makes use of the following parameters:
- $K$: the number of service centers;
- $D$: the sum of the service demands at the centers, so $D = \sum_{k=1}^K D_k$;
- $D_\max$: the largest service demand at any single center;
- $Z$: the average think time, for interactive systems;
- $X$: the system throughput;
- $R$: the system response time.

The bounds are derived considering the extreme conditions of _light_ and _heavy_ loads.
**We assume that**: the service **demand** of a customer at a center does not depend on how many other customers currently are in the system, or at which service centers they are located.

---

#### Open models

In **open models** we have less information than in closed models.

We already calculated a bound on $X$:
$$
X \leq \frac{1}{D_\max}.
$$
Observe that this induces a bound on the arrival rate, in particular, if $\lambda > X$, the queue time of new jobs grows indefinitely: we can't allow it. So it must be $\lambda \leq X$. Hence, a bound on $\lambda$ is given by its saturation value:
$$
\lambda_\text{sat} = \frac{1}{D_\max}.
$$

Now let's compute a bound on $R$. We can have an optimistic bound. In the best case no customer interferes with any other, i.e. we have no queue time. This means that $R_k = D_k$ for every resource (all the time a job spends at a station is service time). Hence, from the General Response Time law:
$$
R = \sum_{k=1}^K R_k = \sum_{k=1}^K D_k = D.
$$
Observe that, since this is an optimistic assumption, this is a lower bound to $R$.

---

Instead, there is no pessimistic bound on $R$.
Let's try to understand why. Fix an arrival rate $\lambda$. Suppose that the customers arrive together in groups of $n$ every $\frac{n}{\lambda}$ time units.
Hence the arrival rate is actually:
$$
\frac{n}{\frac{n}{\lambda}} = \lambda.
$$
Observe that, in this setting, the last customer (once they are put in a queue) has to wait for all the other $n-1$ to be server. Since we can make $n$ as big as we want, there is no upper bound to the response time.

Summarizing we have:
- an **upper bound for $X(\lambda)$**:
$$
X(\lambda) \leq \frac{1}{D_\max};
$$
- a **lower bound for $R(\lambda)$**:
$$
R(\lambda) \geq D.
$$

#### Closed models

We will derive the bounds for $X$ first, then we will convert them into bounds for $R$ thanks to Response Time law.

The **smallest $X$** is obtained when $R$ is the largest.

---

In closed models, the highest possible system response time occurs when each job, at each station, found all the other $N-1$ customers in front of it.
In this case $R = D + (N-1)D = ND$ where $D$ is the time of actual service and $(N-1)D$ is the time in which the job waits for the other $N-1$ to be processed.
Then:
$$
X = \frac{N}{R + Z} = \frac{N}{ND+Z}.
$$
Observe that:
$$
\lim_{N \rightarrow + \infty} \frac{N}{ND + Z} = \frac{1}{D}.
$$

Analogously, the **highest $X$** is obtained when $R$ is the smallest.
In a closed model, the lowest response time can be obtained if a job always finds the queue empty and always starts being served immediately, that is: $R = D$.
In this case:
$$
X = \frac{N}{R+Z} = \frac{N}{D+Z}.
$$

Finally, we always have to keep in mind that:
$$
X \leq \frac{1}{D_\max}.
$$

---

By putting all together, we obtain:
$$
\frac{N}{ND + Z} \leq X(N) \leq \min(\frac{1}{D_\max}, \frac{N}{D+Z}).
$$
Furthermore, we denote with:
$$
N^* = \frac{D+Z}{D_\max}
$$
the population size after which $\frac{1}{D_\max}$ becomes the tightest upper-bound of the throughput.

let's rewrite the previous equation remembering that:
$$
X(N) = \frac{N}{R(N) + Z}.
$$

$$
\frac{N}{ND+Z} \leq \frac{N}{R(N) + Z} \leq \min(\frac{1}{D_\max}, \frac{N}{D+Z}) \text{ iff}
$$
$$
\max(N D_\max, D+Z) \leq R(N) + Z \leq ND + Z \text{ iff}
$$
$$
\max(N D_\max - Z, D) \leq R(N) \leq ND.
$$
