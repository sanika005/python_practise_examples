# What is the output of the above code?

# Ans: 30,30 0,30 0 Wrong input,Wrong input

a,b = 5,6

def add():
    return a+b

def sub():
    return a-b

def mul():
    return a*b

def div():
    return a//b

def xor():
    return a^b

def operations(op):
    switch = {
        'a':add(),
        's':sub(),
        'm':mul(),
        'd':div(),
    }
    # check_items = switch.values()
    # check_fromkeys = dict.fromkeys(switch,switch_copy)
    print(switch)
    print(switch.get(op,'Wrong input'))

operations('p')

# Output: Wrong input