import tkinter as tk
from tkinter import ttk

class CipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cipher Tool")
        self.create_widgets()

    def create_widgets(self):
        # Cipher Type Selection
        cipher_label = ttk.Label(self.root, text="Select Cipher Type:")
        cipher_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.cipher_combobox = ttk.Combobox(self.root, values=["Caesar Cipher", "Vigenere Cipher", "Affine Cipher"], state="readonly")
        self.cipher_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.cipher_combobox.bind("<<ComboboxSelected>>", self.update_fields)

        # Key A Entry (for Affine Cipher)
        self.key_a_label = ttk.Label(self.root, text="Key A:")
        self.key_a_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.key_a_entry = ttk.Entry(self.root)
        self.key_a_entry.grid(row=1, column=1, padx=10, pady=10)

        # Key B Entry (for Affine Cipher)
        self.key_b_label = ttk.Label(self.root, text="Key B:")
        self.key_b_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.key_b_entry = ttk.Entry(self.root)
        self.key_b_entry.grid(row=2, column=1, padx=10, pady=10)

        # Key Entry (for Caesar and Vigenere Ciphers)
        self.key_label = ttk.Label(self.root, text="Key:")
        self.key_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.key_entry = ttk.Entry(self.root)
        self.key_entry.grid(row=1, column=1, padx=10, pady=10)

        # Text Entry
        text_label = ttk.Label(self.root, text="Text:")
        text_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.text_entry = ttk.Entry(self.root)
        self.text_entry.grid(row=3, column=1, padx=10, pady=10)

        # Result Display
        result_label = ttk.Label(self.root, text="Result:")
        result_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")

        self.result_entry = ttk.Entry(self.root, state="readonly")
        self.result_entry.grid(row=4, column=1, padx=10, pady=10)

        # Encrypt Button
        encrypt_button = ttk.Button(self.root, text="Encrypt", command=self.encrypt_text)
        encrypt_button.grid(row=5, column=0, pady=20)

        # Decrypt Button
        decrypt_button = ttk.Button(self.root, text="Decrypt", command=self.decrypt_text)
        decrypt_button.grid(row=5, column=1, pady=20)

        # Clear Button
        clear_button = ttk.Button(self.root, text="Clear", command=self.clear_fields)
        clear_button.grid(row=6, column=0, columnspan=2, pady=20)

    def update_fields(self, event):
        selected_cipher = self.cipher_combobox.get()

        if selected_cipher == "Caesar Cipher" or selected_cipher == "Vigenere Cipher":
            self.key_a_label.grid_remove()
            self.key_a_entry.grid_remove()
            self.key_b_label.grid_remove()
            self.key_b_entry.grid_remove()

            self.key_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            self.key_entry.grid(row=1, column=1, padx=10, pady=10)

        elif selected_cipher == "Affine Cipher":
            self.key_label.grid_remove()
            self.key_entry.grid_remove()

            self.key_a_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            self.key_a_entry.grid(row=1, column=1, padx=10, pady=10)
            self.key_b_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            self.key_b_entry.grid(row=2, column=1, padx=10, pady=10)

    def encrypt_text(self):
        selected_cipher = self.cipher_combobox.get()

        if selected_cipher == "Caesar Cipher":
            shift = int(self.key_entry.get())
            if self.text_entry.get() and self.key_entry.get():
                result = encrypt_caesar(self.text_entry.get(), shift)
                self.result_entry.config(state="normal")
                self.result_entry.delete(0, "end")
                self.result_entry.insert(0, result)
                self.result_entry.config(state="readonly")

        elif selected_cipher == "Vigenere Cipher":
            key = self.key_entry.get()
            if self.text_entry.get() and key:
                result = encrypt_vigenere(self.text_entry.get(), key)
                self.result_entry.config(state="normal")
                self.result_entry.delete(0, "end")
                self.result_entry.insert(0, result)
                self.result_entry.config(state="readonly")

        elif selected_cipher == "Affine Cipher":
            key_a = int(self.key_a_entry.get())
            key_b = int(self.key_b_entry.get())
            if self.text_entry.get() and self.key_a_entry.get() and self.key_b_entry.get():
                result = encrypt_affine(self.text_entry.get(), key_a, key_b)
                self.result_entry.config(state="normal")
                self.result_entry.delete(0, "end")
                self.result_entry.insert(0, result)
                self.result_entry.config(state="readonly")

    def decrypt_text(self):
        selected_cipher = self.cipher_combobox.get()

        if selected_cipher == "Caesar Cipher":
            shift = int(self.key_entry.get())
            if self.text_entry.get() and self.key_entry.get():
                result = decrypt_caesar(self.text_entry.get(), shift)
                self.result_entry.config(state="normal")
                self.result_entry.delete(0, "end")
                self.result_entry.insert(0, result)
                self.result_entry.config(state="readonly")

        elif selected_cipher == "Vigenere Cipher":
            key = self.key_entry.get()
            if self.text_entry.get() and key:
                result = decrypt_vigenere(self.text_entry.get(), key)
                self.result_entry.config(state="normal")
                self.result_entry.delete(0, "end")
                self.result_entry.insert(0, result)
                self.result_entry.config(state="readonly")

        elif selected_cipher == "Affine Cipher":
            key_a = int(self.key_a_entry.get())
            key_b = int(self.key_b_entry.get())
            if self.text_entry.get() and self.key_a_entry.get() and self.key_b_entry.get():
                result = decrypt_affine(self.text_entry.get(), key_a, key_b)
                self.result_entry.config(state="normal")
                self.result_entry.delete(0, "end")
                self.result_entry.insert(0, result)
                self.result_entry.config(state="readonly")

    def clear_fields(self):
        self.text_entry.delete(0, "end")
        self.key_entry.delete(0, "end")
        self.key_a_entry.delete(0, "end")
        self.key_b_entry.delete(0, "end")
        self.result_entry.config(state="normal")
        self.result_entry.delete(0, "end")
        self.result_entry.config(state="readonly")

def encrypt_caesar(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_caesar(ciphertext, shift):
    return encrypt_caesar(ciphertext, -shift)

def encrypt_vigenere(plaintext, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + (ord(key[key_index % len(key)]) - ord('A'))) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + (ord(key[key_index % len(key)]) - ord('A'))) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted_text += char

    return encrypted_text

def decrypt_vigenere(ciphertext, key):
    key = key.upper()
    decrypted_text = ""
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - (ord(key[key_index % len(key)]) - ord('A'))) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - (ord(key[key_index % len(key)]) - ord('A'))) % 26 + ord('A'))
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def encrypt_affine(plaintext, a, b):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((a * (ord(char) - ord('a')) + b) % 26 + ord('a'))
            else:
                encrypted_text += chr((a * (ord(char) - ord('A')) + b) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_affine(ciphertext, a, b):
    mod_inverse_a = mod_inverse(a, 26)
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((mod_inverse_a * (ord(char) - ord('a') - b)) % 26 + ord('a'))
            else:
                decrypted_text += chr((mod_inverse_a * (ord(char) - ord('A') - b)) % 26 + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherGUI(root)
    root.mainloop()
