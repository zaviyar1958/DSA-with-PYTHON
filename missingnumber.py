# nums = list(map(int, input("Enter numbers : ").split()))
# freq_map = {}
# n = len(nums)
# for i in range(n+1):
#     freq_map[i] = 0
# for num in nums:
#     freq_map[num] = freq_map.get(num, 0) + 1
# for num in freq_map :
#     if freq_map[num] == 0 :
#         print("Missing number is : ", num)



# Method 2 (optimal)


nums = list(map(int, input("Enter numbers : ").split()))
n = len(nums)
total = n*(n+1)/2
result = 0
for num in nums : 
    result += num
miss = int(total - result)
print(miss)