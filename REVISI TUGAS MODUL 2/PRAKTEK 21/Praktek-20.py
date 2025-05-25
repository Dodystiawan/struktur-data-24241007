# Vektor
# vektor baris
import numpy as np

vek_1 = np.array([1, 2, 3])

# vektor kolom
vek_2 = np.array([[1],
                  [2],
                  [3]])

# atau menggunakan transpose()
vek_3 = np.array([[1, 2, 3]]).T

print("Vektor Baris")
print(vek_1)

print("Vektor Kolom")
print(vek_2)

print("Vektor Kolom dengan transpose()")
print(vek_3)