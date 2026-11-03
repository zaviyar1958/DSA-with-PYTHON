# Method 1 (brute force)

nums = list(map(int, input("Enter numbers : ").split()))
target = int(input("Enter target value : "))
for i in range(0, len(nums)-1) :
    for j in range(i+1, len(nums)) :
        if nums[i] + nums[j] == target :
            print(i,j)


# Method 2   (optimal)