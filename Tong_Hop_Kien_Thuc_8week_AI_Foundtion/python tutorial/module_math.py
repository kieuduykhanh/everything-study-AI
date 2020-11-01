# math doc: https://docs.python.org/3/library/math.html

# khi dùng thư viện nào phải import thư viện đó, nếu thư viện không có sẵn thì phải cài đặt: pip install tên_thư_viện
import math
# các hàm toán học thường dùng

# hàm math.ceil(n): làm tròn lên (nếu n nguyên thì bằng chính nó)
print('làm tròn lên của 4.3:', math.ceil(4.3))
print('làm tròn lên của 2:', math.ceil(2))
print('------------')

# hàm math.floor(n): làm tròn xuống (nếu n nguyên thì bằng chính nó)
print('làm tròn xuống của 2.8:', math.floor(2.8))
print('làm tròn xuống của 5:', math.floor(5))
print('------------')

# hàm math.comb(n, k): tổ hợp chập k của n
print('tổ hợp chập 3 của 5: ', math.comb(5, 3))
print('------------')

# hàm math.fabs(x): trả về giá trị tuyệt đối của x
print('giá trị tuyệt đối của -3: ', math.fabs(-3))
print('------------')

# hàm math.factorial(n): trả về n! (1*2*3*...*n)
print('6!: ', math.factorial(6))
print('------------')

# hàm math.pi: trả về số pi (3.14...)
print('pi: ', math.pi)
print('------------')

# hàm math.e: trả về số e (2.7...)
print('e: ', math.e)
print('------------')

# hàm math.sqrt(x): trả về căn bận của x
print('căn bậc hai của 4: ', math.sqrt(4))
print('------------')

# hàm math.cos(x): trả về giá trị cosin của x (x phải tính theo đơn vị radian)
print('cos của pi: ', math.cos(math.pi))

# hàm math.sin(x): trả về giá trị sin của x (x phải tính theo đơn radian)
print('sin của e: ', math.sin(math.e))
