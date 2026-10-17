number = int(input("Enter a number : "))
num = number
n = 0
while number > 0 :
    r = number % 10
    number = number // 10
    n = 10 * n + r
if (num == n):
    print ("Given number is a palindrom.")
else :
    print ("Given number is not a palindrom.")