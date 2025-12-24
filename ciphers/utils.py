
import string

def clean_input(text: str) -> str:
    return ''.join([ch for ch in text.lower() if ch in string.ascii_lowercase])