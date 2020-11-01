# set x0 = N/2 (N là số cần tính căn bậc 2), x(n+1) = (xn + N/xn)/2

def quadratic_root(N, so_lan_lap):
    '''
    hàm này tính căn bậc 2 của N
    :param N:
    :return:
    '''
    x = N/2
    for i in range(so_lan_lap):
        x = (x + N/x) / 2
    return x

print(quadratic_root(9, 5))