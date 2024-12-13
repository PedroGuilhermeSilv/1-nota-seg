# Combina as chaves de duas cifras Affine
def combine_keys(a1, b1, a2, b2, m):
    a3 = (a1 * a2) % m
    b3 = (a2 * b1 + b2) % m
    return a3, b3

# Entradas
a1, b1 = 3, 5
a2, b2 = 11, 7
m = 30

# Calculando a chave combinada
a3, b3 = combine_keys(a1, b1, a2, b2, m)
print("Chave combinada a3:", a3)
print("Chave combinada b3:", b3)