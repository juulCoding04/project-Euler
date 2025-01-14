def even_fib_sum(limit):
    n = 0
    n_1 = 1
    n_2 = 1
    sum = 0
    while(n < limit):
        n = n_1 + n_2
        n_2 = n_1
        n_1 = n
        
        if (n % 2 == 0):
            sum += n
    return sum

if __name__ == "__main__":
    print(even_fib_sum(4000000))