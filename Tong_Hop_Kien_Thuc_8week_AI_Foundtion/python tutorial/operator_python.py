# các toán tử trong python: +, -, *, /, //, **, % (python không hỗ trợ toán tử ++ và --)

# khai báo biến có giá trị là 6.5
var1 = 6.5

# khai báo biến có giá trị là 6
var2 = 6

# in ra 2 biến
# .format: thay giá trị của var1 vào {} đầu tiên, giá trị var2 vào {} thứ hai
print('biến 1: {}, biến 2: {}'.format(var1, var2))

# tổng 2 biến: +
tong = var1 + var2
print('tổng: ', tong)
# tổng sẽ có kiểu float vì var1 kiểu float (float + int = float)
print(type(tong))

# hiệu 2 biến: -
hieu = var1 - var2
print('hiệu: ', hieu)

# tích 2 biến: *
tich = var1 * var2
print('tích: ', tich)

# thương 2 biến: /
thuong = var1 / var2
print('thương: ', thuong)

# chia lấy phần nguyên: // (phần nguyên là phần trước dấu ., ví dụ 2.5 thì phần nguyên là 2)
chia_lay_nguyen = var1 // var2
print('chia lấy nguyên: ', chia_lay_nguyen)

# chia lấy dư: % (phần dư = (kết quả phép chia - kết quả phép chia lấy nguyên) * số bị chia, ví dụ 6 / 4 = 2.5 thì kết quả
# phép chia lấy nguyên là 2, kết quả phép chia lấy dư là (2.5 - 2) * 4 = 2)
chia_lay_du = var1 % var2
print('chia lấy dư: ', chia_lay_du)

# luỹ thừa: ** (2**5 = 2^5 = 2*2*2*2*2 = 32)
luy_thua = var2**2 # var2 mũ 2 <-> 6^2 = 6*6 = 36
print("luỹ thừa: ", luy_thua)