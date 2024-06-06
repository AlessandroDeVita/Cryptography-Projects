import rsa

with open("public.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

with open("private.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

#INSERT THE ENCRYPTED MESSAGE IN BITS
encrypted_message = b''
decrypto = rsa.decrypt(encrypted_message, private_key)

print(decrypto)
