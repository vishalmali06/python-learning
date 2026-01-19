"""
NumPy Array Operations – Beginner Friendly Demo
Author: Vishal Mali
Purpose: Learn how NumPy arrays work and why they are powerful
"""

import numpy as np

# -------------------------------------------------
# 1️⃣ Creating NumPy Arrays
# -------------------------------------------------

# Create a 1D array from a Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:", arr1)

# Create a 2D array (matrix)
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])
print("\n2D Array:\n", arr2)

# Create array using arange (similar to range)
arr3 = np.arange(0, 10, 2)  # start, stop, step
print("\narange array:", arr3)

# -------------------------------------------------
# 2️⃣ Array Properties
# -------------------------------------------------

print("\nArray shape:", arr2.shape)     # rows, columns
print("Array size:", arr2.size)         # total elements
print("Array dimensions:", arr2.ndim)   # number of dimensions
print("Data type:", arr2.dtype)         # data type of elements

# -------------------------------------------------
# 3️⃣ Creating Special Arrays
# -------------------------------------------------

zeros_arr = np.zeros((2, 3))  # 2 rows, 3 columns
ones_arr = np.ones((3, 2))
full_arr = np.full((2, 2), 9)

print("\nZeros array:\n", zeros_arr)
print("\nOnes array:\n", ones_arr)
print("\nFull array:\n", full_arr)

# -------------------------------------------------
# 4️⃣ Array Indexing & Slicing
# -------------------------------------------------

arr = np.array([10, 20, 30, 40, 50])

print("\nFirst element:", arr[0])
print("Last element:", arr[-1])
print("Slice [1:4]:", arr[1:4])

# 2D indexing
print("\nElement at row 1, col 2:", arr2[1, 2])

# -------------------------------------------------
# 5️⃣ Vectorized Operations (No Loops!)
# -------------------------------------------------

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("\nAddition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)

# -------------------------------------------------
# 6️⃣ Mathematical Functions
# -------------------------------------------------

nums = np.array([1, 4, 9, 16])

print("\nSquare root:", np.sqrt(nums))
print("Sum:", np.sum(nums))
print("Mean:", np.mean(nums))
print("Max:", np.max(nums))
print("Min:", np.min(nums))

# -------------------------------------------------
# 7️⃣ Reshaping Arrays
# -------------------------------------------------

reshape_arr = np.arange(1, 13)
reshaped = reshape_arr.reshape(3, 4)  # 3 rows, 4 columns

print("\nOriginal array:", reshape_arr)
print("Reshaped array:\n", reshaped)

# -------------------------------------------------
# 8️⃣ Boolean Masking (Very Important)
# -------------------------------------------------

data = np.array([5, 10, 15, 20, 25])

# Get values greater than 15
filtered = data[data > 15]
print("\nValues greater than 15:", filtered)

# -------------------------------------------------
# 9️⃣ Copy vs View
# -------------------------------------------------

original = np.array([1, 2, 3])

view_arr = original.view()
copy_arr = original.copy()

view_arr[0] = 100

print("\nOriginal after view change:", original)
print("View array:", view_arr)
print("Copy array:", copy_arr)

# -------------------------------------------------
# 🔟 Why NumPy is Fast (Key Concept)
# -------------------------------------------------
"""
NumPy arrays:
✔ Store data in contiguous memory
✔ Avoid Python object overhead
✔ Use C-level operations internally
✔ Enable vectorization
"""

print("\n✔ NumPy operations completed successfully!")
