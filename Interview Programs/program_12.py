# convert list into dictionary where list elements are keys
list1 = ['The', 'quick', 'brown', 'fox', 'was', 'quick']

count = 0
for i in list1:
    res = {}
    res = {i:count}
    count+=1
    print(res)