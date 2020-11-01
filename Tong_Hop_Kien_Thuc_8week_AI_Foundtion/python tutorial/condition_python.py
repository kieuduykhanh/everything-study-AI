# các toán tử so sánh: ==, !=, >, <, >=, <=

# khai báo 2 biến
var1, var2 = 1, 2

# toán tử ==: so sánh bằng
print(var1 == var2) # so sánh xem var1 có bằng var2 hay không (False)

# toán tử !=: so sánh khác
print(var1 != var2) # so sánh xem var1 có khác var2 hay không (True)

# toán tử >: so sánh lớn hơn
print(var1 > var2) # so sánh xem var1 có lớn hơn var2 hay không (False)

# toán tử <: so sánh nhỏ hơn
print(var1 < var2) # so sánh xem var1 có nhỏ hơn var2 hay không (True)

# toán tử >=: so sánh lớn hơn hoặc bằng
print(var1 >= var2) # so sánh xem var1 có lớn hơn hoặc bằng var2 hay không (False)

# toán tử <=: so sánh nhỏ hơn hoặc bằng
print(var1 <= var2) # so sánh xem var1 có nhỏ hơn hoặc bằng var2 hay không (True)


# câu lệnh rẽ nhánh if - else
# khai báo
# if điều_kiện: (nếu điều kiện đúng thì thực hiện code xử lý trong khối if, bỏ qua else và ngược lại)
#     code xử lý
# else:
#     code xử lý

# ví dụ
# var1 = 1
if var1 > 2:
    print('biến var1 lớn hơn 2')
else:
    print('biến var1 nhỏ hơn 2')

# câu lệnh rẽ nhánh if - elif - else
# khai báo
# if điều_kiện_1: (nếu điều kiện 1 đúng thì thực hiện code xử lý trong khối if, bỏ qua elif và else, nếu điều kiện sai thì
# xét điều kiện 2 đúng thì thực hiện code xử lý trong khối elif, bỏ qua else và ngược lại)
#     code xử lý
# elif điều_kiện_2: (có thể có nhiều elif)
#     code xử lý
# else:
#     code xử lý

# ví dụ
# var2 = 2
if var2 < 2:
    print('biến var2 nhỏ hơn 2')
elif var2 == 2:
    print('biến var2 bằng 2')
else:
    print('biến var2 lớn hơn 2')

