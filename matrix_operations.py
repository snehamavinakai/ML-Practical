import numpy as np

def input_matrix(rows, cols):
    """Function to input a matrix of given dimensions."""
    print(f"Enter the elements for a {rows}x{cols} matrix:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1} (space-separated): ").split()))
        matrix.append(row)
    return np.array(matrix)

def display_matrix(matrix, name="Matrix"):
    """Function to display a matrix."""
    print(f"{name}:")
    print(matrix)

def main():
    print("Matrix Operations: Addition, Subtraction, Multiplication, Transpose")
    
    # Input dimensions for matrices
    rows1 = int(input("Enter the number of rows for Matrix A: "))
    cols1 = int(input("Enter the number of columns for Matrix A: "))
    rows2 = int(input("Enter the number of rows for Matrix B: "))
    cols2 = int(input("Enter the number of columns for Matrix B: "))
    
    # Input matrices
    print("\nMatrix A:")
    matrix_a = input_matrix(rows1, cols1)
    print("\nMatrix B:")
    matrix_b = input_matrix(rows2, cols2)
    
    # Display matrices
    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    
    # Matrix addition
    if rows1 == rows2 and cols1 == cols2:
        addition = matrix_a + matrix_b
        display_matrix(addition, "Addition (A + B)")
    else:
        print("Matrix addition not possible (dimensions do not match).")
    
    # Matrix subtraction
    if rows1 == rows2 and cols1 == cols2:
        subtraction = matrix_a - matrix_b
        display_matrix(subtraction, "Subtraction (A - B)")
    else:
        print("Matrix subtraction not possible (dimensions do not match).")
    
    # Matrix multiplication
    if cols1 == rows2:
        multiplication = np.dot(matrix_a, matrix_b)
        display_matrix(multiplication, "Multiplication (A x B)")
    else:
        print("Matrix multiplication not possible (columns of A != rows of B).")
    
    # Transpose
    transpose_a = matrix_a.T
    transpose_b = matrix_b.T
    display_matrix(transpose_a, "Transpose of A")
    display_matrix(transpose_b, "Transpose of B")

if __name__ == "__main__":
    main()
