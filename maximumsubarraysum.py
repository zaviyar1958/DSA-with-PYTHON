# Method 1 (brute force)


# nums = list(map(int, input("Enter numbers : ").split()))
# maxi = float("-inf")
# for i in range(0, len(nums)) :
#     total = 0
#     for j in range(i, len(nums)) :
#         total = total + nums[j] 
#         maxi = max(maxi,total) 
# print(maxi)


# Method 2 (optimal solution)


nums = list(map(int, input("Enter numbers : ").split()))
maxi = float("-inf")
total = 0
for i in range(0, len(nums)) :
    total = total + nums[i]
    maxi = max(total, maxi)
    if total < 0 :
        total = 0
print(maxi)