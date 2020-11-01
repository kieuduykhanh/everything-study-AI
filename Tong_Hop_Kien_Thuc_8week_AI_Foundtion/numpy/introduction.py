# Một mảng numpy là một tập hợp các giá trị cùng kiểu dữ liệu và được đánh số bằng các số nguyên dương.
# Numpy là module quan trọng cho việc sử lý dữ liệu và có thể chuyển đổi qua kiểu dữ liệu tensor trong tensorflow và pytorch.

# import thư viện numpy
import numpy as np

# Tạo mảng numpy (ndarray)

# - Tạo ndarray từ list
lis = [i for i in range(10)]
np_arr = np.array(lis)
print('ndarray: ', np_arr)
print('dtype: ', np_arr.dtype) # kiểu dữ liệu ndarray
print('shape: ', np_arr.shape) # kích thước ndarray
print('reshape: ', np_arr.reshape((1,10))) # thay đổi kích thước ndarray
np_arr[2] = 10 # thay đổi giá trị phần tử vị trí index số 2 có giá trị bằng 10
print('đổi giá trị: ', np_arr)

# - Các hàm tạo ndarray

# + Tạo ndarray với hàm zeros()
zeros_arr = np.zeros((3, 4)) # tạo ndarray có shape (3, 4), các phần tử đều là 0
print('np.zeros: \n', zeros_arr)

# + Tạo ndarray với hàm ones()
ones_arr = np.ones((3, 4)) # tạo ndarray có shape (3, 4), các phần tử đều là 1
print('np.ones: \n', ones_arr)

# + Tạo ndarray với hàm full()
full_arr = np.full((3, 4), 2) # tạo ndarray có shape (3, 4), các phần tử đều là 2
print('np.full: \n', full_arr)

# + Tạo ma trận đường chéo (ma trận đường chéo là ma trận vuông có các phần tử ở đường chéo chính bằng 1, còn lại bằng 0)
eye_arr = np.eye(4) # tạo ma trận đường chéo có shape (4, 4): rank 4
print('np.eye: \n', eye_arr)

# - Chuyển mảng về một chiều
arr = full_arr.flatten()
print('chuyển về mảng 1 chiều: ', arr)
