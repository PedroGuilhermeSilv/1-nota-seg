from sympy import mod_inverse

# Função de descriptografia Affine
def affine_decrypt(y, a, b, m):
    a_inv = mod_inverse(a, m)  # Inverso multiplicativo de 'a' módulo 'm'
    return (a_inv * (y - b)) % m

# Mapeamento do alfabeto
alfabeto = {char: idx for idx, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
alfabeto_inverso = {idx: char for char, idx in alfabeto.items()}

# Texto cifrado e chaves
texto_cifrado = "falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj"
a, b = 7, 22
m = 26  # Tamanho do alfabeto

# Descriptografando
indices_texto_plano = [affine_decrypt(alfabeto[char], a, b, m) for char in texto_cifrado]
texto_plano = ''.join(alfabeto_inverso[idx] for idx in indices_texto_plano)

print("Texto descriptografado:", texto_plano)