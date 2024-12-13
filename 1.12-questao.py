#1.12.1------------

from math import gcd
from sympy import mod_inverse

# Função de criptografia Affine
def affine_encrypt(x, a, b, m):
    return (a * x + b) % m

# Função de descriptografia Affine
def affine_decrypt(y, a, b, m):
    a_inv = mod_inverse(a, m)  # Inverso multiplicativo de 'a' módulo 'm'
    return (a_inv * (y - b)) % m

# Exemplo de teste
m = 30  # Tamanho do alfabeto estendido (alemão)
x = 10  # Índice do texto plano (exemplo: 'K' ↔ 10)
a, b = 17, 1  # Chaves da cifra

# Criptografando e descriptografando
y = affine_encrypt(x, a, b, m)
x_decrypted = affine_decrypt(y, a, b, m)

print("Índice do texto cifrado:", y)
print("Índice do texto descriptografado:", x_decrypted)

#1.12.2---------


# Calcula o tamanho do espaço de chaves
def key_space(m):
    phi_m = sum(1 for a in range(m) if gcd(a, m) == 1)  # Conta os coprimos de 'm'
    return phi_m * m  # Número de valores possíveis de 'a' multiplicado por 'b'

# Exemplo para m = 30 (alfabeto estendido alemão)
m = 30
print("Tamanho do espaço de chaves:", key_space(m))

#1.12.3---------------

# Função de descriptografia Affine
def affine_decrypt(y, a, b, m):
    a_inv = mod_inverse(a, m)
    return (a_inv * (y - b)) % m

# Mapeamento do alfabeto estendido alemão
german_alphabet = {char: idx for idx, char in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜß")}
german_inverse = {idx: char for char, idx in german_alphabet.items()}

# Texto cifrado e chaves
texto_cifrado = "ÄUßWß"
a, b, m = 17, 1, 30

# Descriptografando
indices_texto_plano = [affine_decrypt(german_alphabet[char], a, b, m) for char in texto_cifrado]
texto_plano = ''.join(german_inverse[idx] for idx in indices_texto_plano)

print("Texto plano:", texto_plano)