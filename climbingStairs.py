#dynamic programming : bottom up approach
def climbStairs(n): 
    if n == 0: 
        return 0 
    
    if n < 2: # to avoid running into syntax out of range error on line 10 when n is smaller then 2 
        return n
    
    stairs = [0 for x in range(n)]
    stairs[0] = 1 
    stairs[1] = 2 
    for i in range(2, n): 
        stairs[i] = stairs[i - 1] + stairs[i - 2]
    return stairs[n - 1]

print(climbStairs(99999))