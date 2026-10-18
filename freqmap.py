# Method 1;


# freq_map = {}
# numbers = list(map(int,input("Enter numbers : ").split()))
# for i in range (0, len(numbers)):
#     if numbers[i] in freq_map :
#         freq_map[numbers[i]] += 1 
#     else :
#         freq_map[numbers[i]] = 1
# print (freq_map)  



# Method 2;


freq_map = {}
numbers = list(map(int, input("Enter numbers : ").split()))
for i in range(0, len(numbers)):
    freq_map[numbers[i]] = freq_map.get(numbers[i] , 0) + 1      
    #.get() if key does not exist then returns zero else return existing value
print(freq_map)