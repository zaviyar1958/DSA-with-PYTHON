# Using recursion

num = int(input("Enter a number : "))
def fact(n) : 
    if n == 1: 
        return 1
    return n * fact(n-1)
factorial = fact(num)
print("Factorial of the given number is : ", factorial)


# Using loop

# num = int(input("Enter a number : "))
# fact = 1
# for i in range(1, num+1):
#     fact *= i
# print("Factorial of the given number is : ", fact)