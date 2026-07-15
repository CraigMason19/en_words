"""
Reversible T9 Cipher Example:

Original message:
        Hello World!

Encoded message:
        44-33-555-555-666-9-666-777-555-3

Decoded message:
        helloworld
"""

from ciphers.T9 import ReversibleT9Cipher


def reversible_T9_example():
    original = "Hello World!"
    encoded = ReversibleT9Cipher.encode(original)
    decoded = ReversibleT9Cipher.decode(encoded)
    
    # Output
    print("Reversible T9 Example:\n")
    
    print("\nOriginal message:")
    print(f"\t{original}")

    print("\nEncrypted message:")
    print(f"\t{encoded}")
    
    print("\nDecoded message:")
    print(f"\t{decoded}")


if __name__ == "__main__":
    reversible_T9_example()