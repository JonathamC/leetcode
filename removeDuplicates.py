def removeDuplicates(nums): 
    count = 0  
    for i in range(len(nums)): 
        if nums[i] not in nums[:i]: 
            nums[count] = nums[i]
            count += 1 
    return count 



def test1(): 

    nums = [1,1,2]
    expectedNums = [1,2] 

    k = removeDuplicates(nums)

    assert k == len(expectedNums)
    for i in range(k): 
        assert nums[i] == expectedNums[i]


test1()