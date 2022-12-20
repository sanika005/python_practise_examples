# WAP (Write a program) which takes a sequence of numbers and check if all numbers are unique.

def func1(list1):
    print(set(list1))
    if len(list1) == len(set(list1)):
        print("True")
    else:
        print("False")

func1([7,2,3,4,5,6,8,2,3,4,5])