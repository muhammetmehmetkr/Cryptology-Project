import os
#==============================================================================================
# Affine Cipher Algorithms
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26)
                         + ord('A')) for t in text.upper().replace(' ', '')])


def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1]))
                          % 26) + ord('A')) for c in cipher.upper().replace('', '')])
#==============================================================================================
# Caesar Cipher Algorithms
def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():            
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))            
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:            
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)
#==============================================================================================
# Vigenere Cipher Algorithms
def encrypt_vigenere(plaintext, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + (ord(key[key_index % len(key)]) - ord('A'))) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + (ord(key[key_index % len(key)]) - ord('A'))) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

def decrypt_vigenere(ciphertext, key):
    key = key.upper()
    decrypted_text = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - (ord(key[key_index % len(key)]) - ord('A'))) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - (ord(key[key_index % len(key)]) - ord('A'))) % 26 + ord('A'))
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text
#==============================================================================================
while True:
    print("""
1.CAESAR CIPHER
2.AFFINE CIPHER
3.VIGENERE CIPHER
4.EXIT
""")
    choice = input('Please select process: ')
    os.system('cls' if os.name == 'nt' else 'clear')

    if choice == '1':
        while True:
            print("""
********** CAESAR **********
1.ENCRYPT
2.DECRYPT
****************************
""")
            choice2 = input('Please select process: ')
            os.system('cls' if os.name == 'nt' else 'clear')

            if choice2 == '1':
                text = input("Please enter plaintext: ")
                shift = int(input("Enter the shift amount: "))
                print("Ciphertext:", encrypt_caesar(text, shift))
                break
            elif choice2 == '2':
                text = input("Please enter ciphertext: ")
                shift = int(input("Enter the shift amount: "))
                print("Plaintext:", decrypt_caesar(text, shift))
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--> Please select valid process..')
                
    elif choice == '2':
        while True:
            print("""
********** AFFINE **********
1.ENCRYPT
2.DECRYPT
****************************
""")
            choice2 = input("Please select process: ")
            os.system('cls' if os.name == 'nt' else 'clear')

            if choice2 == '1':
                a = int(input('Please enter (a) value: '))
                b = int(input('Please enter (b) value: '))
                text1 = input('\nPlease enter plaintext: ')
                key_value = [a, b]
                print('--> Encrypted Text:', affine_encrypt(text1, key_value))
                break
            elif choice2 == '2':
                a = int(input('Please enter (a) value: '))
                b = int(input('Please enter (b) value: '))
                text2 = input('\nPlease enter ciphertext: ')                
                key_value = [a, b]
                print('--> Decrypted Text:', affine_decrypt(text2, key_value))
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--> Please select valid process..')

    elif choice == '3':        
        while True:
            print("""
********** VIGENERE **********
1.ENCRYPT
2.DECRYPT
******************************
""")
            choice2 = input("Please select process: ")
            os.system('cls' if os.name == 'nt' else 'clear')

            if choice2 == '1':
                plaintext = input("Please enter plaintext: ")
                key = input("Please enter key: ")
                print("--> Encrypted text:", encrypt_vigenere(plaintext, key))
                break
            elif choice2 == '2':
                ciphertext = input("Please enter ciphertext: ")
                key = input("Please enter key: ")
                print("--> Decrypted text:", decrypt_vigenere(ciphertext, key))
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('--> Please select valid process..')

    elif choice == '4':
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('--> Please select valid process..')
