import numpy as np

# Initializing global variables 
row = 0
column = 0

# Function to input matrix from user
def matrix():
    # Ask user for dimensions of the matrix
    row = int(input("No. of rows: "))
    column = int(input("No. of columns: "))

    # Total number of values needed for the matrix
    total = row * column
    print(f"Enter {total} values (row-wise):")

    a = []  # List to store the input values
    for i in range(total):
        x = float(input(f"Value {i+1}: "))  # Take each value as float
        a.append(x)

    # Convert list to NumPy array and reshape it to matrix
    mat = np.array(a).reshape(row, column)
    return mat  # Return the matrix

# Taking input for Matrix A
print("For Matrix A\n")
matA = matrix()

# Taking input for Matrix B
print("For Matrix B\n")
matB = matrix()

# Displaying both matrices
print("\nMatrix A:")
print(matA)
print("\nMatrix B:")
print(matB)

# Function to perform matrix addition
def addition():
    if matA.shape == matB.shape:  # Check if dimensions match
        print(f"MatA + MatB:\n{np.add(matA, matB)}")
    else:
        print("Can't perform addition: Matrices must have the same dimensions.")

# Function to perform matrix subtraction
def subtraction():
    if matA.shape == matB.shape:  # Check if dimensions match
        print(f"MatA - MatB:\n{np.subtract(matA, matB)}")
    else:
        print("Can't perform subtraction: Matrices must have the same dimensions.")

# Function to perform matrix multiplication
def multiply():
    try:
        print(f"MatA * MatB:\n{matA @ matB}")  # @ is matrix multiplication operator
    except ValueError:
        print("Can't perform multiplication: Number of columns in A must equal number of rows in B.")

# Function to calculate determinant (only for square matrices)
def determinant():
    # Determinant for Matrix A
    if matA.shape[0] == matA.shape[1]:  # Check if A is square
        print(f"Determinant of Matrix A: {np.linalg.det(matA)}")
    else:
        print("Matrix A is not square, can't compute determinant.")

    # Determinant for Matrix B
    if matB.shape[0] == matB.shape[1]:  # Check if B is square
        print(f"Determinant of Matrix B: {np.linalg.det(matB)}")
    else:
        print("Matrix B is not square, can't compute determinant.")

# Call all operations
addition()
subtraction()
multiply()
determinant()
