#shift cipher
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

print("----------------WELCOME TO SHIFT CIPHER--------------")

def shift_algo():
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
