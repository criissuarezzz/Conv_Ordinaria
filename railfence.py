 
#RAIL FENCE encriptado con numpys
import numpy as np

def railfence_encrypt(plain_text, key):
    plain_text = plain_text.replace(" ", "")
    plain_text = plain_text.upper()
    plain_text = list(plain_text)
    plain_text = np.array(plain_text)
    plain_text = plain_text.reshape(-1, key)
    plain_text = plain_text.transpose()
    plain_text = plain_text.flatten()
    plain_text = "".join(plain_text)
    return plain_text
railfence_encrypt("hola como estas", 3)