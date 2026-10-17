num = int(input("Enter a number : "))
number =  num 
count = len(str(number))
result = 0 
while num > 0 :
    r = num % 10 
    num = num // 10 
    result = result + r ** count
if (number == result) :
    print("Given number is an armstrong number.")
else :
    print("Given number is not an armstrong number.")