string = "sanika"
output = "sxnxkx"
res = ""
for i in range(len(string)):
    if i%2==0:
        res += string[i] + 'x'     
print(res)


string = "rameshwaram"
output_string = ""

for i in range(len(string)):
    if i%2!=0:
        output_string += "x"
    else:
        output_string += string[i]

print(output_string)
