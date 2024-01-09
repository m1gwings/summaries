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

NumPy’s main object is the **homogeneous multidimensional array**. It is a table of elements, all of the same type, indexed by a tuple of non-negative integers. In NumPy dimensions are called **axes**. NumPy's array class is called **`ndarray`**, it is also known by the alias `array`.

The more important attributes of an `ndarray` are:
- **`ndim`**: the number of axes of the array;
- **`shape`**: a tuple of integers indicating the size of the array in each dimension (the length of `shape` is `ndim`);
- **`size`**: the total number of elements of the array (`size` is the product of the elements of `shape`);
- **`dtype`**: an object describing the type of the elements in the array (one can use standard Python types or the ones provided by NumPy: `numpy.int32`, `numpy.int16`, `numpy.float64`, ... ).

### Array creation

- **`array`**: creates arrays **from a regular Python list or tuple**:
```
a = np.array([1, 2, 3, 4])
```
> The value of `a` is:
```
array([1, 2, 3, 4])
```
> **Sequences of sequences become two-dimensional arrays**, sequences of sequences of sequences become three-dimensional arrays, and so on ... :
```
b = np.array([(1.5, 2, 3), (4, 5, 6)])
```

</div>
<div class="column">

> The value of `b` is:

```
array([[1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
```
> **The type of the array** can also be explictly specified at creation time:
```
c = np.array([[1, 2], [3, 4]],
    dtype=complex)
```
> The value of `c` is:
```
array([[1.+0.j, 2.+0.j],
       [3.+0.j, 4.+0.j]])
```

#### Array with initial placeholder content

- **`zeros`**: creates an **array full of zeros** given its shape (and optionally type):
```
a = np.zeros((3, 4), dtype = np.float64)
```
> The value of `a` is:
```
array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])
```
- **`ones`**: creates an **array full of ones** given its shape (and optionally type):
```
a = np.ones((2, 3), dtype = np.complex64)
```

</div>
<div class="column">

> The value of `a` is
```
array([[1.+0.j, 1.+0.j, 1.+0.j],
       [1.+0.j, 1.+0.j, 1.+0.j]],
       dtype=complex64)
```
- **`empty`**: creates an **array** whose **initial content** is random and **depends on the state of the memory**: 
```
a = np.empty((2, 2), dtype = np.int64)
```
> The value of `a` is:
```
array([[1, 2],
       [3, 4]])
```
> **Remark**: the **default type** for all these array creation functions is **`np.float64`**.

#### Array with sequence of numbers

- **`arange`**: it is **analogous** to the Python built-in `range`, but returns an array:
```
a = np.arange(0, 10, 2)
```
> The value of `a` is:
```
array([0, 2, 4, 6, 8])
```

- **`linspace`**: returns an array of `n` numbers evenly distributed in a segment $[a, b]$ where `n` is specified by us. In particular the first element of the returned array is $a$ and the last is $b$:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
a = np.linspace(0, 2, 9)
```
> The value of `a` is:
```
array([0.  , 0.25, 0.5 , 0.75,
    1.  , 1.25, 1.5 , 1.75, 2.  ])
```

#### More advanced array creation

- **`meshgrid`**: makes N-D coordinate arrays for vectorized evaluations of N-D scalar/vector fields over N-D grids, given one-dimensional coordinate arrays `x1`, `x2`, ..., `xn`. This function supports both indexing convetions through the `indexing` keyword argument: giving the string `"ij"` returns a meshgrid with matrix indexing, while `"xy"` returns a meshgrid with Cartesian indexing. For example:
```
x = np.array([0, 1])
y = np.array([0, 2, 4])
xv, yv = np.meshgrid(x, y, indexing = "ij")
for i in range(x.size):
    for j in range(y.size):
        print(f'({xv[i, j]}, {yv[i, j]})')
```
> The result is:
```
(0, 0)
(0, 2)
(0, 4)
(1, 0)
(1, 2)
(1, 4)
```
> While, with _cartesian_ indexing, the value on the `y` axis is determined by the first index and the value on the `x` axis is determined by the second index:

</div>
<div class="column">

```
x = np.array([0, 1])
y = np.array([0, 2, 4])
xv, yv = np.meshgrid(x, y, indexing = "xy")
for i in range(x.size):
    for j in range(y.size):
        print(f'({xv[j, i]}, {yv[j, i]})')
```
(_The result is the same as before_).

### Printing arrays

When you print an array, NumPy displays it in a similar way to nested lists, but with the following layout:
- the **last axis** is printed from **left to right**,
- the **second-to-last axis** is printed from **top to bottom**,
- the **rest** are also printed from **top to bottom**, with each slice separated from the next by an **empty line**.

One-dimensional arrays are then printed as rows, bidimensional as matrices, and tridimensional as lists of matrices:
```
a = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
```
`a` is printed as:
```
array([[[1, 2],
        [3, 4]],

       [[5, 6],
        [7, 8]]])
```


### Operations on arrays

Most of NumPy operators on arrays **apply _elementwise_**.
For example:

</div>
<div class="column">

```
a = np.array([20, 30, 40, 50])
b = np.arange(4)
c = a + b
```
The value of `c` is:
```
array([20, 31, 42, 53])
```
The value of `b**2` is:
```
array([0, 1, 4, 9])
```

#### Broadcasting

**Broadcasting** allows NumPy's binary operations to deal in a meaningful way with inputs that do not have exactly the same shape.
- The **first rule** of broadcasting is that if all input arrays do not have the same number of dimensions, a "1" will be repeatedly prepended to the shapes of the smaller arrays until all the arrays have the same number of dimensions.
- The **second rule** of broadcasting ensures that arrays with a size of 1 along a particular dimension act as if they had the size of the array with the lalrgest shape along that dimension. The value of the array element is assumed to be the same along that dimension for the "broadcast" array.

That is:
```
a = np.zeros((2, 3))
b = np.arange(3)
```
The value of `a + b` is:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
array([[0., 1., 2.],
       [0., 1., 2.]])
```

> **Remark**: if, after applying the first rule, the two arrays differ in the size of an axis and neither of the two is 1, then the **broadcasting fails**:
```
a = np.zeros((2, 3))
b = np.arange(2)
```
> Then `a + b` produces a **`ValueError`**.

#### Arithmetic operations

NumPy supports all the usual Python arithmetic operators, we will list some:
- **`a + b`**: returns the **elementwise sum** between `a` and `b`;
- **`a * b`**: returns the **elementwise product** between `a` and `b`;
- **`a - b`**: returns the **elementwise difference** between `a` and `b`;
- **`a / b`**: returns the **elementwise division** between `a` and `b`;
- **`a**n`** (where `n` is a number): **raises every element** of `a` to the power `n`.

#### Mathematical functions

NumPy supports all the usual mathematical functions, we will list some: `exp`, `sin`, `cos`, `sqrt`, ... .
They are all **applied _elementwise_**:
```
a = np.array([[0, 1],
              [2, 3]])
```
The value of `np.exp(a)` is:
</div>
<div class="column">

```
array([[ 1.        ,  2.71828183],
       [ 7.3890561 , 20.08553692]])
```

> **Important remark**: all the operations that we've listed so far **return new arrays**. **Some operators**, instead, **act in place to modify an existing array**, for example:
> - **`a += b`**;
> - **`a *= b`**;
> - ... .

### Arrays indexing

**One-dimensional** arrays can be indexed, sliced, and iterated over, much like `list`s and other Python sequences:
```
a = np.arange(12)
```
Then the value of `a[2]` is:
```
2
```
The value of `a[:6:2]` is:
```
array([0, 2, 4])
```

**Multidimensional** arrays can have one index (**or slice**) per axis. These **indices** are **given in a tuple spearated by commas**:
```
a = np.array([[[1, 2, 3], [4, 5, 6]],
              [[6, 5, 4], [3, 2, 1]]])
```
The value of `a[0, 1, 2]` is:

</div>
<div class="column">

```
6
```
**`a[0, :, 2]`** is a one-dimensional array with all the values of `a` in the second axis, after having fixed the value for the first and second axis to 0 and 2 respectively:
```
array([3, 6])
```
The value of `a[0, 1, :2]` is:
```
array([4, 5])
```
(_Of course we can use slicing on more than one axis_).

When **fewer indices are provided** than the number of axes, the **missing indices are considered complete slices**:
```
a = np.array([[1, 2],
              [3, 4]])
```
Then `a[-1]` is equal to `a[-1, :]`:
```
array([3, 4])
```

> **Important remark**: you can also use **indexing on arrays as a taget to assign to**:
```
a = np.array([[0, 1],
              [2, 3]])
a[:, 0] = 0
```
> Then, the value of `a` is:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
array([[0, 1],
       [0, 3]])
```

#### Advanced indexing

NumPy offers more indexing facilities than regular Python sequences. In addition to indexing by integers and slices, arrays can be indexed by arrays of integers and arrays of booleans.

##### Indexing with arrays of integers

Let's start with a **one-dimensional** array first:
```
a = np.arange(12) ** 2
b = np.array([0, 3, 7])
```

Then the value of `a[b]` is:
```
array([ 0,  9, 49])
```

If `a` is **multidimensional** instead, we can give indexes for more than one dimension. The **arrays of indices for each dimension must have the same shape**.
For example:
```
a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
i = np.array([[0, 1],
              [1, 2]])
j = np.array([[2, 1],
              [3, 3]])
```
Then `a[i, j]` is equal to:
```
array([[ 2,  5],
       [ 7, 11]])
```

</div>
<div class="column">

We can also use arrays of indices in conjuction with slices or normal indexing:
```
a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])
b = np.array([0, 2])
```
Then, the value of `a[b, :]` is:
```
array([[ 0,  1,  2,  3],
       [ 8,  9, 10, 11]])
```

##### Indexing with arrays of booleans

To understand indexing with arrays of booleans we have to introduce the `nonzero` function:
- **`nonzero`**: returns a tuple of arrays, one for each dimension of a, containing the indices of the non-zero elements in that dimension (for boolean arrays, non-zero means `True`).
For example:
```
a = np.array([False, True, False, True])
```
> Then, the value of `a.nonzero()` is:
```
(array([1, 3]),)
```
Indexing `a` with an array of booleans `b` (which is achieved through the syntax `a[b]`), is equivalent to: `a[b.nonzero()]` which we can interpret with the "indexing with arrays of integers semantics".
For example:
```
a = np.array([[1, 2],
              [3, 4]])
```

</div>
<div class="column">

```
b = np.array([[True, False],
              [False, True]])
```
Then the value of `a[b]` is:
```
array([1, 4])
```
Indeed `b.nonzero()` is:
```
(array([0, 1]), array([0, 1]))
```
(_Of course, since indexing with arrays of booleans boils down to indexing with arrays of integers, we can use indexing with arrays of boolean together with normal indexing or slicing_).

### Aggregations on arrays

NumPy allows easily to compute the sum, minimum, maximum, ... of **all** the elements in an array through the corresponding methods: **`sum`**, **`min`**, **`max`**, ... .
For example:
```
a = np.array([[3, 4],
              [5, 8]])
```
Then, the value of `a.max()` is:
```
8
```

By specifying the **`axis` parameter** we can apply an aggregation along the specified axis of an array:
```
b = np.array([[ 0,  1,  2,  3],
              [ 4,  5,  6,  7],
              [ 8,  9, 10, 11]])
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

The value of `b.sum(axis = 0)` is the **sum of each column** of `b`:
```
array([12, 15, 18, 21])
```
while `b.sum(axis = 1)` is the **sum of each row**:
```
array([0, 4, 8])
```

More **advanced aggregation operators** are:
- **`cumsum`**: which is the cumulated sum of the array (if we don't specify an axis, multidimensional arrays are "unwinded" in one-dimensional arrays, see `ravel` in the "Shape manipulation" paragraph);
- **`mean`**: _it has straightforward semantics_.

### Shape manipulation

The **shape** of an **array can be changed** with various commands.

- **`ravel`**: returns the array, **flattened**:
```
a = np.array([[1, 2, 3],
              [4, 5, 6]])
```
> The value of `a` is:
```
array([1, 2, 3, 4, 5, 6])
```
> The order of the elements in the array resulting from `ravel` is normally "C-style", that is, the rightmost index "changes the fastest", so the element after `a[0, 0]` is `a[0, 1]`.

- **`reshape`**: returns the array **with a modifies shape**.
For example, let:
</div>
<div class="column">

```
a = np.arange(12)
```
> Then, the value of `a.reshape(3, 4)` is:
```
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
```
> The new shape must have the same `size` as the old one: the array is flattened and then rebuilt with the new shape.
If a dimension is given as `-1` in a reshaping operation, it is automatically calculated:
```
a = np.arange(15)
```
> Then, the value of `a.reshape(3, -1)` is:
```
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
```
> **Important remark**: both `ravel` and `reshape` **don't modify the original array**, they return a new one.

- **`newaxis`**: **increases the dimension** of an array:
```
a = np.arange(5)
```
> Then, the value of `a[:, np.newaxis]` is:
```
array([[0],
       [1],
       [2],
       [3],
       [4]])
```

</div>
<div class="column">

> (_That is, a column vector_). While, the value of `a[np.newaxis, :]` is:
```
array([[0, 1, 2, 3, 4]])
```
> (_That is, a row vector_).

### Copies

- **`copy`**: makes a **complete** (deep) copy of the array and its data:
```
a = np.arange(4).reshape(2, -1)
d = a.copy()
a[0, 0] = 42
```
> But, the value of `d` remains:
```
array([[0, 1],
       [2, 3]])
```

</div>
</div>
