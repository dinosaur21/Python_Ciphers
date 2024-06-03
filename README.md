# PYTHON_CIPHERS

## SHIFT CIPHER
- It takes input text and shift amount(number) and replaces each character with the character in the alphabet which is obtained after going forward 'shift' times (adding the shift amount)
- example:
  text: h
  shift: 5
  encrypted text: ASCII(h) + 5 = m
- For decryption it subtracts the shift amount from the character and goes in reverse direction in the alphabet.
- For caesar cipher , substitute shift = 3
<img width="600" height="250" alt="Screenshot 2024-06-03 at 6 45 19 PM" src="https://github.com/dinosaur21/PYTHON_CIPHERS/assets/140154294/7ff4602f-af27-4ce8-8fc2-ed9399ecd210">


### VIGENÈRE CIPHER
- Is a method of encrypting alphabetic text using a simple form of polyalphabetic substitution.
- It uses a keyword to shift each letter of the plaintext. Here the keyword's characters act as shift for each letter of the plaintext.
- the keyword is repeated until it matches the length of the plaintext.
- Encyrption: Addition of ASCII value of keyword letter to plaintext
- Decryption: Subtraction of ASCII value of keyword letter from cipher text.

<img width="600" height="250" alt="Screenshot 2024-06-03 at 6 43 30 PM" src="https://github.com/dinosaur21/PYTHON_CIPHERS/assets/140154294/38353ddf-d3e2-41a0-811a-6190ab7969fe">

### RAIL FENCE CIPHER
- It is a transposition cipher where letters are placed in zig zag fashion in a matrix with 'key' rows.
- Final result is letters read from left to right starting from 1st row.
  
  <img width="800" height="300" alt="Screenshot 2024-06-03 at 6 58 25 PM" src="https://github.com/dinosaur21/PYTHON_CIPHERS/assets/140154294/9788889f-9a21-4f86-841d-09b07f7d3b2e">

  <img width="600" height="300" alt="Screenshot 2024-06-03 at 6 58 10 PM" src="https://github.com/dinosaur21/PYTHON_CIPHERS/assets/140154294/cc4716c7-4a1d-4126-95c5-15785f08066d">
