---
theme: summary
---
# Elasticsearch

<div class="author">

Cristiano Migali

</div>

<div class="centered-definition-expression">

(_adapted from Andrea Tocchetti's slides_)

</div>

**Elasticsearch** is a search and analytic engine.

## Indices

Data in Elasticsearch is stored in JSON format and organized into **indices**.

### Shards

The data inside an index is **patitioned into shards**.
**Shards** distribute operations to:
- increase resistance to faults and hardware failuers;
- improve performance;
- increase capacity to serve read requests.

There are two types of shards, namely **primaries** and **replicas**.
Each document in an index belongs to one **primary shard**.
**Replica shards** are copies of primary shards, stored on a different node.

**Write operations** are performed on the primary shard and then on replicas.
**Read operations** are either performed on a primary shard or a replica.

### Mappings

The structure of the documents stored in a certain index is defined by its **mapping**. In particular a mapping describes the **data type of a document's fields**.
There are two types of mapping:
- **dynamic mapping** where Elasticsearch takes case of adding the new fields automatically when a document is indexed, inferring the type by the value;
- **explicit mapping** where you have to define the mapping manually and must take care of any changes in the structure of the index.

The supported **mapping types** are:

<style>
.table-container {
    display: flex;
    justify-content: center;
}
</style>

<div class="centered-definition-expression">
<div class="table-container">

| type                          | description                                       |
|-------------------------------|---------------------------------------------------|
| **binary**                    | Binary value encoded as a base64 string.          |
| **boolean**                   | Either true or false.                             |
| **keyword**                   | Used for structured content (e.g. IDs, ...).      |
| **long**                      | A signed 64-bit integer.                          |

</div>
</div>

---

<div class="centered-definition-expression">
<div class="table-container">

| type                          | description                                       |
|-------------------------------|---------------------------------------------------|
| **double**                    | A double-precision 64-bit floating point number.  |
| **date**                      | A string containing formatted dates.              |
| **object**                    | A JSON object.                                    |
| **text**                      | The traditional field type for full text-content. |
| **geo_point**                 | Latitude and longitude points                     |

</div>
</div>

> **Important remark**: when performing queries, **text fields are analyzed** (_the exact transformation depends on the analyzer, but usually spaces, commas, etc. are removed, words are made lowercase, ..._), while **keyword fields are not**.

## Analyzers

Elasticsearch supports several **analyzers** which process text for performing full-text search.

They are:

<div class="centered-definition-expression">
<div class="table-container">

| analyzer | description |
|---|---|
| **standard analyzer** | It divides text into terms on word boundaries (using the UTS algorithm). It removes most punctuation, lowercases terms, and supports removing stop words. |
| **simple analyzer** | It divides text into terms whenever it encounters a character which is not a letter. It lowercases all terms. |
| **whitespace analyzer** | It divides text into terms whenever it encounters any whitespace character. It does not lowercase terms. |
| **stop analyzer** | It is like the simple analyzer, but also supports removal of stop words. |
| **pattern analyzer** | It uses a regular expression to split the text into terms. It supports lower-casing and stop words. |
| **language analyzer** | Language-specific analyzers (e.g., english, etc.) |

</div>
</div>

**Analyzers can be tested on sample texts** through the following syntax:

<div class="algorithm">

```
    POST _analyze
    {
        "analyzer": "standard",
        "text": "I really like sunsets."
    }
```

</div>

## Interaction

**Interactions** with Elasticsearch happen through requests to REST endpoints.
The actions that can be performed depend on the HTTP verb, namely:
- **GET** is used to read documents, indices metadata, mappings, ... ;

---

- **POST** and **PUT** are often used to create new documents, indices, ...;
- **DELETE** is used to delete documents, indices, ... .

> **Important remark**: there is a relevant difference between **POST** and **PUT**:
> - **POST doesn't require** the ID of the resource that we want to create. If omitted, Elasticsearch takes care of creating and assigning IDs to documents. The sytnax is: `POST /index_name/_doc`;
> - **PUT requires** the ID of the resource. The syntax is: `PUT /index_name/_doc/document_id`.

For example, we can **create a document** as follows:

<div class="algorithm">

```
    POST /my_index/_doc
    {
        "author": "Andrea",
        "title": "Set up Elasticsearch and Kibana in 15 minutes!",
        "date": "Tue 25 Feb 2021 11:40:00+0000",
        "categories": [ "elasticsearch", "tutorial", "data science", "bigdata" ],
        "lang": "en-US"
    }
```

</div>

### Creating a new index

To create a new index, it's enough to use the **PUT** operator: `PUT /my_index`.

**Important**: when defining an index, it is also possible to setup some parameters, namely one or more aliases, the **number of shards**, **the number of replicas**, and many more. For example:


<div class="algorithm">

```
    PUT /my_index
    {
        "settings": {
            "number_of_replicas": 3,
            "number_of_shards": 3
        }
    }
```

</div>

#### Creating a new index with explicit mapping

When creating an index, it is possible to define the **mapping** straight away:

<div class="algorithm">

```
    PUT /my_index
    {
        "mappings": {
            "proeprties": {
                "age": { "type": "integer" },
                "email": { "type": "keyword" },
                "name": { "type": "text" }
            }
        }
    }
```

</div>

---

> **Important remark**: Of course we can define the mapping, the number of shards, and the number of replicas in the same request (we just need to put in the body of the request both `mappings` and `settings` objects).

#### Adding a field to a mapping

To **add a field to an existing mapping** we can perform the following request:

<div class="algorithm">

```
    PUT /my_index/_mapping
    {
        "properties": {
            "surname": { "type": "text" },
            "index": false
        }
    }
```

</div>

(_The `index` field **defines whether a field is indexed and queryable**_).

#### Visualising a mapping

We can **visualise and existing mapping** through the following request: `GET /my_index/_mapping`.
Sometimes, it is not even encessary to have a look at the whole mapping. Instead, it could be interesting to take a look at the mapping of a single field. The syntax is: `GET /my_index/_mapping/field/my_field`.

### Retrieving documents

**Retrieving a single document** can be done using its unique identifier: `GET /index_name/_doc/identifier`.

### Queries

Elasticsearch supports two different categories of query clauses:
- **leaf query clauses** which **look for a particular value in a particular field**. They can be used by themselves. This category includes **match**, **term** and **range** queries;
- **compound query clauses** which **wrap other leaf or compoung queries** and are used to combine multiple queries **in a logical fashion**. This category includes **bool** queries and many more.

**Important**: by default, Elasticsearch sorts matching search results by **relevance score**, which measures _**how well each document matches a query**_.
Each query type can calculate relevance scores differently. Furthermore, score calculation is performed or not depending on whether the query clause is run in a **query** or in a **filter contex**.

---

In particular:
- in **query context**, applied with the **`query` parameter**, score calculation **is computed**;
- in **filter context**, applied with the **`filter`** or **`must_not` parameters**, score calculation **is not computed**.

#### Leaf query clauses

##### Match queries

**Match queries** return documents that match a provided text, number, date or boolean value. **Important**: whenever a text value (through which we want to find matches) is provided, it is analyzed before matching. The syntax is:

<div class="algorithm">

```
    GET /index_name/_search
    {
        "query": {
            "match": {
                "field": {
                    "query": "value"
                }
            }
        }
    }
```

</div>

**Match queries** can be performed using a compact style:

<div class="algorithm">

```
    GET /steam_overviews/_search
    {
        "query": {
            "match": {
                "field": "value"
            }
        }
    }
```

</div>

Depending on the value of the **operator** parameter, text is matched in an **OR** or in an **AND** fashion:
- the **OR** operator matches documents whose field contains at least 1 word among the ones in the text value that we've provided (after it has been analyzed);
- the **AND** operator matches documents whose field contains all the words in the text value that we've provided (after it has been analyzed).
The syntax is:

<div class="algorithm">

```
    "match": {
        "field": {
            "query": "text",
            "operator": "or
        }
    }
```

</div>

---

##### Term queries

**Term queries** return documents that contain an **exact term** in a provided field.
**DO NOT use** term queries for **text fields**. Remember that text fields are analyzed. Such an approach make it difficult to find exact matches.
The syntax is:

<div class="algorithm">

```
    GET /index_name/_search
    {
        "query": {
            "term": {
                "field": {
                    "value": "value"
                }
            }
        }
    }
```

</div>

where the **`value`** parameter contains the term to look for in the document.
(_We can use the compact syntax also for term queries_).

**Term queries** support the following parameters:
- **`boost`**: it is a float number used to decrease or increase the relevance score (by multiplying it) of a query. It is useful for searches with multiple queries (_as we'll see later_);
- **`case_insensitive`**: it is a boolean that allows insensitive case matching (the default is **true**).

These parameters must be added together with **`value`**.

##### Range queries

**Range queries** return documents that contain terms within a provided range. They are usually employed with numerical fields or dates.
The syntax is:

<div class="algorithm">

```
    GET /index_name/_search
    {
        "query": {
            "range": {
                "field": {
                    "operator1": "value1",
                    "operator2": "value2",
                    ...
                }
            }
        }
    }
```

</div>

where the **supported operators** are:
- **`gt`**, that is, **greater than**;

---

- **`gte`**, that is, **greater than or equal to**;
- **`lt`**;
- **`lte`**.

Furhtermore, even range queries **support the `boost` operator**.

When performing ranged queries involving dates, it can be useful to know a little bit of the so-called `Date Math`. There are three main parts, namely:
- an **anchor date** which is either `now` or a date followed by `II`;
- a **match expression** made of a math operator, a number and a time unit (`d` for days, `M` for months, `Y` for years, ...);
- (optionally) an **operator** to round the date to the closest, chosen time unit.

Examples are:
- `now +1d /M`;
- `now -1Y /Y`;
- `2022.07.28II +2M /M`.

#### Compound query clauses

##### Boolean queries

**Boolean queries** are **logical combinations** of other queries. They are built using one or more **boolean clauses**. The table below highlights the **available boolean clauses**:

<div class="centered-definition-expression">
<div class="table-container">

| boolean clause | description |
|---|---|
| **`must`** | The documents must satisfy the condition of this query and **it will contribute** to the score. |
| **`filter`** | The documents must satisfy the condition of this query. However, unlike must, **the score** of the query **will be ignored**. |
| **`should`** | The documents should satisfy the condition of this query. **It will contribute** to the score. |
| **`must_not`** | The documents must not satisfy the condition of this query. The **scoring is ignored**. |

</div>
</div>

**Each of the clauses described may contain multiple conditions**.
The syntax is:

<div class="algorithm">

```
    GET /index_name/_search
    {
        "query": {
            "bool": {
                "must": [
                    leaf_query1,
                    leaf_query2,
                    ...
```

</div>

---

<div class="algorithm">

```
                ],
                "filter": [ ... ],
                ...
            }
        }
    }
```

</div>

where **`leafquery1`** is what we assigned to the **`query`** field when performing simple leaf queries (for example `{ "match": { ... } }`).

**You can write boolean queries that include all or just a few of the clauses described**.

#### Aggregations

Elasticsearch supports three different types of aggregations, namely:
- **metric aggregations** that calculate metrics from field values;
- **bucket aggregations** that group documents into buckets, based on field values, ranges, or other criteria;
- **pipeline aggregations** that take input from other aggregations instead of documents or fields.

> **Important remark**: in Elasticsearch, aggregations return the **set of documents** on which we're performing the aggregation, before the aggregations themselves. The **`size`** parameter defines how many of these documents are returned.

Aggregations can be run as part of a search by specifying the **aggs** parameter. The syntax for **bucket aggregations** is the following:

<div class="algorithm">

```
    GET index_name/_search
    {
        "size": 0,
        "aggs": {
            "aggregation_name": {
                "terms": {
                    "field": "field_name"
                }
            }
        }
    }
```

</div>


We can perform **bucket aggregrations on the result of a query**, through this syntax:

<div class="algorithm">

```
    GET index_name/_search
    {
        "size": 0,
        "query": { ... },
        "aggs": {
            ...
        }
    }
```

</div>

---

Within the same `aggs` operator it is possible to **perform multiple bucket aggregations on different fields**:

<div class="algorithm">

```
    GET index_name/_search
    {
        "size": 0,
        "aggs": {
            "aggregation_name1": {
                "terms": {
                    "field": "field_name1"
                }
            },
            "aggregation_name2": {
                "terms": {
                    "field": "field_name2"
                }
            }
        }
    }
```

</div>

Finally, Elasticsearch supports **sub-aggregations** which are computed for each aggregation by considering the documents in each one of them.

<div class="algorithm">

```
    GET index_name/_search
    {
        "size": 0,
        "aggs": {
            "aggregation_name": {
                "terms": {
                    "field": "field_name1"
                },
                "aggs": {
                    "sub_aggregation_name": {
                        "terms": {
                            "field": "field_name2"
                        }
                    }
                }
            }
        }
    }
```

</div>

The syntax for **metric aggregation** is analogous:

```
    GET index_name/_search
    {
        "size": 0,
        "aggs": {
            "aggregation_name": {
                operator: {
                    "field": "field_name"
                }
            }
        }
    }
```
where **`operator`** is one among **`"sum"`**, **`"avg"`**, ... .
Of course we can perform **metric aggregations** as **sub-aggregations** of **bucket aggregations**. **The syntax follows from straightforward adaptation**.
