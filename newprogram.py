def text_to_binary(text):
    return ' '.join(format(ord(i), '08b') for i in text)

def binary_to_text(binary):
    binary_values = binary.split(' ')
    return ''.join(chr(int(b, 2)) for b in binary_values)

# --- Use it ---
msg = input("Apna secret message likho: ")
binary_version = text_to_binary(msg)

print(f"\nBinary Code:\n{binary_version}")

print(f"\nWapas Text Mein:\n{binary_to_text(binary_version)}")