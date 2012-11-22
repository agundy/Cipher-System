# Aaron Gunderson


def caesar_encrypt(plaintext,mod):
    alphabet_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


    for i in range(0,26):
        crypt[i] = (alphabet_num[i] + mod) % 26

    upper = len(plaintext)
    newstring = ''
    low = 0
    up = 1
    
    for l in range(0, upper):
        if plaintext[low:up].isspace():
            newstring += ' '
        else:
            newstring += alphabet[crypt[alphabet.index(plaintext[low:up])]]
        low +=1
        up +=1
        
        
    print "\n Here is the coded message: " + newstring 
    print
    

def caesar_multiply(plaintext,mod):
    alphabet_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


    for i in range(0,26):
        crypt[i] = (alphabet_num[i] * mod) % 26

    upper = len(plaintext)
    newstring = ''
    low = 0
    up = 1
    
    for l in range(0, upper):
        if plaintext[low:up].isspace():
            newstring += ' '
        else:
            newstring += alphabet[crypt[alphabet.index(plaintext[low:up])]]
        low +=1
        up +=1

    print "\n Here is the coded message: " + newstring 
    print
    

##def keyed_caesar(plaintext,key,mod):
##    alphabet_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
##    crypt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
##
##    key = re.sub(r'([a-z])\1+', r\1, key)
##
##    print key
##    for i in range(0,26):
##        crypt[i] = (alphabet_num[i] + mod) % 26
##    
##    upper = len(plaintext)
##    newstring = ''
##    low = 0
##    up = 1
##    
##    for l in range(0, upper):
##        if plaintext[low:up].isspace():
##            newstring += ' '
##        else:
##            newstring += alphabet[crypt[alphabet.index(plaintext[low:up])]]
##        low +=1
##        up +=1
##        
##        
##    print "\n Here is the coded message: " + newstring 
##    print
##    
    

def caesar_decrypt_key(mod):
    alphabet_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt_alphabet = []

    for i in range(0,26):
        crypt[i] = int((alphabet_num[i] + mod) % 26)

    low = 0
    
    for n in range(0,26):
        ciphered_number = int(crypt[low])
        cipherletter = alphabet[ciphered_number]
        crypt_alphabet.append(cipherletter)
                                
        low += 1
        
    print
    print "Here is your key. \n"
    print "Alphabet | Cipher Alphabet" 
    for n in range(0,26):
        print "  ", alphabet[n], "    |   ", crypt_alphabet[n]
        
    
def caesar_multiply_decrypt_key(mod):
    alphabet_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt_alphabet = []

    for i in range(0,26):
        crypt[i] = int((alphabet_num[i] * mod) % 26)

    low = 0
    
    for n in range(0,26):
        ciphered_number = int(crypt[low])
        cipherletter = alphabet[ciphered_number]
        crypt_alphabet.append(cipherletter)                        
        low += 1
        n+=1
        
    print
    print "Here is your key."
    for n in range(0,26):
        print "  ", alphabet[n], "    |   ", crypt_alphabet[n]
        

def caesar_decipher(cipher,mod):
    alphabet_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


    for i in range(0,26):
        crypt[i] = (alphabet_num[i] - mod) % 26

    upper = len(cipher)
    newstring = ''
    low = 0
    up = 1
    
    for l in range(0, upper):
        if cipher[low:up].isspace():
            newstring += ' '
        else:
            newstring += alphabet[crypt[alphabet.index(cipher[low:up])]]
        low +=1
        up +=1
        
        
    print "\n Here is the coded message: " + newstring 
    print

def again():
    answer = raw_input("Would you like to do something else? (y/n)")
    if answer == 'y':
        start()
    elif answer == 'n':
        print
        print "Thanks for using Aaron Gunderson's Cipher System"
        raw_input()
        
def start():
    while True:
        try:
            mode = int(raw_input("What would you like to do? \n 1 Encrypt \n 2 Decrypt \n 3 Create a key \n   :"))
            break
        except mode != 1 or mode != 2 or mode != 3 or ValueError :
            print "Enter a valid integer \n"
    if mode == 1:
        while True:
            try:
                mode = int(raw_input('What encryption would you like to use? \n 1 Caesar \n 2 Caesar Multiply \n 3 Caesar Key \n    : '))
                break
            except mode != 1 or mode != 2 or mode != 3 or ValueError :
                print "Enter a valid option \n"

        if mode == 1:
            plaintext = raw_input("Enter a plaintext: ")
            plaintext = str.lower(plaintext)
            mod = raw_input("Enter the number you would like to shift by: ")
            mod = int(mod)
            caesar_encrypt(plaintext,mod)
        elif mode == 2:
            plaintext = raw_input("Enter a plaintext: ")
            plaintext = str.lower(plaintext)
            mod = raw_input("Enter the multiple you would like to shift by: \n (Note it must be a relative prime of 26)  \n    : ")
            mod = int(mod)
            caesar_multiply(plaintext,mod)
        elif mode == 3:
            plaintext = raw_input("Enter a plaintext: ")
            plaintext = str.lower(plaintext)
            key = raw_input("Enter the key word:")
            key = str.lower(key)
            mod = raw_input("Enter the number you would like to shift by: \n (Note it must be a relative prime of 26)  \n    : ")
            mod = int(mod)
            caesar_multiply(plaintext,mod)
    elif mode == 2:
        while True:
            try:
                mode = int(raw_input('What decipher key would you like to use? \n 1 Caesar \n 2 Caesar Multiply \n    : '))
                break
            except mode != 1 or mode != 2 or mode != 3 or ValueError :
                print "Enter a valid option \n"
        if mode == 1:
            mod = raw_input("What Caesar shift number would you like to use?  \n    : ")
            cipher = raw_input("What is the ciphered message?")
            if mod.isdigit():
                mod = int(mod)
                caesar_decipher(cipher,mod)
            elif mod == "all":
                for n in range(0,25):
                    mod = n
                    caesar_decipher(cipher,mod)
                    n+=1
    elif mode == 3:
        while True:
            try:
                mode = int(raw_input('What decipher key would you like to make? \n 1 Caesar \n 2 Caesar Multiply \n    : '))
                break
            except mode != 1 or mode != 2 or ValueError :
                print "Enter a valid option \n"
        if mode == 1:
            mod = raw_input("What Caesar shift number would you like to use?  \n    : ")
            if mod.isdigit():
                mod = int(mod)
                caesar_decrypt(mod)
            elif mod == "all":
                for n in range(0,25):
                    mod = n
                    caesar_decipher(mod)
                    n+=1
        elif mode == 2:
            mod = raw_input("What Caesar shift multiple would you like to use?  \n    : ")
            if mod.isdigit():
                mod = int(mod)
                caesar_multiply_decrypt_key(mod)
            elif mod == "all":
                for n in range(0,25):
                    mod = n
                    caesar_multiply_decrypt_key(mod)
                    n+=1
            
    else:
        print "Please enter either 1 or 2!"
        start()
    again()
    
import re

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print "Welcome to Cipher Systems... "
print "Created by: Aaron Gunderson \n"

start()
