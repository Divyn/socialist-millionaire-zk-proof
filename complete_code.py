# https://en.wikipedia.org/wiki/Socialist_millionaire_problem
  
import random


# Function to perform modular exponentiation
def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)


# Generate parameters
def generate_parameters():
    p = 23  # Prime number
    h = 5  # Generator
    return p, h


# Generate secret values
def generate_secrets(p):
    return random.randint(1, p - 2), random.randint(1, p - 2)


# Diffie-Hellman style key exchange
def diffie_hellman(h, secret, p):
    return mod_exp(h, secret, p)


# Socialist Millionaire Protocol
def socialist_millionaire(p, h, x, y):
    # Random secrets
    a, alpha = generate_secrets(p)
    b, beta = generate_secrets(p)

    # Generate Diffie-Hellman shared values
    g = mod_exp(h, a * b, p)
    gamma = mod_exp(h, alpha * beta, p)

    # Random values for proof
    r = random.randint(1, p - 2)
    s = random.randint(1, p - 2)

    # Pa and Qa for Alice
    Pa = mod_exp(gamma, r, p)
    Qa = (mod_exp(h, r, p) * mod_exp(g, x, p)) % p
    print("Pa", Pa)
    print("Qa", Qa)

    # Pb and Qb for Bob
    Pb = mod_exp(gamma, s, p)
    Qb = (mod_exp(h, s, p) * mod_exp(g, y, p)) % p
    print("Pb", Pb)
    print("Qb", Qb)
    # Verify
    c = mod_exp(Qa * pow(Qb, -1, p), alpha * beta, p)
    print("c", c)
    Pa_Pb_inv = (Pa * pow(Pb, -1, p)) % p
    print("Pa_Pb_inv", Pa_Pb_inv)
    return c == Pa_Pb_inv


if __name__ == "__main__":
    # Public parameters
    p, h = generate_parameters()

    # Secrets for Alice and Bob
    x = 5000  # Alice's secret
    y = 10000001  # Bob's secret

    # Check if secrets are equal without revealing them
    if socialist_millionaire(p, h, x, y):
        print("Secrets are equal.")
    else:
        print("Secrets are not equal.")

        
# Explanation

# Parameters:
# p: A large prime number.
# h: A generator of a subgroup modulo pp.

# Secrets:
# x: Alice’s secret.
# y: Bob’s secret.

# Protocol:
# Both parties perform computations involving their secrets and the public parameters.
# They exchange certain values and verify whether the secrets match without revealing the actual values.

# Result:
# The program outputs whether x=yx = y.
