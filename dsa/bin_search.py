def search_item(nums,target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        index = (low + high)//2
        if nums[index] == target:
            return index
        elif nums[index] > target:
            high = index+1
        elif nums[index] < target:
            low = index - 1
    return -1

print(search_item([1,2,3,4,5,6,7,8,9],7))