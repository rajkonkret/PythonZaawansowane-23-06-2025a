import numpy as np

# ndarray

A = np.array([[2, 3, 1],
              [4, 1, 2],
              [3, 2, 4]])

B = np.array([1, 2, 3])

# linalg.solve - rozwiązywanie układu równań

x = np.linalg.solve(A, B)

print(f"Rozwiązanie układu równań (x,y,z): {x}")
# Rozwiązanie układu równań (x,y,z): [0.2 0.  0.6]

# weryfikacja - mnozenie macieży A i wektora x powinno dać  B
B_check = np.dot(A, x)
print(f"Weryfikacja (A*x): {B_check}")  # Weryfikacja (A*x): [1. 2. 3.]

print("__ utworzenie tablicy 11 wymiarowej __")
array_11d = np.zeros((2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2))

print(f"Kształt tablicy: {array_11d.shape}")
# Kształt tablicy: (2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2)
print(f"liczba wymiarów: {array_11d.ndim}")  # liczba wymiarów: 11
