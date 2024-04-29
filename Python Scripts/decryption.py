from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as f_in:
        ciphertext = f_in.read()

    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()

    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    with open(output_file, 'wb') as f_out:
        f_out.write(unpadded_data)

# Example usage:
input_file = 'encrypted_file.txt'
output_file = 'decrypted_file.txt'
encryption_key = b'my_secret_key_123'  # Replace with your actual encryption key

decrypt_file(input_file, output_file, encryption_key)
print("File decrypted successfully!")
