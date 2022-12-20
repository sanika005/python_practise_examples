# Remove duplicates from list.
list1 = [3, 2, 2, 1, 1, 1]
temp = []
for i in range(len(list1)+1):
    if i+1<len(list1):
        if list1[i]!=list1[i+1]:
            if list1[i] not in temp:
                temp.append(list1[i])
        if list1[i]==list1[i+1]:
            if list1[i] not in temp:
                temp.append(list1[i])
list1 = temp
print(list1)