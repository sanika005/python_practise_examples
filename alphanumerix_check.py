# import re
# def isalphanumeric(str_pattern):
#     regex = "^(?=.*[a-zA-Z])(?=.*[0-9])[A-Za-z0-9]+$"
#     p = re.compile(regex)

#     if str_pattern == None:
#         return False
        
#     if(re.search(p, str_pattern)):
#         return True
#     else:
#         return False
        
# str1 = str(input("Enter your string:"))
# print(str1, ":",isalphanumeric(str1))

def is_alnum(z):
    try:
        n = int(z, base=10)
        print(n)
    except ValueError:
        print(False)
    else:
        print(True)

is_alnum("Abc123")