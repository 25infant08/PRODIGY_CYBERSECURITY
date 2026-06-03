def caesar_cipher(txt,shift):
    encrypted_txt = ""
    for char in txt:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            encrypted_txt += new_char
        else:
            encrypted_txt += char
    return encrypted_txt
message = input("Enter the message: ")
try:
    shift = int(input("Enter the shift value: "))
    encrypted = caesar_cipher(message,shift)
    print("Encrypted message: ",encrypted)
except ValueError:
    print("Invalid shift value. Please enter a valid integer.")