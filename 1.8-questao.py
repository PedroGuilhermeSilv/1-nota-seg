def extended_gcd(a, m):
    if a == 0:
        return m, 0, 1
    gcd, x1, y1 = extended_gcd(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return gcd, x, y

def find_inverse(a, m):
    """Find multiplicative inverse of a mod m if it exists"""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    return x % m

def check_inverses():
    moduli = [11, 12, 13]
    a = 5
    
    print(f"Finding multiplicative inverses of {a}:")
    for m in moduli:
        inv = find_inverse(a, m)
        if inv is None:
            print(f"\nIn Z{m}: No multiplicative inverse exists")
            print(f"Because gcd(5,{m}) ≠ 1")
        else:
            print(f"\nIn Z{m}: {inv}")
            print(f"Verification: {a} * {inv} mod {m} = {(a * inv) % m}")

check_inverses()