def mod_multiply(a, b, m):
    """Compute (a * b) mod m and ensure result is in range [0, m-1]"""
    result = (a * b) % m
    # Handle negative numbers to get positive result
    if result < 0:
        result += m
    return result

def solve_modular_problems():
    modulus = 13
    
    # 1. 15 · 29 mod 13
    result1 = mod_multiply(15, 29, modulus)
    
    # 2. 2 · 29 mod 13
    result2 = mod_multiply(2, 29, modulus)
    
    # 3. 2 · 3 mod 13
    result3 = mod_multiply(2, 3, modulus)
    
    # 4. -11 · 3 mod 13
    result4 = mod_multiply(-11, 3, modulus)
    
    print("Results:")
    print(f"1. 15 · 29 mod 13 = {result1}")
    print(f"2. 2 · 29 mod 13 = {result2}")
    print(f"3. 2 · 3 mod 13 = {result3}")
    print(f"4. -11 · 3 mod 13 = {result4}")
    
    print("\nRelationships:")
    if result1 == result2:
        print("Results 1 and 2 are equal because 15 ≡ 2 (mod 13)")
    if result3 == result4:
        print("Results 3 and 4 are equal because -11 ≡ 2 (mod 13)")

solve_modular_problems()