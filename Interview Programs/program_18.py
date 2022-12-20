# Print characters from a string that are present at an even index number
str1= "pynative"
evn_char = ""
for i in range(len(str1)):
    if i%2==0:
        evn_char += str1[i]
print(evn_char) 