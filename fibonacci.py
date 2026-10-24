# Beginner approach

# num = int(input("Enter number of count : "))
# def fibo (n,x,y,i) :
#     if (n == 1) :
#         print("Fibonacci series : ",end= "")
#         print (x)
#         return
#     if (n == 2) :
#         print("Fibonacci series : ",end= "")
#         print(x,y)
#         return
#     if (i == 0):
#         print("Fibonacci series : ",end= "")
#         print (x,y, end= " ")
#     if (i < n-2 and n > 2) :
#         sum = x+y
#         print(sum, end= " ")
#         x = y
#         y = sum
#         i += 1
#         fibo(n,x,y,i)
# fibo(num, 0, 1, 0)


# Intermediate approach

num = int(input("Enter number of count : "))
def fibo(num):
    if num == 0 or num ==1 :
        return num
    return fibo(num - 1) + fibo(num - 2)
result = fibo(num)
print("Fibonacci number at ",num ," : ",result)