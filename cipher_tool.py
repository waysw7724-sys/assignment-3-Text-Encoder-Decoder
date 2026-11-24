1. Caesar Cipher Algorithm
def caesar_cipher(text: str, shift: int, mode: str = 'encode') -> str:
    if mode == 'decode':
        shift = -shift
    
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift character and wrap around the 26-letter alphabet
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            # Keep spaces, numbers, and punctuation unchanged
            result.append(char)
    return ''.join(result)


# 2. Vigenère Cipher Algorithm
def vigenere_cipher(text: str, key: str, mode: str = 'encode') -> str:
    key = ''.join(filter(str.isalpha, key)).upper()
    if not key:
        raise ValueError("Key must contain at least one alphabetic character.")
    
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(ke
