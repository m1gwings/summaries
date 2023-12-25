---
theme: summary
---
# Cypher

<div class="author">

Cristiano Migali

</div>

**Cypher** is **Neo4j**'s declarative query language.
In the following we will provide a (_not comprehensive_) quick guide on how to perform CRUD operations on a Neo4j's DB through Cypher.

## Basic concepts

### Patterns

Cypher is based on the concept of **pattern matching**: we perform queries by providing a pattern that embeds all and only the properties that we want the returned data to satisfy. In the context of graph databases as Neo4j, patterns represent a subgraph or, more in general, a class of subgraphs with certain properties.

#### Nodes

Each **node** in a Neo4j database is characterized by:
- a **label**, and
- some **properties**.

The following patterns allow to characterize nodes:
- `()` matches **any node**;
- `(n)` matches **any node** and **assigns to it the name `n`** (which we can use later in the query);
- `(n: Label)` matches **any node with label `Label`**;
- `(n: Label1:Label2)` matches **any node with both label `Label1` and `Label2`**;
- `(n: Label { property1: value1, ... })` matches **any node with label `Label` which has `property1` with value `value1`, ...**.

#### Relationships

Each **relationship** in a Neo4j database is characterized by:
- a **type** (equivalent to the label of a node),
- some **properties**,
- a **direction**,
- the **two end nodes that it connects**.

The following patterns allow to characterize relationships:
let `n` and `m` be two nodes
- `(n)--(m)` matches **any relationship between `n` and `m`** (without a specified direction);

---

- `(n)-->(m)` matches **any relationship from `n` to `m`** (analogously `(n)<--(m)` matches any relationship from `m` to `n`);
- `(n)-[r]->(m)` matches **any relationship from `n` to `m`** and **assigns to it the name `r`** (which we can use later in the query);
- `(n)-[r: TYPE]->(m)` matches **any relationship from `n` to `m` of type `TYPE`**;
- `(n)-[r: TYPE1|TYPE2]->(m)` matches **any relationship from `n` to `m` either of type `TYPE1` or `TYPE2`**;
- `(n)-[r: TYPE { property1: value1, ... }]->(m)` matches **any relationship from `n` to `m` of type `TYPE` which has `property1` with value `value1`, ...**.

#### Paths and subgraphs

We can combine the patterns for nodes and relationships to build **patterns for** (_generalized_) **paths**, for example:
- `(n: Label1 { propertyOfN1: valueN1, ... })-[r: TYPE1 { propertyOfR1: valueR1, ... }]->(m: Label2 { propertyOfM1: valueM1, ... })<-[s: TYPE2 { propertyOfS1: valueS1, ... }]-(p: Label3 { propertyOfP1: valueP1, ... })`.

Furthermore, through the patterns for paths, we can build **patterns for subgraphs**: we combine several path patterns by separating them with a "`,`", different path patterns are linked by using the same variable name for some nodes, defining a subgraph. For example:
- `(n)-[r1: TYPE1]->(m)-[r2: TYPE2]->(p), (m)-[r3: TYPE3]->(o)`.

We can even express **patterns for variable length paths**:
- `(n)-[*]->(m)` matches any **variable length path of one or more relationships between `(n)` and `(m)`**;
- `(n)-[*..y]->(m)` matches any **variable length path of a number of hops between 1 and `y` from `n` to `m`**;
- `(n)-[x..*]->(m)` matches any **variable length path of a number of hops greater or equal to `x` from `n` to `m`**;
- `(n)-[*x..y]->(m)` matches any **variable length path of a number of hops between `x` and `y` from `n` to `m`**;
- `(n)-[:TYPE*x..y]->(m)` matches any **variable length path of a number of hops between `x` and `y` through relationships of type `TYPE` from `n` to `m`**.
- `(n)-[r: TYPE*x..y WHERE predicate]->(m)` matches any **varibale length path of a number of hops between `x` and `y` through relationships of type `TYPE` from `n` to `m` which satisfy the predicate `predicate`** (_see predicates_).

Finally, we can express also **patterns for the shortest path between two nodes**:
- `shortestPath((n)-[:TYPE*x..y]->(m))` matches any **shortest path of a number of hops between `x` and `y` through relationships of type `TYPE` from `n` to `m`**;
- `allShortestPaths(...)` is analogous to the previous function, with the only difference that returns **all** the shortest paths with a given pattern instead of only one.

---

### Predicates

Given some variables which correspond to nodes or relationships (for example retrieved with pattern matching as we will see later), we can build predicates that evaluate to boolean values.

#### Filtering on labels

The predicate `n: Label` is true iff `n` has the label `Label`.

#### Filtering on properties

We can access the properties of nodes and relationships through the ususal dot notation: `n.property1`.
Then we can compare them with the usual operators: `=`, `<>`, `<`, `>`, `<=`, `>=`, `IS NULL`, `IS NOT NULL`.

#### Filtering on patterns

We can use patterns inside predicates: the semantics is given by **existential quantification**.

#### Compose predicates

We can compose "_atomic_" preidcates through the usual boolean operators: `AND`, `OR`, `XOR`, or `NOT`.

## Read queries

## Create, Update and Delete queries