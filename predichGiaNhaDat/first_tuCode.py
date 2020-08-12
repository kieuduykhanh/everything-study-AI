import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# lay data tu file csv duoi dang ma tran
data = pd.read_csv('data_linear.csv').values
N = data.shape[0] #lay ra so hang cua ma tran data
x = data[:, 0].reshape(-1, 1) #lay ra cot dien tich trong data (cot dau tien)
y = data[:, 1].reshape(-1, 1) #lay ra cot gia nha thuc te trong data (cot thu 2)
plt.scatter(x, y) #show cac diem (x, y) tuong ung
# plt.plot(x, y) #noi cac diem (x, y) thanh duong di
plt.xlabel('mét vuông')
plt.ylabel('giá')
# plt.show()
x = np.hstack((np.ones((N, 1)), x)) #bo sung vao ma tran x mot cot toan so 1 (de nhan voi w0)
# w = np.array([[0.], [1.]])
w = np.array([0.,1.]).reshape(-1,1) #tao ma tran w co shapes(2, 1), co the dung dong code tren
numOfIteration = 100 #so lan hoc
cost = np.zeros((numOfIteration,1)) #tao ma tran cost kich thuoc (100, 1)
learning_rate = 0.000001 #toc do hoc
for i in range(1, numOfIteration):
    r = np.dot(x, w) - y
    cost[i] = 0.5*sum(r*r)
    w[0] -= learning_rate*np.sum(r)
    w[1] -= learning_rate*np.sum(np.multiply(r, x[:,1].reshape(-1,1)))
    print(cost[i])
predict = np.dot(x, w)
plt.plot((x[0][1], x[N-1][1]),(predict[0], predict[N-1]), 'r') #ve duong thang gan nhat voi cac diem (x, y)
plt.show()
# Lưu w với numpy.save(), định dạng '.npy'
np.save('weight.npy', w)
# Đọc file '.npy' chứa tham số weight
w = np.load('weight.npy')
print(w)


dientich = float(input("Nhap vao dien tich can du doan: "))
print("So tien du doan la: ",(w[0] + w[1]*dientich))
