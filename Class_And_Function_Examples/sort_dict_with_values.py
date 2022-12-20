dict1 = {166:'sanika',12:'jigar',38:'bhosale',40:'modha'}
# Sort with values
data_list = []
for j in dict1.values():
    data_list.append(j)
    for i in range(0,len(data_list)):
        for j in range(0,len(data_list)):
            if data_list[j]>data_list[i]:
                temp = data_list[i]
                data_list[i]=data_list[j]
                data_list[j]=temp
print(data_list)

# Sort with keys
keys_list = []
for key in dict1.keys():
    keys_list.append(key)
    for i in range(0,len(keys_list)):
        for j in range(0,len(keys_list)):
            if keys_list[i]<keys_list[j]:
                temp = keys_list[i]
                keys_list[i] = keys_list[j]
                keys_list[j] = temp
print(keys_list)