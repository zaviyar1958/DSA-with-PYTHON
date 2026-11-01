nums = [3,1,2,4,1,5,2,6,4]
def merge_sort(nums):
    if len(nums) <= 1 :
        return nums
    mid = len(nums) // 2
    left_arr = nums[ :mid]
    right_arr = nums[mid: ]
    left = merge_sort(left_arr)
    right = merge_sort(right_arr)
    return merge_arr(left, right)
def merge_arr(left, right):
    result = []
    i, j = 0, 0
    n, m = len(left), len(right)
    while i < n and j < m :
        if left[i] < right[j] :
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    while i < n :
        result.append(left[i])
        i += 1
    while j < m :
        result.append(right[j])
        j += 1
    return result
array = merge_sort(nums)
print(array)