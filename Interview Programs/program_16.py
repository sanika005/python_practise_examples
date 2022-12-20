# Get the first element from each nested list in a list

li = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
res = []
for i in li:
    fetch_first_ele = i[0]
    res.append(fetch_first_ele)
print(res)

res = [i[0] for i in li]
print(res)