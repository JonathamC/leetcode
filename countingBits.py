def dec_to_binary(n): 
    return bin(n).replace("0b", "")

def oneCounter(binary): 
    return len(binary.replace("0", ""))

def countBits(n): 
    # ones = [0 for i in range(n + 1)]
    # for i in range(n + 1): 
    #     if int(oneCounter(dec_to_binary(i))) > 0: 
    #         ones[i] = int(oneCounter(dec_to_binary(i)))
    # return ones

    # same as above but written in one line
    return [int(oneCounter(dec_to_binary(i))) for i in range(n + 1)]
    

print(countBits(5))

