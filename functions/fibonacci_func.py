def cache_fibonacci(cache = {}): # creating cache dict
    def fibonacci(n):
        # checking if the value is already in cache
        if n in cache:
            return cache[n]
        # checking if it's 0 or less
        elif n <= 0:
            return 0
        # if equals 1
        elif n == 1:
            return 1
        # calculating using recursion
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
    
    # return of the inner fucntion
    return fibonacci


# closure
fibo = cache_fibonacci()