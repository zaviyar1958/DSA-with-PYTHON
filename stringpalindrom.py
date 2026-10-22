# Using slicing

# x = input("Enter a string : ")
# n = len(x)
# m = x[::-1]
# if(x == m):
#     print("Given string is palindrom.")
# else :
#     print("Given string is not palindrom.")


# Using recursion

# text = input("Enter a string : ")
# s = list(text)
# n = len(s) - 1
# def rev(s, i, j):
#     if (i >= j):
#         return "".join(s)               #Converting list into string
#     s[i], s[j] = s[j], s[i]
#     return rev(s, i+1, j-1) 
# result = rev(s, 0, n)
# if result == text :
#     print("String is palindrom.")
# else :
#     print("String is not palindrom.")



# Method 3 


# text = input("Enter a string : ")
# right = len(text) - 1
# def Pal_check(s, left, right) :
#     while (left < right) :
#         if (s[left] != s[right]) :
#             return False
#         left += 1
#         right -= 1
#     return True
# result = Pal_check(text, 0, right)
# if (result == True):
#     print ("String is a palindrom.")
# else :
#     print ("String is not a palindrom.")


# Method 4

text = input("Enter a string : ")
left = 0
right = len(text) -1
def Pal_check(s, i, j):
    if i >= j :
        return True
    if (s[i] != s[j]) :
        return False
    return Pal_check(s, i+1, j-1)
result = Pal_check(text, left, right)
if result :
    print ("String is a palindrom.")
else :
    print ("String is not a palindrom.")