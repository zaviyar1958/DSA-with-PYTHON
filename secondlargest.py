nums = list(map(int, input("Enter numbers : ").split()))
n = len(nums)

if n == 1:
    print("There is only one element.")
else:
    f_large = float("-inf")
    s_large = float("-inf")

    for num in nums:
        if num > f_large:
            f_large = num

    for num in nums:
        if num != f_large and num > s_large:
            s_large = num

    print("Largest number :", f_large)
    print("Second largest number :", s_large)