import math

def caculator_mean(numbers):
    return sum(numbers)/len(numbers)

def caculator_variance(numbers):
    mean = caculator_mean(numbers)
    numbers_ = list(map(lambda x: (x - mean)**2, numbers))
    return sum(numbers_)/len(numbers_)

lis1 = [7,18,29,2,10,9,9]
lis2 = [1,6,12,8,6,21,10]


def caculator_corraelation(lis1, lis2):
    # mean1 = caculator_mean(lis1)
    # mean2 = caculator_mean(lis2)
    sumq = 0
    for i in range(len(lis1)):
        sumq += lis1[i] * lis2[i]
    return (len(lis1)*sumq - sum(lis1)*sum(lis2))/\
           (math.sqrt(len(lis1)*sum(list(map(lambda x: x**2, lis1))) - sum(lis1)**2)*
            math.sqrt(len(lis2)*sum(list(map(lambda x: x**2, lis2))) - sum(lis2)**2))

print(caculator_corraelation(lis1, lis2))