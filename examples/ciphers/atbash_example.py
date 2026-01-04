"""
Atbash Cipher Example:

Original message:
        Hello World!

Encoded message:
        Svool Dliow!

Decoded message:
        Hello World!
"""

from ciphers.atbash import Atbash


def atbash_example():
    original = "Hello World!"
    encoded = Atbash.encode(original)
    decoded = Atbash.decode(encoded)

    # Output
    print("Atbash Cipher Example:")

    print("\nOriginal message:")
    print(f"\t{original}")

    print("\nEncoded message:")
    print(f"\t{encoded}")

    print("\nDecoded message:")
    print(f"\t{decoded}")


if __name__ == "__main__":
    atbash_example()