import rsa

var = input("What do you want to do? ")
message = "Hello World"
with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

encrypted_message = rsa.encrypt(message.encode(), public_key)

clear_message = rsa.decrypt(encrypted_message, private_key)

if var == "Decrypt":
    print(clear_message)
elif var == "Encrypt":
    print(encrypted_message)