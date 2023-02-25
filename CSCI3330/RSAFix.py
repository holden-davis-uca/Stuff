# CSCI 3330 - CRN 22104 - Fall 2021 - Dr. Hu
# Holden Davis, Jordan Maxwell, Tyler Walters
# Project 1 - RSA: An asymmetric cryptosystem for cybersecurity

# Import sys for proper program exit functionality on any Operating System
import sys
import random as rnd

# Define Program Math Functions
def keyGen() -> list:
    
    # this function generates p
    # it tests large numbers until a pseudo prime for p is found
    def generateP():
        found = False
        while found == False:
            p = rnd.randint(10000,50000)
            found = fermatTest(p)
        return p

    # this function generates q
        # it tests large numbers until a pseudo prime for q is found
    def generateQ():
        found = False
        while found == False:
            q = rnd.randint(10000,50000)
            found = fermatTest(q)
        return q   

    # this function tests if a number is pseudo prime
    def fermatTest(n):
        tests=[]
        for i in range(0, 99):
            tests.append(rnd.randint(1,n-1))
            
        truth = True 
        i = 0
        while i<99 and truth==True:
            answer = pow(tests[i], n-1, n)
            if answer == 1:
                truth = True
            else:
                truth = False
            i=i+1  
        return truth

    # this function generates a public key, e
        # the e value must relitively prime to (p-1)(q-1)
    def generateE(p, q):
        phi = (p-1)*(q-1)
        temp = 0
        
        while temp != 1:
            e = rnd.randint(2,phi)
            temp = gcd(e, phi)
        return e

    # this helper-function generates the gcd of 2 numbers 
    def gcd(a,b):
        if b==0:
            return a
        else:
            return gcd(b, a%b)

    # this function generates the private key, d
        # d is found using extended Euclidean algorithm - solving for x
    def generateD(e, phi):
        d = extended_gcd(e, phi)[0]
        if d < 0:
            d = d % phi
        return d

    # this helper-function computes the extended Euclidean algorithm
    def extended_gcd(a, b):
        if b == 0:
            return(1, 0, a)
        (x, y, d) = extended_gcd(b, a%b)
        return y, x - a//b*y, d

    # Do math magic to generate n, e, and d from p and q
    p = generateP()
    q = generateQ()
    e = generateE(p,q)
    phi: int = (p-1)*(q-1)
    d = generateD(e,phi)
    n = p * q
    public_key = [n, e]
    private_key = [n, d]
    keys = [private_key, public_key]
    print("\n!--- Public and Private Keys Generated ---!")
    return keys

#Encrypt a given message with the public key
def encrypt(message, pubkey) -> str:
    encrypted_message = [pow(ord(index),int(pubkey[1]),int(pubkey[0])) for index in message]
    return encrypted_message

#Decrypt a given message with the private key
def decrypt(emessage, privkey) -> str:
    if "[" in emessage:
        emessage = emessage[1:]
    if "]" in emessage:
        emessage = emessage[0:-1]
    split = emessage.split(', ')
    for chartest in split:
        if chartest.isnumeric() == False and chartest != "," and chartest != " ":
            print("\n!--- Invalid Encrypted Message ---!")
            requestEncryptedMessage(privkey)            
    M2 = [pow(int(index),int(privkey[1]),int(privkey[0])) for index in split]
    decrypted_message = ""
    for ind in M2:
        decrypted_message += str(chr(ind))
    return decrypted_message

#Authenticate a given signature with the public key alonside the signed and original message
def authSignature(omessage, signature, message, pubkey) -> bool:
    if "[" in message:
        message = message[1:]
    if "]" in message:
        message = message[0:-1]
    split = message.split(', ')
    for chartest in split:
        if chartest.isnumeric() == False and chartest != "," and chartest != " ":
            print("\n!--- Invalid Signed Message ---!")
            requestMessage(omessage, signature, pubkey)
    if "[" in omessage:
        omessage = omessage[1:]
    if "]" in omessage:
        omessage = omessage[0:-1]
    split2 = omessage.split(', ')
    for chartest in split2:
        if chartest.isnumeric() == False and chartest != "," and chartest != " ":
            print("\n!--- Invalid Original Message ---!")
            requestOMessage(signature, pubkey)
    m1 = [pow(int(i), int(pubkey[1]), int(pubkey[0])) for i in split]   #decrypt using d
    decrypt_m = [m1[i] - int(signature) for i in range(len(m1))]        #decrypt using digital signature
    split2 = [int(i) for i in split2]
    tf = True
    for i in range(len(decrypt_m)):
        if split2[i] != decrypt_m[i]:
            tf = False
    return tf

# Define Program Logic Functions
def printReturn():
    print("00: Return To User Choice")

def printExit():
    print("0: Exit")


def printBack():
    print("\n9: Back")

#Program start point; request user type
def start():
    print("\nEnter User Type:")
    print("\n1: Public User")
    print("2: Private User\n")
    printExit()
    choice = input("\n---> ")
    if choice == "1":
        publicStart()
    elif choice == "2":
        privateStart()
    elif choice == "0":
        sys.exit()
    else:
        print("\n!--- Command Not Understood ---!")
        start()

#Provide access to functions for public key holders
def publicStart():
    print("\nPublic Key (n,e): " + str(keys[0][0]) + ", " + str(keys[0][1]) + "\n")
    print("Select Public User Task:")
    print("\n1: Encrypt Message")
    print("2: Authenticate Signature")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "1":
        requestEncryptionMessage(keys[0])
    elif choice == "2":
        requestSignature(keys[0])
    elif choice == "9":
        start()
    elif choice == "0":
        sys.exit()
    else:
        print("\n!--- Command Not Understood ---!")
        publicStart()

#Provide access to functions for private key holders 
def privateStart():
    print("\nPublic Key (n,e): " + str(keys[0][0]) + ", " + str(keys[0][1]))
    print("Private Key (n,d): " + str(keys[1][0]) + ", " + str(keys[1][1]) + "\n")
    print("Select Private User Task:\n")
    print("1: Decrypt Message")
    print("2: Generate Signature")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "1":
        requestEncryptedMessage(keys[1])
    elif choice == "2":
        requestMessageSignature(keys[1])
    elif choice == "9":
        start()
    elif choice == "0":
        sys.exit()
    else:
        print("\n!--- Command Not Understood ---!")
        privateStart()

#Request the message to be encrypted with the public key
def requestEncryptionMessage(pubkey):
    print("\nInput Message For Encryption:")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "9":
        publicStart()
    elif choice == "0":
        sys.exit()
    encrypted_message = encrypt(choice, pubkey)
    showEncryptedMessage(encrypted_message, pubkey)

#Show the message encrypted with the public key
def showEncryptedMessage(encrypted_message, pubkey):
    print("\nEncrypted Message: \n")
    print(encrypted_message)
    printBack()
    printExit()
    printReturn()
    choice = input("\n---> ")
    if choice == "9":
        requestEncryptionMessage(pubkey)
    elif choice == "00":
        start()
    elif choice == "0":
        sys.exit()
    else:
        print("\n!--- Command Not Understood ---!")
        showEncryptedMessage(encrypted_message, pubkey)

#Request the signature to validate
def requestSignature(pubkey):
    print("\nInput Signature")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "9":
       publicStart()
    elif choice == "0":
        sys.exit()
    if " " in choice:
        print("\n!--- Signature Should Be A Single Integer ---!")
        requestSignature(pubkey)
    if choice.isnumeric() == False:
        print("\n!--- Signature Should Be An Integer ---!")
        requestSignature(pubkey)
    requestOMessage(choice, pubkey)

#Request the original message to compare against signed message
def requestOMessage(signature, pubkey):
    print("\nInput Original Message:")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "9":
        requestSignature(pubkey)
    elif choice == "0":
        sys.exit()
    requestMessage(choice, signature, pubkey)

#Request the signed message
def requestMessage(omessage, signature, pubkey):
    print("\nInput Signed Message:")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "9":
        requestOMessage(signature, pubkey)
    elif choice == "0":
        sys.exit()
    else:
        if authSignature(omessage, signature, choice, pubkey) == True:
            showValidSignature(omessage, signature, pubkey)
        else: showInvalidSignature(omessage, signature, pubkey)

#Inform user that signature is valid
def showValidSignature(omessage, signature, pubkey):
    print("\nSignature Valid!")
    printBack()
    printExit()
    printReturn()
    choice = input("\n---> ")
    if choice == "9":
        requestMessage(omessage, signature, pubkey)
    elif choice == "00":
        start()
    elif choice == "0":
        sys.exit()
    else:
        print("\n!--- Command Not Understood ---!")
        showValidSignature(omessage, signature, pubkey)

#Inform user that signature is invalid
def showInvalidSignature(omessage, signature, pubkey):
    print("\nSignature Invalid!")
    printBack()
    printExit()
    printReturn()
    choice = input("\n---> ")
    if choice == "9":
        requestMessage(omessage, signature, pubkey)
    elif choice == "00":
        start()
    elif choice == "0":
        sys.exit()
    else:
        print("\n!--- Command Not Understood ---!")
        showInvalidSignature(omessage, signature, pubkey)

#Request a message to sign
def requestMessageSignature(privatekey):
    print("\nInput Message to Sign:")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "9":
        privateStart()
    elif choice == "0":
        sys.exit()
    x = [ord(c) for c in choice]
    requestWordSignature(x, privatekey)

#Request a word to generate signature from
def requestWordSignature(message, privatekey):
    print("\nInput Word, Name, or Other Phrase to Generate Digital Signature:")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "9":
        requestMessageSignature(privatekey)
    elif choice == "0":
        sys.exit()
    st = 0
    for x in choice:
        st = st + ord(x)
    showResult(st, message, privatekey)

#Inform the user of the original message, digital signature, and signed message
def showResult(word, message, privatekey):
    print("\nOriginal Message:\n")
    print(message)
    print("\nDigital Signature:\n")
    print(word)
    print("\nSigned Message:\n")
    c = [pow(message[j] + word, int(privatekey[1]), int(privatekey[0])) for j in range(len(message))]
    print(c)
    printBack()
    printExit()
    printReturn()
    choice = input("\n---> ")
    if choice == "9":
        requestWordSignature(message, privatekey)
    elif choice == "00":
        start()
    elif choice == "0":
        sys.exit()
    print("\n!--- Command Not Understood ---!")

#Request the encrypted message
def requestEncryptedMessage(privatekey):
    print("\nInput Message For Decryption")
    printBack()
    printExit()
    choice = input("\n---> ")
    if choice == "9":
        privateStart()
    elif choice == "0":
        sys.exit()
    decrypted_message = decrypt(choice, privatekey)
    showDecryptedMessage(decrypted_message, privatekey)

#Show the decrypted message
def showDecryptedMessage(decrypted_message, privatekey):
    print("\nDecrypted Message: " + decrypted_message)
    printBack()
    printExit()
    printReturn()
    choice = input("\n---> ")
    if choice == "9":
        requestEncryptedMessage(privatekey)
    elif choice == "00":
        start()
    elif choice == "0":
        sys.exit()
    else:
        print("\n!--- Command Not Understood ---!")
        showDecryptedMessage(decrypted_message, privatekey)

#Generate public and private keys outside of the scope of the user
keys = keyGen()
#Begin the program
start()