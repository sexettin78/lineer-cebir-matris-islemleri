import sympy as sp

# Matris tanımlama
A = sp.Matrix([
    [2, 1, -3, 4, 7],
    [0, 5, -4, -2, 1],
    [4, 1, 6, -3, 1],
    [3, -2, 1, 5, 2],
    [1, -1, 2, 1, -1]
])

# Adjugate matrisin hesaplanması
adjA = A.adjugate()

# Ters matrisin hesaplanması
A_inv = A.inv()

# Determinantın hesaplanması
det_A = A.det()

print("Matris A:")
sp.pprint(A)

print("\nAdjugate Matris (adjA):")
sp.pprint(adjA)

print("\nTers Matris (A^-1):")
sp.pprint(A_inv)

# Cofaktörlerin hesaplanması ve yazdırılması
rows, cols = A.shape
print("\nCofactors:")
cofactors = A.cofactor_matrix()
sp.pprint(cofactors)

print("\nDeterminant of A:")
sp.pprint(det_A)
