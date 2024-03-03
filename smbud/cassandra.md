---
marp: true
theme: summary
---
# Cassandra

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Andrea Tocchetti's slides_)

</div>

**Apache Cassandra** is a highly scalable, high performance, distributed database designed to handle large amounts of data, providing high availability with no single point of failure. It's a **column-based** NoSQL database.

To query the data stored within Cassandra, a dedicated query language named **Cassandra Query Language** (**CQL**) was developed.

**CQL** offers a model similar to **MySQL** under many different aspects:
- it is used to query data stored in **tables**;
- each table is made by **rows** and **columns**;
- most of the **operators** are the ones used in MySQL.

**CQL** commands and queries can either be run in the console or by reading a textual file with the corresponding command.

## Managing "keyspaces" and tables

### Create a keyspace

The **first operation** to perform before creating a table is **creating the keyspace**. A keyspace is the **outermost** container in Cassandra.

Keyspaces are created using the **`CREATE KEYSPACE`** command:

<div class="algorithm">

```
    CREATE KEYSPACE <keyspace_name> WITH <properties>;
```

</div>

An example of `<properties>` is `replication = { "class": "SimpleStrategy", "replication_factor": 2 }`.

### Inspect properties

The **`DESCRIBE`** command can be used to check whether a keyspace (or a table) has been correctly created:

<div class="algorithm">

```
    DESCRIBE keyspaces;
```

</div>

It can also be applied to other elements.

---

### Use a keyspace

To be able to perform the operations on the tables, we must choose in which keyspace we want to work. The command **`USE`** covers such need:

<div class="algorithm">

```
    USE <keyspace_name>;
```

</div>

### Delete or modify a keyspace

Keyspaces can be also modified (with **`ALTER`**) and deleted (with **`DROP`**); the syntax is the following:

<div class="algorithm">

```
    ALTER KEYSPACE <keyspace_name> WITH <properties>;
```

</div>

and

<div class="algorithm">

```
    DROP KEYSPACE <keyspace_name>;
```

</div>

### Create a table

We can create tables through the **`CREATE`** command:

<div class="algorithm">

```
    CREATE TABLE <table_name> (
        <column_definition>,
        <column_definition>,
        ...,
        PRIMARY KEY (<column_name>, <column_name>, ...)
    );
```

</div>

We can also **include some options** by using **`WITH <options>`**.

The **definition of the columns** has the following syntax:

<div class="algorithm">

```
    <column_name> <column_type>
```

</div>

Among the **available types** there are:
- **`boolean`**;
- **`date`**;
- **`double`**;
- **`duration`**;
- **`float`**;
- **`int`**;
- **`text`**;

---

- **`time`** (time without corresponding date value);
- **`timestamp`** (time + date);
- **`uuid`** (when inserting data, we can use the **`uuid()`** function).

> **Important remark**: when creating the **`PRIMARY KEY`** of the table with the syntax that we showed above, the columns that you put in the **`PRIMARY KEY`** statement have different meaning depending on the order and the brackets (if present).
The **first value** (or **set of values if using round brackets**) is named **partition key**. It defines the way in which the data is partitioned within the cassandra nodes. All the values after the first (or the first set of values sorrounded by brackets) are named **clustering keys**. They are used to define the way in which the data is stored within a partition (that is, the sorting).


> **Remark**: when creating a table, **clustering keys can be used to define an ordering**:

<div class="algorithm">

```
    CREATE TABLE <table_name> ( ... )
    WITH CLUSTERING ORDER BY (<clustering_key> ASC, <clustering_key> DESC, ...)
```

</div>

### Modify a table

Tables can be also modified through the **`ALTER`** command:

<div class="algorithm">

```
    ALTER TABLE <table_name> <instructions>;
```

</div>

For example we can **add a new column**:

<div class="algorithm">

```
    ALTER TABLE <table_name> ADD <column_name> <column_type>;
```

</div>

or **remove a column**:

<div class="algorithm">

```
    ALTER TABLE <table_name> DROP <column_name>;
```

</div>

### Delete and empty a table

Tables can be also **deleted through** the **`DROP`** command:

<div class="algorithm">

```
    DROP TABLE <table_name>;
```

</div>

Rather than deleting the table, it is possible to **empty it** through the **`TRUNCATE`** command:

<div class="algorithm">

```
    TRUNCATE TABLE <table_name>;
```

</div>

---

### Create and delete a secondary index

**Indexes** are one of the most important elements in Cassandra: as we will see later, inside queries, we can "filter" only w.r.t. **columns which are included in the primary key or have a secondary index**.
**Secondary indexes** are **created** with the following command:

<div class="algorithm">

```
    CREATE INDEX <index_name>
    ON <table_name> (<column_name>);
```

</div>

Indexes can also be **deleted** through the **`DROP`** command:

<div class="algorithm">

```
    DROP INDEX <index_name>;
```

</div>

## CRUD operations

### Insert data

We can insert data into a table with the **`INSERT`** command:

<div class="algorithm">

```
    INSERT INTO <table_name>(<column_name>, <column_name>, ...)
    VALUES (<value>, <value>, ...)
    USING <option>;
```

</div>

(_The `<option>` part is NOT mandatory_).

### Retrieve data

We can retrieve data from tables with the usual SQL query syntax:

<div class="algorithm">

```
    SELECT <column_name>, <column_name>, ...
    FROM <table_name>
    WHERE <conditions>;
```

</div>

> **Important remark**: As we mentioned earlier when talking about indexes, we can filter only w.r.t. columns which are part of the primary key or have a secondary index; that is, we can put inside the `WHERE` clause's condition only such columns.

---

### Update data

We can update tuples in our database with the **`UPDATE`** command:

<div class="algorithm">

```
    UPDATE <table_name>
    SET <column_name> = <new_value>, ...
    WHERE <condition>;
```

</div>

### Delete data

We can delete tuples in our database with the **`DELETE`** command:

<div class="algorithm">

```
    DELETE
    FROM <table_name>
    WHERE <condition>;
```

</div>

> **Important remark**: **also** when using the **`UPDATE`** and **`DELETE`** command, we can put inside the `WHERE` clause **only columns which are part of the primary key or have an index**.

> **Remark**: a set of insert, update, and delete operations can be organized in a batch, allowing them to be executed one after another as a single command. The syntax is:

<div class="algorithm">

```
    BEGIN BATCH
        <insert_statement>;
        <update_statement>;
        <delete_statement>;
    APPLY BATCH;
```

</div>

## "Advanced" stuff

### `CAPTURE` and `EXPAND`

When the amount of data within a database grows, it can be really tough to visualize it with a terminal. Fortunately, Cassandra provides us with a few commands to overcome this problem.

The **`CAPTURE`** command followed by a path allows to store outputs in a text file. The syntax is:

<div class="algorithm">

```
    CAPTURE path/to/file.txt;
```

</div>

---

To **interrupt `CAPTURE`** you can run the following command:

<div class="algorithm">

```
    CAPTURE off;
```

</div>

The **`EXPAND`** command provides extended outputs within the console when performing queries. It must be executed before the query to enable it:

<div class="algorithm">

```
    EXPAND on;
```

</div>

To **interrupt the `EXPAND`** you can run the following command:

<div class="algorithm">

```
    EXPAND off;
```

</div>

### `SOURCE`

The **`SOURCE`** command allows you to run queries from textual files. The command accepts the path to the file with the query:

<div class="algorithm">

```
    SOURCE path/to/query.txt;
```

</div>

### Collections

Cassandra supports **fields which have a collection as a value**.
The syntax to **define a "collection" field** is pretty easy:

<div class="algorithm">

```
    CREATE TABLE <table_name> (
        <collection_column_name> list<type>,
        ...
    )
```

</div>

(_for example `email list<text>`_).

It is also easy to **update a collection**:

<div class="algorithm">

```
    UPDATE <table_name> SET <collection_column_name> = <collection_column_name> + [ ... ]
    WHERE ...
```

</div>

---

### User-defined data types

When it comes to user-defined data types the complexity increases, as it is necessary to **define the data type** before using it:

<div class="algorithm">

```
    CREATE TYPE <type_name> (
        <column_definition>,
        <column_definition>,
        ...
    );
```

</div>

To check that the new type has been properly created, you can use the **`DESCRIBE`** operator. User-defined data types support also the **`ALTER`** and **`DROP`** operations.

> **Important remark**: when using a user-defined data type it is necessary to use the **`frozen`** keyword: `frozen<user_defined_data_type>`. A frozen data type can only be overwritten, it can't be edited anymore.