#rail fence encriptar

def rail_fence_encrypt(plain_text, key):
    cipher_text = [''] * key
    for col in range(len(plain_text)):
        row = col % (2 * (key - 1))
        if row >= key:
            row = 2 * (key - 1) - row
        cipher_text[row] += plain_text[col]
    return ''.join(cipher_text)

print(rail_fence_encrypt('hola', 3))