from secretpy import Vigenere, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll

var = input('What do you want to do? ')
plaintext = u""
key = ""
cipher = Vigenere()

cm0 = CryptMachine(cipher, key)
cm = SaveAll(cm0)
cm.set_alphabet(al.ITALIAN)

def encdec(machine, plaintext):
    enc = machine.encrypt(plaintext)
    print(enc)

def decenc(machine, plaintext):
    dec = machine.decrypt(plaintext)
    print(dec)

if var == "Encrypt":
    encdec(cm, plaintext)
elif var == "Decrypt":
    decenc(cm, plaintext)