# substract values from list
# from first element 
# with reduce() function -> import from functools
list1 = [738,89,21,65,90,23,56,9]
from functools import reduce
def substract(a,b):
    return a-b
    
a = reduce(substract,list1)
print(a)

# without using reduce function:
list1 = [738,89,21,65,90,23,56,9]
def substract_from_first(num_list):
    first_ele = list1[0]
    for i in list1[1:]:
        res = first_ele-i
        first_ele = res
    print(res)
substract_from_first(list1)