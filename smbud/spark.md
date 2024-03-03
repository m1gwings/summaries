---
marp: true
theme: summary
---
# Spark

<div class="author">

Cristiano Migali

</div>

**Apache Spark** is a multi-language engine for executing data engineering, data science, and machine learning on single-node machines or clusters.

When using Spark it is important to keep in mind two core concepts:
- an **RDD** is a **fundamental structure** and a fixed collection of data that calculates on a cluster's different nodes. It enable a developer to process computations on large clusters inside the memory in a resilient and efficient manner;
- a **DataFrame** is an RDD **arranged into named columns**. It is a fixed distributed data collection that enables Spark developers to implement a structure on distributed data, allowing high-level abstraction.

## Basics

### Create a Spark session

The first thing to do in order to interact with Spark from Python is to create a Spark session:

<div class="algorithm">

```
    from pyspark.sql import SparkSession

    # Create an entry point to the PySpark Application
    spark = SparkSession.builder \
        .master("local") \
        .appName("spark_tutorial") \
        .getOrCreate()
```

</div>

### Uploading data into an RDD

We can upload data into an RDD from a list:

<div class="algorithm">

``` 
    data = [
        ( value11, value12, ... ),
        ( value21, value22, ... ),
        ...
    ]

    # Create an RDD
    rdd_list = spark.sparkContext.parallelize(data)
```

</div>

or from a text file:

<div class="algorithm">

```
    rdd_text = spark.sparkContext.textFile("menu.txt")
```

</div>

---

### Converting an RDD into a DataFrame

We can easily convert RDDs into DataFrames:

<div class="algorithm">

```
    df_from_rdd = rdd.toDF()
```

</div>

Furthermore, we can **specify the name of the columns** corresponding to the fields of the elements in the RDD:

<div class="algorithm">

```
    columns = [ "Column Name 1", "Column Name 2", ... ]
    df_from_rdd_with_schema = rdd.toDF(columns)
```

</div>

### Creating a DataFrame

Or we can directly create a DataFrame:

<div class="algorithm">

```
    df_data = [
        ( value11, value2, ...  ),
        ( value21, value22, ... ),
        ...
    ]
        
    columns = ["Column Name 1", "Column Name 2", ... ]
    df = spark.createDataFrame(data = df_data, schema = columns)
```

</div>

### Loading a DataFrame from a CSV

We can also load a DataFrame from a CSV file:

<div class="algorithm">

```
    df_from_csv = spark.read.option("header", True).option("delimiter", ...) \
        .csv("path/to/file.csv")
```

</div>

### Specify the schema of a DataFrame

When creating a DataFrame, we can also specify explicitly its schema, that is, the type of values in each columns. This is acheved as follows:

<div class="algorithm">

```
    from pyspark.sql.types import StructType, StructField

    # Create the schema using StructField(Name, Type, Nullable)
    schema = StructType([
        StructField("Column Name 1", type_1, ...),
        StructField("Column Name 2", type_2, ...),
        ...
    ])
    
    df = spark.createDataFrame(data = df_data, schema = schema)
```

</div>

---

where `type_i` can be `StringType()`, `FloatType()`, `ArrayType()`, ... .

### Retrieving the schema of a DataFrame

We can retrieve the schema of a DataFrame throgh `df.printSchema()`.

### Extract the list of rows in a DataFrame

We can extract the **list** of rows in a DataFrame with the syntax `df.collect()`. **`df.collect[i]` is the `i`-th row of the DataFrame, and `df.collect()[i][j]` is the `j`-th value in the `i`-th row**.

## Projections

### Show

We can **return the whole DataFrame** with `show`:

<div class="algorithm">

```
    df.show(truncate = False)
```

</div>

### Sort

We can **sort the DataFrame on the values of some columns** with `sort` (or `orderBy` equivalently):

<div class="algorithm">

```
    df.sort(col("Column Name 1"), col("Column Name 2"),  ...).show(truncate = False)
```

</div>

We can specify if we want the values in ascending or descending order with the syntax:

<div class="algorithm">

```
    df.sort(col("Column 1").desc(), col("Column 2").asc(),  ...).show(truncate = False)
```

</div>

### Select

We can **create a DataFrame with a subset of the columns** (with all the values) **of another DataFrame** with `select` (similar to SQL):

<div class="algorithm">

```
    projected_df = df.select(col("Column Name 1"), col("Column Name 2"), ...)
```

</div>

### Explode

The `explode` operator can be used inside of `select` to get a **behavior analogous to `$unwind` in MongoDB**. The syntax is:

---

<div class="algorithm">

```
    exploded_df = df.select(col("Column 1"), ...,
        explode(col("Column with array values")))
```

</div>

### Rename columns

To rename columns we can use the following syntax:

<div class="algorithm">

```
    aliased_df = df.withColumnRenamed("Old Name", "New Name")
```

</div>

### Remove columns

We can remove columns with the following syntax:

<div class="algorithm">

```
    without_a_column_df = df.drop("Column Name")
```

</div>

### Limit

We can **create a DataFrame with just `n` rows of another DataFrame** with `limit`:

<div class="algorithm">

```
    limited_df = df.limit(n)
```

</div>

## Filtering

The `filter` method allows to **create a DataFrame from another DataFrame with all and only the values that satisfy a certain condition**. The syntax is:

<div class="algorithm">

```
    filtered_df = df.filter(condition)
```

</div>

where `condition` involves (the values inside) some columns through the usual syntax `col("Column Name")` plus some operators.
Possible conditions are:
- `col("Column Name") == ...` (**hint**: when comparing the float values in a column with another fixed float value it is possible to sorround the fixed float value with quotes to perform "rounded matching");
- `col("Column Name") != ...`;
- `col("Column Name").isin([ value1, value2, ... ])`;
- `col("Column Name").startsWith(string)`;
- `col("Column Name").endsWith(string)`;
- `col("Column Name").contains(string)`;
- `col("Column Name").like(%something%)`;
- `col("Column Name").rlike(regex)`;

---

- `array_containts(col("Array column"), value)`.

We can **compose atomic conditions** into **complex conditions** using the **logical operators**: `|` (for **or**) and `&` (for **and**).

---

## Aggregation

We can **create a DataFrame with aggregated values** with the following syntax:

<div class="algorithm">

```
    agg_df = df.groupBy("Column 1", "Column 2", ...).operator("Column to aggregate")
```

</div>

where **`operator`** is an **aggregation operator** like:
- `sum`;
- `count` (**remark**: count doesn't require `"Column to aggregate"`);
- `avg`;
- `min`;
- ... .

If we want to apply **more than one aggregation operator** we can exploit the following syntax:

<div class="algorithm">

```
    agg_df = df.groupby("Column 1", "Column 2", ...).agg(
        operator1("Column to aggregate 1").alias("Alias 1"),
        operator2("Column to aggregate 2").alias("Alias 2"),
        ...
    )
```

</div>

(_Of couse **`alias` is not required**_).

If we want to compute an **aggregation** on all the rows of the DataFrame, we can use the syntax:

<div class="algorithm">

```
    agg_df = df.select(aggregation_function("Column Name"))
```

</div>

where **`aggregation_function`** can be one of the operators listed above, but also some special functions like:
- **`approx_count_distinct("Column Name")`**: returns the **number of distinct elements** in `col("Column Name")`;
- **`collect_list("Column Name")`**: **collects** the **values** of `col("Column Name")` **inside a list**;
- **`collect_set("Column Name")`**: analogous to `collect_list`;
- **`countDistinct("Column Name 1", "Column Name 2")`**: equivalent to `approx_count_distinct`;
- **`first("Column Name")`**: returns the **first non-null value** in `col("Column Name")`;
- **`last("Column Name")`**: analogous to `first`.

---

## Joins

We can perform **join operations** with the following syntax:

<div class="algorithm">

```
    df_1.alias("df_1")
    df_2.alias("df_2")
    df_1.join(df_2, col("df_1.Column1") == col("df_2.Column2"), type_of_join)
```

</div>

where `type_of_join` can be: `"inner"`, `"outer"`, `"full"`, `"fullouter"`, `"left"`, `"leftouter"`, `"right"`, `"rightouter"`, `"leftsemi"`, `"leftanti"`.