import math

def lcm(a, b):
    return a*b//math.gcd(a,b)

def smallest_mult(r):
    res = 1
    for i in range(r):
        res = lcm(res, i+1)

    return res

if __name__ == "__main__":
    print(lcm(1,2))
    print(lcm(lcm(1, 2), 3))
    print(lcm(lcm(lcm(1, 2), 3), 4))
    print(" ")
    print(smallest_mult(10))
    print(smallest_mult(20))