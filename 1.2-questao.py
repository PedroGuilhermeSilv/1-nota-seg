def letter_frequency(text):
    # Initialize frequency dictionary
    freq = {}
    # Count each letter
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

def shift_text(text, shift):
    result = ""
    for char in text.lower():
        if char.isalpha():
            # Shift the character
            ascii_val = ord(char) - ord('a')
            shifted = (ascii_val - shift) % 26
            result += chr(shifted + ord('a'))
        else:
            result += char
    return result

# Given ciphertext
ciphertext = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds"

try:
    # Get frequency analysis
    freq = letter_frequency(ciphertext)
    
    # Print frequencies
    print("Letter frequencies:")
    total_chars = sum(freq.values())
    for char, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        percentage = (count/total_chars) * 100
        print(f"{char}: {percentage:.2f}%")

    # Find most frequent letter
    most_frequent = max(freq.items(), key=lambda x: x[1])[0]
    # Calculate shift assuming most frequent letter should be 'e'
    shift = (ord(most_frequent) - ord('e')) % 26

    print("\nTrying shift:")
    plaintext = shift_text(ciphertext, shift)
    print(f"\nShift {shift}: {plaintext}")

except Exception as e:
    print(f"An error occurred: {e}")