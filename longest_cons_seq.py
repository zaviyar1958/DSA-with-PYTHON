nums = list(map(int, input("Enter numbers : ").split()))
myset = set(nums)
longest = 0
for num in myset :
    if num - 1 not in myset :
        x = num 
        count = 1
        while x + 1 in myset :
            count += 1
            x += 1
        longest = max (longest, count)
print(longest)