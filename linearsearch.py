nums = list(map(int, input("Enter numbers : ").split()))
target = int(input("Enter target number : "))
for i in range(0, len(nums)) :
    if nums[i] == target :
        print("Target found at location : ",i)
    else :
        continue