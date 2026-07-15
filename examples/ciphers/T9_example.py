"""
T9 Cipher Example:

Original message:
        Hello World!

Encoded message:
        4355696753
"""

from ciphers.T9 import T9Cipher


def T9_example():
    original = "Hello World!"
    encoded = T9Cipher.encode(original)
    
    # Output
    print("T9 Example:\n")
    
    print("\nOriginal message:")
    print(f"\t{original}")

    print("\nEncrypted message:")
    print(f"\t{encoded}")
    

if __name__ == "__main__":
    T9_example()