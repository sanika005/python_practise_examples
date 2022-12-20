I = [1,2,3,8,5,6,9,3,4]
O = [[1,2,3],[5,6],[3,4]]

def func1(list1):
    temp = []
    res_list = []
    for i in range(len(list1)+1):
        if i+1<len(list1):
            if list1[i+1]-list1[i] == 1:
                temp.append(list1[i])
            else:
                temp.append(list1[i])
                list1.remove(list1[i+1])
                res_list.append(temp)
                temp = []
        if i+1==len(list1):
            temp.append(list1[i])
            res_list.append(temp)
            temp = []
    print(res_list)
func1(I)