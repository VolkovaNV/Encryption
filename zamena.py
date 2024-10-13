import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
from collections import Counter
import re


window = Tk()
window.title("Лабораторная №1 шифр")
window.geometry("500x250")
 


#зашифровать 
 
def Zah():
    s=e.get()
    alphabet =     'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    substitution = 'яюэыьъщшчцхфутсраонмлкйизжёедгвбп'
    encrypted_text = ""
    for char in s:
        if char in alphabet:
            encrypted_text += substitution[alphabet.index(char)]
        else:
            encrypted_text += char
    txt['text'] = encrypted_text
    print(encrypted_text)

def Rah():
    s=e.get()
    alphabet =     'яюэыьъщшчцхфутсраонмлкйизжёедгвбп'
    substitution = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    encrypted_text = ""
    for char in s:
        if char in alphabet:
            encrypted_text += substitution[alphabet.index(char)]
        else:
            encrypted_text += char
    txt['text'] = encrypted_text

   # from collections import Counter


def Vzlom():
    encrypted_text = e.get()
    # encrypted_text = 'ом – вмр нмолфмлоя ьяссдй э питон, фрмрояп рмрюояшяъм рьцс сяюро э ьолырт сяюроъ чсязъсцх. '
    # Частоты букв в русском языке
    frequencies = {
        'о': 0.090, 'е': 0.072, 'а': 0.062, 'и': 0.062, 'н': 0.053, 'т': 0.053, 'с': 0.045, 'р': 0.040, 'в': 0.038,
        'л': 0.035, 'к': 0.028, 'м': 0.026, 'д': 0.025, 'п': 0.023, 'у': 0.021, 'я': 0.018, 'ы': 0.016, 'з': 0.016,
        'ь': 0.014, 'б': 0.014, 'г': 0.013, 'ч': 0.012, 'й': 0.010, 'х': 0.009, 'ж': 0.007, 'ш': 0.006, 'ю': 0.006,
        'ц': 0.004, 'щ': 0.003, 'э': 0.003, 'ф': 0.002, 'ё': 0.001, 'ъ': 0.001
    }

    def count_frequencies(text):
        freq = {}
        total_chars = 0
        for char in text:
            if char.isalpha():  # Считаем только буквы
                if char in freq:
                    freq[char] += 1
                else:
                    freq[char] = 1
                total_chars += 1
        for char in freq:
            freq[char] /= total_chars
        return freq

    # Сопоставление частот
    def match_frequencies(encrypted_freq, known_freq):
        sorted_encrypted = sorted(encrypted_freq.items(), key=lambda item: item[1], reverse=True)
        sorted_known = sorted(known_freq.items(), key=lambda item: item[1], reverse=True)
        mapping = {}
        for i in range(min(len(sorted_encrypted), len(sorted_known))):
            mapping[sorted_encrypted[i][0]] = sorted_known[i][0]
        return mapping

    # Расшифровка текста
    def decrypt_text(text, mapping):
        decrypted_text = ""
        for char in text:
            if char in mapping:
                decrypted_text += mapping[char]
            else:
                decrypted_text += char
        return decrypted_text

    # Основная логика
    # encrypted_text = "Твой зашифрованный текст здесь"
    encrypted_freq = count_frequencies(encrypted_text)
    mapping = match_frequencies(encrypted_freq, frequencies)
    decrypted_text = decrypt_text(encrypted_text, mapping)

    txt['text'] = decrypted_text
    print(decrypted_text)


Label( text = "Введите  сообщение: ").pack()
e = Entry( width=90, bd=50)
e.pack()
e.focus_set()

go = Button( text = "Зашифровать", command=Zah)
go.pack()

go1 = Button( text = "Расшифровать", command=Rah)
go1.pack()

go2 = Button( text = "Взлом", command=Vzlom)
go2.pack()

txt = Label(window, text="Результат", height=10, width=60)
txt.pack()

window.mainloop()