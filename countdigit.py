# Method number 1;

number = int(input("Enter a number to count digit: "));
count = 0 ;
while number > 0 :
    count += 1 ;
    n = number % 10 ;
    number = number // 10 ;
print ("Digits in the given number is = ", count);

# Method number 2;

# from math import *
# number = int(input("Enter a number to count digit: "));
# def digitcount(number) :
#     if(number == 0) : 
#         return print("Digits in the given number is = 1") ;     #handles math domain error 
#     n = int(log10(number)) + 1;
#     print ("Digits in the given number is = ", n);
# digitcount(number);