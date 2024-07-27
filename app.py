from flask import Flask, render_template, request, redirect, url_for, flash
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

class AESCipher:
    def __init__(self, key):
        self.key = key
        self.backend = default_backend()
        self.block_size = algorithms.AES.block_size

    def encrypt(self, plaintext):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(self.block_size).padder()
        padded_data = padder.update(plaintext.encode()) + padder.finalize()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return iv + ciphertext

    def decrypt(self, ciphertext):
        iv = ciphertext[:16]
        actual_ciphertext = ciphertext[16:]
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=self.backend)
        decryptor = cipher.decryptor()
        unpadder = padding.PKCS7(self.block_size).unpadder()
        padded_data = decryptor.update(actual_ciphertext) + decryptor.finalize()
        plaintext = unpadder.update(padded_data) + unpadder.finalize()
        return plaintext.decode()

key = os.urandom(32)  # AES-256 key
aes_cipher = AESCipher(key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    plaintext = request.form['input_text'].strip()
    if plaintext:
        ciphertext = aes_cipher.encrypt(plaintext)
        flash(f'Encrypted Text: {ciphertext.hex()}', 'success')
    else:
        flash('Please enter some text to encrypt.', 'danger')
    return redirect(url_for('index'))

@app.route('/decrypt', methods=['POST'])
def decrypt():
    ciphertext_hex = request.form['input_text'].strip()
    if ciphertext_hex:
        try:
            ciphertext = bytes.fromhex(ciphertext_hex)
            plaintext = aes_cipher.decrypt(ciphertext)
            flash(f'Decrypted Text: {plaintext}', 'success')
        except Exception as e:
            flash(f'An error occurred during decryption: {e}', 'danger')
    else:
        flash('Please enter some ciphertext to decrypt.', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
