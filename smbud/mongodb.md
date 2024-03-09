---
marp: true
theme: summary
math: mathjax
---
# MongoDB

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Andrea Tocchetti's slides_)

</div>

**MongoDB** is a document-oriented database that stores data **within collections**, as **documents**.
- **Documents** consist of key-value pairs which are the basic unit of data in MongoDB.
- **Collections** contain sets of documents.
- **Databases** are made by one or more collections.

## Document structure

MongoDB's documents are defined through JSON. We're free to structure the document as we prefer, except for the fact that **every document must have an `_id` field which identifies it univocally** (if we don't specify one, it is automatically added by MongoDB):

```
{
    _id: ObjectId("..."),
    ...
}
```

### The `ObjectId` type

`ObjectId` is the type associated with the `_id` field.
It is a 12-byte value which consists of three different elements:
- a **4-byte timestamp value** which corresponds to the **creation time of the document** and is measured in seconds since the Unix epoch;
- a **4-byte random value** generate once **per process**. This random value is (_hopefully_) unique to the machine and process;
- a **3-byte incrementing counter**, initialized to a random value.

## Create documents

- **A document can be added** to a collection using the **`insertOne({ ... })`** method.

- **Multiple documents can be added** using the **`insertMany([ { ... }, { ... }, ... ])`** method.

**These methods are defined on a collection object**, the **full syntax** is: `db.collection_name.insertOne({ ... })` (_analogous for `insertMany`_).

---

## Create indexes

**Indexes** are data structures that **store** a small portion of the collection's data set in an easy to traverse form, ordered by the value of the field. **Indexes** support the efficient execution of some types of queries.

- **They are created with** the **`createIndex`** operator, which accepts a list of the fields with respect to which create the index and their corresponding ordering, that is, **ascending (1)** or **descending(-1)**.

The **full syntax** is: `db.collection_name.createIndex( { field1: 1, field2: -1, ... } )`.

## Collect documents & Filtering

- **A document can be collected** using the **`findOne(filter)`** method. It collect the first document that satisfies the conditions defined in `filter` (we will see in a moment the syntax for defining filters).

- **Multiple documents can be collected** using the **`find(filter)`** method. It behaves exactly like its individual counterpart, although it collects all the documents rather than the first one.

The **full syntax** is: `db.collection_name.find(filter)`.

- Whenever it is necessary to **return the number of documents in a collection that satisfy a certain filter**, the **`countDocuments(filter)`** method can be applied.

### Filters

MongoDB filters are based on **pattern matching**. **The simplest filter** is:
```
{
    field1: value1,
    field2: value2,
    ...
}
```
which matches all the documents which have `field1` with `value1`, `field2` with `value2`, ... .

> **Important remark**: filtering operations may behave differently based on the type of complex field they are accessing (that is, subdocuments and arrays). Queries evaluating one or more conditions on the fields of a **subdocument** are **not subject to any particular behavior change**. **On the other hand**, queries evaluating a **single condition** on an **array** field will return the **main document** if **at least one** of the documents (_they could also be simple objects_) in the array satisfies the condition. This happens when we write: `{ ...  arrayField: scalarValue ... }` (_for an array which does not contain documents_) or `{ ... arrayField.elementField: scalarValue ... }` (_for an array of subdocuments_) (_cont'd_).

---

> (_cont'd_) Whenever **multiple** conditions are evaluated on the documents in an **array** field, they will be assessed individually on the array's documents, hence returning the main document if, **for each condition**, there exists **at least one** document that satisfies it. It doesn't matter whether there's **only one** document satisfying all conditions or **multiple** documents satisfying one each. This happens when we write: `{ ... arrayField.elementField1: scalarValue1, arrayField.elementField2: scalarValue2 ... }`.
Whenever a query is targeted at evaluating **multiple** conditions on the fields of the **same** document of an **array**, it is necessary to apply the **`$elemMatch`** operator. In particular, it matches documents containing an array field with **at least one** document that **satisfies all** the specified query criteria. **The syntax** is:
```
{
    ...
    arrayField: { $elemMatch: { elementField1: scalarValue1, elementField2: scalarValue2 } }
    ...
}
```

#### Comparison query operators

We can perform different kinds of comparisons (not only equality checking) through **comparison operators**. **The syntax** is:
```
{
    field1: { operator1: value1 },
    field2: { operator2: value2 },
    ...
}
```

The **available operators** are:
- **`$eq`**: matches values **equal** to a specified value (_we can directly use the simpler syntax intorduced before_);
- **`$gt`** (**`$gte`**): matches values **greater** (**greater or equal**) than a specified value;
- **`$lt`** (**`$lte`**): matches values **smaller** (**smaller or equal**) than a specified value;
- **`$in`**: matches any of the values specified **in an array** (_the full syntax is `... field: { $in: [ ..., ... ] } ...`_);
- **`$ne`**: matches value **not equal** to a specified value;
- **`$nin`**: matches values **not contained in** a specified array.

#### Element query operators

MongoDB supports a few **element query operators**, namely:
- **`$exists`**: matches documents **with a specified field**;
- **`$type`**: matches documents whose chosen field **is of a specified type**.

**The syntax** is analogous:
```
...
field: { $exists: true }
...
```

---

and
```
...
field: { $type: "type" }
...
```

#### Evaluation query operators

MongoDB supports multiple **evaluation query operators**, namely:
- **`$text`**: matches documents based on **text search** on indexed fields;
- **`$regex`**: matches documents based on a **specified regular expression**;
- **`$where`**: matches documents based on a **JavaScript expression**.

Also in this case the **syntax is the usual one**.

#### Logical query operators

MongoDB allows to define complex filters by combining them through logical operators.
**The syntax** is:
```
{
    logicalOperator: [
        filter1,
        filter2,
        ...
    ]
}
```
where `filteri` can be a "simple" pattern matching filter as the ones that we've explained before or a "composed" filter (_that is we can compose logical operators_). In the case of **unary operators** the syntax is a even simpler:
```
{
    logicalUnaryOperator: filter
}
```

The supported **logical query operators** are:
- **`$and`**;
- **`$not`**;
- **`$nor`**;
- **`$or`**.

(_The semantics is the ususal_).

### Projections

When collecting documents, it is possible to restrict, explicit, or expand the fields to be returned through **projections**. They are list of key-value pairs made by the field name and a boolean value representing whether the field **will be returned** (**1**) or **not** (**0**).

---

Whenever a list specifies a subset of fields **to be** returned, the other ones won't be returned. Conversely, whenever a list specifies a subset of fields **not to be** returned, the other ones will be returned by default.
For example:
```
{
    fieldN1: 1,
    fieldN2: 1,
    ...
}
```
specifies that only fields `fieldNi` are to be returned, while:
```
{
    fieldN1: 0,
    fieldN2: 0,
    ...
}
```
specifies that all the fields except for `fieldNi` are to be returned.
**The syntax** is: `db.collection_name.find(filter, projection)`.

Furthermore, it is possible to shape projections **create new fields**, the syntax is:
```
{
    ...
    newField: expression
    ...
}
```

### Sort & Limit

When collecting documents, it is possible to sort and limit the results. These operations can be performed through the **`sort`** and **`limit`** methods.

The **`sort`** method accepts a list of fields and their ordering, that is, **descending** (**-1**) and **ascending** (**1**). The earlier a field is referenced, the more relevant it is for ordering.

The **`limit`** method accepts a number representing the **number of elements to collect**.

Possible **syntaxes** are: `db.collection_name.find(...).sort({ field1: 1, field2: 1 })`, `db.collection_name.find(...).limit(n)`, `db.collection_name.find(...).sort(...).limit(...)`.

### Aggregations

The **`aggregate`** method allows to apply a pipeline of operations to a MongoDB collection: the output of an operation is the input to the next. Through this pipeline we can perform all the operations that we've already discussed (filtering, projecting, sorting, ...), but also aggregations and more complex operations.
**The syntax** is:
```
db.collection_name.aggregate([
    { pipelineOperator1: ... },
    { pipelineOperator2: ... },
    ...
])
```

---

The **available "pipeline" operators** are:
- **`$unwind`**: we can apply the `$unwind` operator to collections of documents which have an array of subdocuments, it shapes the collection so that **each** document is **replaced with a set of new ones**, that is, **one for each subdocument in the array** (_on which the unwind stage is applied_). These documents contain all the fields from the main one and a field with the name of the array field that contains one of its documents. **The syntax** is: `{ $unwind: { path: "$arrayField" } }`, **the `$` is required**.

- **`$group`**: `$group` allows to perform aggregations. **The syntaxes** are:
```
{
    $group: {
        _id: "$field",
        newField1: { accumulator: "$otherField" },
        ...
    }
}
```
> if we want to **group by a single field** (_**all the `$` are required**_);
```
{
    $group: {
        _id: { field1: "$field1", field2: "$field2", ... },
        newField1: { accumulator: "$otherField" },
        ...
    }
}
```
> if we want to **group by multiple fields** (_**all the `$` are required**_);
```
{
    $group: {
        _id: scalarValue,
        newField1: { accumulator: "$otherField" },
        ...
    }
}
```
> if we want to **group everything together**.

> Possible **accumulators** are:
> - **`$addToSet`**;
> - **`$avg`**;
> - **`$sum`**;
> - **`$max`**;
> - **`$min`**.

- **`$sort`**: the **syntax** is `{ $sort: howToSort }` where `howToSort` is an object defined as we've explained for the `sort` method.

- **`$limit`**: the **syntax** is `{ $limit: n }`.

- **`$match`**: allows to perform the filtering, the **syntax** is `{ $match: fitler }` where `filter` is a filter object like the ones that we've explained for the `find` method.

---

- **`$project`**: allows to perform the projections, the **syntax** is `{ $project: projection }` where `projection` is a projection object like the ones that we've explained for the `find` method.

## Update documents

**A document** can be **updated** using the **`$updateOne`** method. It collects the documents that satisfy the conditions defined by a `filter` and updates the first one according to a list of comma-separated fields' updates.

**Multiple documents** can be updated using the **`$updateMany`** method. It behaves exactly like its individual counterpart, although it updates all the collected documents rather than just the first one.

**The syntax** is:
```
db.collection_name.update(
    filter,
    { $set: {
        fieldToUpdate1: expression1,
        fieldToUpdate2: expression2,
        ...
    } }
)
```

## Delete documents

**A document** can be deleted using the **`deleteOne`** method. It collects the documents that satisfy one or more conditions defined in a **`filter`** and deltes the first one found.

**Multiple documents** can be deleted using the **`deleteMany`** method. It behaves exactly like its counterpart, although it deletes all the collected documents.

**The syntax** is:
```
db.collection_name.delete(filter)
```
