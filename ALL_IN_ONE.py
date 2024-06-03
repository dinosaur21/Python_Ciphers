



#---------------------------------------------------------------
#shift cipher    
def shift():
#for CAESAR_CIPHER enter the shift as 3


    def encrypt(text, s):
        result = []

        for char in text:
            if char.isalpha():
                shift = 65 if char.isupper() else 97
                result.append(chr((ord(char) - shift + s) % 26 + shift))
            else:
                result.append(char)

        return ''.join(result)

    

    def shift_algo():
        print("----------------WELCOME TO SHIFT CIPHER--------------\n")
        text = input("enter string:  ")
        s = int(input("enter shift value:   "))
        print("Text  : " + text)
        print("Shift : " + str(s))
        print("Cipher: " + encrypt(text,s))
        print("\n")
        ip= input("Do you wanna try again? (yes/no) :   ")
        if ip=="yes":
            shift_algo()
        else:
            print("EXITING....")

    shift_algo()


#---------------------------------------------------------------
#vignere cipher
def vig():
    
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

#---------------------------------------------------------------
# Rail Fence Cipher 

# encryption
def encrypt_rail_fence(text, key):
    # rail matrix
    rail = ['' for _ in range(key)]
    
    dir_down = False
    row = 0

    for char in text:
        # Reverse direction 
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        rail[row] += char
        
        row += 1 if dir_down else -1

    return ''.join(rail)

# decryption
def decrypt_rail_fence(cipher, key):
    # rail matrix
    rail = [['' for _ in range(len(cipher))] for _ in range(key)]
    
    dir_down = None
    row, col = 0, 0
    
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        row += 1 if dir_down else -1

    index = 0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c] == '*' and index < len(cipher):
                rail[r][c] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        
        row += 1 if dir_down else -1

    return ''.join(result)


# main function
def railcipher():
    print("-------------WELCOME TO RAILFENCE CIPHER---------------\n")

    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ")
        if choice not in ('e', 'd'):
            print("Invalid!! Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        text = input("Enter the text: ")
        key = int(input("Enter the key: "))
        
        if choice == 'e':
            encrypted_text = encrypt_rail_fence(text, key)
            print("Encrypted Text:", encrypted_text)
        elif choice == 'd':
            decrypted_text = decrypt_rail_fence(text, key)
            print("Decrypted Text:", decrypted_text)
        
        repeat = input("Do you want to perform another operation? (yes/no): ")
        if repeat != 'yes':
            print("Exiting...")
            break



def rf():
    railcipher()

#---------------------------------------------------------------------
#main main function
print("***********WELCOME TO CIPHER TOWN*********\n")
print("1-  Shift Cipher\n2-  Vigenère Cipher\n3-  Rail Fence Cipher\n")
r=int(input("WHICH CIPHER DO YOU WANT TO TRY?(1/2/3)"))

if r==1:
    shift()
elif r==2:
    vig()
else:
    rf()
