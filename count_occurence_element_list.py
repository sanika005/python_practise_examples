def countOccur(list,ele):
    count = 0
    for i in list:
        if i == ele:
            count += 1
    print(count)
    return count

list1 = [2,2,56,89,76,21,89,89,89,89]
x = 89
countOccur(list1,x)