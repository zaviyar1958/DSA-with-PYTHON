nums = list(map(int, input("Enter numbers : ").split()))
k = int(input("Enter number of rotation : "))
n = len(nums)
k = k % n
nums[:] = nums[n-k : n] + nums[0 : n-k]
print("Rotated array is : ")
print(nums)

# Method 2

# nums = list(map(int, input("Enter numbers : ").split()))
# k = int(input("Enter number of rotation : "))
# n = len(nums)
# k = k % n
# temp = nums[n-k : n] 
# for i in range(n-k-1, -1, -1):
#     nums[i+k] = nums[i]
#     if i == 0 :
#         nums[0:k] = temp
# print("Rotated array is : ")
# print(nums)