class test1:
    def count_occr_of_each_char(str1):
        result = {}
        for ele in str1:
            if ele in result:
                result[ele] += 1
            else:
                result[ele] = 1
        print(result)
        return result

str1 = "GEEKSFORGEEKS"
obj = test1()
obj.count_occr_of_each_char(str1)