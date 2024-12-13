def mod_exp(base, exp, mod):
    """Efficient modular exponentiation using square-and-multiply"""
    if exp == 0:
        return 1
    result = 1
    base = base % mod
    while exp > 0:
        if exp & 1:  # If exp is odd
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def discrete_log(g, h, p):
    """Find x where g^x ≡ h (mod p) using brute force"""
    for x in range(p):
        if mod_exp(g, x, p) == h:
            return x
    return None

def solve_problems():
    print("1. 3² mod 13:")
    result1 = mod_exp(3, 2, 13)
    print(f"   3² = 9 ≡ {result1} (mod 13)")
    
    print("\n2. 7² mod 13:")
    result2 = mod_exp(7, 2, 13)
    print(f"   7² = 49 ≡ {result2} (mod 13)")
    
    print("\n3. 3¹⁰ mod 13:")
    print("   Using square-and-multiply:")
    print("   3¹⁰ = (3²)⁵ = 9⁵ mod 13")
    result3 = mod_exp(3, 10, 13)
    print(f"   Result: {result3}")
    
    print("\n4. 7¹⁰⁰ mod 13:")
    print("   Using square-and-multiply algorithm")
    result4 = mod_exp(7, 100, 13)
    print(f"   Result: {result4}")
    
    print("\n5. Find x where 7ˣ ≡ 11 (mod 13):")
    x = discrete_log(7, 11, 13)
    print(f"   x = {x}")
    if x is not None:
        print(f"   Verification: 7^{x} mod 13 = {mod_exp(7, x, 13)}")

solve_problems()