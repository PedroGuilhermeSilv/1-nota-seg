def extended_gcd(a, m):
    """Extended Euclidean Algorithm to find modular multiplicative inverse"""
    if a == 0:
        return m, 0, 1
    
    gcd, x1, y1 = extended_gcd(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """Find modular multiplicative inverse of a mod m"""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Modular inverse does not exist')
    return x % m

def solve_modular_problems():
    # 1. 1/5 mod 13
    inv1 = mod_inverse(5, 13)
    print(f"1. 1/5 mod 13 = {inv1}")
    print(f"   Verification: {(5 * inv1) % 13 = }")
    
    # 2. 1/5 mod 7
    inv2 = mod_inverse(5, 7)
    print(f"\n2. 1/5 mod 7 = {inv2}")
    print(f"   Verification: {(5 * inv2) % 7 = }")
    
    # 3. 3 * (2/5) mod 7
    # First calculate 2/5 = 2 * (1/5) mod 7
    two_fifths = (2 * mod_inverse(5, 7)) % 7
    result3 = (3 * two_fifths) % 7
    print(f"\n3. 3 * 2/5 mod 7 = {result3}")
    print("   Steps:")
    print(f"   - First find 1/5 mod 7 = {inv2}")
    print(f"   - Then 2/5 = 2 * {inv2} mod 7 = {two_fifths}")
    print(f"   - Finally 3 * {two_fifths} mod 7 = {result3}")

solve_modular_problems()