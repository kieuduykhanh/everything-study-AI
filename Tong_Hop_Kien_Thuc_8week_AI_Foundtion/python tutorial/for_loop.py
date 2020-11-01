# iterable (có thể lặp): string, range(), list, tuple, dict

# iterable string: ví dụ 'khanh' -> 'k', 'h', 'a'. 'n', 'h'
# iterable range(start=0, stop, step=1): ví dụ range(10) -> 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# cấu trúc vòng for
# khối code xử lý phải được thụt lề 1 tab
# câu lệnh dừng lặp: break

# for element in iterable:
#     code xử lý

# ví dụ:
for num in range(10):
    print(num)
    if num == 2:
        break

for char in 'khanh':
    print(char)