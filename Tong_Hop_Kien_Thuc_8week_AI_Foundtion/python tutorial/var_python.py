# in ra màn hình console
print("In ra man hinh console")

# khai báo biến, nên đặt tên biến có ý nghĩa, người khác đọc hoặc mình đọc lại biến ý nghĩa của biến đó luôn
# có thể gán mọi kiểu dữ liệu cho biến (int, float, string, boolean, ...)
# giá trị kiểu int: -1, 0, 1, 2, 3, ...
# giá trị kiểu float: 1.1, -5.2, ...
# giá trị kiểu string: 'khánh', "linh", ...
# giá trị kiểu boolean: True, False

# khai báo biến kiểu int
int_var = 2
# in ra giá trị của biến
print(int_var)
# in ra kiểu dữ liệu của biến: type(tên_biến)
print(type(int_var))

# khai báo biến kiểu string (giá trị của biến phải nằm trong dấu "" hoặc '', 2 dấu nháy là như nhau, không được dùng
# cọc cạch "')
str_var = 'biến kiểu string'
print(str_var)
print(type(str_var))

# dùng lại biến kiểu int đã khai báo và gán kiểu dữ liệu khác
int_var = 'biến kiểu int -> kiểu string'
print(int_var)
print(type(int_var))

# giá trị biến nhập từ bàn phím
var_input = input('Nhập giá trị: ')
print(var_input)
print(type(var_input))

# giá trị biến nhập từ bàn phím luôn luôn là kiểu string, muốn là int, float, ... thì phải ép kiểu
var_input_int = int(input('Nhập giá trị kiểu int: '))
print(var_input_int)
print(type(var_input_int))