nums = list(map(int,input("Enter numbers : ").split()))
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        if (nums[i] > nums[j]):
            nums[i], nums[j] = nums[j], nums[i]
print (nums)