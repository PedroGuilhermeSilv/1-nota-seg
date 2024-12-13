from sympy import mod_inverse

# Quebra da cifra Affine com dois pares texto plano-texto cifrado
def break_affine(x1, y1, x2, y2, m):
    a = (y2 - y1) * mod_inverse(x2 - x1, m) % m
    b = (y1 - a * x1) % m
    return a, b

# Exemplo de pares texto plano-texto cifrado
x1, y1 = 0, 1  # Primeiro par
x2, y2 = 1, 17  # Segundo par
m = 30

a, b = break_affine(x1, y1, x2, y2, m)
print("Chave recuperada a:", a)
print("Chave recuperada b:", b)