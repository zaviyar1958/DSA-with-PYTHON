num = list(map(int,input("Enter numbers of list : ").split()))
j = len(num)-1
def reverselist(num, i, j):
    if i >= j :
        print(num)
        return
    temp = num[i]
    num[i] = num[j]
    num[j] = temp
    reverselist(num, i+1, j-1)
reverselist(num, 0, j)