from itertools import product
Alist = [([2, 8, 9], 'Mon'), ([7, 5, 6], 'Wed')]
list1 = []
list2 = []
for i,j in Alist:
    for t1 in i:
        tup1 = (t1,j)
        list1.append(tup1)
print(list1)

# With product
for i,j in Alist:
    for t1 in product(i,[j]):
        list2.append(t1)
print(list2)