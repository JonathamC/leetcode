import locale 
locale.setlocale(locale.LC_ALL, 'en_US')

# Top down is better than bottom up approach
def top_down_fib(n): 
    fib = [] 
    if n == 0 or n == 1: 
        return n 
    
    fib.append(1)
    fib.append(1)
    for i in range(2, n): 
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n-1]

def bottom_up_fib(n):
    fib = [0] * n 
    if n == 0: 
        return 0

    if n == 1: 
        return 1

    fib[0] = 1 
    fib[1] = 1 

    for i in range(2, n): 
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n - 1]

def bottom_up_appraoch_Test(n):
    print("\nBottom Up Approach fib({}): {}".format(n,locale.format("%d", bottom_up_fib(n), grouping=True)))

def top_down_approach_Test(n): 
    print("Top Down Approach fib({}): {}\n".format(n, locale.format("%d", top_down_fib(n), grouping=True)))

bottom_up_appraoch_Test(3) 
top_down_approach_Test(3)

