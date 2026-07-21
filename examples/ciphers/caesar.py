"""
Caesar Example:

Original message:
        Hello World!

Encoded message:
        Khoor Zruog!
"""

from ciphers.caesar import Caesar


def caesar_example():
    original = "Hello World!"
    encoded = Caesar.encode(original)
    decoded = Caesar.decode(encoded)
    
    # Output
    print("Caesar Example:\n")

    print("\nOriginal message:")
    print(f"\t{original}")

    print("\nEncrypted message:")
    print(f"\t{encoded}")
    
    print("\nDecrypted message:")
    print(f"\t{decoded}")
    

if __name__ == "__main__":
    caesar_example()