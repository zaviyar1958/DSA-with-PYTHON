# Method 1 (brute force)

# nums = list(map(int, input("Enter numbers : ").split()))
# n = len(nums)
# pos_ele = []
# neg_ele = []
# # updated = []
# for num in nums :
#     if num > 0 :
#         pos_ele.append(num)
#     else :
#         neg_ele.append(num)
# for i in range(0, n//2) :
#     # udpated.append(pos_ele[i])
#     # updated.append(neg_ele[i])
#     nums[2*i] = pos_ele[i]
#     nums[2*i+1] = neg_ele[i]
# # print(updated)
# print(nums)


# Method 2 (optimal)


nums = list(map(int, input("Enter numbers : ").split()))
n = len(nums)
result = [0] * n
P, N = 0, 1
for i in range(0, n) :
    if nums[i] > 0 :
        result[P] = nums[i] 
        P += 2
    else :
        result[N] = nums[i]
        N += 2
print(result)