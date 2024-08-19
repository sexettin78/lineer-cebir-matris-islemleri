import sympy as sp

# Değişkenleri tanımla
x, y, z, w = sp.symbols('x y z w')

# Denklem sistemini oluştur
denklemler = [
    x + y + 2*z + 3*w - 13,
    x - 2*y + z + w - 8,
    3*x + y + z - w - 1
]

# Denklem sistemini çöz
çözümler = sp.linsolve(denklemler, x, y, z, w)

print("Çözüm kümesi:")
for çözüm in çözümler:
    print(f"x = {çözüm[0]}, y = {çözüm[1]}, z = {çözüm[2]}, w = {çözüm[3]}")
