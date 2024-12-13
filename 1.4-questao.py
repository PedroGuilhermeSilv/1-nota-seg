import math

def analyze_password_keyspace():
    # 1. Calculate key space for 8 ASCII characters (7-bits each)
    ascii_chars = 128  # 2^7 possible characters
    password_length = 8
    ascii_keyspace = ascii_chars ** password_length
    
    # 2. Convert ASCII keyspace to bits
    ascii_bits = math.log2(ascii_keyspace)
    
    # 3. Calculate key space for lowercase letters
    lowercase_chars = 26
    lowercase_keyspace = lowercase_chars ** password_length
    lowercase_bits = math.log2(lowercase_keyspace)
    
    # 4. Calculate required length for 128-bit security
    # a. Using 7-bit ASCII
    required_ascii_length = math.ceil(128 / math.log2(ascii_chars))
    
    # b. Using lowercase letters
    required_lowercase_length = math.ceil(128 / math.log2(lowercase_chars))
    
    print("1. Key space size (8 ASCII chars):", f"{ascii_keyspace:,.0f}")
    print("2. Equivalent key length:", f"{ascii_bits:.1f} bits")
    print("3. Key length with lowercase only:", f"{lowercase_bits:.1f} bits")
    print("4. Required password length for 128-bit security:")
    print(f"   a. Using ASCII chars: {required_ascii_length} characters")
    print(f"   b. Using lowercase: {required_lowercase_length} characters")

analyze_password_keyspace()