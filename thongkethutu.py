import numpy as np

x = np.array([[14, 96],
              [46, 82],
              [80, 67],
              [77, 91],
              [99, 87]])

print("X = ", x)

print("Giá trị lớn nhất: ", np.amax(x))
print("Giá trị bé nhất: ", np.amin(x))

print("Giá trị lớn nhất (axis = 0): ", np.amax(x, axis=0))
print("Giá trị lớn nhất (axis = 1): ", np.amax(x, axis=1))

#Để bỏ qua các phần tử nan:
x = np.array([[14, 96],
              [np.nan, 82],
              [80, 67],
              [77, np.nan],
              [99, 87]])

print("X = ", x)

print("Giá trị lớn nhất: ", np.nanmax(x))
print("Giá trị bé nhất: ", np.nanmin(x))

#Phạm vi giá trị chính là max - min trong một dãy số
print("x = ", x)

print("Range = ", np.ptp(x))
print("Range (axis = 0) = ", np.ptp(x, axis=0))
print("Range (axis = 1) = ", np.ptp(x, axis=1))