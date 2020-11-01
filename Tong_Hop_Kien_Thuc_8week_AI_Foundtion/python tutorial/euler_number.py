# e ~~ 1 + 1/1! + 1/2! + 1/3! + ... + 1/n!

def giai_thua(x):
    '''
    hàm này tính giai thừa của x
    :param x:
    :return: trả về giá trị x!
    '''
    giaithua = 1
    for i in range(1, x+1):
        giaithua *= i
    return giaithua

def e_caculator(n):
    '''
    hàm này tính số e theo công thức trên
    :param n:
    :return: trả về giá trị số e khi n = n
    '''
    e = 1
    for x in range(1, n+1):
        e += 1/giai_thua(x)
    return e

print(e_caculator(100))