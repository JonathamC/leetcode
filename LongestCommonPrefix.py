def LongestCommonPrefix(strs): 
    result = ""
    for i in range(len(strs[0])): 
        for s in strs: 
            if i == len(s) or s[i] != strs[0][i]: 
                return result 
        result += strs[0][i]
    return result

def print_str(str): 
    if len(str) == 0: 
        print("EMPTY STRING")
    else: 
        print(str)

strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
strs3 = ["cir", "car"]


print_str(LongestCommonPrefix(strs1))
print_str(LongestCommonPrefix(strs2))
print_str(LongestCommonPrefix(strs3))