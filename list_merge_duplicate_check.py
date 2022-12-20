def list_check():
    listA = []
    final_list = []
    n = int(input("Enter number of elements in the list : "))
    for i in range(0, n):
        print("Enter element No-{}: ".format(i + 1))
        ele = [input(), int(input())]
        listA.append(ele)
        print("The entered list is: ",listA)
        for j in listA:
            for ele_list in j:
                if int(ele_list) not in final_list:
                    final_list.append(int(ele_list))
    print(final_list)
list_check()

