# sort list of elements with ascending order
list1 = [10,1,9,2,8,3,7,4,6,5]
def sort_asecnding():
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[j]<list1[i]:
                list1[i],list1[j] = list1[j],list1[i]
    print(list1)
sort_asecnding()

# sort with sort() func
list1.sort()
print(list1)