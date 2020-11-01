# Array indexing: Numpy cung cấp một số cách để truy xuất phần tử trong mảng. Truy xuất phần tử dùng kỹ thuật
# slicing tương tự như danh sách (list) trong python.
import numpy as np

a_arr = np.array([[1,2,3], [4,5,6]])
print('mảng a: \n', a_arr)
b_arr = a_arr[:, 1:3] # lấy ra từ mảng a_arr all dòng (:), cột 1, cột 2 (1:3) và gán vào mảng b_arr
print('mảng b:\n', b_arr)

# - lấy một dòng dữ liệu
row0 = a_arr[0:1, :] # lấy ra từ mảng a_arr dòng 0 (0:1), all cột (:)
print('dòng đầu mảng a_arr: ', row0)

col1 = a_arr[:, 1:2] # lấy ra từ mảng a_arr all dòng (:), cột 1 (1:2)
print('cột 1 mảng a_arr: \n', col1)

# so sánh các phần tử trong mảng với điều kiện
arr_dk = a_arr > 3
print('mảng điều kiện phần tử lớn hơn 3: \n', arr_dk)

# lấy các phần tử trong a_arr thoả mãn điều kiện lớn hơn 3
thoa_man = a_arr[arr_dk] # hoặc thoa_man = a_arr[a_arr > 3]
print('các phần tử thoả mãn điều kiện: ', thoa_man)