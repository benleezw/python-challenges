from random import randint, choice

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&()-=_.?+"
password = ""

def genPassword(password):
    for r in range (0, randint(12,32)):
        password += choice(characters)
    return password

def encrypt(password):
    encrypted_password = ""
    for r in range (0, len(password)):
        encrypted_password += "*"
    return encrypted_password

def decrypt(password, encrypted_password):
    for r in range (0, len(encrypted_password)):
        cracked = False
        while cracked == False:
            char = choice(characters)
            if char == password[r]:
                enc_pass_list = list(encrypted_password)
                enc_pass_list[r] = char
                enc_pass_str = ''.join(enc_pass_list)
                print(enc_pass_str)
                encrypted_password = enc_pass_str
                cracked = True
            else:
                enc_pass_list = list(encrypted_password)
                enc_pass_list[r] = char
                enc_pass_str = ''.join(enc_pass_list)
                print(enc_pass_str)
        if encrypted_password == password:
            return "Decrypted."

password = genPassword(password)
encrypted_password = encrypt(password)
print(encrypted_password)
decrypted_password = decrypt(password, encrypted_password)
print()
print(decrypted_password)
print(password)
            
    
