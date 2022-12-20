a = [122,323,255,566,877,868]
def sort_list(list1):
    temp = 0
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]>list1[j]:
                temp = list1[i]
                list1[i] = list1[j]
                list1[j] = temp
    print(list1)
    
sort_list(a)