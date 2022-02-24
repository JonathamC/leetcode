

def maxSubArray(nums): 
    largestSum = nums[0] 
    currentSum = 0 
    for i in nums: 
        
        if currentSum < 0: 
            currentSum = 0 
        currentSum += i 
        largestSum = max(largestSum, currentSum)
    return largestSum


nums = [-2,-1]
print(maxSubArray(nums))