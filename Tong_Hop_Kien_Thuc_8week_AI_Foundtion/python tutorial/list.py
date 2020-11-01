# list trong python có thể hiểu như 1 mảng trong ngôn ngữ khác, nhưng list mềm dẻo hơn nhiều vì các phần tử của list
# không cần cùng kiểu dữ liệu, hoặc chứa list khác
# list được quán lí theo index, index chạy từ 0 đến (size list - 1)
# exam

# khai báo list
list_exam = [1, 2, 'khánh', True, 3.2, [5, 6, 7]]

# lấy phần tử trong list_exam ở vị trí 0
print('phần tử ở vị trí 0: ', list_exam[0])

# dùng for_loop duyệt list
for element in list_exam:
    print(element)
    print(type(element))


# slicing list (cắt list)
# lấy list từ phần tử start -> end - 1: list_name[start:end]

print('clicing lấy ra phần tử thứ 2 đến (4-1) trong list: ', list_exam[2:4]) # lấy ra phần tử thứ 2, 3 trong list_exam
print('clicing lấy ra phần tử từ đầu list đến phần tử thứ (4-1) trong list: ', list_exam[:4]) # lấy ra các phần tử trong list cho đến phần tử thứ 3 (0, 1, 2, 3)
print('clicing lấy ra phần tử thứ 4 đến cuối list: ', list_exam[4:]) # lấy ra các phần tử trong list tính từ phần tử thứ 4 (4, 5)

# ngoài duyệt xuôi từ đầu mảng đến cuối mảng thì mình có thể duyệt ngược, ví dụ như phần tử cuối cùng trong mảng có
# index là len - 1 thì phần tử đó đồng thời cũng có index là -1, dấu trừ thể hiện vị trí của phần tử đó khi duyệt từ
# cuối list lên đầu list

print('phần tử cuối cùng trong list khi biết index là: ', list_exam[5]) # lấy ra phần tử cuối mảng khi biết list có size là 6
print('phần tử cuối cùng trong list khi không biết index là: ', list_exam[-1]) # lấy ra phần tử cuối mảng, không cần biết size list là bao nhiêu

# các hàm liên quan đến list (https://docs.python.org/3/tutorial/datastructures.html)

# thêm phần tử vào list: list_name.append(element), phần tử element được mặc định thêm vào cuối list

list_exam.append('phần tử được thêm')
print('list sau khi được thêm phần tử: ', list_exam)

# chèn phần tử vào vị trí nào đó trong list: list_name.insert(index, element), index là vị trí muốn chèn phần tử element vào
list_exam.insert(2, 'phần tử mới được chèn vào vị trí số 2')
print('list sau khi chèn phần tử: ', list_exam)

# xoá phần tử tại ví trí index: del list_name[index]
del list_exam[-1] # xoá phần tử cuối cùng trong list
print('list sau khi xoá phần tử cuối cùng: ', list_exam)

# đảo ngược lại list
list_exam.reverse()
print('list sao khi đảo ngược: ', list_exam)

# đến số lần xuất hiện element trong list: list_name.count(element)
print('số lần xuất hiện phần tử có giá trị là 6 trong list là: ', list_exam.count(6))

# sắp xếp list: list_name.sort() (chú ý khi dùng hàm này thì các phần tử trong list phải cùng kiểu dữ liệu)
list_exam2 = [1,5,4,23,7,4,2,7,32,5]
print('list trước khi được sắp xếp: ', list_exam2)
list_exam2.sort()
print('list sau khi được sắp xếp: ', list_exam2)

# nhân list với 1 số n thì tương ứng là list mới với size gấp n lần list ban đầu
list_exam3 = 2 * list_exam2
print('list sau khi nhân với số 2: ', list_exam3)

# cộng 2 list
list_exam4 = list_exam + list_exam2
print('cộng 2 list: ', list_exam4)