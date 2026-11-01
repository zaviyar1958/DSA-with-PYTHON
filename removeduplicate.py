nums = list(map(int, input("Enter numbers : ").split()))
result = []
for number in nums :
    if number in result :
        continue
    else :
        result.append(number)
print(result)