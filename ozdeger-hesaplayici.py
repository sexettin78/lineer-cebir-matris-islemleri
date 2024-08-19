import sympy as sp

# Değişken tanımlama
λ = sp.symbols('λ')

# Orijinal matrisi tanımla
A = sp.Matrix([
    [3, -1, 1],
    [7, -5, 1],
    [6, -6, 2]
])

# Karakteristik polinomun hesaplanması
char_poly = A.charpoly(λ)
print("Karakteristik polinom:")
sp.pprint(char_poly)

# Polinomun köklerini bul
eigenvalues = char_poly.all_roots()

# Özdeğerleri yazdır
print("Özdeğerler:")
for eigenvalue in eigenvalues:
    print(eigenvalue)
