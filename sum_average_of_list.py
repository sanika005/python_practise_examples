list1 = [2,2,56,89,76,21,89,89,89]

def sum(list):
    count = 0
    for i in list:
        count += i
    print(f"Sum of all list elements:{count}")
    avg = count/len(list)
    print(f"Average of all list elements:{avg}")
sum(list1)