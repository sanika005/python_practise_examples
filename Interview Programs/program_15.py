# Count occurrences of each value in a list
list1 = ['blue', 'pink', 'green', 'green', 'yellow', 'pink', 'orange']
res_dict = {}
for i in list1:
    if i not in res_dict:
        res_dict[i]=1
    else:
        res_dict[i]+=1
print(res_dict)