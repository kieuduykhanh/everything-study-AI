def caculator_mean(numbers):
    return sum(numbers)/len(numbers)

def caculator_variance(numbers):
    mean = caculator_mean(numbers)
    numbers_ = list(map(lambda x: (x - mean)**2, numbers))
    return sum(numbers_)/len(numbers_)

print(caculator_variance([5,3,6,7,4]))
print('sdhuisahdh')