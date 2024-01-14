---
marp: true
theme: cheatsheet
paginate: true
---
<style>
img {
    filter: none;
}
</style>
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

- **`block`**: assembles an array from nested list of blocks. Block in the innermost lists are concatenated along the last dimension, then these are conateneted along the second-last dimentions, and so on.
```
a = np.block([
    [ np.zeros((4, 4)), np.ones((4, 2)) ],
    [ np.ones((1, 4)),  np.zeros((1, 2)) ]
])
```
> Then, the value of `a` is:
```
array([[0., 0., 0., 0., 1., 1.],
       [0., 0., 0., 0., 1., 1.],
       [0., 0., 0., 0., 1., 1.],
       [0., 0., 0., 0., 1., 1.],
       [1., 1., 1., 1., 0., 0.]])
```

</div>
<div class="column">

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">



</div>
<div class="column">

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


### Basic operations on arrays

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
a = np.array([[1, 2],
              [3, 4]])
a[:, 0] = 0
a[:, 1] = [ 11, 12 ]
```
> Then, the value of `a` is:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
array([[ 0, 11],
       [ 0, 12]])
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

### Predicates on arrays

#### Atomic predicates

**Atomic predicates** on arrays, defined for example through the usual comparison operators, are **evaluated _elementwise_** and return **arrays of booleans**, _which can be used for indexing_:
```
a = np.array([[7, 11, 2],
              [3, 8, 4]])
```
The value of `a <= 5` is:
```
array([[False, False,  True],
       [ True, False,  True]])
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

All the usual comparison operators are supported: `<=`, `>=`, `==`, `!=`, `<`, `>`.

#### Compound predicates

We can compose atomic predicates into **compound predicates** through the usual **logical connectors**.
- **`logical_or`**: computes the truth value of `x1 OR x2` elementwise.
For example, let:
```
a = np.array([[7, 9, 9],
              [1, 3, 2]])
```
> Then, the value of `np.logical_or(a <= 2, a >= 9)` is:
```
array([[False,  True,  True],
       [ True, False,  True]])
```
- **`logical_and`**: computes the truth value of `x1 AND x2` elementwise.
- **`logical_not`**: computes the truth value of `NOT x` elementwise.
- **`logical_xor`**: computes the truth value of `x1 XOR x2` elementwise.

### Randomness

- **`random.seed`**: sets the seed of the NumPy random number generator. For example:
```
np.random.seed(0)
```
- **`random.uniform`**: samples an array of shape specified by the parameter `size` from a uniform distribution with lower boundary specified by the parameter `low` and upper boundary specified by the parameter `high`.

</div>
<div class="column">

> For example:
```
np.random.seed(0)
a = np.random.uniform(low = 0, high = 5,
    size = (3, 2))
```
> The value of `a` is:
```
array([[2.74406752, 3.57594683],
       [3.01381688, 2.72441591],
       [2.118274  , 3.22947057]])
```
> (_The default values for the parameters are: `size = None` (it returns just one number), `low = 0.0`, `high = 1.0`_).

- **`random.normal`**: samples an array of shape specified by the parameter `size` from a normal (gaussian) distribution with mean specified by the paramter `loc` and standard deviation specified by the paramter `scale`.
(_The default values for the parameters are: `size = None`, `loc = 0.0`, `scale = 1.0`_).

- **`random.shuffle`**: modifies a sequence in-place by shuffling its content.
For example, let:
```
a = np.arange(6)
np.random.seed(0)
np.random.shuffle(a)
```
> Then, the value of `a` is:
```
array([5, 2, 1, 3, 0, 4])
```

- **`random.choice`**: generates a random sample from a given one-dimensional array.

</div>
<div class="column">

> The `size` parameter allows to specify the shape of the output array filled with samples. By default the sampling is with replacement.

```
np.random.seed(0)
a = np.random.choice(np.array([1, 5, 7]),
    size = (3, 2))
```
> Then, the value of `a` is:
```
array([[1, 5],
       [1, 5],
       [5, 7]])
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">



</div>
<div class="column">



</div>
<div class="column">

### Linear algebra

In this paragraph we will deal with bidimensional arrays which represent matrices and vectors. (_Yes, also vectors are represented by bidimensional arrays, take a look at the "Shape manipulation" paragraph, and, in particular, at the `newaxis` operator_).

#### Create matrices with a certain structure

- **`zeros`**: we've already encountered this function in the "Array creation" paragraph, it can be used to create the matrix $0_{m \times n}$.
- **`ones`**: we've already encountered this funciton in the "Array creation" paragraph, it can be used to create the matrix $1_{m \times n}$.

- **`identity`**: returns the identity matrix $I_n$:
```
I_5 = np.identity(5)
```
> Then, the value of `I_5` is:
```
array([[1., 0., 0., 0., 0.],
       [0., 1., 0., 0., 0.],
       [0., 0., 1., 0., 0.],
       [0., 0., 0., 1., 0.],
       [0., 0., 0., 0., 1.]])
```
- **`diag`**: returns a diagonal matrix with the specified elements on the diagonal:
```
d = np.arange(5)
D = np.diag(d)
```
> Then, the value of `D` is:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
array([[0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 2, 0, 0],
       [0, 0, 0, 3, 0],
       [0, 0, 0, 0, 4]])
```

#### Linear algebra operations

- **`A @ B`**: returns the matrix product between `A` and `B`:
```
A = np.arange(16).reshape(4, 4)
B = np.ones((4, 5))
```
> Then, the value of `A @ B` is:

```
array([[ 6.,  6.,  6.,  6.,  6.],
       [22., 22., 22., 22., 22.],
       [38., 38., 38., 38., 38.],
       [54., 54., 54., 54., 54.]])
```
> (_`A @ B` is equivalent to `np.dot(A, B)`_).

- **`outer`**: computes the outer product between two vectors:
```
v = np.arange(5)[:, np.newaxis]
u = np.arange(6)[np.newaxis, :]
```
> Then, the value of `np.outer(v, u)` is:
```
array([[ 0,  0,  0,  0,  0,  0],
       [ 0,  1,  2,  3,  4,  5],
       [ 0,  2,  4,  6,  8, 10],
       [ 0,  3,  6,  9, 12, 15],
       [ 0,  4,  8, 12, 16, 20]])
```

</div>
<div class="column">

- **`A.T`**: returns the tranpose of `A`:
```
A = np.arange(12).reshape(3, 4)
```
> Then, the value of `A.T` is:
```
array([[ 0,  4,  8],
       [ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11]])
```

- **`linalg.norm`**: computes the norm of the given matrix or vector. By default, calling `x` the input array, it returns the 2-norm of `x.ravel()`:

```
x = np.arange(1, 3, 2)[:, np.newaxis]
```
> Then, the value of `np.linalg.norm(x)` is:
```
3.7416573867739413
```
> Furthermore, it takes an `axis` parameter which allows to specifies the axis along which to compute the norm. 

#### Decompositions

- **`linalg.svd`**: returns the SVD of the matrix `A`. The boolean parameter `full_matrices` allow to choose between the full SVD and the "reduced" one (in this case, with reduced form, we mean that both `U` and `V` have $\min(m, n)$ columns, where $A \in \mathbb{R}^{m \times n}$).

> For example, let:
```
A = np.arange(12).reshape(4, 3)
```
> Note that `2*A[:, 1] - A[:, 0]` is:

</div>
<div class="column">

```
array([ 2,  5,  8, 11])
```
> which corresponds to `A[:, 2]`, hence `A` is singular.
Now, let:
```
U, s, V_T = np.linalg.svd(A)
```
> Then `U.shape` is `(4, 4)`, `V_T.shape` is `(3, 3)` and `s` is:
```
array([2.24467488e+01, 1.46405850e+00,
       1.54736923e-15])
```
> (_The default value of `full_matrices` is `True`_).
To reconstruct `A` we can do the following:
```
S = np.zeros((U.shape[0], V_T.shape[0]))
for i in range(s.size):
    S[i, i] = s[i]

A_rec = U @ S @ V_T
```
> Indeed, the value of `np.round(A_rec)` is:
```
array([[ 0.,  1.,  2.],
       [ 3.,  4.,  5.],
       [ 6.,  7.,  8.],
       [ 9., 10., 11.]])
```

> If we were instead to put `full_matrices` to `False`:
```
U_r, s_r, V_T_r = np.linalg.svd(A,
       full_matrices = False)
```
> then `U_r.shape` would be `(4, 3)`.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

- **`linalg.qr`**: computes the QR factorization of the given matrix. The parameter `mode` allows to specify if we want the reduced form (with the value `"reduced"`), or the complete one (with the value `"complete"`).
For example:
```
A = np.arange(12).reshape(4, 3)
Q, R = np.linalg.qr(A)
```

### Some useful stuff

- **`maximum`**: computes the **_elementwise_** maximum of the **two** given arrays:
```
a = np.array([[1, 2],
              [-1, 5]])
b = np.array([[0, 3],
              [-2, 6]])
c = np.maximum(a, b)
```
> Then, the value of `c` is:
```
array([[ 1,  3],
       [-1,  6]])
```

- **`argmax`**: returns the indices of the maximum values along an axis. By default, the index is into the flattened array, otherwise along the specified axis:
```
a = np.array([[1, 2],
              [-1, 2]])
b = np.argmax(a, axis = 0)
```
> Then, the value of `b` is:
```
array([0, 0])
```

</div>
<div class="column">



</div>
</div>

---

## Matplotlib

<div class="multiple-columns">
<div class="column">

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations.

### Importing

We can import Matplotlib with:
```
import matplotlib.pyplot as plt
```

### The basics

The **fundamental classes** in Matplotlib are:
- **`Artist`**: basically, everything which is visible on a Matplotlib plot is an `Artist`;
- **`Figure`**: represents the **whole** plotted figure. It keeps track of all the child `Axes`, a group of 'special' `Artist`s (titles, figure legends, colorbars, etc. ), and even nested subfigures;
- **`Axes`**: it is an `Artist` attached to a `Figure` that contains a region for plotting data, and usually includes two (or three in the case of 3D) `Axis` objects (**be aware of the difference between `Axes` and `Axis`**). Each `Axes` also has a title, an x-label, an y-label (and, in the 3D case, a z-label);
- **`Axis`**: they provide ticks and tick labels to set scales for the data in the `Axes`.

### Create a `Figure` with some `Axes`

- **`subplots`**: allows to create a `Figure` with a certain number of `Axes`. In particular:

```
fig, axes = plt.subplots()
```

<p align="center">
    <img src="http://localhost:8080/naml/static/axes.png" width="250mm" />
</p>

</div>
<div class="column">

> creates a `Figure` with a single `Axes`.
We can also create a figure with several `Axes` arranged in a "matrix-like" fashion with the `nrows` and `ncols` parameters:

```
fig, axes = plt.subplots(nrows = 2, ncols = 2)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/multiple-axes.png" width="300mm" />
</p>

> in this case, `axes` is a bidimensional NumPy array, which allows us to access the `Axes` object in a certain position.
Finally we can specify the size of the figure through the `figsize` parameter which takes the width and height of the figure (in this order) in a pair (the units are inches):

```
fig, axes = plt.subplots(nrows = 2, ncols = 3, figsize = (8, 4))
```

<p align="center">
    <img src="http://localhost:8080/naml/static/figsize.png" width="350mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Plotting on a `Axes`

Plotting functions expect NumPy arrays as input, or objects that can be passed to `np.asarray`.
- **`plot`**: plots y versus x as lines and/or markers.
In particular:

```
fig, axes = plt.subplots()

y = np.arange(12) ** 2
axes.plot(y)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/plot.png" width="450mm" />
</p>

> plots `y` using the index array `[0, ..., y.size - 1]` as `x`; while

```
fig, axes = plt.subplots()

x = np.linspace(0, 1, 10)
y = x ** 2
axes.plot(x, y)
```

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/plot-y-vs-x.png" width="270mm" />
</p>


> plots y versus x with the given `x`.
`plot` provides several parameters to change the default plotting style:
> - `linestyle`: with values `"-"`, `"--"`, '"-."', ":", ... allows to specify the style of the line;
> - `linewidth`: allows to specify the width (in points) of the line;
> - `markersize`: allows to specify the size (in points) of marker.

> Additionally, we can use several "format strings" to specify the plotting style, for example:

```
fig, axes = plt.subplots()
x = np.linspace(0, 2 * np.pi, 20)
y = np.sin(x)

axes.plot(x, y, 'v-.')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/format-strings.png" width="300mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

> You can find all the available format strings here: [https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) .

- **`scatter`**: makes a scatter plot y versus x, with varying marker size and/or color:

```
fig, axes = plt.subplots()

np.random.seed(0)
n = 10
x = np.random.uniform(0, 5, n)
y = np.random.uniform(-1, 3, n)
axes.scatter(x, y)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/scatter.png" width="330mm" />
</p>

> Through the `s` parameter we can change the size of the markers, `c` allows to change their color (with `cmap` we can set the color map to use):

```
fig, axes = plt.subplots()

np.random.seed(0)
n = 10
x = np.random.uniform(0, 5, n)
y = np.random.uniform(-1, 3, n)
s = (np.arange(n) + 1) * 5
c = x * y
axes.scatter(x, y, s = s, c = c)
```

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/scatter-with-size-and-color.png" width="330mm" />
</p>

> Finally, the `marker` parameter allows to change the style of the marker using the same syntax of `plot`'s format strings (with only the character relative to the marker) and the `c` parameter can be used also to set a color for all the markers:

```
fig, axes = plt.subplots()

np.random.seed(0)
n = 10
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)

axes.scatter(x, y, marker = 'v', c = 'r')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/scatter-with-marker-and-color.png" width="330mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

- **`semilogy`**: analogous to plot, but the y axis is logarithmic. For example:

```
fig, axes = plt.subplots()

x = np.linspace(0, 1, 10)
y = np.exp(x)
axes.semilogy(x, y)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/semilogy.png" width="290mm" />
</p>

- **`loglog`**: analogous to plot, but both the x and y axis are logarithmic. For example:

```
fig, axes = plt.subplots()

x = np.linspace(0, 10, 100)
y = x ** 2
axes.loglog(x, y)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/loglog.png" width="290mm" />
</p>

</div>
<div class="column">

### Style `Axes`

#### Set `Axes`' title

- **`set_title`**: allows to set the title of an `Axes`:

```
fig, axes = plt.subplots()

axes.set_title("My title")
```

<p align="center">
    <img src="http://localhost:8080/naml/static/title.png" width="260mm" />
</p>

#### Add `Axes` labels

- **`set_xlabel`**: sets the label of the `Axes`. **`set_ylabel`** has analogous behavior:

```
fig, axes = plt.subplots()

axes.set_xlabel("My x label")
axes.set_ylabel("My y label")
```

<p align="center">
    <img src="http://localhost:8080/naml/static/axis-label.png" width="260mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### Add `Axes` legend

Often we want to identify lines or markers onto an `Axes`. For doing so, we can use the **`label`** parameter inside the plotting functions that we discussed earlier. Finally, we need to invoke the **`legend`** method:

```
fig, axes = plt.subplots(ncols = 2)

x = np.linspace(0, 1, 100)
y1 = x
y2 = np.exp(x)

np.random.seed(0)
u = np.random.normal(loc = 0.5, scale = 0.5, size = (20, 2))

axes[0].semilogy(x, y2, 'b-', label = '$e^x$')
axes[1].plot(x, y1, 'b-', label = '$x$')
axes[1].scatter(u[:, 0], u[:, 1], marker = '^', c = 'r',
    label = '$y_1$ vs $y_2$')

for a in axes:
    a.legend()
```

<p align="center">
    <img src="http://localhost:8080/naml/static/legend.png" width="500mm" />
</p>

</div>
<div class="column">

#### Hide `Axes`'s ticks

- **`axis`**: can be used to hide the ticks of an `Axes`:

```
fig, axes = plt.subplots()

axes.plot(np.sqrt(np.arange(100)))
axes.axis('off')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/hidden-axis.png" width="400mm" />
</p>

#### Set `Axes` aspect ratio

- **`axis`**: can be used to set the aspect ratio of an `Axes` to 1:1 :

```
fig, axes = plt.subplots()

theta = np.linspace(0, 2*np.pi, 100)
x = np.cos(theta)
y = np.sin(theta)

axes.plot(x, y, 'r:')
axes.axis('equal')
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/1-1-aspect-ratio.png" width="250mm" />
</p>

### More advanced stuff

#### 3D scatterplot

When performing a 3D plot we need to create a `Figure` and add an `Axes` to it in two separate phases. When we add the `Axes` object, the `projection` parameter of the `add_subplot` method allows to specify that we want a 3D plot:

```
fig = plt.figure()
axes = fig.add_subplot(projection = '3d')

np.random.seed(0)
u = np.random.normal(size = (100, 3))
axes.scatter(u[:, 0], u[:, 1], u[:, 2], marker = 'v',
    c = u[:, 0] * u[:, 1] * u[:, 2], s = np.max(u, axis = 1) * 10)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/3d-scatter.png" width="270mm" />
</p>

</div>
<div class="column">

Through the **`view_init`** method, we can move the virtual camera which produces the 3D plot: the `elev` parameter allows to specify the elevation angle in degrees which rotates the camera above the plane pierced by the vertical axis, the `azim` parameter allows to specify the angle in degrees which rotates the camera about the vertical axis, finally the `roll` parameter allows to specify the angle in degrees which rotates the camera about the viewing axis:

```
fig = plt.figure()
axes = fig.add_subplot(projection = '3d')

np.random.seed(0)
u = np.random.normal(size = (100, 3))
axes.scatter(u[:, 0], u[:, 1], u[:, 2], marker = 'v',
             c = u[:, 0] * u[:, 1] * u[:, 2],
             s = np.max(u, axis = 1) * 10)
axes.view_init(45, 45, 0)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/3d-scatter-different-view.png" width="270mm" />
</p>

#### Plotting shapes

##### Plotting circles

We can create a `Circle` `Patch` through the constructor provided in the `patches` package. Then we can add it to the `Axes` through the **`add_patch`** method (_when plotting circles, remember to set the aspect ration of the `Axes` to 1:1_):

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
fig, axes = plt.subplots()

import matplotlib.patches as patches

np.random.seed(0)
n = 20
r = np.random.uniform(1, 6, n) / 100
c = np.random.uniform(size = (n, 2))

for i in range(n):
    axes.add_patch(patches.Circle(c[i, :], radius = r[i],
                                  color = 'r', alpha = 0.5))

axes.axis('equal')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/circles.png" width="450mm" />
</p>

##### Plotting vectors

- **`arrow`**: allows to plot a vector (an arrow), the parameters `x` and `y` specify the coordinates of the arrow base, the `dx` and `dy` parameters specify the length of the arrow along `x` and `y` direction.

</div>
<div class="column">

```
fig, axes = plt.subplots()

axes.arrow(0, 1, 1, -1,
           head_width = 0.05, head_length = 0.05,
           length_includes_head = True,
           color = 'r')
axes.arrow(1, 0, 1, 1,
           head_width = 0.05, head_length = 0.05,
           length_includes_head = True,
           color = 'b')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/arrows.png" width="450mm" />
</p>

#### Plotting images

- **`imread`**: allows to read an image into a three-dimensional NumPy array. To each pixel correspond three values to represent its color with RGB encoding.

```
A_RGB = plt.imread("colorful-image.jpg")
```

- **`imshow`**: allows to plot images onto an `Axes`. The `cmap` parameter allows us to plot the image in gray scale.

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
A = A_RGB.mean(axis = 2)

fig, axes = plt.subplots()

axes.imshow(A, cmap = "gray")
axes.axis('off')
```

<p align="center">
    <img src="http://localhost:8080/naml/static/image.png" width="450mm" />
</p>

</div>
<div class="column">

#### Add colorbar

- **`colorbar`**: allows to add a color bar for a certain plot on an `Axes`. For example, it can add colorbars to images:

```
A_RGB = plt.imread("colorful-image.jpg")

fig, axes = plt.subplots()
img = axes.imshow(A_RGB)
axes.axis('off')

fig.colorbar(img, ax = axes)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/colorbar.png" width="450mm" />
</p>

</div>
</div>

---

## Other packages

<div class="multiple-columns">
<div class="column">

### `pandas`

#### Creating a `DataFrame`

We can create a `DataFrame` from a dictionary with NumPy arrays as values:
```
a = np.array([0, 1, 2])
b = np.array([11, 12, 3])
df = pd.DataFrame({
       "A": a,
       "B": b
})
```
Then, `df` is:
```
   A   B
0  0  11
1  1  12
2  2   3
```

- **`read_csv`**: constructs a `DataFrame` from a CSV file:
```
cat data.csv
```
```
A, B
0, 11
1, 12
```
```
df = pd.read_csv("data.csv")
```
Then, the value of `df` is:
```
   A   B
0  0  11
1  1  12
```

</div>
<div class="column">

#### Inspecting a `DataFrame`

- **`describe`**: returns several statistics about the `DataFrame`:
```
a = np.array([0, 1, 2])
b = np.array([11, 12, 3])
df = pd.DataFrame({
       "A": a,
       "B": b
})
```
> The output of `df.describe` is:
```
         A          B
count  3.0   3.000000
mean   1.0   8.666667
std    1.0   4.932883
min    0.0   3.000000
25%    0.5   7.000000
50%    1.0  11.000000
75%    1.5  11.500000
max    2.0  12.000000
```

- **`info`**: returns the number of non-null entries in each column and the corresponding type.
The value of `df.info()` for the `DataFrame` created above is:
```
RangeIndex: 3 entries, 0 to 2
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   A       3 non-null      int64
 1   B       3 non-null      int64
dtypes: int64(2)
memory usage: 180.0 bytes
```

</div>
<div class="column">

- **`head`**: returns the first `n` rows of the `DataFrame`. The default value of `n` is 5.
For example:
```
df = pd.DataFrame({
    "A": np.arange(16),
    "B": np.arange(4, 20)
})
```
> Then, `df.head()` is:
```
   A  B
0  0  4
1  1  5
2  2  6
3  3  7
4  4  8
```

#### Computing statistics on a `DataFrame`

- **`mean`**: returns the mean of the values in the columns of the `DataFrame`:

```
df = pd.read_csv("data.csv")
df_mean = df.mean()
```
> The value of `df_mean` is:
```
A      0.5
 B    11.5
dtype: float64
```
> Furthermore, we can subtract `df_mean` from `df`, obtaining a behavior similar to NumPy broadcasting:
```
centered_df = df - df_mean
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

> The value of `centered_df` is:
```
     A    B
0 -0.5 -0.5
1  0.5  0.5
```

- **`std`**: returns the sample standard deviation of the values in the columns the `DataFrame`:
```
df = pd.read_csv("data.csv")
centered_df = df - df.mean()
df_std = centered_df.std()
```
> Then, the value of `df_std` is:
```
A     0.707107
 B    0.707107
dtype: float64
```
> As with `mean`, we can divide `centered_df` by `df_std`, obtaining a behavior similar to NumPy broadcasting:
```
normalized_df = centered_df / df_std
```
> The value of `normalized_df` is:
```
          A         B
0 -0.707107 -0.707107
1  0.707107  0.707107
```

- **`corr`**: returns the pairwise (sample) correlation of the columns, excluding null values:
```
df = pd.read_csv("data.csv")
```

</div>
<div class="column">

> Then, the value of `df.corr()` is:
```
      A    B
A   1.0  1.0
 B  1.0  1.0
```

#### Accessing the columns of a `DataFrame`

- **`df["Column Name"]`**: returns the column named `ColumnName` in the `df` `DataFrame`:
```
df = pd.read_csv("data.csv")
```
> Then, the value of `df["A"]` is:
```
0    0
1    1
Name: A, dtype: int64
```

#### Some useful stuff

- **`nunique`**: returns the number of unique elements in the `df` column:
```
df = pd.read_csv("data.csv")
n = df["A"].nunique()
```
> Then, the value of `n` is:
```
2
```

- **`dropna`**: drops the rows of the `DataFrame` where at least the value of a column is missing:

</div>
<div class="column">

```
df = pd.DataFrame({
    "name": ['Alfred', 'Batman',
        'Catwoman'],
    "toy": [np.nan, 'Batmobile',
        'Bullwhip'],
    "born": [pd.NaT,
        pd.Timestamp("1940-04-25"),
        pd.NaT]})
```
> The value of `df` is:
```
       name        toy       born
0    Alfred        NaN        NaT
1    Batman  Batmobile 1940-04-25
2  Catwoman   Bullwhip        NaT
```
> Then, `df.dropna()` is:
```
     name        toy       born
1  Batman  Batmobile 1940-04-25
```

- **`to_numpy`**: converts a `DataFrame` into a bi-dimensional NumPy array:
```
df = pd.read_csv("data.csv")
A = df.to_numpy()
```
> Then, the value of `A` is:
```
array([[ 0, 11],
       [ 1, 12]])
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### `jax`
#### Performing "NumPy computations" in Jax
When we want to apply `jax` transformations to a function, this function must not have side-effects. Then, if we need to use NumPy functions with `jax`, we need to invoke the corresponding function from `jax.numpy`:
```
import jax.numpy as jnp

x = jnp.array([1, 2, 3])
y = jnp.array([4, 5, 6])
```
Then, the value of `jnp.dot(x, y)` is:
```
Array(32, dtype=int32)
```

#### Compile functions

- **`jit`**: compiles the function in input and returns the compiled version:
```
def f(x, y):
    return jnp.sqrt(jnp.dot(x**2, y**2))

jitted_f = jax.jit(f)
```
> The value of `jitted_f(jnp.array([1, 2, 3]), jnp.array([4, 5, 6]))`:
```
Array(20.976177, dtype=float32)
```

#### Automatic differentiation

- **`grad`**: returns a function which evaluates the gradient of the function in input. The `argnums` parameter allows to specify the argument w.r.t. which we differentiate.

</div>
<div class="column">

```
def f(x, y):
    return jnp.cos(x) + jnp.exp(y)

df_dy = jax.grad(f, argnums = 1)
```
Then, the value of `df_dy(1., 1.)` is:
```
Array(2.7182817, dtype=float32,
    weak_type=True)
```

- **`jacrev`**: returns a function which evaluates row-by-row the jacobian of the input function using reverse-mode AD:
```
def f(x):
    return jnp.sum(jnp.exp(x))

grad = jax.jacrev(f)
```
> The value of `grad(jnp.array([0., 0.]))` is:
```
Array([1., 1.], dtype=float32)
```

- **`jacfwd`**: returns a function which evaluates column-by-column the jacobian of the input function using forward-mode AD:
```
def f(x):
    return jnp.sum(jnp.exp(x))

grad = jax.jacrev(f)
hess = jax.jacfwd(grad)
```
> The value of `hess(jnp.array([0., 0.]))` is:

</div>
<div class="column">

```
Array([[1., 0.],
       [0., 1.]], dtype=float32)
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">



</div>
<div class="column">

### **`numpy.fft`**

- **`fft`**: computes the Discrete Fourier Transform (DFT) of the input discrete signal. We can put an additional argument zero pad the signal, the argument is the length of the padded signal:
```
k = np.ones(10) / 10
v = np.sin(10 * np.linspace(-10*np.pi,
    10*np.pi, 1000))

V = np.fft.fft(v)
K = np.fft.fft(k, v.size)
```
Let $X$ be the DFT of the input signal. The array returned by `fft` is:
$$
[X[0], X[1], ..., X[\frac{n_x}{2}-1], X[-\frac{n_x}{2}], ..., X[-1]] \text{ if } n_x \text{ is even,}
$$
$$
[X[0], X[1], ..., X[\frac{n_x-1}{2}], X[-\frac{-(n_x-1)}{2}], ..., X[-1]] \text{ if } x_x \text{ is odd.}
$$

Furthermore (_see [https://math.stackexchange.com/questions/1585060/sampling-fourier-transform-and-discrete-fourier-transform](https://math.stackexchange.com/questions/1585060/sampling-fourier-transform-and-discrete-fourier-transform)_) if some hypotheses are verified:
$$
X[k] \approx f_s X_{cont}(k f_0)
$$
where we assume that:

</div>
<div class="column">

- the discrete signal $\underline{x}$ has been sampled from the continuos signal $x_{cont}$;
- the time instant corresponding to $\underline{x}[n_x - 1]$ minus the time instant corresponding to $\underline{x}[0]$ is $T_0$;
- $\underline{x}[i] = x_{cont}(t_0 + i T_s)$;
- $f_0 = \frac{1}{T_0}$;
- $f_s = \frac{1}{T_s}$.

That is, the DFT is an "approximated sample" of the continuous Fourier transform.
Hence, if we want to plot the DFT as to resemble the continuous FT, we need to assign the elements returned by `fft` to the corresponding frequence (achieved through `fftfreq`), and then plot them in the right order (achieved through `fftshift`).

- **`fftfreq`**: returns the DFT sample frequencies. It provides an additional `d` paramter to specify the value of $T_s$, the default value is 1. .

Now, if we try to plot, the DFT without any additional step, we get the following result:
```
v = np.zeros(100)
v[25:50] = 1
V = np.fft.fft(v)

fig, axes = plt.subplots()
freq = np.fft.fftfreq(v.size)
axes.plot(freq, np.abs(V))
```

<p align="center">
    <img src="http://localhost:8080/naml/static/not-shifted-ft.png" width="240mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

To solve the problem (as anticipated), we have to use `fftshift`:
- **`fftshift`**: shifts the zero-frequency component to the center of the spectrum (in particular it swaps the two halves of the input array).

Now, the result is:
```
v = np.zeros(100)
v[25:50] = 1
V = np.fft.fft(v)

fig, axes = plt.subplots()
freq = np.fft.fftfreq(v.size)
axes.plot(np.fft.fftshift(freq), np.fft.fftshift(np.abs(V)))
```

<p align="center">
    <img src="http://localhost:8080/naml/static/ft.png" width="270mm" />
</p>

- **`ifft`**: computes the inverse DFT of the input array.
(_Note that, when plotting the reconstructed signal, we **have to take the real part**_).
```
v = np.zeros(100)
v[25:50] = 1
V = np.fft.fft(v)
v_rec = np.real(np.fft.ifft(V))
fig, axes = plt.subplots()
axes.set_title("IDFT reconstruction")
axes.plot(v_rec, 'k-', label = "Reconstructed signal")
axes.plot(v, 'r:', label = "Original signal")
axes.legend()
```

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/idft-reconstruction.png" width="400mm" />
</p>

We can also work with 2D data (for exmaple, images).

- **`fft2`**: applies the 2D fft to the input data.
- **`ifft2`**: applies the 2D ifft to the input data.

```
# Create a 2D signal
T_s = 0.1
x = np.arange(-2*np.pi, 2*np.pi, T_s)
y = np.arange(-2*np.pi, 2*np.pi, T_s)
xx, yy = np.meshgrid(x, y)
f1 = 1
f2 = 2
z = np.sin(2*np.pi*f1*xx) + np.sin(2*np.pi*f2*yy)

# Perform the 2D FT
Z = np.fft.fft2(z)
shifted_Z = np.fft.fftshift(Z)

shifted_freq_x = np.fft.fftshift(np.fft.fftfreq(x.size, d = T_s))
shifted_freq_y = np.fft.fftshift(np.fft.fftfreq(y.size, d = T_s))
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
# Perform the 2D IFT
z_reconstructed = np.fft.ifft2(Z)

# Plotting
fig, axes = plt.subplots(nrows = 1, ncols = 3)
axes[0].set_title("Original")
axes[0].imshow(z)
axes[0].axis("off")

axes[1].set_title("FFT")
axes[1].imshow(np.absolute(shifted_Z))
axes[1].axis("off")

axes[2].set_title("Reconstructed")
axes[2].imshow(np.real(z_reconstructed))
axes[2].axis("off")
```

<p align="center">
    <img src="http://localhost:8080/naml/static/2D-ft.png" width="500mm" />
</p>


### `seaborn`

Seaborn is a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
We can import it through:
```
import seaborn as sns
```


- **`displot`**: plots a univariate o bivariate distribution:

</div>
<div class="column">

```
np.random.seed(0)
data = pd.DataFrame({
    "A": 1 + 2 * np.random.normal(size = 100),
    "B": -2 + 3 * np.random.normal(size = 100)
})
```
```
sns.displot(data["A"])
```

<p align="center">
    <img src="http://localhost:8080/naml/static/univariate-displot.png" width="230mm" />
</p>

```
sns.displot(data)
```

<p align="center">
    <img src="http://localhost:8080/naml/static/bivariate-displot.png" width="300mm" />
</p>

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

- **`scatterplot`**: produces a scatter plot:
```
np.random.seed(0)
data = pd.DataFrame({
    "A": 1 + 2 * np.random.normal(size = 100),
    "B": -2 + 3 * np.random.normal(size = 100),
    "C": np.arange(100)
})

sns.scatterplot(data = data, x = "A" ,y = "B", hue = "C")
```

<p align="center">
    <img src="http://localhost:8080/naml/static/seaborn-scatter.png" width="300mm" />
</p>

- **`heatmap`**: can be used to visualize the covariance matrix of a data set as a heat map. The parameter `annot` set to `True` adds the corresponding numeric value to every rectangle of the heat map.

```
np.random.seed(0)
U = 2 * np.random.normal(size = (100, 2))
data = pd.DataFrame({
    "A": U[:, 0],
    "B": U[:, 1],
    "C": 0.1 * U[:, 0] - 0.05 * U[:, 1],
    "D": U[:, 0] * U[:, 1]
})

sns.heatmap(data.corr(), annot = True)
```

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/correlation-heatmap.png" width="500mm" />
</p>

- **violinplot**: performs a violin plot of the input data on the given `Axes`. A violin plot depicts the quartiles along with the "smoothed" distribution:

```
np.random.seed(0)
U = 2 * np.random.normal(size = (10000, 2))
data = pd.DataFrame({
    "A": U[:, 0],
    "B": U[:, 1],
    "C": 0.1 * U[:, 0] - 0.05 * U[:, 1],
    "D": U[:, 0] * U[:, 1],
    "E": np.arange(10000) / 500
})

fig, axes = plt.subplots()
axes.set_title("Violin plot")
sns.violinplot(data = data, ax = axes)
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/violin-plot.png" width="500mm" />
</p>

- **`jointplot`**: performs a joint plot:
```
actual = np.random.uniform(size = 100)
predicted = actual + 0.1 * np.random.normal(size = 100)

data = pd.DataFrame({
    "Actual": actual,
    "Predicted": predicted
})

sns.jointplot(data = data, x = "Actual", y = "Predicted")
```

</div>
<div class="column">

<p align="center">
    <img src="http://localhost:8080/naml/static/joint-plot.png" width="500mm" />
</p>

</div>
</div>

---

## Methods & Algorithms

<div class="multiple-columns">
<div class="column">

### SVD

#### Compute the _cumulate fraction_ and _fraction of explained variance_ of singular values

(_See lab 1_).
Let $k$ be the number of singular values.
The $i$-th **_cumulate fraction_** is:
$$\frac{\sum_{j=1}^i \sigma_j}{\sum_{j=1}^k \sigma_j}$$
The $i$-th **_fraction of explained variance_** is:
$$\frac{\sum_{j=1}^i \sigma_j^2}{\sum_{j=1}^k \sigma_j^2}$$

```
_, s, _ = np.linalg.svd(A, full_matrices = False)

cumulate_fraction = s.cumsum() / s.sum()

fract_expl_variance = (s**2).cumsum() / (s**2).sum()
```

#### Compute the _best rank $k$_ approximation

```
def best_rank_k(U, s, V_T, k):
    if k > s.size: raise ValueError()
    return U[:, :k] @ np.diag(s[:k]) @ V_T[:k, :]
```

#### Randomized SVD

(_See lecture 5.15_).
Let $A \in \mathbb{R}^{m \times n}$
We start by sampling $k + p$ (where $p$ is an oversampling factor) normal vectors, and we put them in the matrix $\Omega \in \mathbb{R^{n \times (k + p)}}$.
Then, the column space of $Y = (A A^T)^q A \Omega$ is a "sample" of the column space of $A$, but the singular values of $Y$ are $\sigma_k^q$ where $\sigma_k$ are the singular values of $A$ (this improves the result).
Let's apply QR factorization to $Y$: $\:QR = Y$.
The columns of $Q = [\underline{q}_1 ... \underline{q}_n]$ are an orthonormal basis for the column space of $Y$.

</div>
<div class="column">

Hence, $QQ^T = [\underline{q}_1 \underline{q}_1^T ... \underline{q}_n \underline{q}_n^T ]$ is a projection matrix onto the column space of $Y$.
Then, since $C(Y) \approx C(A_k)$, it follows that $QQ^TA \approx A_k$.  Let $B = Q^T A$. By the SVD $B = \tilde{U} \Sigma V^T$. Hence $A_k \approx Q \tilde{U} \Sigma V^T$.

```
def rSVD(A, k, q, p):
    omega = np.random.normal(size = (A.shape[1], k + p))
    Y = A @ omega
    for _ in range(q):
        Y = A @ A.T @ Y
    Q = np.linalg.qr(Y)[0][:, :k]
    B = Q.T @ A
    U_tilde, s, V_T = np.linalg.svd(B)
    return Q @ U_tilde, s, V_T
```

### PCA

#### PCA where _rows are samples_

(_See lecture 10.1_).
Let $A \in \mathbb{R}^{m \times n}$. Let $\overline{A}$ be $A$ after the centering.
$$C = \frac{1}{m} \overline{A}^T \overline{A}$$
is the sample covariance matrix, which has the same eigenvectors of $\overline{A}^T \overline{A}$.
Let $U \Sigma V^T = \overline{A}$, then, the eigenvectors of $C$ are (by how the SVD is defined) the columns of $V$, which we call **principal directions**.
The **principal components** are the coordinates of the data, w.r.t. the principal directions. If we want to put them on rows as the original data matrix: $\Phi = \overline{A} V$.

```
def PCA(A, k):
    if k > A.shape[1]: raise ValueError
    centered_A = A - A.mean(axis = 0)
    _, _, V_T = np.linalg.svd(centered_A)
    princ_dir = V_T.T[:, :k]
    princ_comp = centered_A @ princ_dir
    
    return princ_comp, princ_dir
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### PCA where _columns are samples_

Let $A \in \mathbb{R}^{m \times n}$.
Let $\overline{A}$ be $A$ after the centering.
$$C = \frac{1}{n} \overline{A} \overline{A}^T$$
is the sample covariance matrix, which has the same eigenvectors of $\overline{A} \overline{A}^T$.
Let $U \Sigma V^T = \overline{A}$, then, the eigenvectors of $C$ are (by how the SVD is defined) the columns of $U$, which we call **principal directions**.
The **principal components** are the coordinates of the data, w.r.t. the principal directions. If we want to put them on columns as the original data matrix: $\Phi = U^T \overline{A}$.

```
def PCA(A, k):
    if k > A.shape[0]: raise ValueError
    centered_A = A - A.mean(axis = 1)[:, np.newaxis]
    U, _, _ = np.linalg.svd(centered_A)
    princ_dir = U[:, :k]
    princ_comp = U.T @ centered_A
    
    return princ_comp, princ_dir
```

### Binary classifier evaluation

(_See lab 2_).
From the predicated and actual labels, we can compute the **_confusion matrix_**:
```
def confusion_matrix(predicted_labels, actual_labels,
                     false_class_val, true_class_val):
    true_positives = np.logical_and(
        actual_labels == true_class_val,
        predicted_labels == true_class_val
    ).sum()
    false_positives = np.logical_and(
        actual_labels == false_class_val,
        predicted_labels == true_class_val
    ).sum()
    true_negatives = np.logical_and(
        actual_labels == false_class_val,
        predicted_labels == false_class_val).sum()
```

</div>
<div class="column">

```
    false_negatives = np.logical_and(
        actual_labels == true_class_val,
        predicted_labels == false_class_val
    ).sum()
    return true_positives, false_positives, \
        true_negatives, false_negatives
```

From the confusion matrix, we can compute the **_accuracy_** of the classifier:
```
def accuracy(true_positives, false_positives,
             true_negatives, false_negatives):
    return (true_positives + true_negatives) / \
        (true_positives + false_positives +
         true_negatives + false_negatives)
```

#### Classifiers with output $[0, 1]$ (not $\{0, 1\}$)

In this case the evaluation of the accuracy takes into account also the "confidence" of the classification:
```
def accuracy(predicted_labels, actual_labels):
    true_positives = predicted_labels[actual_labels == 1]
    true_negatives = 1 - predicted_labels[actual_labels == 0]
    return (jnp.sum(true_positives) + jnp.sum(true_negatives)) / \
        actual_labels.size
```

### Multi-class classifier evaluation

We compute accuracy as the number of correct classifications over the number of samples (in analogy to the definition for binary classification). The function below computes the accuracy when the classifier is a NN:

```
def accuracy(x, y, params):
    # Assumes samples on the rows
    return jnp.mean(np.argmax(ANN(x, params), axis = 1) \
        == np.argmax(y, axis = 1))
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Singular Value Truncation (SVT)

(_See lecture 7.16_).

```
def SVT(A, omega, tau, tol):
    def overwrite_known_values(X, A, omega):
        for i, j in omega:
            X[i, j] = A[i, j]
    
    X = np.zeros(A.shape)
    overwrite_known_values(X, A, omega)
    while True:
        X_old = X.copy()
        U, s, V_T = np.linalg.svd(X, full_matrices = False)
        s[s <= tau] = 0
        X = U @ np.diag(s) @ V_T
        overwrite_known_values(X, A, omega)
        
        if np.linalg.norm(X - X_old) < tol:
            break
    
    return X
```

</div>
<div class="column">



</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Computing the pseudoinverse

(_See lecture 7.9_).
Let $A = U \Sigma V^T$. Then $A^+ = V \Sigma^+ U^T$, where $\Sigma^+$ is the result of **transposing** $\Sigma$ and taking the **reciprocal** of the non-null values on the diagonal. (If we exploit the "reduced" form, with the meaning intended in NumPy by putting `full_matrices = False`, we don't need to take the transpose of $\Sigma$ (since it is diagonal)).

```
def pinv(A):
    U_r, s, V_T_r = np.linalg.svd(A, full_matrices = False)
    s[s > 0] = 1 / s[s > 0]
    return V_T_r.T @ np.diag(s) @ U_r.T
```

### Least Squares (LS)

(_See lecture 7.10_).
We can solve LS through the pseudoinverse: $\hat{\underline{w}} = X^+ y$.
In particular, to have a linear affine model (instead of a purely linear one), we can enrich the feature vector with a constant feature of value $1$: $X_{ext} = \left[ \begin{matrix} X & \underline{1} \end{matrix} \right]$.
Then $\hat{\underline{w}} = X_{ext}^+ y$.
```
def LS(X, y):
    X_ext = np.block([X, np.ones((X.shape[0], 1))])
    return np.linalg.pinv(X_ext) @ y
```

#### Ridge regression

(_See lecture 8.7_).
The model result from ridge regression with hyperparameter $\lambda > 0$ is:
$$
\hat{\underline{w}}_{RR} = (X^TX + \lambda I)^{-1} X^T \underline{y} \text{ .}
$$

```
def RR(X, y, lam):
    X_ext = np.block([X, np.ones((X.shape[0], 1))])
    return np.linalg.solve(
        X_ext.T @ X_ext + lam * np.identity(X_ext.shape[1]),
        X_ext.T @ y
    )
```

</div>
<div class="column">

#### Kernel regression

(_See lecture 9.10_).
Let $X \in \mathbb{R}^{n \times p}$. We want to enrich the available features through a feature map $\phi(\underline{x_i})$ which provides "non-linear" features.
Let $k(\underline{x}_i, \underline{x}_j) = f(g(\underline{x}_i, \underline{x}_j))$ where $g : \mathbb{R}^p \times \mathbb{R}^p \rightarrow \mathbb{R}$ has complexity $O(p)$, be a kernel function s.t. $k(\underline{x}_i, \underline{x}_j) = \phi(\underline{x}_i)^T \phi(\underline{x}_j)$.
Let $\Phi = \phi(X)$ (_$\phi$ applied to every row_). Hence
$$
K = \left[ \begin{matrix}
k(\underline{x}_1, \underline{x}_1) & ... & k(\underline{x}_1, \underline{x}_n) \\
... & ... & ... \\
k(\underline{x}_n, \underline{x}_1) & ... & k(\underline{x}_n, \underline{x}_n)
\end{matrix} \right] = \Phi \Phi^T \text{ .}
$$

Through algebraic manipulation, we can rewrite the ridge regression model as (we use $\Phi$ instead of $X$):
$$
\underline{\hat{w}}_{KR} = \Phi^T U (\Sigma \Sigma^T + \lambda I)^{-1} U^T \underline{y} \text{ .}
$$
Let $\underline{\alpha} = U (\Sigma \Sigma^T + \lambda I)^{-1} U^T y$. Then $\underline{\hat{w}}_{KR} = \Phi^T \underline{\alpha} = \sum \alpha_i \phi(\underline{x}_i)$.

By applying the SVD to $\Phi$ it is easy to see that
$$
\underline{\alpha} = U (\Sigma \Sigma^T + \lambda I)^{-1} U^T y = (\Phi \Phi^T + \lambda I)^{-1} \underline{y} \text{ .}
$$
Then
$$
\underline{\alpha} = (K + \lambda I)^{-1} \underline{y} \text{ .}
$$
Finally, we can perform predictions without having to explicitly compute $\Phi$:
$$
y_{pred} = \phi(\underline{x})^T \underline{\hat{w}}_{RR} = \phi(\underline{x})^T \Phi^T \underline{\alpha} = [ k(\underline{x}, \underline{x}_1) ... k(\underline{x}, \underline{x}_n) ] \underline{\alpha} = \sum \alpha_i k(\underline{x}, \underline{x}_i) \text{ .}
$$

If we want to predict an entire vector from the data $\tilde{X} \in \mathbb{R}^{l \times p}$:
$$
\underline{\tilde{y}} = \left[ \begin{matrix}
k(\underline{x}_1, \underline{x}_1) & ... & k(\underline{x}_1, \underline{x}_n) \\
... & ... & ... \\
k(\underline{x}_l, \underline{x}_1) & ... & k(\underline{x}_l, \underline{x}_n)
\end{matrix} \right] \underline{\alpha} = \tilde{K} \underline{\alpha} \text{ .}
$$
</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
def KR(X, y, k, lam):
    K = np.array([[
        k(X[i, :], X[j, :])
        for j in range(X.shape[0]) ]
        for i in range(X.shape[0]) ])
    return np.linalg.solve(
        K + lam * np.identity(X.shape[0]),
        y
    )
```

```
def KR_pred(X_tilde, X, alpha, k):
    K_tilde = np.array([[
        k(X_tilde[i, :], X[j, :])
        for j in range(X.shape[0]) ]
        for i in range(X_tilde.shape[0]) ])
    return K_tilde @ alpha
```

### AutoDiff with dual numbers

Dual numbers are defined as follows: $\mathbb{D} = (\mathbb{R}^2, +_D, \cdot_D)$ where:
- $(x_1, x_2) +_D (y_1, y_2) = (x_1 + y_1, x_2 + y_2)$;
- $(x_1, x_2) \cdot_D (y_1, y_2) = (x_1 \cdot y_1, x_1 \cdot y_2 + y_1 \cdot x_2)$.

We define $\epsilon = (0, 1) \in \mathbb{D}$. Then $\epsilon^2 = 0$. (This allows us to write dual numbers as $x_1 + \epsilon x_2$).
We define the **extension** of a function $f : \mathbb{R} \rightarrow \mathbb{R}$ to $\mathbb{D}$ as:
$$
\begin{matrix}
\hat{f} : \mathbb{D} \rightarrow \mathbb{D} \\
(x_1, x_2) \mapsto (f(x_1), f'(x_1)x_2)
\end{matrix}
$$
$\hat{f}$ has a lot of good properties:
- $\hat{(f + g)}(x_1, x_2) = \hat{f}(x_1, x_2) +_D \hat{g}(x_1, x_2)$;
- $\hat{(f \cdot g)}(x_1, x_2) = \hat{f}(x_1, x_2) \cdot_D \hat{g}(x_1, x_2)$;
- $\hat{\frac{1}{f}}(x_1, x_2) = \frac{1}{\hat{f}(x_1, x_2)}$ (_the reciprocal is taken in $\mathbb{D}$_);
- $\hat{(f \circ g)}(x_1, x_2) = \hat{f} \circ \hat{g} (x_1, x_2)$;
- $\hat{id_\mathbb{R}} = id_\mathbb{D}$.

</div>
<div class="column">

Then, if $f$ is the composition of sum, products and reciprocals of functions $g_i$ for which we know the derivative, we can compute $\hat{g_i}$ through the definition, and then $\hat{f}$ is obtained by performing sum, products and reciprocals **in $\mathbb{D}$**.

Finally $\hat{f}(x_1, 1) = (f(x_1), f'(x_1))$.

Let's put everything in a library:

```
class DualNumber:
    def __init__(self, real, dual):
        # dual number: 'real' + 'dual' * eps
        self.real = real
        self.dual = dual

    def __add__(self, other):
        # implement the operation "self + other"
        if isinstance(other, DualNumber):
            return DualNumber(self.real + other.real,
                self.dual + other.dual)
        else:
            return DualNumber(self.real + other, self.dual)

    def __radd__(self, other):
        # implement the operation "other + self"
        return self.__add__(other)

    def __sub__(self, other):
        # implement the operation "self - other"
        if isinstance(other, DualNumber):
            return DualNumber(self.real - other.real,
                self.dual - other.dual)
        else:
            return DualNumber(self.real - other, self.dual)

    def __rsub__(self, other):
        # implement the operation "other - self"
        return DualNumber(other, 0) - self
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
    def __mul__(self, other):
        # implement the operation "self * other"
        if isinstance(other, DualNumber):
            return DualNumber(self.real * other.real,
            self.dual * other.real + self.real * other.dual)
        else:
            return DualNumber(other * self.real, other * self.dual)

    def __rmul__(self, other):
        # implement the operation "other * self"
        return self.__mul__(other)

    def __truediv__(self, other):
        # implement the operation "self / other"
        if isinstance(other, DualNumber):
            return DualNumber(self.real / other.real,
                (self.dual * other.real - \
                self.real * other.dual) / (other.real ** 2))
        else:
            return (1/other) * self

    def __rtruediv__(self, other):
        # implement the operation "other / self"
        return DualNumber(other, 0.0).__truediv__(self)

    def __pow__(self, other):
        # implement the operation "self ** other"
        # f^g = e^(g log f) => (f^g)' = e^(g log f) *
        # (g' * log f + g * 1/f * f') =
        # = f^g * (g' * log f + g/f * f')
        if isinstance(other, DualNumber):
            return DualNumber(self.real ** other.real,
                self.real ** other.real * (other.dual * \
                np.log(self.real) + other.real / self.real \
                 * self.dual))
        else:
            return DualNumber(self.real ** other,
                other * (self.real ** (other - 1)) * self.dual)
```

</div>
<div class="column">

```
    def __repr__(self):
        return repr(self.real) + ' + ' + repr(self.dual) + 'ε'
```

Then, we can extend usual functions to $\mathbb{D}$:

```
def sin(x):
    if isinstance(x, DualNumber):
        return DualNumber(np.sin(x.real), np.cos(x.real) * x.dual)
    else:
        return np.sin(x)

def cos(x):
    if isinstance(x, DualNumber):
        return DualNumber(np.cos(x.real), -np.sin(x.real) * x.dual)
    else:
        return np.cos(x)

def exp(x):
    if isinstance(x, DualNumber):
        return DualNumber(np.exp(x.real), np.exp(x.real) * x.dual)
    else:
        return np.exp(x.real)
```

Finally, we can perform AutoDiff as follows:

```
def auto_diff(f, x):
    return f(DualNumber(x, 1)).dual
```

### Convolutions
#### Direct formula
(_See lecture 12, add-on to convolutions, and lab 5_).
Let $\underline{k}$ be a vector of $n_k$ elements and $\underline{v}$ be a vector of $n_v$ elements. We assume that $n_k \leq n_v$ ($\underline{k}$ is known as _kernel_).
In particular the $(i+1)$-th element of $\underline{k}$ is $\underline{k}[i]$, same for $\underline{v}$ (that is, we index starting from 0).

From _add-on to convolutions, page 2_, we can compute the convolution between $\underline{k}$ and $\underline{v}$ as:

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

$$
(\underline{k} * \underline{v})[i] = \sum_{j = \max(0, i-n_v+1)}^{\min(i, n_k-1)} \underline{k}[j] \underline{v}[i-j] \text{ for } i \in \{ 0, ..., n_k+n_v-2 \} \text{ .}
$$

```
def conv(k, v):
    return np.array([
        np.array([
            k[j] * v[i - j]
            for j in range(
                max(0, i - v.size + 1),
                min(i, k.size - 1) + 1
            )
        ]).sum()
        for i in range(k.size + v.size - 1)])
```

The definition of circular convolution is extended to $\underline{k}$ and $\underline{v}$ of different size by making $\underline{k}$ of the same size of $\underline{v}$ through zero padding:
$$
\tilde{\underline{k}}^T = [ \underline{k}^T \: \underline{0}_{n_v - n_k}^T ] \text{ .}
$$
That is:
$$
(\underline{k} \circledast \underline{v})[i] =^{def} (\tilde{\underline{k}} \circledast \underline{v})[i] \text{ for } i \in \{ 0, ..., n_v - 1 \} \text{ .}
$$
From _lecture 12.4_:
$$
(\tilde{\underline{k}} \circledast \underline{v})[i] = \begin{cases}
\sum_{j = 0}^{i} \tilde{\underline{k}}[j] \underline{v}[i-j] + \sum_{j=i+1}^{n_v-1} \tilde{\underline{k}}[j]\underline{v}[i+n_v-j] \text{ if } i \in \{ 0, ..., n_v-2 \} \\
\sum_{j = 0}^{n_v-1} \tilde{\underline{k}}[j]\underline{v}[i-j] \text{ if } i = n_v-1
\end{cases} \text{ .}
$$
Now let $i \geq n_k-1$, $i < n_v-1$, then, if $j \geq i+1 \geq n_k$, it follows that $\tilde{\underline{k}}[j] = 0$.
Hence:
$$
(\tilde{\underline{k}} \circledast \underline{v})[i] = \sum_{j = 0}^{n_k-1} \underline{k}[j] \underline{v}[i-j] + \sum_{j = n_k}^{i} 0 \underline{v}[i-j] + \sum_{j=i+1}^{n_v-1} 0 \underline{v}[i+n_v-j] = \sum_{j = 0}^{n_k-1} \underline{k}[j] \underline{v}[i-j] =
$$
$$
= \sum_{j = \max(0, i-n_v+1)}^{\min(i, n_k-1)} \underline{k}[j] \underline{v}[i-j] = (\underline{k} * \underline{v})[i] \text{ .}
$$

Analogously: $(\tilde{\underline{k}} \circledast \underline{v})[n_v - 1] = (\underline{k} * \underline{v})[n_v - 1]$.

</div>
<div class="column">

That is:
$$
(\tilde{\underline{k}} \circledast \underline{v})[i] = (\tilde{\underline{k}} \circledast \underline{v})[i] \forall i \in \{ n_k-1, ..., n_v-1 \} \text{ .}
$$

We define **valid** this "_portion_" of the circular convolution which is equal to the "standard" (linear) one.

Furthermore, from _lecture 12.5_:
$$
(\tilde{\underline{k}} \circledast \underline{v})[i] = \sum_{j = 0}^{n_v - 1} \tilde{\underline{k}}[j] \underline{v}[(i-j)\mod n] = \sum_{j = 0}^{n_k - 1} \underline{k}[j] \underline{v}[(i-j)\mod n] \text{ for } i \in \{ 0, ..., n_v-1 \} \text{ .}
$$

```
def circular_conv(k, v):
    if k.size > v.size: raise ValueError
    return np.array([
        (k * v[(i - np.arange(k.size)) % v.size]).sum()
        for i in range(v.size)])
```

Now computing the "valid convolution" is straightforward:
```
def valid_conv(k, v):
    return circular_conv(k, v)[k.size - 1:]
```

#### Toeplitz matrices

By _add-on to convolutions, page 4_, we can compute the convolution between $\underline{k}$ and $\underline{v}$ (where $n_k \leq n_v$) with the Toeplitz matrix with first column:
$$
\underline{c} = \left[ \begin{matrix} \underline{k} \\ \underline{0}_{n_v-1} \end{matrix} \right]
$$
and first row:
$$
\underline{r} = \left[ \begin{matrix} \underline{k}[0] \\ \underline{0}_{n_v-1} \end{matrix} \right] \text{ .}
$$

We can create Toeplitz matrices with **`scipy.linalg.toeplitz`**:
```
from scipy.linalg import toeplitz
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
def toeplitz_conv(k, v):
    if k.size > v.size: raise ValueError
    c = np.zeros(k.size + v.size - 1)
    c[:k.size] = k
    r = np.zeros(v.size)
    r[0] = k[0] # Not needed
    K = toeplitz(c, r)
    return K @ v
```

#### DFT

From the convolution rule, we have that:
$$
\mathcal{F}(\tilde{\underline{k}} \circledast \underline{v}) = \mathcal{F}(\tilde{\underline{k}}) \odot \mathcal{F}(\underline{v}) \text{ .}
$$

```
def DFT_conv(k, v):
    if k.size > v.size: raise ValueError
    V = np.fft.fft(v)
    K = np.fft.fft(k, v.size)
    K_conv_V = K * V
    return np.real(np.fft.ifft(K_conv_V))
```

#### `scipy.signal.convolve`

`scipy` offers a method for computing the "valid convolution":
```
from scipy import signal
k_valid_conv_v = signal.convolve(v, k, mode = 'valid')
```

</div>
<div class="column">

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Hessian related stuff

#### Computing the hessian

Observe that:
$$
H = H^T = \left[ \begin{matrix}
\frac{\partial}{\partial x_1} (\frac{\partial f}{\partial x_1}) & ... & \frac{\partial}{\partial x_n} (\frac{\partial f}{\partial x_1}) \\
... & ... & ... \\
\frac{\partial}{\partial x_1} (\frac{\partial f}{\partial x_n}) & ... & \frac{\partial}{\partial x_n} (\frac{\partial f}{\partial x_n})
\end{matrix} \right] = 
\frac{\partial}{\partial \underline{x}} \left[ \begin{matrix}
\frac{\partial f}{\partial x_1} \\
... \\
\frac{\partial f}{\partial x_n}
\end{matrix} \right] =
\frac{\partial}{\partial \underline{x}} \nabla f = \frac{\partial}{\partial \underline{x}} (\frac{\partial}{\partial \underline{x}} f)^T \text{ .}
$$

Hence, we can use `jax.jacrev` and `jax.jacfwd` to compute the hessian. Note that, when applied to a function with values in $\mathbb{R}$, `jax.jacrev` returns a function which computes the jacobian and returns it as a one-dimensional array. Then, the difference between $(\frac{\partial}{\partial \underline{x}} f)^T$ and $\frac{\partial}{\partial \underline{x}} f$ is immaterial.

```
hess = jax.jacfwd(jax.jacrev(f))
```

#### Hessian vector product

Observe that:
$$
\Phi = (\nabla f)^T \underline{v}
$$
$$
\nabla_{\underline{x}} \Phi = \left[ \begin{matrix}
\frac{\partial}{\partial x_1}[(\nabla f)^T \underline{v}] \\
... \\
\frac{\partial}{\partial x_n}[(\nabla f)^T \underline{v}]
\end{matrix} \right] =
\left[ \begin{matrix}
\frac{\partial}{\partial x_1}[v_1 \frac{\partial f}{\partial x_1} + ... + v_n \frac{\partial f}{\partial x_n}] \\
... \\
\frac{\partial}{\partial x_n}[v_1 \frac{\partial f}{\partial x_1} + ... + v_n \frac{\partial f}{\partial x_n}]
\end{matrix} \right] =
$$
$$
= \left[ \begin{matrix}
\frac{\partial}{\partial x_1} (\frac{\partial f}{\partial x_1}) & ... & \frac{\partial}{\partial x_1} (\frac{\partial f}{\partial x_n}) \\
... & ... & ... \\
\frac{\partial}{\partial x_n} (\frac{\partial f}{\partial x_1}) & ... & \frac{\partial}{\partial x_n} (\frac{\partial f}{\partial x_n})
\end{matrix} \right] \left[ \begin{matrix} v_1 \\ ... \\ v_n \end{matrix} \right] = H \underline{v}
$$

Then, we can compute the hessian vector product in a smart way:
```
grad = jax.grad(f)
phi = lambda x, v: jnp.dot(grad(x), v)

hess_vec_product = jax.grad(phi, argnums = 0)
```

</div>
<div class="column">



</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Neural networks
#### Parameters initialization
##### Glorot Normal initialization

It works as follows:
- inizialize the biases with zero value;
- inizialize the weights sampling from a normal distribution with zero mean and with standard deviation 

$$
\sqrt{\frac{2}{n + m}}
$$
where $n$ and $m$ are the number of input and output neurons of the corresponding weights matrix.

```
def glorot_normal_params_init(layers_size):
    np.random.seed(0)
    params = [ ]
    for i in range(len(layers_size) - 1):
        n = layers_size[i]
        m = layers_size[i + 1]
        W = np.sqrt(2/(n+m)) * np.random.normal(size = (m, n))
        b = np.zeros(shape = (m, 1))
        params += [ W, b ]
    return params
```

#### Neural network definition

The following function implements a feed-forward NN with the parameters in a list with this structure: $[W_1, \underline{b}_1, ..., W_l, \underline{b}_l]$. It works with **row vectors** (that is, if we put in input a matrix, the inputs are the rows).

```
def ANN(x, params):
    # Define the activation function as
    # a global variable `activ`
    
    num_layers = int(len(params)/2) + 1
    W = params[0::2]
    b = params[1::2]
```

</div>
<div class="column">

```

    layer = x.T
    for i in range(num_layers - 1):
        layer = W[i] @ layer + b[i]
        if i < num_layers - 2:
            layer = activ(layer)
        else:
            # Last layer
            ...
    return layer.T
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### Activation functions

- **Soft-max**

$$
\hat{z}_i = \frac{e^{z_i}}{\sum_{j=1}^n e^{z_j}}
$$

```
def softmax(layer):
    l = jnp.exp(layer)
    return l / jnp.sum(l, axis = 0)
```

</div>
<div class="column">



</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Loss functions
#### MSE

$$
\mathcal{L}(x, y, \theta) = \frac{1}{N} \sum_{i=1}^{N} (y_i - ANN_\theta(x_i))^2
$$

```
def mse_loss(x, y, params):
    return jnp.mean((y - ANN(x, params))**2)
```

#### Binary classification cross-entropy

$$
\mathcal{L}(x, y, \theta) = \frac{1}{N} \sum_{i=1}^{N} - (y_i \log(p_i) + (1 - y) \log(1 - p_i))
$$

$$
\text{where } p_i = ANN_\theta(x_i)
$$

```
def x_entropy_loss(x, y, params):
    y_pred = ANN(x, params)
    return -jnp.mean((1-y)*jnp.log(1-y_pred) + \
        y*jnp.log(y_pred))
```

#### Multi-class classification cross-entropy

$$
\mathcal{L}(x, y, \theta) = \frac{1}{N} \sum_{i=1}^{N} - \sum_{c=1}^M y_i[c] \log(p_i[c])
$$

$$
\text{where } p_i = ANN_\theta(x_i)
$$

```
def m_x_entropy_loss(x, y, params):
    # Assumes samples on the rows 
    return -jnp.mean(jnp.sum(y * jnp.log(ANN(x, params)),
        axis = 1))
```

</div>
<div class="column">



</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Training
#### Helper functions

Let's list some helper functions.
- **`UpdatablePlot`**: allows the training algorithm to update the plot during the trainings.
```
from IPython import display

class UpdatablePlot():
    def __init__(self, title, progress_quantity, max_progress,
                 delta_prog_upd = 100):
        self.title = title
        self.progress_quantity = progress_quantity
        self.max_progress = max_progress
        self.delta_prog_upd = delta_prog_upd
        
        _, self.axes = plt.subplots()
        
        self.progress = 0
        self.data = {}
        
        self.__update()
    
    PLOTTING_STYLES = [ 'b-', 'r-', 'k-', 'g:' ]
    LEFT_LIM = 0.1
    RIGHT_LIM_MARGIN = 10
    
    def __update(self):
        self.axes.clear()
        self.axes.set_title(f'{self.title}' +
            f' ({self.progress}/{self.max_progress})')
        self.axes.set_xlabel(self.progress_quantity)
        i = 0
        plotted = False
        for quantity in self.data:
            self.axes.loglog(self.data[quantity][:self.progress],
                           self.PLOTTING_STYLES[i],
                           label = quantity)
            plotted = True
```

</div>
<div class="column">

```
            i += 1
            i %= len(self.PLOTTING_STYLES)
        self.axes.set_xlim(self.LEFT_LIM, self.progress +
            self.RIGHT_LIM_MARGIN)
        if plotted:
            self.axes.legend()
        
        display.display(plt.gcf())
        display.clear_output(wait = True)
        
        self.last_upd_progress = self.progress
    
    def make_progress(self, progress, data):
        if progress < self.progress: raise ValueError
        self.progress = progress
        self.data = data
        
        if (self.progress - self.last_upd_progress >= \
            self.delta_prog_upd or self.progress == \
                self.max_progress) and self.progress >= 2:
            self.__update()
```

- **`update_history`**: updates the data structure used to store the history of loss functions during the training.

```
def update_history(history, losses, params):
    for loss_name, loss in losses:
        history[loss_name].append(loss(x, y, params))
```

> The version below plots the losses on both training and validation set (**see next page**):
```
def update_history(history, losses, params):
    for loss_name, loss in losses:
        history[f"{loss_name} (train)"].append(loss(x_train, y_train,
                                                  params))
        history[f"{loss_name} (valid)"].append(loss(x_valid, y_valid,
                                                  params))
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

> In case you want to use an history on both training and validation set, remember to update `history` initialization in the training algorithm:
```
history = { ext_loss_name: [ ] for loss_name, _ in losses
            for ext_loss_name in [ f"{loss_name} (train)",
                                   f"{loss_name} (valid)"] }
```

</div>
<div class="column">



</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### 1st order methods

- **Gradient descent (GD)**

$$
g^{(e)} = \frac{1}{N} \sum_{i = 1}^N \nabla_\theta \mathcal{L}(x_i, y_i, \theta^{(e)})
$$

$$
\theta^{(e+1)} = \theta^{(e)} - \lambda g^{(e)}
$$

```
def gd(layers_size, learning_rate, num_epochs):
    # Define the ANN function as
    # a global function `ANN`.
    
    # Analogously define the parameters'
    # initialization function as `params_init`.
    
    # Put the loss functions in a list:
    # `losses = [ ("Loss name", loss_func), ... ]`;
    # the first one, is the one that will be used for
    # the training.
    
    # Define the function `update_history`.
    
    # Put input and output in the global
    # variables `x` and `y` respectively.
    
    upd_plot = UpdatablePlot("Training", "epochs",
            num_epochs)
    
    jitted_losses = [ ]
    for i in range(len(losses)):
        jitted_losses.append((losses[i][0], jax.jit(losses[i][1])))
    
    history = { loss_name: [ ] for loss_name, _ in losses }
    
    params = params_init(layers_size)
    
    update_history(history, losses, params)
    
    jitted_grad = jax.jit(jax.grad(losses[0][1], argnums = 2))
```

</div>
<div class="column">

```
    
    for e in range(num_epochs):
        g = jitted_grad(x, y, params)
        for i in range(len(params)):
            params[i] -= learning_rate * g[i]
        
        update_history(history, jitted_losses, params)
        
        upd_plot.make_progress(e + 1, history)
    
    return params
```

- **Stochastic gradient descent (SGD)**

$$
\lambda_e = \max(\lambda_{\min}, \lambda_{\max}(1-\frac{e}{E}))
$$

$$
g^{(e)} = \frac{1}{|I_e|} \sum_{i \in I_e} \nabla_\theta \mathcal{L}(x_i, y_i, \theta^{(e)}) \text{ where } I_e \subset \{ 1, ..., N \} \text{ sampled uniformly }
$$

$$
\theta^{(e+1)} = \theta^{(e)} - \lambda_e g^{(e)}
$$

```
def sgd(layers_size, learning_rate_min, learning_rate_max,
        learning_rate_decay, num_epochs, batch_size):
    # Define the ANN function as
    # a global function `ANN`.
    
    # Analogously define the parameters'
    # initialization function as `params_init`.
    
    # Put the loss functions in a list:
    # `losses = [ ("Loss name", loss_func), ... ]`;
    # the first one, is the one that will be used for
    # the training.
    
    # Define the function `update_history`.
    
    # Put input and output in the global
    # variables `x` and `y` respectively.
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
    
    upd_plot = UpdatablePlot("Training", "epochs",
            num_epochs)
    
    jitted_losses = [ ]
    for i in range(len(losses)):
        jitted_losses.append((losses[i][0], jax.jit(losses[i][1])))
    
    history = { loss_name: [ ] for loss_name, _ in losses }
    
    params = params_init(layers_size)
    
    update_history(history, losses, params)
    
    jitted_grad = jax.jit(jax.grad(losses[0][1], argnums = 2))
    
    for e in range(num_epochs):
        learning_rate = np.maximum(learning_rate_min,
            learning_rate_max * (1 - e/learning_rate_decay))
        for _ in range(int(x.shape[0] / batch_size)):
            I = np.random.choice(x.shape[0], batch_size)
            g = jitted_grad(x[I, :], y[I, :], params)
            for i in range(len(params)):
                params[i] -= learning_rate * g[i]
        
        update_history(history, jitted_losses, params)
        
        upd_plot.make_progress(e + 1, history)
    
    return params
```

- **SGD with momentum**

$$
\lambda_e = \max(\lambda_{\min}, \lambda_{\max}(1-\frac{e}{E}))
$$

$$
g^{(e)} = \frac{1}{|I_e|} \sum_{i \in I_e} \nabla_\theta \mathcal{L}(x_i, y_i, \theta^{(e)}) \text{ where } I_e \subset \{ 1, ..., N \} \text{ sampled uniformly }
$$

$$
v^{(e+1)} = \alpha v^{(e)} - \lambda_e g^{(e)}, v^{(0)} = 0
$$

</div>
<div class="column">

$$
\theta^{(e+1)} = \theta^{(e)} + v^{(e+1)}
$$

```
def momentum(layers_size, learning_rate_min, learning_rate_max,
        learning_rate_decay, num_epochs, batch_size, alpha = 0.9):
    # Define the ANN function as
    # a global function `ANN`.
    
    # Analogously define the parameters'
    # initialization function as `params_init`.
    
    # Put the loss functions in a list:
    # `losses = [ ("Loss name", loss_func), ... ]`;
    # the first one, is the one that will be used for
    # the training.
    
    # Define the function `update_history`.
    
    # Put input and output in the global
    # variables `x` and `y` respectively.
    
    upd_plot = UpdatablePlot("Training", "epochs",
            num_epochs)
    
    jitted_losses = [ ]
    for i in range(len(losses)):
        jitted_losses.append((losses[i][0], jax.jit(losses[i][1])))
    
    history = { loss_name: [ ] for loss_name, _ in losses }
    
    params = params_init(layers_size)
    
    update_history(history, losses, params)
    
    jitted_grad = jax.jit(jax.grad(losses[0][1], argnums = 2))
    
    velocity = [ np.zeros(param.shape) for param in params ]
    
    for e in range(num_epochs):
        learning_rate = np.maximum(learning_rate_min,
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
            learning_rate_max * (1 - e/learning_rate_decay))
        for _ in range(int(x.shape[0] / batch_size)):
            I = np.random.choice(x.shape[0], batch_size)
            g = jitted_grad(x[I, :], y[I, :], params)
            for i in range(len(params)):
                velocity[i] = alpha * velocity[i] - \
                    learning_rate * g[i]
                params[i] += velocity[i]
        
        update_history(history, jitted_losses, params)
        
        upd_plot.make_progress(e + 1, history)
    
    return params
```

- **AdaGrad**

$$
g^{(e)} = \frac{1}{|I_e|} \sum_{i \in I_e} \nabla_\theta \mathcal{L}(x_i, y_i, \theta^{(e)}) \text{ where } I_e \subset \{ 1, ..., N \} \text{ sampled uniformly }
$$

$$
r^{(e+1)} = r^{(e)} + g^{(e)} \odot g^{(e)}, r^{(0)} = 0
$$

$$
\theta^{(e+1)} = \theta^{(e)} - \frac{\lambda}{\delta + \sqrt{r^{(e+1)}}} \odot g^{(e)}
$$

```
def adagrad(layers_size, learning_rate, num_epochs,
            batch_size, delta = 1e-7):
    # Define the ANN function as
    # a global function `ANN`.
    
    # Analogously define the parameters'
    # initialization function as `params_init`.
    
    # Put the loss functions in a list:
    # `losses = [ ("Loss name", loss_func), ... ]`;
    # the first one, is the one that will be used for
    # the training.
    
    # Define the function `update_history`.
```

</div>
<div class="column">

```
    
    # Put input and output in the global
    # variables `x` and `y` respectively.
    
    upd_plot = UpdatablePlot("Training", "epochs",
            num_epochs)
    
    jitted_losses = [ ]
    for i in range(len(losses)):
        jitted_losses.append((losses[i][0], jax.jit(losses[i][1])))
    
    history = { loss_name: [ ] for loss_name, _ in losses }
    
    params = params_init(layers_size)
    
    update_history(history, losses, params)
    
    jitted_grad = jax.jit(jax.grad(losses[0][1], argnums = 2))
    
    cumul_square_grad = [ np.zeros(param.shape) for param in params ]
    
    for e in range(num_epochs):
        for _ in range(int(x.shape[0] / batch_size)):
            I = np.random.choice(x.shape[0], batch_size)
            g = jitted_grad(x[I, :], y[I, :], params)
            for i in range(len(params)):
                cumul_square_grad[i] += g[i]**2
                params[i] -= learning_rate / \
                    (delta + np.sqrt(cumul_square_grad[i])) * g[i]
        
        update_history(history, jitted_losses, params)
        
        upd_plot.make_progress(e + 1, history)
    
    return params
```

- **RMSProp**

$$
g^{(e)} = \frac{1}{|I_e|} \sum_{i \in I_e} \nabla_\theta \mathcal{L}(x_i, y_i, \theta^{(e)}) \text{ where } I_e \subset \{ 1, ..., N \} \text{ sampled uniformly }
$$

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

$$
r^{(e+1)} = \rho r^{(e)} + (1 - \rho) g^{(e)} \odot g^{(e)}, r^{(0)} = 0
$$

$$
\theta^{(e+1)} = \theta^{(e)} - \frac{\lambda}{\delta + \sqrt{r^{(e+1)}}} \odot g^{(e)}
$$

```
def rms_prop(layers_size, learning_rate, num_epochs,
             batch_size, decay_rate, delta = 1e-7):
    # Define the ANN function as
    # a global function `ANN`.
    
    # Analogously define the parameters'
    # initialization function as `params_init`.
    
    # Put the loss functions in a list:
    # `losses = [ ("Loss name", loss_func), ... ]`;
    # the first one, is the one that will be used for
    # the training.
    
    # Define the function `update_history`.
    
    # Put input and output in the global
    # variables `x` and `y` respectively.
    
    upd_plot = UpdatablePlot("Training", "epochs",
            num_epochs)
    
    jitted_losses = [ ]
    for i in range(len(losses)):
        jitted_losses.append((losses[i][0], jax.jit(losses[i][1])))
    
    history = { loss_name: [ ] for loss_name, _ in losses }
    
    params = params_init(layers_size)
    
    update_history(history, losses, params)
    
    jitted_grad = jax.jit(jax.grad(losses[0][1], argnums = 2))
    
    cumul_square_grad = [ np.zeros(param.shape) for param in params ]
```

</div>
<div class="column">

```
    
    for e in range(num_epochs):
        for _ in range(int(x.shape[0] / batch_size)):
            I = np.random.choice(x.shape[0], batch_size)
            g = jitted_grad(x[I, :], y[I, :], params)
            for i in range(len(params)):
                cumul_square_grad[i] = decay_rate * \
                    cumul_square_grad[i] + (1 - decay_rate) * \
                        g[i] ** 2
                params[i] -= learning_rate / \
                    (delta + np.sqrt(cumul_square_grad[i])) * g[i]
        
        update_history(history, jitted_losses, params)
        
        upd_plot.make_progress(e + 1, history)
    
    return params
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### 2nd order methods

- **Newton method**

$$
x^{(e+1)} = x^{(e)} - H^{-1} \nabla f
$$

```
from jax.config import config
config.update("jax_enable_x64", True)

def newton_method(f, x_guess, num_epochs, tol):
    x = x_guess.copy()
    
    jitted_f = jax.jit(f)
    jitted_grad = jax.jit(jax.grad(f))
    jitted_hess = jax.jit(jax.jacfwd(jax.jacrev(f)))
    
    upd_plot = UpdatablePlot("Training", "epoch", num_epochs, 1)
    data = { "$f$": [ jitted_f(x) ] }
    
    for e in range(num_epochs):
        g = jitted_grad(x)
        H = jitted_hess(x)
        incr = np.linalg.solve(H, -g)
        x += incr
        
        if np.linalg.norm(incr) < tol:
            break
        
        data["$f$"].append(jitted_f(x))
        
        upd_plot.make_progress(e + 1, data)
    
    return x
```

- **BFGS**

(_See [Wikipedia](https://en.wikipedia.org/wiki/Broyden%E2%80%93Fletcher%E2%80%93Goldfarb%E2%80%93Shanno_algorithm)_).

$$
p^{(e)} = - B_e^{-1} \nabla f(x^{(e)})
$$

$$
\alpha_e = \arg \min f(x^{(e)} + \alpha p^{(e)}) \text{ (in practice, we do a line search)}
$$

</div>
<div class="column">

$$
s^{(e)} = \alpha_e p^{(e)}
$$

$$
x^{(e+1)} = x^{(e)} + s^{(e)}
$$

$$
y^{(e)} = \nabla f(x^{(e+1)}) - \nabla f(x^{(e)})
$$

$$
\rho = \frac{1}{(y^{(e)})^T s^{(e)}}
$$

$$
E = I - \rho y^{(e)} (s^{(e)})^T
$$

$$
B_{e+1}^{-1} = E^T B_e^{-1} E + \rho s^{(e)} (s^{(e)})^T
$$

```
from jax.config import config
config.update("jax_enable_x64", True)
from scipy.optimize import line_search

def BFGS(f, x_guess, num_epochs, tol):
    x = x_guess.copy()
    
    jitted_f = jax.jit(f)
    jitted_grad = jax.jit(jax.grad(f))
    
    upd_plot = UpdatablePlot("Training", "epoch", num_epochs, 1)
    data = { "$f$": [ jitted_f(x) ] }
    
    g = jitted_grad(x)
    B_inv = np.identity(x.size)
    
    for e in range(num_epochs):
        p = - B_inv @ g
        alpha = line_search(jitted_f, jitted_grad, x, p)[0]
        
        if alpha is None:
            break
        
        s = alpha * p
        x += s
        data["$f$"].append(jitted_f(x))
        upd_plot.make_progress(e + 1, data)
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

```
        y = jitted_grad(x) - g
        
        rho = 1. / np.dot(y, s)
        E = np.identity(x.size) - rho * np.outer(y, s)
        B_inv = E.T @ B_inv @ E + rho * np.outer(s, s)
        
        if np.linalg.norm(g) < tol:
            break
        
        g += y
    
    return x
```

</div>
<div class="column">



</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

#### Regularization

- **$L^2$ regularization**

We achieve $L^2$ regularization by adding a penalty term:
$$
MSW = \frac{1}{N_w} \sum_{i=1}^{N_w} w_i^2
$$
to the loss function (where $N_w$ is the number of weights, $w_i$ is the $i$-th weight).

```
def msw(params):
    n_w = 0.
    squared_w_sum = 0.
    for W in params[0::2]:
        squared_w_sum += (W**2).sum()
        n_w += W.size
    return squared_w_sum / n_w
```

The "regularized" loss function is:
$$
\mathcal{L}_{reg}(x, y, \theta) = \mathcal{L}(x, y, \theta) + \beta MSW(\theta)
$$

```
def l2_regularization(loss, beta):
    # Define the `msw` global function
    return lambda x, y, params: loss(x, y, params) + \
        beta * msw(params)
```

We can use the following function to compare different values of the penalry coefficient $b$:

```
def train_for_every_beta(betas, loss, loss_name):
    # Define a Callable `training_method` (use a lambda function)
    loss_train = [ ]
    loss_valid = [ ]
    mean_squared_w = [ ]
    
    
    for beta in betas:
        losses[0] = (f"Regularized {loss_name}",
```

</div>
<div class="column">

```
                     l2_regularization(loss, beta))
        params = training_method()
        loss_train.append(loss(x_train, y_train, params))
        loss_valid.append(loss(x_valid, y_valid, params))
        mean_squared_w.append(msw(params))
    
    return loss_train, loss_valid, mean_squared_w
```

The result of the above function can be used to plot the "Tikhonov L-curve" (MSE (train) vs MSW):

```
# Tikhonov L-curve (MSE (train) vs MSW)
fig, axes = plt.subplots()
axes.set_title("MSE (train) vs MSW")
axes.plot(loss_train, mean_squared_w, 'bo-')
```

</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">

### Adversarial attack

In an aversarial attack we sligthly modify the input in the direction given by the gradient of the loss function (to "maximize" the loss associated to the small modifiaction).

```
def adversarial_attack(x, y, params, alpha):
    # Define the `losses` list as for the training methods
    dir = jax.grad(losses[0][1], argnums = 0)(x, y, params)
    return x + alpha * dir
```

Then, we can compute the new prediction:
```
ANN(adversarial_attack(x, y, params, alpha), params)
```

</div>
<div class="column">



</div>
</div>

---

<div class="multiple-columns without-title">
<div class="column">



</div>
<div class="column">



</div>
<div class="column">



</div>
</div>