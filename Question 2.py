def matrix_multiply(A, B):
    if len(A[0]) != len(B):
        return "Error: Matrices are not multipliable"
    
    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i+1} of the matrix: ").split()))
        if len(row) != cols:
            raise ValueError("Incorrect number of columns in row")
        matrix.append(row)
    return matrix

rows_A = int(input("Enter the number of rows for matrix A: "))
cols_A = int(input("Enter the number of columns for matrix A: "))
A = input_matrix(rows_A, cols_A)

rows_B = int(input("Enter the number of rows for matrix B: "))
cols_B = int(input("Enter the number of columns for matrix B: "))
B = input_matrix(rows_B, cols_B)

result = matrix_multiply(A, B)
print("Result:" if result != "Matrices are not multipliable" else result)
if result != "Matrices are not multipliable":
    for row in result:
        print(" ".join(map(str, row)))