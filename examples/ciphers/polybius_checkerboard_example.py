"""
Polybius Checkerboard Example:

     1    2    3    4    5    
1    A    B    C    D    E    
2    F    G    H    I    K    
3    L    M    N    O    P    
4    Q    R    S    T    U    
5    V    W    X    Y    Z    

Original message:
        The Greek teacher Anaximander brought the first sundial to Greece.

Encrypted message:
        44 23 15 22 42 15 15 25 44 15 11 13 23 15 42 11 33 11 53 24 32 11 33 14 15 42 12 42 34 45 22 23 44 44 23 15 21 24 42 43 44 43 45 33 14 24 11 31 44 34 22 42 15 15 13 15

Decrypted message:
        THEGREEKTEACHERANAXIMANDERBROUGHTTHEFIRSTSUNDIALTOGREECE
"""

from ciphers.polybius_checkerboard import PolybiusCheckerboard


def polybius_example():
    original = "The Greek teacher Anaximander brought the first sundial to Greece."
    encoded = PolybiusCheckerboard.encode(original)
    decoded = PolybiusCheckerboard.decode(encoded)
    
    # Output
    print("Polybius Checkerboard Example:\n")
    
    PolybiusCheckerboard.pretty_print()

    print("\nOriginal message:")
    print(f"\t{original}")

    print("\nEncrypted message:")
    print(f"\t{encoded}")
    
    print("\nDecrypted message:")
    print(f"\t{decoded}")


if __name__ == "__main__":
    polybius_example()