import sympy as sp

# Matris tanımlama
A = sp.Matrix([
    [1, 2, -3, 4],
    [2, 3, -8, 5],
    [2, 6, 2, 6]
])

# İndirgenmiş eşolan matrisin hesaplanması
rref_matrix, pivot_columns = A.rref()

print("İndirgenmiş Eşolan Matris (RREF):")
sp.pprint(rref_matrix)

print("\nPivot Sütunlar:")
print(pivot_columns)
