# cấu trúc:
# khi condition đúng thì thực hiện code xử lý, condition sai thì thoát vòng lặp
# while condition:
#     code xử lý

var = 10
i = 0

while i < var: # kiểm tra i có nhỏ hơn var không, đúng thì thực hiện code bên trong, sai thì thoát vòng lặp
    print(i)
    i += 1 # sau khi in ra giá trị i thì tăng i lên 1 để tránh bị vòng lặp vô hạn
# sau khi i tăng đến 10 thì điều kiện i < var không đúng nữa nên thoát vòng lặp, chạy câu lệnh print ngoài vòng lặp
print('đã thoát vòng lặp while')

print('----------------------')

import random

# dừng vòng lặp khi thoả mãn điều kiện nào đó
while True: # điều kiện luôn đúng
    number = random.randint(0, 10)
    print('số sinh ra ngẫu nhiên là: ', number)

    if number == 7: # điều kiện thoát vòng lặp
        break

print('đã thoát vòng lặp')