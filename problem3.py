def is_prime(n):
    if (n <= 1):
        return False
    
    for i in range(2, n):
        if (n%i == 0):
            return False
    
    return True

def max_prime_factor(number):
    i = 0
    primes = []

    while(number != 1):
        if (is_prime(i)):
            if (number % i == 0):
                if i not in primes:
                    primes.append(i)
                number /= i
            else:
                i += 1
        else:
            i += 1;

    return max(primes)

if __name__ == "__main__":
    print(max_prime_factor(600851475143))