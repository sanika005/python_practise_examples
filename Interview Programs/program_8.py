pets = ['dog','cat','fish','fish','cat']
res_dict = {}

for i in pets:
    if i in res_dict:
        res_dict[i] += 1
    else:
        res_dict[i] = 1
print(res_dict)