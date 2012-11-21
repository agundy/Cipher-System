# Aaron Gunderson


def caesar_encrypt(string,mod):
    alphabet_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


    for i in range(0,26):
        crypt[i] = (alphabet_num[i] + mod) % 26

    upper = len(string)
    newstring = ''
    low = 0
    up = 1
    
    for l in range(0, upper):
        newstring += alphabet[crypt[alphabet.index(string[low:up])]]
        low +=1
        up +=1
        l +=1
        
    print "\n Here is the coded message: " + newstring 
    print
    
    ##print alphabet[crypt[alphabet.index(string[0:1])]]
    ##print alphabet[0:9]
    ##print alphabet[0]

    again()

def caesar_multiply(string,mod):
    alphabet_num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    crypt = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]


    for i in range(0,26):
        crypt[i] = (alphabet_num[i] * mod) % 26

    upper = len(string)
    newstring = ''
    low = 0
    up = 1
    
    for l in range(0, upper):
        newstring += alphabet[crypt[alphabet.index(string[low:up])]]
        low +=1
        up +=1

    print "\n Here is the coded message: " + newstring 
    print
    
    again()
    

def caesar_decrypt(mod):
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
        
    again()
    
def caesar_multiply_decrypt(mod):
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
     
##    print alphabet
##    print crypt_alphabet

    again()

def again():
    answer = raw_input("Would you like to do something else? (y/n)")
    if answer == 'y':
        start()
    elif answer == 'n':
        print
        print "Thanks for using Aaron Gunderson's Cipher System"
        raw_input()
        
def start():
    mode = int(raw_input("What would you like to do? \n 1 Encrypt \n 2 Decrypt \n"))
    if mode == 1:
        mode = int(raw_input('What encryption would you like to use? \n 1 Caesar \n 2 Caesar Multiply \n    : '))
        if mode == 1:
            string = raw_input("Enter a string: ")
            mod = raw_input("Enter the number you would like to shift by: ")
            mod = int(mod)
            caesar_encrypt(string,mod)
        elif mode == 2:
            string = raw_input("Enter a string: ")
            mod = raw_input("Enter the multiple you would like to shift by: \n (Note it must be a relative prime of 26)  \n    : ")
            mod = int(mod)
            caesar_multiply(string,mod)
    elif mode == 2:
        mode = int(raw_input('What decryption would you like to use? \n 1 Caesar \n 2 Caesar Multiply \n    : '))
        if mode == 1:
            mod = raw_input("What Caesar shift number would you like to use?  \n    : ")
            if mod.isdigit():
                mod = int(mod)
                caesar_decrypt(mod)
            elif mod == "all":
                for n in range(0,25):
                    mod = n
                    caesar_decrypt(mod)
                    n+=1
        elif mode == 2:
            mod = raw_input("What Caesar shift multiple would you like to use?  \n    : ")
            if mod.isdigit():
                mod = int(mod)
                caesar_multiply_decrypt(mod)
            elif mod == "all":
                for n in range(0,25):
                    mod = n
                    caesar_multiply_decrypt(mod)
                    n+=1
            
    else:
        print "Please enter either 1 or 2!"
        start()

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print "Welcome to Cipher Systems... "
print "Created by: Aaron Gunderson \n"
start()
