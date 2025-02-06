'''
ufuncs (short for Universal Functions) in NumPy are functions that perform element-wise operations on ndarrays (NumPy arrays). They provide a convenient way to apply mathematical operations to entire arrays, rather than having to iterate over each element manually.

Why Use ufuncs?
Vectorization:
ufuncs allow you to perform operations on arrays without the need for explicit loops. This is called vectorization, and it leads to faster code execution, especially on large datasets.

Broadcasting:
ufuncs support broadcasting, which means they can operate on arrays of different shapes and sizes by expanding the smaller array to match the shape of the larger array.

Additional Features:

reduce: Apply an operation across the elements of an array (e.g., summing all elements).
accumulate: Keep a running total as the operation is applied to the array.
where: Conditionally apply operations based on a boolean array.
dtype: Specify the data type of the output.

What is Vectorization?

What are ufuncs?
ufuncs (short for Universal Functions) in NumPy are functions that perform element-wise operations on ndarrays (NumPy arrays). They provide a convenient way to apply mathematical operations to entire arrays, rather than having to iterate over each element manually.

Why Use ufuncs?
Vectorization:
ufuncs allow you to perform operations on arrays without the need for explicit loops. This is called vectorization, and it leads to faster code execution, especially on large datasets.

Broadcasting:
ufuncs support broadcasting, which means they can operate on arrays of different shapes and sizes by expanding the smaller array to match the shape of the larger array.

Additional Features:

reduce: Apply an operation across the elements of an array (e.g., summing all elements).
accumulate: Keep a running total as the operation is applied to the array.
where: Conditionally apply operations based on a boolean array.
dtype: Specify the data type of the output.
What is Vectorization?
Vectorization refers to converting loop-based operations into operations that can be performed on entire arrays or vectors. For example, instead of iterating over the elements of two lists to sum them, you can use a vectorized operation to do it all at once. This is much faster be
cause modern CPUs are optimized for such parallel computations.

'''
import numpy as np

#adding elements in two arrays
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

for i, j in zip(x, y):
  z.append(i + j)
print(z)

#ufunc for the above

w = np.add(x, y)

print(w)