def fib(N):
    """Compute the N-th Fibonacci number
    
    >>> fib(42)
    433494437
    >>> [fib(i) for i in range(10)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    n0 = 1
    n1 = 1
    for i in range(N - 1):
        n1, n0 = n1 + n0, n1
    return n1


if __name__ == "__main__":
    for i in range(15):
        print(fib(i))
