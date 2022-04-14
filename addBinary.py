def decimalToBinary(n): 
    if n > 1: 
        decimalToBinary(n // 2)
    print(n%2, end='')

def addBinary(a,b): 
    n1 = int(a,2)
    n2 = int(b,2)
    n = bin(a + b).replace("0b")
    return decimalToBinary(n)

a = "11"
b = "1"
addBinary(a,b)


"""
Version 2(Shorter)

author: Jonatham Chang 

def addBinary(a: str, b: str): 
    decA = int(a, 2)
    decB = int(b, 2)
    return bin(decA + decB)[2:]


#test1 
print(addBinary("11", "1")) #--> 100 
print(addBinary("1010", "1011")) #--> 10101 


"""