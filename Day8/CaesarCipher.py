print("Welcome to Caesar Cipher!")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n")) % 26

def encrypt(text, shift):
    encrypted_list = [] 
    for i in text:
        encrypted_list.append(alphabet[text.index(i) + shift - 1])
    
    encrypted_text = "".join(encrypted_list)
    print(encrypted_text)
  
# def decrypt(text, shift):
    


# if direction == 'encode':    
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)

encrypt(text, shift)