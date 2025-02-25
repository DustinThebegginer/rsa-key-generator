from Crypto.Util import number

# Function to generate a prime number of specified bit length
def generate_prime(bits):
    prime = number.getPrime(bits)
    return prime

# Function to generate RSA public and private keys
def generate_rsa_keypair():
    # Input validation for bit length
    while True:
        try:
            bits = int(input("Enter the number of bits for the prime numbers (p and q): "))
            if bits < 512:  # Minimum bit length for reasonable security
                print("The bit length should be at least 512 bits.")
            else:
                break
        except ValueError:
            print("Please enter a valid number for the bit length.")

    p = generate_prime(bits)
    q = generate_prime(bits)

    # Ensure p and q are not equal
    while p == q:
        q = generate_prime(bits)

    # Calculate n and φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Choose a public exponent (e) that is coprime with φ(n)
    e = 65537  # Common choice for e

    # Compute the modular inverse of e to get d
    d = number.inverse(e, phi_n)

    # Public and private keys
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

# Generate the RSA keypair
public_key, private_key = generate_rsa_keypair()

# Print the public and private keys
print("\nPublic Key (e, n):")
print(public_key)

print("\nPrivate Key (d, n):")
print(private_key)
