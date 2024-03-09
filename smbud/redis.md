---
marp: true
theme: summary
math: mathjax
---
# Redis

<div class="author">

Cristiano Migali

</div>

**Redis** is in the family of databases called **key-value stores**.

## Store, retrieve and delete values

The syntax for **setting a value** is:

<div class="algorithm">

```
    SET <key> <value>
```

</div>

Then we can **retrieve it** with: 

<div class="algorithm">

```
    GET <key>
```

</div>

Furthermore, we can **check if there is some value stored with a given key** with:

<div class="algorithm">

```
    EXISTS <key>
```

</div>

(_The output is either 1 or 0, with obvious semantics_).

Finally we can **delete a key** with:

<div class="algorithm">

```
    DEL <key>
```

</div>

## Basic arithmetic operations

Redis supports some **basic arithmetic operations** for integer values, namely:
- **`INCR <key>`** (_increments the value stored at `<key>` by 1_);
- **`INCRBY <key> n`** (_increments the value stored at `<key>` by `n`_);
- **`DECR <key>`**;
- **`DECRBY <key> n`**.

The reason for using such operations is that **they are atomic**.

## Expiring values

Redis can be told that a **key should only exist for a certain length of time** (**time to live**, or **TTL**). We can set such length of time with the following syntax:

---

<div class="algorithm">

```
    EXPIRE <key> <TTL in seconds>
```

</div>

You can **test how long a key will exist** with:

<div class="algorithm">

```
    TTL <key>
```

</div>

The value -2 for the TTL of a key, means that it doesn't exist anymore. Instead, -1 means that the key will never expire.

The commands **`PEXPIRE`** and **`PTTL`** are analogous to `EXPIRE` and `TTL`, but operate using **TTL in milliseconds** instead of seconds.

We can **set a value and it's TTL in a single expression**:

<div class="algorithm">

```
    SET <key> <value> EX <time length in seconds>
```

</div>

It is also possible to **cancel the TTL of a key** removing the expire and making the key permanent again:

<div class="algorithm">

```
    PERSIST <key>
```

</div>

## Complex data structures as values

Redis supports **several complex data structures as values** for a given key.

When dealing with complex data structures in Redis we have to keep in mind the following concept: **you don't create a key first, and add things to it later, but you can just directly use the command in order to add new elements**. **As a side effect the key will be created if it did not exist**. **Similarly keys that will result empty  after executing some command will automatically be removed from the key space**.

### Lists

We can **add elements to the end of a  list** with:

<div class="algorithm">

```
    RPUSH <list key> <list element 1> <list element 2> ...
```

</div>

or **to the beginning of a list** with:

<div class="algorithm">

```
    LPUSH <list key> <list element 1> <list element 2> ...
```

</div>

---

> **Important remark**: by what we said before, these commands also **allow to create lists** (when we add the first element).

**`LRANGE`** gives a **subset of the list**. It takes the index of the first element you want to retrieve as its first parameter and the index of the last name you want to retrieve as its second parameter.

<div class="algorithm">

```
    LRANGE <list key> <index of first element> <index of last element>
```

</div>

A value -1 for the second parameter means to retrieve elements until the end of the list, -2 means to include up to the penultimate, and so forth.

We can **remove the first element from the list and retrieve it** with:

<div class="algorithm">

```
    LPOP <list key>
```

</div>

or **the last element** with:

<div class="algorithm">

```
    RPOP <list key>
```

</div>

We can retrieve the **length** of a list with:

<div class="algorithm">

```
    LLEN <list key>
```

</div>

### Sets

A set is similar to a list, except it does not have a specific order and each element may only appear once. In a set we can "only" **test if a given element is inside it or not** (**membership**).

We can **add elements to a set** with:

<div class="algorithm">

```
    SADD <set key> <set element 1> <set element 2> ...
```

</div>

and **remove elements from a set** with:

<div class="algorithm">

```
    SREM <set key> <set element>
```

</div>

Furthermore, `SADD` (`SREM`) returns 1 or 0 to signal if the member was already (actually) there or not.

---

We can **test for membership** with:

<div class="algorithm">

```
    SISMEMEBER <set key> <set element>
```

</div>

(_It returns 1 or 0 with obvious semantics_).

We can **retrieve the elements of the set as a list** with:

<div class="algorithm">

```
    SMEMBERS <set key>
```

</div>

Finally, **`SUNION`** **combines two or more sets and returns the list of all elements** (none of the operands are modified):

<div class="algorithm">

```
    SUNION <set key 1> <set key 2> ...
```

</div>

Sets also have a command to remove random elements from the set and return them to the client in a single operation, the syntax is:

<div class="algorithm">

```
    SPOP <set key> <num of random elements to remove and return>
```

</div>

There is also a command to return random elements without removing such elements from the set, the arguments are similar to `SPOP`, but if you specify a negative count instead of a positive one, it may also return repeating elements:

<div class="algorithm">

```
    SRANDMEMBER <set key> <num of random elements to remove and return>
```

</div>

### Sorted sets

A sorted set is similar to a regular set, but now **each value has an associated score**. This score is used to sort (in ascending order) the elements in the set.
We can add elements to a sorted set with:

<div class="algorithm">

```
    ZADD <sorted set key> <score> <element>
```

</div>

Sorted sets (other then commands analogous to sets' ones) support the `ZRANGE` command (_with obvious semantics_):

<div class="algorithm">

```
    ZRANGE <sorted set key> <first element index> <last element index>
```

</div>

---

### Hashes

Hashes are **maps between string fields and string values**, so they are the perfect data type to represent objects.

We can **set a field** with:

<div class="algorithm">

```
    HSET <hash key> <field name> <field value>
```

</div>

We can **retrieve the values of each field** with:

<div class="algorithm">

```
    HGETALL <hash key>
```

</div>

(_Data is returned as a list `[<field name 1>, <field value 1>, <field name 2> <field value 2>, ...]`_).

We can also **set multiples fields at once**:

<div class="algorithm">

```
    RHMSET <hash key> <field name 1> <field value 1> <field name 2> <field value 2> ...
```

</div>

or **retrieve just the value of a single filed**:

<div class="algorithm">

```
    HGET <hask key> <field name>
```

</div>

**Numerical values in hash fields** are handled exactly the same as in simple strings and there are operations to increment such values in an atomic way:

<div class="algorithm">

```
    HINCRBY <hash key> <field name> n
```

</div>

Finally, we can **delete fields from hashes** with:

<div class="algorithm">

```
    HDEL <hash key> <field name>
```

</div>
