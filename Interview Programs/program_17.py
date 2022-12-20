import re
string1 = "####Welcome to the vapi####"
gmail = "sanikabhosale005@gmail.com"
search_pattern = re.search("^#.*#$",string1)
find_pattern = re.findall("to",string1)
split_pattern = re.split("to",string1)
replace_pattern = re.sub("to the","in",string1)
# print(find_pattern)
# print(split_pattern)
# print(replace_pattern)

gmail_pattern = re.findall("^[a-zA-z].*[0-9].{1}@{1}gmail.com$",gmail)
if gmail_pattern:
    print("True",gmail_pattern)
else:
    print("False")
if search_pattern:
    print("Yes, we got a match")
else:
    print("No match found")