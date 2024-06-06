from secretpy import Polybius, CryptMachine, alphabets as al
from secretpy.cmdecorators import SaveAll

var = input("What do you want to do? ")
#INSERIRE LA CHIAVE SENZA MAIUSCOLE
key = ""
plaintext = u""
cipher = Polybius()
cm0 = CryptMachine(cipher, key)
cm = SaveAll(cm0)
alphabet = [
    u"p", u"h", u"q", u"g", u"m",
    u"e", u"a", u"y", u"l", u"n",
    u"o", u"f", u"d", u"x", u"k",
    u"r", u"c", u"v", u"s", u"z",
    u"w", u"b", u"u", u"t", u"ij"
]
cm.set_alphabet(alphabet)

def encdec(machine, plaintext):
    enc = machine.encrypt(plaintext)
    print(enc)

#RICORDA CHE QUANDO DECRYPTA ELIMINA LE MAIUSCOLE!
def decenc(machine, plaintext):
    dec = machine.decrypt(plaintext)
    print(dec)

if var == "Encrypt":
    encdec(cm, plaintext)
elif var == "Decrypt":
    decenc(cm, plaintext)