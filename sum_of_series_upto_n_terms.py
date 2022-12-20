# Function to calculate sum
def mystery(n):
	# Return sum
    v = (pow(10, n + 1)*(9 * n - 1)+10)/pow(9, 3)-n*(n + 1)/18
    return v

# driver code
n = int(input("Enter the no.: "))

print(int(mystery(n)))
