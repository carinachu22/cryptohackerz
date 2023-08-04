def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def decrypt(ciphertext, d, n):
    plaintext = [chr(pow(i, d, n)) for i in ciphertext]
    return "".join(plaintext)

def solve(encrypted_message, encrypted_n, encrypted_e):
    mapping = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
        "I": 9,
        "X": 0
    }

    encrypted = encrypted_message.split()
    message = []
    for i in encrypted:
        x = [str(mapping[j]) for j in i]
        message.append(int("".join(x)))

    n = int("".join([str(mapping[j]) for j in encrypted_n]))
    e = int("".join([str(mapping[j]) for j in encrypted_e]))

    factors = prime_factors(n)
    p, q = factors[0], factors[1]
    z = (p - 1) * (q - 1)

    d = 0
    while True:
        if (e * d) % z == 1:
            break
        d += 1

    flag = decrypt(message, d, n)
    return flag

if __name__ == "__main__":
    encrypted_message = "AABI BAFI BE ACHC IFH CEBG CIBA CI AHAX HGE BHED IAD AHAX AFHA AFBF AXCE DGB CIBA AXCE CAFD ADA"
    encrypted_n = "DAHG"
    encrypted_e = "ABCG"

    rsa = solve(encrypted_message, encrypted_n, encrypted_e)
    print(rsa)