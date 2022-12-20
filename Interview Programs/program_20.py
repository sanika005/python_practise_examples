# Write python function which takes a variable number of arguments.
def func(*var):
    for i in var:
        print(i)

func(1)
func(20,6,65,56,0)