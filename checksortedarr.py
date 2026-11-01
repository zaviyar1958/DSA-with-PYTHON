nums = list(map(int, input("Enter numbers : ").split()))
for i in range (0, len(nums)-1):
    if nums[i] < nums[i+1] :
        result = True
    else :
        result = False
        break
if result == True :
    print("Array is sorted.")
else:
    print("Array is not sorted.")