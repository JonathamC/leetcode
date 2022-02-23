def strStr(haystack: str, needle: str) -> int:
        if needle == "": 
            return 0 
    
        n = len(needle)
        
        for i in range(len(haystack)): 
            if haystack[i:i+n] == needle: 
                return i 
        return -1

def test1(): 
    haystack = "hello"
    needle = "ll"
    correctOutput = 2
    if strStr(haystack, needle) == correctOutput: 
        print("Test 1: Passed")
    else: 
        print("Test 1: Failed")

def test2(): 
    haystack = "aaaaa"
    needle = "bba"
    correctOutput = -1
    if strStr(haystack, needle) == correctOutput: 
        print("Test 2: Passed")
    else: 
        print("Test 2: Failed")

def test3(): 
    haystack = ""
    needle = ""
    correctOutput = 0
    if strStr(haystack, needle) == correctOutput: 
        print("Test 3: Passed")
    else: 
        print("Test 3: Failed")

test1() 
test2()
test3()