def decor_mul(func):
    res_list = []
    def inner():
        x = func()
        for i in x:
            a = i*5
            res_list.append(a)
        return res_list
    return inner
    
@decor_mul
def num_list():
    return [2,3,4,5]
    
print(num_list())