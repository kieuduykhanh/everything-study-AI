# simulation of coin tossing

import random
import math

# khai báo 3 biến: biến đếm số lần tung đồng xu ra mặt lẻ, biến số lần tung đồng xu ra mặt chẵn, biến số lần tung
so_mat_le = 0
so_mat_chan = 0
so_lan_tung = 100000

for lan_tung in range(so_lan_tung):
    if random.randint(0, 1) == 0:
        so_mat_le += 1
    else:
        so_mat_chan += 1

print('xác xuất xuất hiện mặt lẻ: ', (so_mat_le / so_lan_tung))
print('xác xuất xuất hiện mặt chẵn: ', (so_mat_chan / so_lan_tung))


# PI estimation: số pi sấp xỉ bằng 4 * số điểm trong hình tròn / số điểm trong hình vuông
# vì: gọi Ns là số điểm trong hình vuông, Nc là số điểm trong hình tròn, As là diện tích hình vuông, Ac là diện tích
# hình tròn, n là độ dài cạnh hình vuông -> r = n/2 (r là bán kính hình tròn nội tiếp hình vuông)
# ta có: As / Ac ~~ Ns / Nc <-> (n^2 / pi*r^2) ~~ (Ns/Nc) <-> pi ~~ (s^2 * Nc) / (r^2 * Ns) (*)
# mà r = s/2 -> s^2 / r^2 = 4 -> (*) <-> pi ~~ 4 * Nc / Ns

so_diem = 100000
so_diem_trong_hinh_tron = 0

for diem in range(so_diem):
    x = 2 * random.random()
    y = 2 * random.random()
    if math.sqrt((1-x)**2 + (1-y)**2) <= 1:
        so_diem_trong_hinh_tron += 1

print('số điểm trong hình vuông: ', so_diem)
print('số điểm trong hình tròn: ', so_diem_trong_hinh_tron)
print('số pi: ', (4 * so_diem_trong_hinh_tron / so_diem))


