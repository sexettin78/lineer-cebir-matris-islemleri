import sympy as sp

# Değişkenleri tanımla
x, y, z, k = sp.symbols('x y z k')

# Denklem sistemini oluştur
denklemler = [
    x + 0*y - 3*z + 3,
    2*x + k*y + 3*z + 2,
    5*x + 9*y + k*z - 1
]

# Denklem sistemini çöz
çözümler = sp.linsolve(denklemler, x, y, z)

print("Çözüm kümesi:")
for çözüm in çözümler:
    print(f"x = {çözüm[0]}, y = {çözüm[1]}, z = {çözüm[2]}")
