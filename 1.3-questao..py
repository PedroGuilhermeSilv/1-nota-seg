

def calculate_key_search_time():
    # Constants
    keys_per_second_per_asic = 5e8
    asic_cost = 50
    overhead_multiplier = 2
    total_budget = 1_000_000
    universe_age_years = 1e10

    # Calculate number of ASICs
    total_cost_per_asic = asic_cost * overhead_multiplier
    num_asics = total_budget // total_cost_per_asic
    
    # Calculate total keys per second
    total_keys_per_second = keys_per_second_per_asic * num_asics
    
    # Calculate average search time
    key_space = 2**128
    avg_keys_to_check = key_space / 2
    seconds_needed = avg_keys_to_check / total_keys_per_second
    
    # Convert to years
    years_needed = seconds_needed / (365 * 24 * 3600)
    
    # Compare to universe age
    universe_ratios = years_needed / universe_age_years
    
    print(f"Number of parallel ASICs: {num_asics:,}")
    print(f"Years needed: {years_needed:.2e}")
    print(f"Multiple of universe age: {universe_ratios:.2e}")

calculate_key_search_time()


def calculate_future_break_time():
    # Constants
    CURRENT_KEYS_PER_ASIC = 5e8
    ASIC_COST = 50
    OVERHEAD_MULTIPLIER = 2
    TOTAL_BUDGET = 1_000_000
    TARGET_HOURS = 24
    
    # Calculate current capacity
    num_asics = TOTAL_BUDGET // (ASIC_COST * OVERHEAD_MULTIPLIER)
    current_keys_per_second = CURRENT_KEYS_PER_ASIC * num_asics
    
    # Calculate required capacity for 24-hour break
    key_space = 2**128
    avg_keys_to_check = key_space / 2
    target_keys_per_second = avg_keys_to_check / (TARGET_HOURS * 3600)
    
    # Calculate required improvement factor
    improvement_needed = target_keys_per_second / current_keys_per_second
    
    # Calculate years using Moore's Law
    # If power doubles every 18 months, then in n months we get 2^(n/18) improvement
    import math
    months_needed = 18 * math.log2(improvement_needed)
    years_needed = months_needed / 12
    
    print(f"Current keys/second: {current_keys_per_second:.2e}")
    print(f"Required keys/second: {target_keys_per_second:.2e}")
    print(f"Improvement factor needed: {improvement_needed:.2e}x")
    print(f"Years until breakable: {years_needed:.1f}")

calculate_future_break_time()