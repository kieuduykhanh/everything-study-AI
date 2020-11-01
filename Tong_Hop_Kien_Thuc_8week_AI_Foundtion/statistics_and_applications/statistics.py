## mean

# Chúng ta đều hiểu bản chất của khái niệm trung bình là lấy tổng của dãy số cho trước sau đó chia cho độ dài của
# dãy số.
# ví dụ ta có một dãy số: 10, 2, 42, 45, 21, 39, 99
# mean = sum(dãy số)/len(dãy số) (sum là tổng đãy, len là độ dài dãy)

dayso = [10, 2, 42, 45, 21, 39, 99, 100]
print('dãy số: ', dayso)
mean = sum(dayso)/len(dayso)
print('mean: ', mean)

## median

# Số trung vị là một số đứng ở vị trí giữa trong dãy số đã được sắp xếp theo thứ tự tăng dần, median chia dãy số cho
# trước thành 2 nửa bằng nhau. Nếu độ dài của dãy số là số lẻ, thì số ở giữa là median, nếu chiều dài của dãy số là
# số chẵn thì median được xác định bằng cách lấy trung bình của hai số ở giữa.

# sắp xếp dãy số
# lấy phần tử nằm giữa
import math

dayso_sort = sorted(dayso)

def cal_median(dayso):
    if len(dayso) % 2 == 0:
        so_truoc = dayso[int(len(dayso)/2) - 1]
        so_sau = dayso[int(len(dayso)/2)]
        return (so_truoc + so_sau)/2
    else:
        return dayso[math.floor(len(dayso)/2)]

print('median: ', cal_median(dayso_sort))

## mode

# Mode trả về phần tử có số lần xuất hiện nhiều nhất trong dãy số cho trước. Ví dụ, ta có điểm thi toán của 20 học
# sinh với thang 10 điểm:

from collections import Counter
points = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10]
print('điểm: ', points)
print('điểm số xuất hiện nhiều nhất: ', Counter(points).most_common(1)[0][0])

## range

# Độ phân tán (range) của dữ liệu cho biết dữ liệu chúng ta có giá trị trải rộng như thế nào. Ví dụ, nếu chỉ quan
# tâm đến trung bình thì có khi ta đánh giá sai dữ liệu. Độ phân tán dữ liệu đơn giản là độ lệch giữa giá trị lớn nhất
# và giá trị nhỏ nhất của tập dữ liệu.

max_point = max(points)
min_point = min(points)
space = max_point - min_point
print('max: {}, min: {}, space: {}'.format(max_point, min_point, space))

## Variance

# Phương sai (variance) cho ta biết các giá trị trong tập dữ liệu có khác biệt nhiều với giá trị trung bình của cả tập
# hay không? Đánh giá mức độ phân tán của dữ liệu so với giá trị trung bình. Nếu muốn tính độ lệch chuẩn chỉ cần lấy
# căn bậc hai của phương sai.

def cal_variance(points):
    mean = sum(points) / len(points)
    do_lech = []
    for point in points:
        do_lech.append((point - mean)**2)
    return sum(do_lech) / len(do_lech)

print('phương sai: ', cal_variance(points))
# dộ lệnh chuẩn bằng căn bậc 2 của phương sai
print('độ lệch chuẩn: ', math.sqrt(cal_variance(points)))

## CORRELATION COEFFECIENT

# Khi phân tích hồi quy tuyến tính thì yêu cầu hai biến độc lập phải có mối quan hệ tuyến tính với nhau.
# Khi đó ta đánh giá qua hệ số tương quan. Hệ số tương quan thể hiện mối quan hệ tương quan tuyến tính giữa hai biến,
# hệ số tương quan nằm trong khoảng [-1; 1],

# – Khi hệ số tương quan bằng 0 thì ta kết luận hai biến không có tương quan tuyến tính với nhau (nhưng không chắc chúng độc lập).
# – Khi hệ số gần bằng 1 thì ta nói có mối quan hệ tuyến tính dương (cùng tăng hoặc cùng giảm).
# – khi hệ số gần bằng -1 thì ta nói hai biến số có mối quan hệ tuyến tính âm (x giảm y tăng và ngược lại).

def cal_corr(x, y):
    n = len(x)
    xy = []
    for xi, yi in zip(x, y):
        xy.append(xi * yi)
    tu = n * sum(xy) - sum(x) * sum(y)
    x2 = list(map(lambda x: x**2, x))
    y2 = list(map(lambda y: y**2, y))
    mau1 = math.sqrt(n * sum(x2) - sum(x)**2)
    mau2 = math.sqrt(n * sum(y2) - sum(y)**2)
    return tu/(mau1*mau2)

x = [7, 18, 29, 2, 10, 9, 9]
y = [1, 6, 12, 8, 6, 21, 10]
print('Hệ số tương quan tuyến tính giữa hai biến x,y: ', cal_corr(x,y))