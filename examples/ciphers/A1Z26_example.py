"""
A1Z26 Example:

Original message:
        The quick brown fox jumps over the lazy dog.

Encoded message:
        20 8 5 / 17 21 9 3 11 / 2 18 15 23 14 / 6 15 24 / 10 21 13 16 19 / 15 22 5 18 / 20 8 5 / 12 1 26 25 / 4 15 7

Decoded message:
        THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
"""

from ciphers.A1Z26 import A1Z26


def A1Z26_example():
    original = "The quick brown fox jumps over the lazy dog."
    encoded = A1Z26.encode(original)
    decoded = A1Z26.decode(encoded)

    # Output
    print("A1Z26 Example:")

    print("\nOriginal message:")
    print(f"\t{original}")

    print("\nEncoded message:")
    print(f"\t{encoded}")

    print("\nDecoded message:")
    print(f"\t{decoded}")


if __name__ == "__main__":
    A1Z26_example()