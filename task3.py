from math import gcd

# Given data
ciphertext = [
    218,
    34,
    194,
    164,
    220,
    50,
    237,
    77,
    68,
    151,
    135,
    21,
    101,
    167,
    196,
    98,
    196,
    219,
    89,
    241,
    16,
    134,
    240,
    43,
    36,
    193,
    37,
    17,
    184,
    61,
    81,
    41,
    81,
    148,
    18,
    172,
    193,
    37,
    203,
    233,
    244,
    145,
    18,
    1,
    121,
    46,
    18,
    193,
]
y = 109
n = 247
p = 13
q = 19


# Function to calculate Legendre symbol
def legendre_symbol(x, p):
    ls = pow(x, (p - 1) // 2, p)
    if ls == p - 1:
        return -1
    return ls


# Function for decrypting Goldwasser-Micali
def decrypt_goldwasser_micali(ciphertext, y, n, p, q):
    bits = []
    for c in ciphertext:
        legendre_p = legendre_symbol(c, p)
        legendre_q = legendre_symbol(c, q)
        if legendre_p == -1 or legendre_q == -1:
            bits.append(1)
        else:
            bits.append(0)

    message = bits_to_bytes(bits)  # Decrypt to byte sequence
    return message


# Function to convert from bit sequence to byte sequence
def bits_to_bytes(bits):
    bytes_list = []
    for i in range(0, len(bits), 8):
        byte = bits[i : i + 8]
        byte_value = int("".join(map(str, byte)), 2)
        bytes_list.append(byte_value)
    return bytes_list


# Function to convert from byte sequence to ASCII string
def bytes_to_ascii(byte_list):
    return "".join(chr(byte) for byte in byte_list)


# Decrypt the message and display the result before and after conversion
message_bytes = decrypt_goldwasser_micali(ciphertext, y, n, p, q)
print("Decrypted Message (before ASCII conversion):", message_bytes)

# Convert byte list to ASCII string
message_ascii = bytes_to_ascii(message_bytes)
print("Decrypted Message (after ASCII conversion):", message_ascii)
