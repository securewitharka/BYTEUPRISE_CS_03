'''
Task 03 ByteUprise
'''
import sys

print("\t\t\tThis is a Text Encrypter and Decrypter Tool made by Arka\n")
alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
         'u','v','w','x','y','z']

def encryption(plain,shift):
    cipher = ""
    for char in plain:
        if char in alpha:
            pos = alpha.index(char)
            bpos = (pos+shift)%26
            cipher += alpha[bpos]
        else:
            cipher += char
    print(f"Text after Encryption: {cipher}\n")

def decryption(cipher,shift):
    plain = ""
    for char in cipher:
        if char in alpha:
            pos = alpha.index(char)
            bpos = (pos-shift)%26
            plain += alpha[bpos]
        else:
            plain += char
    print(f"Text after decryption: {plain}\n")

finish = False
while not finish:
    cryption = input("Type 'e' to encrypt the code or Type 'd' to decrypt the code:  \n")
    message = input("Type your message that you want to encrypt/decrypt: \n").lower()
    shiftnum = int(input("Type a number that is not divisble by 26 to shift and remember it while decrypting the text: \n"))

    if cryption=="e":
        encryption(plain=message,shift=shiftnum)

    elif cryption=="d":
        decryption(cipher=message,shift=shiftnum)

    again = input("Type 'run' to run the script again or type 'exit' to exit the code: \n")
    if again=="exit":
        finish=True
        print("Thank you for using the code..!!")
        sys.exit()






