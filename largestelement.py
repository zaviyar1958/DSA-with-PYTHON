nums = list(map(int, input("Enter numbers : ").split()))
n = len(nums)
i = 0
greater = nums[0]
for i in range(i, n) :
    if nums[i] > greater :
        greater = nums[i]
print("Maximum number in array is : ", greater)
