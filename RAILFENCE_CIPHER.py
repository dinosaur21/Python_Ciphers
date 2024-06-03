# Rail Fence Cipher Encryption and decryption

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


print("-------------WELCOME TO RAILFENCE CIPHER---------------")
# main function
def railcipher():
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

railcipher()
