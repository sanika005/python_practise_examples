def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

no = int(input("Enter the no. to find factorial of:"))
print("Factorial of",no,"is:",factorial(no))