"""
Morse Code Example:

Original message:
        Hello World!

Encoded message:
        .... . .-.. .-.. --- / .-- --- .-. .-.. -..

Decoded message:
        hello world
"""

from ciphers.morse_code import MorseCode


def morse_code_example():
    original = "Hello World!"
    encoded = MorseCode.encode(original)
    decoded = MorseCode.decode(encoded)

    # Output
    print("Morse Code Example:")

    print("\nOriginal message:")
    print(f"\t{original}")

    print("\nEncoded message:")
    print(f"\t{encoded}")

    print("\nDecoded message:")
    print(f"\t{decoded}")


if __name__ == "__main__":
    morse_code_example()