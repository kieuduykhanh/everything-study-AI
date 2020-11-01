# set khá giống list nhưng các phần tử trong set là duy nhất
# khởi tạo 1 set không có phần tử
set_null = set()
print(set_null)

# khởi tạo set có phần tử, các phần tử trong set nằm trong dấu {}

set_not_null = {1,1,2,3,4,2,13,4}
print(set_not_null)

# cộng set với set
set_not_null.update({1,2,35})
print(set_not_null)

# cộng set với list
set_not_null.update([8,7,6])
print(set_not_null)

# thêm phần tử vào set
set_not_null.add(11)
print(set_not_null)

# tìm hiểu thêm về set: https://docs.python.org/2/library/sets.html