import sympy as sp

# Değişkenleri tanımla
x, y, z, w, t = sp.symbols('x y z w t')

# Denklem sistemini oluştur
denklemler = [
    x + 2*y - 3*z - 2*w + 4*t - 1,
    2*x + 5*y - 8*z - w + 6*t - 4,
    x + 4*y - 7*z + 5*w + 2*t - 8
]

# Denklem sistemini çöz
çözümler = sp.linsolve(denklemler, x, y, z, w, t)

print("Çözüm kümesi:")
for çözüm in çözümler:
    print(f"x = {çözüm[0]}, y = {çözüm[1]}, z = {çözüm[2]}, w = {çözüm[3]}, t = {çözüm[4]}")
