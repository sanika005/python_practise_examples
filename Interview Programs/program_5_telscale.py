# [0, 2, 4, 6, 8]

# The original code
temp = []
for i in range(0,10):
    if i%2==0:
        temp.append(i)
print(temp)

lambda_func = lambda z:z if z%2==0 else 0
print(list(set(map(lambda_func,[i for i in range(0,10)]))))