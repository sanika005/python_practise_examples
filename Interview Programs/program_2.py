string = "Sanika ahmedabad"
dict1 = {'s':'1','a':'5','n':'1','i':'1','k':'1',' ':'1','h':'1','m':'1','e':'1','d':'2','b':'1'}

res_dict = {}
for ch in string:
    if ch in res_dict:
        res_dict[ch] += 1
    else:
        res_dict[ch] = 1
print(res_dict)