from sympy import Matrix, pprint, pretty

# Define the matrix using a list of lists
M = Matrix([
    [6, -1, 0,0, 30],
    [-1, 9, -4, 0, 20],
    [0, -4, 7, -2, 40],
    [0, 0, -2, 7, 10]
])

# Use the 
# .rref() method to row reduce
rref_matrix, pivot_columns = M.rref()
rref_matrix = rref_matrix.evalf()

pprint(M)
print("Row Reduced Matrix:")
pprint(rref_matrix)
print("\nPivot Column Indices:")
print(pivot_columns)