# print("Welcome to Caesar Cipher!")

# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n")) % 26

# def encrypt(text, shift):
#     print("Let's encode!")
#     encrypted_list = [] 
#     for i in text:
#         if i not in alphabet:
#             encrypted_list.append(i)
#         else:
#             encrypted_list.append(alphabet[text.index(i) + shift])
#     encrypted_text = "".join(encrypted_list)
#     print(f"Encrypt code: {encrypted_text}")
  
# def decrypt(text, shift):
#     print("Let's decode!")
#     decrypted_list = []
#     for i in text:
#         if i not in alphabet:
#             decrypted_list.append(i)
#         else:
#             decrypted_list.append(alphabet[text.index(i) - shift])
    
#     decrypted_text = "".join(decrypted_list)
#     print(f"Decrypt code: {decrypted_text}")
    
# def ceasar(text, shift, direction):
#     if direction == 'encode':    
#         encrypt(text, shift)
#     else:
#         decrypt(text, shift)

# ceasar(text, shift, direction)

print("Welcome to Caesar Cipher!")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) % 26

def encrypt(text, shift):
    print("Let's encode!")
    encrypted_list = [] 
    for i in text:
        if i not in alphabet:
            encrypted_list.append(i)
        else:
            # Find the index of the character in the alphabet and shift it
            new_index = (alphabet.index(i) + shift) % 26
            encrypted_list.append(alphabet[new_index])
    encrypted_text = "".join(encrypted_list)
    print(f"Encrypt code: {encrypted_text}")
  
def decrypt(text, shift):
    print("Let's decode!")
    decrypted_list = []
    for i in text:
        if i not in alphabet:
            decrypted_list.append(i)
        else:
            # Find the index of the character in the alphabet and shift it backwards
            new_index = (alphabet.index(i) - shift) % 26
            decrypted_list.append(alphabet[new_index])
    
    decrypted_text = "".join(decrypted_list)
    print(f"Decrypt code: {decrypted_text}")
    
def ceasar(text, shift, direction):
    if direction == 'encode':    
        encrypt(text, shift)
    else:
        decrypt(text, shift)

ceasar(text, shift, direction)
