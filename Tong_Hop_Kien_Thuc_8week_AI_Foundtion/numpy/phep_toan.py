import numpy as np

arr1 = np.array([1,2,3,4,5], dtype=np.int)
print('arr1: ', arr1)
arr2 = np.array([5,4,3,2,1], dtype=np.int)
print('arr2: ', arr2)

print('cộng')
print('\tarr1 + arr2: ', arr1 + arr2)
print('\tnp.add(arr1, arr2): ', np.add(arr1, arr2))

print('trừ')
print('\tarr1 - arr2: ', arr1 - arr2)
print('\tnp.subtract(arr1, arr2): ', np.subtract(arr1, arr2))

print('nhân')
print('\tarr1 * arr2: ', arr1 * arr2)
print('\tnp.multiply(arr1, arr2): ', np.multiply(arr1, arr2))

print('chia')
print('\tarr1 / arr2: ', arr1 / arr2)
print('\tnp.divide(arr1, arr2): ', np.divide(arr1, arr2))

print('căn bậc 2 của arr1: ', np.sqrt(arr1))

print('tích vô hướng (inner product)')
print('\tarr1.dot(arr2): ', arr1.dot(arr2))
print('\tnp.dot(arr1, arr2): ', np.dot(arr1, arr2))

print('tích giữa vecto và ma trận')
matrix = np.array([[1, 2], [3, 4]])
vecto = np.array([3, 6])
print('\tmatrix.dot(vecto): ', matrix.dot(vecto))
print('\tvecto.dot(matrix): ', vecto.dot(matrix))
print('\tnp.dot(matrix, vecto): ', np.dot(matrix, vecto))
print('\tnp.dot(vecto, matrix): ', np.dot(vecto, matrix))

print('tích giữa 2 ma trận')
matrix_temp = np.array([[3, -1], [3, 4]])
print('\tmatrix.dot(matrix_temp):\n', matrix.dot(matrix_temp))
print('\tnp.dot(matrix, matrix_temp):\n ', np.dot(matrix, matrix_temp))

print('tính tổng matrix_temp: ', matrix_temp.sum())
print('tính tổng matrix_temp theo dòng: ', matrix_temp.sum(axis=1))
print('tính tổng matrix_temp theo cột: ', matrix_temp.sum(axis=0))

