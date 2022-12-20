def find_max(nums):
    max_num = 2
    for num in nums:
        if num>max_num:
            max_num = num
    print(max_num)

nums = [4,5,6,21,67,0]
find_max(nums)