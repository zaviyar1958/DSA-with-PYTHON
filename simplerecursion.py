# Program to print from 1 to N using recursion

# num = int(input("Enter a number : "))
# result = 1
# def func(result, n):
#     if result > n :
#         return
#     else :
#         print(result)
#     func(result + 1, n)
# func(result,num)
    

# Program to print sum from 1 to N using recursion


num = int(input("Enter a number: "))
def func(sum, i, n):
    if i > n:
        print(sum)
        return
    func(sum + i, i + 1, n)
func(0, 1, num)