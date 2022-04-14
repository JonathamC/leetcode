from re import I


def mySqrt(x): 
    i = 0 
    while (1): # run while loop infinitely 
        if i * i == x: 
            return i
        
        elif i * i > x: 
            return i - 1 
        
        else: 
            i += 1 



print(mySqrt(4)) # 2 
print(mySqrt(8)) # 2