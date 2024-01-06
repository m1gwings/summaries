---
marp: true
theme: cheatsheet
paginate: true
---
# NAML Cheatsheet (A. Y. 2023/2024)

## NumPy

<div class="multiple-columns with-title">
<div class="column">

### The basics

NumPy’s main object is the **homogeneous multidimensional array**. It is a table of elements, all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called **axes**. NumPy's array class is called `ndarray`, it is also known by the alias `array`.

The more important attributes of an `ndarray` are:
- `ndim`: the number of axes of the array;
- `shape`: a tuple of integers indicating the size of the array in each dimension (the length of `shape` is `ndim`);
- `size`: the total number of elements of the array (`size` is the product of the elements of `shape`);
- `dtype`: an object describing the type of the elements in the array (one can use standard Python types or the ones provided by NumPy: `numpy.int32`, `numpy.int16`, `numpy.float64`, ... ).

### Array creation

- Create arrays **form a regular Python list of tuple**:
We can use the `array` function:
```
a = np.array(<sequence (list or tuple)>)
```
> It transformes sequences of sequences into two-dimensional arrays, sequences of sequences of sequences into three-dimensional arrays, and so on ... .
For example:
```
b = np.array([(1.5, 2, 3), (4, 5, 6)])
```
> The value of `b` is:

</div>
<div class="column">

```
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```
> The type of the array can also be explictly specified at creation time:
```
c = np.array([[1, 2], [3, 4]],
    dtype=complex)
```
> The value of `c` is:
```
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])
```

- Create arrays **with initial placeholder content**:

> The function **`zeros`** creates an array full of zeros:
```
np.zeros(<shape>, dtype = <dtype>)
```
> The function **`ones`** creates an array full of ones:
```
np.ones(<shape>, dtype = <dtype>)
```
> The function **`empty`** creates an array whose initial contant is random and depends on the state of the memory. 
```
np.empty(<shape>, dtype = <dtype>)
```
> By **default**, the **`dtype`** of the create array is `numpy.float64`.

</div>
<div class="column">

- Create arrays **with sequences of numbers**:
NumPy provides the **`arange`** function which is **analogous** to the Python built-in `range`, but returns an array:
```
a = np.arange(<start>, <end>, <step>)
```
> The **`linspace`** function returns an array of `n` numbers evenly distributed in a segment $[a, b]$ where `n` is specified by us. In particular the first element of the returned array is $a$ and the last is $b$.
```
a = np.linspace(<start>, <end>,
    <num of points>)
```
> For example:
```
a = np.linspace(0, 2, 9)
```
> The value of `a` is:
```
array([0.  , 0.25, 0.5 , 0.75,
    1.  , 1.25, 1.5 , 1.75, 2.  ])
```

### Printing arrays

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:
- the last axis is printed from left to right,
- the second-to-last axis is printed from top to bottom,
- the rest are also printed from top to bottom, with each slice separated from the next by an empty line.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

One-dimensional arrays are then printed as rows, bidimensionals as matrices, and tridimensionals as lists of matrices.
If an array is too large to be printed, NumPy automatically skips the central part of the array and only prints the corners.

### Operations

#### Aritmethic operations

**Arithmetic operators on arrays apply _elementwise_**. A **new array** is created and filled with the result.
For example:
```
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a - b
```
The value of `c`:
```
array([20, 29, 38, 47])
```
The value of `b**2` is:
```
array([0, 1, 4, 9])
```
> **Important remark**: unlike in many matrix languages, the **product operator `*` operates elementwise** in NumPy arrays. The **matrix product** can be performed using the **`@` operator** or the **`dot`** function or method. For example:
```
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]]
```

</div>
<div class="column">

> Then the value of `A * B` is:
```
array([[2, 0],
       [0, 4]])
```
> the value of `A @ B` is:
```
array([[5, 4],
       [3, 4]])
```
> which is the same as `A.dot(B)`.

Some **operators**, such as `+=` and `*=`, **act in place to modify an existing array** rather than create a new one.

#### Aggregations

NumPy allow easily to compute the sum, minimum, maximum, ... of all the elements in an array through the corresponding methods: **`sum`**, **`min`**, **`max`**, ... .

By specifying the **`axis` parameter** you can apply an operation along the specified axis of an array:
```
b = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
```
The value of `b.sum(axis = 0)` is the **sum of each column**:
```
array([12, 15, 18, 21])
```
while `b.sum(axis = 1)` is the **sum of each row**:
```
array([0, 4, 8])
```

</div>
<div class="column">

More **advanced aggregation operators** are:
- **`cumsum`**: which is the cumulated sum of the array (if we don't specify an axis, multidimensional arrays are "unwinded" in one-dimensional arrays);
- **TODO ...**

</div>
</div>