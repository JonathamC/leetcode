def isValid(s): 
    """
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'
    """
    if len(s) % 2 != 0: 
        return False 
    dict = {'(' : ')', '[' : ']', '{' : '}'}
    stack = [] 
    for i in s: 
        if i in dict.keys(): 
            stack.append(i)
        else: 
            if stack == []: 
                return False
            a = stack.pop()
            if i != dict[a]: 
                return False 
    return stack == []


# s = ["[]"] 
# # output = [true, true, false, false, true]

# for i in s: 
#     print(i, isValid(i))
dict = {'(' : ')', '[' : ']', '{' : '}'}
print(dict.keys())