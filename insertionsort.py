nums = list(map(int,input("Enter numbers : ").split()))
n = len(nums)
for i in range(1, n):
    key = nums[i]
    j = i-1 
    while j >= 0 and key < nums[j]:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key
print(nums)
