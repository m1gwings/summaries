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
Then we can compare them with the usual operators: `=`, `<>`, `<`, `>`, `<=`, `>=`, `IS NULL`, `IS NOT NULL`, **`IN`** (**to check if a value is in a list**). Furthermore, **we can apply the available functions to properties' values**.

#### Filtering on patterns

We can use patterns inside predicates: the semantics is given by **existential quantification**.

#### Compose predicates

We can compose "_atomic_" preidcates through the usual boolean operators: `AND`, `OR`, `XOR`, or `NOT`.

## Queries

A query is made up from several clauses chained together. (_Some of these will be discussed more in detail later_). The semantics of a whole query is defined by the semantics of its clauses. Each clause has as input **the state of the graph** and a **table of intermediate results** consisting of the current variables. The output of a clause is a new state of the graph and a new table of intermediate results, serving as input to the next clause. The first clause takes as input the state of the graph before the query and an empty table of intermediate results. The output of the last clause is the result of the query.

### Read queries

Read queries (_usually_) start with a `MATCH` clause and must end with a `RETURN` clause.

#### `MATCH` + `WHERE`

The `MATCH` clause allows you to specify the patterns Neo4j will search for in the database. The syntax is `MATCH pattern` where `pattern` is a pattern of the ones that we've described before. This clause won't touch the structure of the graph. 

---

The intermediate results produced will be, for each variable in the pattern, the set of values that we can assign to them in order to match the pattern.

If the `MATCH` clause that we're writing is not the first in the query, we can use the variables in the intermediate results (provided by the previous clause) inside the pattern. The semantics is the following: for each possible value of the variables in the intermediate results, we perform a `MATCH` with the pattern obtained by substituting such values to the corresponding variables; at the end we merge all the obtained intermediate results.

`MATCH` clauses are often followed by a `WHERE` clause. The syntax is the following: `MATCH pattern WHERE predicate` where `predicate` is a predicate built with the operators that we described before. In this setting the `WHERE` clause has to be intended as part of the `MATCH` clause: the predicate allows to complete the pattern that we want to describe.

> **Remark**: in a `MATCH` clause we can define variables whose values are the paths which match a certain pattern; the syntax is the following: `MATCH p1 = path_pattern1, p2 = ...`.

##### `OPTIONAL MATCH`

`OPTIONAL MATCH` matches patterns against a graph database, just as `MATCH` does. The difference is that if no matches are found, `OPTIONAL MATCH` will use a `null` for missing parts of the pattern. If `OPTIONAL MATCH` is followed by a `WHERE` clause (_as we remarked previously_), the corresponding predicate is part of the pattern description.

#### `RETURN`

The `RETURN` clause defines the parts of a pattern (nodes, relationships, and/or properties) to be included in the query result.
It must be the **last clause of a query**.

We can:
- **return nodes**: `RETURN n`;
- **return relationships**: `RETURN type(r)`,
- **return properties**: `RETURN n.property`;
- **return all elements**: `RETURN *`;
- **specify column aliases**: `RETURN n.property AS alias`;
- **return other expessions defined through the operators and functions available in Cypher**, in particular we can perform aggregations (_take a look at the available functions_);
- **return unique results**: `RETURN DISTINCT ...`.

#### `WITH`

The `WITH` clause allows query parts to be chained together, piping the results from one to be used as starting points or criteria in the next. It behaves (analogous syntax) as `RETURN` but we are not forced to put it as the last clause.

---

It is useful when we want to perform some sort of computation (usually aggregations) on the intermediate values before feeding them to the next clause.

> **Important remark**: as `RETURN`, `WITH` performs a projection on the intermediate results, that is, all the variables whose name is not in the list of things returned by `WHIT` are discarded; we can use the `*` wildcard if we don't want to lose anything.

#### `WHERE`

The `WHERE` clause is not a clause in its own right, rather, it is part of the `MATCH`. `OPTIONAL MATCH`, and `WITH` clauses.

When used with `MATCH` and `OPTIONAL MATCH`, `WHERE` adds constraints to the patterns described. _It should not be seen as a filter after the matching is finished_.

In the case of `WITH`, however, `WHERE` simply filters the results (the syntax is the usual: `WHERE predicate`).

#### `ORDER BY`

`ORDER BY` is a sub-clause **following `RETURN` or `WITH`**, and it specifies how the output of a clause should be sorted.
We can:
- **order nodes by a property**: `ORDER BY n.property`;
- **order nodes by multiple properties**: `ORDER BY n.property1, n.property2`;
- **order nodes depending on the value of an expression**;
- **order nodes in descending order**: `ORDER BY n.property DESC`.

#### `SKIP & LIMIT`

By using `SKIP`, the intermediate results will get trimmed from the top. The syntax is the following: `SKIP N` where `N` is the number of "rows" in the intermediate results that we want to skip.

`LIMIT` constrains the number of returned rows. It accepts any expression that evaluates to a positive integer and does not refer to nodes or relationships.

#### `UNION` 

`UNION` combines the results of two or more queries into a single result set that includes all the rows that belong to any queries in the union.

The number and the names of the columns must be identical in all queries combined by using `UNION`. To keep all the result rows, use `UNION ALL`. Using just `UNION` will combine and remove duplicates from the result set. The syntax is `query1 UNION query2`.

---

### Create, Update and Delete queries

#### `CREATE`

The `CREATE` clause allows you to crate nodes and relationships. To define these entities, `CREATE` uses a syntax similar to that of `MATCH`. However, while patterns only need to evaluate to either true or false, the syntax for `CREATE` needs to specify exactly what nodes and relationships to create.

When we create nodes, each node can be assigned labels and properties. You can bind each node to a variable that you can refer to later in the query. Multiple labels are separated by colons.
For example:
```
CREATE (charlie:Person:Actor {name: 'Charlie Sheen'}),
    (oliver:Person:Director {name: 'Oliver Stone'})
```

Relationships can also be created using the `CREATE` clause. Unlike nodes, relationships always need exactly one relationship type and a direction. Similar to nodes, relationships can be assigned properties and relationship types and be bound to variables.
For example:
```
CREATE (charlie:Person:Actor {name: 'Charlie Sheen'})-[:ACTED_IN {role: 'Bud Fox'}]->
    (wallStreet:Movie {title: 'Wall Street'})
        <-[:DIRECTED]-(oliver:Person:Director {name: 'Oliver Stone'})
```


#### `DELETE`

The `DELETE` clause is used to delete nodes, relationships or paths.
It is not possible to delete nodes with relationships connected to them without also deleting the relationships. This can be done by either explicitly deleting specific relationships, or by using the `DETACH DELETE` clause.

We can:
- **delete a single node**: `DELETE n`;
- **delete relationships only**: `DELETE r`;
- **delete a node with all its relationships**: `DETACH DELETE n`.

#### `SET`

The `SET` clause is used to update labels on nodes and properties on nodes and relationships.

We can:
- **set properties**: `SET n.property1 = value1, n.property2 = value2, ...`;
- **assign labels**: `SET n:Label1:Label2:...`.

---

#### `REMOVE`

The `REMOVE` clause is used to remove properties from nodes and relationships, and to remove labels from nodes.

We can:
- **remove properties**: `REMOVE n.property1, n.property2, ...`;
- **remove labels**: `REMOVE n:Label1:Label2`.

#### `MERGE`

The `MERGE` clause either matches existing node patterns in the graph and binds them or, if not present, creates new data and binds that. In this way, it acts as a combination of `MATCH` and `CREATE` that allows for specific actions depending on whether the specified data was matched or created.

> **Important remark**: when using `MERGE` on full patterns, the behavior is that either the whole pattern matches, or the whole pattern is created. `MERGE` will not partially use existing patterns. If partianl matches are needed, this can be accomplished by splitting a pattern into multiple `MERGE` clauses.

The last part of a `MERGE` clause is the `ON CREATE` and/or `ON MATCH` operators. These allow a query to express additional changes to the properties of a node or relationship, depending on whether the element was matched (`MATCH`) in the database or if it was created (`CREATE`).

The syntax right after `MERGE` is analogous to `CREATE`; `ON CREATE` and `ON MATCH` (if present) are followed by a `SET` clause with the usual syntax.

#### `LOAD CSV`

`LOAD CSV` is used to import data from CSV files.

We can:
- **load a local CSV file**: `LOAD CSV FROM file:///path/to/file AS row`, then we can access the fields with `row[i]`;
- **load a local CSV file with headers**: `LOAD CSV WITH HEADERS FROM file:///path/to/file AS row`, then we can access the fields by their name with `row.field`;
- **load a local CSV file with a custom field delimiter**: `LOAD CSV FROM file:///path/to/file AS row FIELDTERMINATOR ';'`;
- **local a remote CSV file**: `LOAD CSV FROM https://... AS row`.

---

## Functions

Cypher supports several functions which allow for example to do math or manipulate strings.

### Mathematical functions

We will list only some of them: `abs`, `ceil`, `cos`, `exp`, `floor`, `sign`, `sin`.

### Aggregating functions

Aggregating functions can be used inside `RETURN` or `WITH` clauses.

> **Important remark**: the non-aggregating expressions that are in the `RETURN` or `WITH` clauses along with aggregating expressions are treated as **grouping keys**: the intermediate results of the previous clause are grouped according to their value first, then, for each group, the aggregation is performed.

The most important aggregating functions are: `avg(expression)`, `count(expression)`, `sum(expression)`, `max(expression)`, `min(expression)`, `collect(expression)`.
The `collect` function returns a list with all the "aggregated" values.
Some syntactic sugar is available, for example: `count(*)`, `count(DISTINCT *)`.

### Predicate functions

The function `all` returns `true` if the predicate holds for all elements in the given list.
The syntax is `all(variable IN list WHERE predicate)`.
Analogously the functions `any`, `none`, and `single` are defined.

`exists` returns `true` if a match for the given pattern exists in the graph. The syntax is `exists(pattern)`. It can be useful, for example, in a `RETURN` or `WITH` clause.

### Nodes and paths functions

- `labels` returns a `LIST<STRING>` containing the string representations for all the labels of a `NODE`.
- `nodes` returns a `LIST<NODE>` containing all the `NODE` values in a `PATH`. (_Remember that we can bind path pattern to variables in the `MATCH` clause_).
- `relationships` returns a `LIST<RELATIONSHIP>` containing all the `RELATIONSHIP` values in a `PATH`.
- `length` returns the length **of a `PATH`**.

### List functions

- **Pattern comprehension** is a synctactic construct available in Cypher for creating a list based on matchings of a pattern. A pattern comprehension matches the specified pattern like a normal `MATCH` caluse, with predicates like a normal `WHERE` clause, but yields a custom projection as specified.

---

> For example:
```
MATCH (keanu:Person {name: 'Keanu Reeves'})
RETURN [(keanu)-->(b:Movie) WHERE b.title CONTAINS 'Matrix' | b.released] AS years
```

- **List comprehension** is a syntactic construct available in Cypher for creating a list based on existing lists. For example:
```
MATCH (keanu:Person {name:'Keanu Reeves'})
RETURN [x IN keanu.resume WHERE x contains 'The Matrix'] AS matrixList
```

- `size` returns the length of a list (or a string).
