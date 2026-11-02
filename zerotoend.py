nums = list(map(int, input("Enter numbers : ").split()))
i, j = 0, 1
while j < len(nums) :
    if nums[i] == 0 and nums[j] != 0 :
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j += 1
    elif nums[i] == 0 and nums[j] == 0 :
        j += 1
    elif (nums[i] != 0 and nums[j] == 0) or (nums[i] != 0 and nums[j] != 0) :
        i += 1 
        j += 1
print(nums)