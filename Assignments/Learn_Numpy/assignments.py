import numpy as np

# 1. Create an Array
arr1 = np.arange(10, 55, 5)
print("Array 1:", arr1)
print("Shape:", arr1.shape)
print("Size:", arr1.size)
print("Data type:", arr1.dtype)

# 2. Generate a Matrix with Random Values
arr2 = np.random.randint(1, 101, (4, 5))
print("\nArray 2:\n", arr2)
print("Max value:", arr2.max(), "at index", np.unravel_index(arr2.argmax(), arr2.shape))
print("Min value:", arr2.min(), "at index", np.unravel_index(arr2.argmin(), arr2.shape))

# 3. Reshape an Array
arr3 = np.arange(1, 25)
matrix3 = arr3.reshape(4, 6)
print("\nMatrix 3:\n", matrix3)
print("2nd row:", matrix3[1])
print("3rd column:", matrix3[:, 2])

# 4. Boolean Indexing
arr4 = np.random.randint(0, 51, 15)
print("\nOriginal Array 4:", arr4)
arr4[arr4 > 25] = -1
print("Modified Array 4:", arr4)

# 5. Mathematical Operations
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# 6. Statistical Computations
arr6 = np.random.rand(5, 5)
print("\nArray 6:\n", arr6)
print("Mean:", np.mean(arr6))
print("Median:", np.median(arr6))
print("Variance:", np.var(arr6))
print("Standard Deviation:", np.std(arr6))

# 7. Matrix Multiplication
A = np.arange(1, 7).reshape(3, 2)
B = np.arange(7, 13).reshape(2, 3)
print("\nMatrix A:\n", A)
print("Matrix B:\n", B)
C = A @ B 
print("Result of A @ B:\n", C)

# 8. Slice and Modify
arr8 = np.arange(1, 37).reshape(6, 6)
print("\nOriginal Array 8:\n", arr8)
arr8[2:5, 2:5] = 0
print("Modified Array 8:\n", arr8)

# 9. Use of np.where
arr9 = np.array([5, 10, 15, 20, 25])
result9 = np.where(arr9 > 15, 99, 0)
print("\nArray 9 Result:", result9)

# 10. Broadcasting Example
arr10 = np.full((4, 4), 10)
sub = np.array([0, 1, 2, 3])
print("\nOriginal Array 10:\n", arr10)
result10 = arr10 - sub  # broadcasting
print("Broadcasted Result:\n", result10)