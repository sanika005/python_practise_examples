# remove negetive values from list
# with filter function
# def remove_neg(x):
#     return True if x>=0 else False
    
# list1 = [-10,2,-78,3,21,89,-6]
# a = [i for i in filter(remove_neg,list1)]
# print(a)

# without filter func:
list1 = [-10,2,-78,3,21,89,-6]
res = []
for i in list1:
    if i>=0:
        res.append(i)
print(res)