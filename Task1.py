# Function to compute the Jacobi symbol
def jacobi_symbol(a, n):
    if n % 2 == 0:
        return "Invalid input"
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            if n % 8 == 3 or n % 8 == 5:
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0


# Function to compute the Kronecker symbol
def kronecker_symbol(a, n):
    if n < 0:
        n = -n
        if a < 0:
            a = -a
        else:
            return -kronecker_symbol(a, n)
    result = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            if n % 8 == 3 or n % 8 == 5:
                result = -result
        a, n = n, a
        if a % 4 == n % 4 == 3:
            result = -result
        a %= n
    if n == 1:
        return result
    else:
        return 0


# Main function
def main():
    a = int(input("Enter the first number (a): "))
    n = int(input("Enter the second number (n): "))

    jacobi_result = jacobi_symbol(a, n)
    kronecker_result = kronecker_symbol(a, n)

    print("The Kronecker symbol", a, "with", n, "is:", kronecker_result)
    print("The Jacobi symbol of", a, "with", n, "is:", jacobi_result)


if __name__ == "__main__":
    main()
