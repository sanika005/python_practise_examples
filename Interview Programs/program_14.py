# Filter even values out of a list with list comprehension
list1 = [1,2,3,4,5,6,7,8,9,10]
res_list = [i for i in list1 if i%2!=0]
print(res_list)