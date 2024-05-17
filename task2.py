# Function to compute the Jacobi symbol
def jacobi_symbol(a, n):
    if n % 2 == 0:
        return "Invalid input"
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
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


# Function to compute the Legendre symbol
def legendre_symbol(x, p):
    ls = pow(x, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls


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
            a //= 2
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


n = 35
a = [i for i in range(n)]

# Lists to store quadratic and non-quadratic residues
quadratic_residue = []
non_quadratic_residue = []

# Determine quadratic and non-quadratic residues
for elem in a:
    legendre_5 = legendre_symbol(elem, 5)
    legendre_7 = legendre_symbol(elem, 7)
    if legendre_5 >= 0 and legendre_7 >= 0:
        quadratic_residue.append(elem)
    else:
        non_quadratic_residue.append(elem)

print("Quadratic Residue =", quadratic_residue)
print("Non-Quadratic Residue =", non_quadratic_residue)

# Print Legendre symbols for all elements in 'a'
print("\nLegendre Symbols:")
for elem in a:
    print(
        f"{elem}: (a/5) = {legendre_symbol(elem, 5)}, (a/7) = {legendre_symbol(elem, 7)}"
    )

# Print Kronecker-Jacobi symbols for all elements in 'a'
print("\nKronecker-Jacobi Symbols:")
for elem in a:
    kronecker_result = kronecker_symbol(elem, 35)
    jacobi_result = jacobi_symbol(elem, 35)
    print(f"For a = {elem}")
    print("The Kronecker symbol is:", kronecker_result)
    print("The Jacobi symbol is:", jacobi_result)
    print()

# Find special cases
special_cases = []
for elem in non_quadratic_residue:
    if jacobi_symbol(elem, 35) == 1 & kronecker_symbol(elem, 35) == 1:
        special_cases.append(elem)

print("Special cases: ", special_cases)
