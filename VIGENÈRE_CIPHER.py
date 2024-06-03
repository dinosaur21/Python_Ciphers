
def generate_key(text, keyword):
    key = list(keyword)
    if len(text) == len(key):
        return key
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return ''.join(key)

def encrypt_vigenere(text, key):
    cipher_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            shift = 65 if text[i].isupper() else 97
            x = (ord(text[i]) + ord(key[i % len(key)]) - 2 * shift) % 26 + shift
            cipher_text.append(chr(x))
        else:
            cipher_text.append(text[i])
    return ''.join(cipher_text)

def decrypt_vigenere(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = 65 if cipher_text[i].isupper() else 97
            x = (ord(cipher_text[i]) - ord(key[i % len(key)]) + 26) % 26 + shift
            orig_text.append(chr(x))
        else:
            orig_text.append(cipher_text[i])
    return ''.join(orig_text)


print("--------------WELCOME TO VIGENÈRE CIPHER---------------\n")


#main fucntion
def vigcipher():
    
    text = input("Enter the text to be encrypted: ")
    keyword = input("Enter the keyword: ")
    key = generate_key(text, keyword)
    cipher_text = encrypt_vigenere(text, key)
    print("\n")
    print("Ciphertext:", cipher_text)
    decrypted_text = decrypt_vigenere(cipher_text, key)
    print("Decrypted Text:", decrypted_text)
    print("\n")
    repeat = input("Do you want to perform another operation? (yes/no): ")
    if repeat=="yes":
        vigcipher()
    else:
        print("EXITING....")


vigcipher()
