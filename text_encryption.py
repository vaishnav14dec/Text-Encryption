from Crypto.Cipher import AES
import base64

def encrypt(message, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext)
    nonce = ciphertext[:16]
    cipher = AES.new(key.encode('utf-8'), AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext[16:]).decode('utf-8')
    return plaintext

message = input("Enter message: ")
key = input("Enter key (16 characters): ")
ciphertext = encrypt(message, key)
print(f"Encrypted: {ciphertext}")
decrypted = decrypt(ciphertext, key)
print(f"Decrypted: {decrypted}")
