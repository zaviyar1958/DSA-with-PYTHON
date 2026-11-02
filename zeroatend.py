nums = list(map(int, input("Enter numbers : ").split()))
i, j = 0, len(nums)-1
counter = 0
while i <= j :
    if nums[j] == 0 :
        j -= 1
    elif nums[i] != 0 :
        i += 1
    else :
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
        counter += 1
print(nums)
print(counter)