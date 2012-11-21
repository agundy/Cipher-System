# Aaron Gunderson


def caesar_encrypt(string,mod):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
    print newstring
    ##print alphabet[crypt[alphabet.index(string[0:1])]]
    ##print alphabet[0:9]
    ##print alphabet[0]
    answer = raw_input("Would you like to encrypt something else? (y/n)")
    if answer == 'y':
        start()

def caesar_multiply(string,mod):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
        l +=1
    print newstring
    
    answer = raw_input("Would you like to encrypt something else? (y/n)")
    if answer == 'y':
        start()

def start():
        mode = int(raw_input('What encryption would you like to use? \n 1 Caesar \n 2 Caesar Multiply \n'))
        if mode == 1:
            string = raw_input("Enter a string: ")
            mod = raw_input("Enter the number you would like to shift by: ")
            mod = int(mod)
            caesar_encrypt(string,mod)
        elif mode == 2:
            string = raw_input("Enter a string: ")
            mod = raw_input("Enter the multiple you would like to shift by: \n (Note it must be a relative prime of 26)")
            mod = int(mod)
            caesar_multiply(string,mod)
        

answer = raw_input("Would you like to encrypt something? (y/n)")
if answer == 'y':
    start()

