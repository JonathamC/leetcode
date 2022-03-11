import locale 
locale.setlocale(locale.LC_ALL, 'en_US')


# used in top down approach 
F = [-1] * 50 

def top_down_fib(n): 
    if F[n] < 0: 
        if (n == 0): 
            F[n] = 0
        elif (n == 1): 
            F[n] = 1
        else: 
            F[n] = top_down_fib(n - 1) + top_down_fib(n - 2)

    return F[n]

def bottom_up_fib(n):
    fib = [0] * n 
    fib[0] = 1 
    fib[1] = 1 

    for i in range(2, n): 
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n - 1]

def bottom_up_appraoch_Test(n):
    print("\nBottom Up Approach fib({}): {}".format(n,locale.format("%d", bottom_up_fib(n), grouping=True)))

def top_down_approach_Test(n): 
    print("Top Down Approach fib({}): {}\n".format(n, locale.format("%d", top_down_fib(n), grouping=True)))

bottom_up_appraoch_Test(49) 
top_down_approach_Test(49)

