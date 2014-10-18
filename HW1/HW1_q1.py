# !env python
# Michael Herrera
# 10/17/14
# HW1, Problem 1
# Write out the Fibonacci Sequence to n numbers

def fib(n):
    """
    Writes out the Fibonacci Sequence to n numbers
    Inputs:
        n = Number of elements in sequence
    Output:
        fibnums = Fibonacci Sequence to n numbers
    """

    fibnums= [0]
    for i in range(n):
        if (i == 0):
            fibnums.append(1)
        else:
            fn1 = fibnums[i]
            fn2 = fibnums[i-1]
            fibnums.append(fn1+fn2)
    
    return fibnums[1:]

if __name__ == '__main__':
    print 'Problem 1:'
    print 'fib(1): ',fib(1)
    print 'fib(2): ',fib(2)
    print 'fib(6): ',fib(6)





