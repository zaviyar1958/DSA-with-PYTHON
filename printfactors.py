#Better solution


# result = []
# num = int(input("Enter a number to check factors: "))
# for i in range(1 , num//2+1) :
#     if (num % i == 0) :
#         result.append(i)
# result.append(num)
# print("Factors are : ",result)


#Optimal solution


import math
result = []
num = int(input("Enter a number to check factors: "))
for i in range(1 , int(num ** 0.5)+1) :
    if (num % i == 0) :
        result.append(i)
        if (i != num // i):
            result.append(num//i)
result.sort()                          #To sort the result
print("Factors are : ",result)