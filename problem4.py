def palindrome_num(n):
    lowest = int('1' + '0'*(n-1))
    highest = int('9'*n)

    pal = 0
    i_used = 0
    j_used = 0

    for i in range(lowest+1, highest+1):
        for j in range(lowest+1, highest+1, (1 if i % 11 != 0 else 11)):
            prod = i*j
            x = str(prod)
            if x == x[::-1]:
                if prod > pal:
                    pal = prod
                    i_used = i
                    j_used = j


    return pal, i_used, j_used

if __name__ == "__main__":
    print(palindrome_num(2))
    print(palindrome_num(3))