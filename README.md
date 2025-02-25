```markdown
# RSA Key Generator

## Overview

This project implements an RSA key pair generator in Python. RSA is a widely-used public key cryptosystem that enables secure data transmission. The generator produces two prime numbers, `p` and `q`, and uses them to calculate the public and private keys.

The public key is used for encryption, while the private key is used for decryption. This simple implementation allows users to specify the bit length of the primes and generates the corresponding RSA key pair.

## Features

- Generates two large prime numbers `p` and `q`.
- Computes the modulus `n = p * q`.
- Calculates Euler’s Totient Function `φ(n) = (p - 1)(q - 1)`.
- Uses `e = 65537` as the public exponent (a commonly used value).
- Computes the private exponent `d` using the modular inverse of `e` modulo `φ(n)`.
- Returns the public key `(e, n)` and private key `(d, n)`.

## Requirements

- Python 3.x
- `pycryptodome` library for cryptographic operations.

## Installation


git clone https://github.com/DustinThebegginer/rsa-key-generator.git
pip install pycryptodome
```

## Usage

1. Run the RSA key generator script:

   ```bash
   python rsa_key_generator.py
   ```

2. Enter the number of bits you want for the prime numbers `p` and `q` when prompted (e.g., 1024 or 2048 bits).

3. The script will output the generated public and private keys.

### Example Output

```bash
Enter the number of bits for the prime numbers (p and q): 1024

Public Key (e, n):
(65537, 1234567890123456789)

Private Key (d, n):
(9876543210987654321, 1234567890123456789)
```

## How It Works

1. **Prime Generation**: Two large prime numbers `p` and `q` are generated using the `pycryptodome` library.
2. **Modulus Calculation**: The modulus `n` is calculated as `n = p * q`. This value is part of both the public and private keys.
3. **Euler’s Totient Function**: `φ(n)` is calculated as `(p - 1)(q - 1)`. It’s used to compute the private exponent.
4. **Public and Private Exponents**: The public exponent `e` is set to 65537, and the private exponent `d` is calculated as the modular inverse of `e` modulo `φ(n)`.
5. **Key Pair**: The final public key is `(e, n)`, and the private key is `(d, n)`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests with improvements. If you encounter any bugs or have feature requests, please create an issue in the GitHub repository.

## Acknowledgments

- This project uses the `pycryptodome` library for cryptographic operations. Check out their [documentation](https://pycryptodome.readthedocs.io/) for more details on cryptographic functions.
```
