# cách khai báo hàm:
# - def: khai báo hàm
# - function_name: tên hàm
# - parameters: tham số của hàm (hàm có thể không có tham số, 1 tham số hoặc nhiều tham số)
# - parameter_default: tham số mặc định nếu không truyền vào thì mặc định giá trị là 'kiều duy khánh'
# - function_doc: tài liệu về hàm (hướng dẫn, tham số, kiểu trả về, ...), viết trong dấu ''' tài liệu '''
# (dấu '''''' thể hiện đây là chuỗi nhiều dòng), viết ngay dưới dòng khai báo hàm (qui chuẩn chung)
# - code xử lý phải thụt vào 1 tab (4 lần space - tuỳ ide)
# - return: trả về (hàm có thể không có giá trị trả về, trả về 1 giá trị hoặc trả về nhiều giá trị)

def function_name(parameters, parameter_default = 'kiều duy khánh'):
    '''
    function_doc
    :param parameters:
    :return:
    '''
    # code xử lý
    value = 0
    return

# ví dụ hàm tính tổng 2 số
def sum(var1, var2):
    '''
    đây là hàm tính tổng 2 số
    :param var1:
    :param var2:
    :return: tổng 2 số
    '''
    tong = var1 + var2
    return tong

# khai báo 2 biến trên cùng 1 dòng
var1, var2 = 4, 5

print('var1: {}, var2: {}'.format(var1, var2))

# khai báo biến tong và gán giá trị bằng giá trị trả về của hàm sum khi truyển vào 2 biến var1 và var2
tong = sum(var1, var2)
print('tổng 2 số: ', tong)

# khai báo hàm có tham số mặc định var2 = 2
def luy_thua(var1, var2 = 2):
    '''
    đây là hàm tính luỹ thừa
    :param var1:
    :param var2:
    :return: var1 ^ var2
    '''
    luy_thua = var1 ** var2
    return luy_thua

luy_thua_var2_default = luy_thua(var1)
print('luỹ thừa mới var2 mặc định: ', luy_thua_var2_default)

luy_thua = luy_thua(var1, var2)
print('luỹ thừa var1 ^ var2: ', luy_thua)