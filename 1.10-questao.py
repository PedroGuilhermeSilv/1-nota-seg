from math import gcd

# Função para calcular números relativamente primos a 'm'
def euler_phi(m):
    # Lista de números n que são coprimos a m
    coprimos = [n for n in range(m) if gcd(n, m) == 1]
    return coprimos, len(coprimos)

# Valores de m
valores_m = [4, 5, 9, 26]

for m in valores_m:
    coprimos, phi_m = euler_phi(m)
    print(f"Para m = {m}, os números relativamente primos são: {coprimos}")
    print(f"φ({m}) = {phi_m}")