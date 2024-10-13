import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
# from collections import Counter
# import re


window = Tk()
window.title("Лабораторная №2 шифр")
window.geometry("500x550")
 


 #зашифровать 
 
# def Zah():
    
#     s=e.get()
   # Таблица шифрования 6x6
# polybius_square = {
#     'A': 'abcdefghiklmnopqrstuvwxyz',
#     'D': '0123456789',
#     'F': 'ADFGVX'
# }

get_polybius_square = [
        ['a', 'b', 'c', 'd', 'e', 'f'],
        ['g', 'h', 'i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p', 'q', 'r'],
        ['s', 't', 'u', 'v', 'w', 'x'],
        ['y', 'z', '0', '1', '2', '3'],
        ['4', '5', '6', '7', '8', '9']
    ]

# def generate_polybius_square():
#     alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
#     alphabet = list(alphabet)
#     random.shuffle(alphabet)
#     polybius_square = [[None]*6 for _ in range(6)]
#     index = 0
#     for i in range(6):
#         for j in range(6):
#             polybius_square[i][j] = alphabet[index]
#             index += 1
#     return polybius_square

def Zah():
    plaintext=e.get() 
    key=n.get()
    chars = "ADFGVX"
    encrypted_text = ''
    for char in plaintext.lower():
        if char.isalnum():
            for i, row in enumerate(get_polybius_square):
                if char in row:
                    j = row.index(char)
                    encrypted_text += chars[i] + chars[j]
                    break

    col_len = (len(encrypted_text) + len(key) - 1) // len(key)
    columns = [''] * len(key)
    
    for i, char in enumerate(encrypted_text):
        columns[i % len(key)] += char
    
    sorted_key = sorted([(char, i) for i, char in enumerate(key)])
    final_encrypted_text = ''
    
    for _, index in sorted_key:
        final_encrypted_text += columns[index]
        
        #encrypted = adfgvx_encrypt(plaintext, key, polybius_square)
            
    txt['text'] =final_encrypted_text



def Rah():
    ciphertext=e.get()
    key=n.get()
    col_len = len(ciphertext) // len(key)
    extra = len(ciphertext) % len(key)
    
    columns = [''] * len(key)
    index = 0
    for i, char in enumerate(sorted(key)):
        col_size = col_len + (1 if i < extra else 0)
        columns[key.index(char)] = ciphertext[index:index + col_size]
        index += col_size
    
    decrypted_text = ''
    for i in range(col_len + 1):
        for col in columns:
            if i < len(col):
                decrypted_text += col[i]
    
    chars = "ADFGVX"
    plaintext = ''
    # for i in range(0, len(decrypted_text), 2):
    #     row = chars.index(decrypted_text[i])
    #     col = chars.index(decrypted_text[i + 1])
    #     plaintext += get_polybius_square[row][col]
    for i in range(0, len(decrypted_text) - 1, 2):
        row = chars.index(decrypted_text[i])
        col = chars.index(decrypted_text[i + 1])
        plaintext += get_polybius_square[row][col]
    
    txt['text']=plaintext


Label( text = "Введите  сообщение: ").pack()
e = Entry( width=90, bd=50)
e.pack()
e.focus_set()
Label( text = "Введите  ключ: ").pack()
n = Entry( width=90, bd=50)
n.pack()
n.focus_set()
go = Button( text = "Зашифровать",command=Zah )
go.pack()
go1 = Button( text = "Расшифровать",command=Rah)
go1.pack()


# B1.bind("<Button>", Zah)
#Button(window, text='Выйти', command=window.destroy).pack()
txt = Label(window, text="Результат", height=10, width=60)
txt.pack()

# go.bind("<Button>", command = FixedSubstitutionCipher)
#AFFDXFGDVFXDDFAXVX secret hello world

window.mainloop()