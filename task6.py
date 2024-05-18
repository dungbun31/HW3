def modular_exponentiation(base, exponent, modulus):
    # Handle the special case where modulus is 1
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus  # Ensure base is in the correct range

    # If exponent is negative, find the modular multiplicative inverse
    if exponent < 0:
        base = pow(base, -1, modulus)  # Compute the modular inverse
        exponent = -exponent

    # Main loop for modular exponentiation
    while exponent > 0:
        if (exponent % 2) == 1:  # If exponent is odd, multiply the result by base
            result = (result * base) % modulus
        exponent = exponent >> 1  # Divide exponent by 2
        base = (base * base) % modulus  # Square the base
    return result


# Old feature: using default values
bases = [5, 51, 3, 3]
exponents = [23, -100, 322, 7777777777]
moduli = [7, 101, 47, 20]


# input values from the user
# def input_array(prompt):
#     return list(map(int, input(prompt).split()))

# Prompt the user to enter arrays
# bases = input_array("Enter the base values, separated by spaces: ")
# exponents = input_array("Enter the exponent values, separated by spaces: ")
# moduli = input_array("Enter the modulus values, separated by spaces: ")

# Calculate and print results for each set of input values
for base, exponent, modulus in zip(bases, exponents, moduli):
    result = modular_exponentiation(base, exponent, modulus)
    print(f"{base}^{exponent} (mod {modulus}) = {result} (mod {modulus})")
