import sympy as sp

# Değişkenleri tanımla
x, y, z = sp.symbols('x y z')

# Denklem sistemini oluştur
denklemler = [
    2*x + y - 3*z - 5,
    3*x - 2*y + 2*z - 5,
    5*x - 3*y - z - 16
]

# Denklem sistemini çöz
çözümler = sp.linsolve(denklemler, x, y, z)

print("Çözüm kümesi:")
for çözüm in çözümler:
    print(f"x = {çözüm[0]}, y = {çözüm[1]}, z = {çözüm[2]}")
