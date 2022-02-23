def searchInsertAux(nums, target, mid): 
    if nums[mid] == target: 
        return mid 

    elif len(nums) == 1: 
        if nums[mid] > target: 
            return mid - 1 
        else: 
            return mid + 1
    else: 
        if nums[mid] > target: 
            return searchInsertAux(nums[:mid], target, len(nums[:mid])//2)
        elif nums[mid] < target: 
            return searchInsertAux(nums[mid+1:], target, len(nums[mid+1:])//2)


def searchInsert(nums, target): 
    return searchInsertAux(nums, target, len(nums) // 2)

nums = [1,3,5,6]; target = 7

print(searchInsert(nums, target))