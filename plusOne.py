def plusOne(digits): 
    digit = int("".join(map(str, digits)))
    digit += 1
    return [int(x) for x in str(digit)]

digits = [9]
print(plusOne(digits))