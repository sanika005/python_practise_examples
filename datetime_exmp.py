from datetime import datetime

date = str(datetime.now())[:19].replace('-',").replace(':',").replace(' ',"")
print(date)
# print(int(date[4]))
date = str(int(date[2]) + int(date[3]) + int(date[4]) + int(date[5]) + int(date[6:]))
print(date)
# import numpy as np
# data = np.random.randint(100,size=(10))
# print(data)

# from random import randint

# def random_with_N_digits(n):
#     range_start = 10**(n-1)
#     range_end = (10**n)-1
#     return randint(range_start, range_end)
    
# print(random_with_N_digits(2))
# print(random_with_N_digits(3))
# print(random_with_N_digits(10))