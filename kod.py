import random
import math
import numpy as np
import tkinter as tk
from tkinter import messagebox
import string

def Filter(Ot, jazyk):
    Tabulka = str.maketrans({
        'á': 'a', 'č': 'c', 'ď': 'd', 'é': 'e', 'ě': 'e', 'í': 'i', 
        'ň': 'n', 'ó': 'o', 'ř': 'r', 'š': 's', 'ť': 't', 'ú': 'u', 
        'ů': 'u', 'ý': 'y', 'ž': 'z','Á': 'A', 'Č': 'C', 'Ď': 'D', 'É': 'E', 'Ě': 'E', 'Í': 'I',
        'Ň': 'N', 'Ó': 'O', 'Ř': 'R', 'Š': 'S', 'Ť': 'T', 'Ú': 'U',
        'Ů': 'U', 'Ý': 'Y', 'Ž': 'Z'
    })

    number_words = {
        '1': ['X', 'O', 'N', 'E', 'X'],
        '2': ['X', 'T', 'W', 'O', 'X'],
        '3': ['X', 'T', 'H', 'R', 'E', 'E', 'X'],
        '4': ['X', 'F', 'O', 'U', 'R', 'X'],
        '5': ['X', 'F', 'I', 'V', 'E', 'X'],
        '6': ['X', 'S', 'I', 'X', 'X'],
        '7': ['X', 'S', 'E', 'V', 'E', 'N', 'X'],
        '8': ['X', 'E', 'I', 'G', 'H', 'T', 'X'],
        '9': ['X', 'N', 'I', 'N', 'E', 'X'],
        '0': ['X', 'Z', 'E', 'R', 'O', 'X']
    }

    text = Ot.translate(Tabulka)
    text = text.upper()

    n = len(text)
    c = []
    for i in range(n):
        if jazyk == True and text[i] == 'W':
            c.append('V')
        elif jazyk == False and text[i] == 'J':
            c.append('I')
        elif text[i].isdigit():
            c.extend(list(number_words[text[i]]))
        elif text[i] == ' ':
            c.extend(['X', 'M', 'E', 'Z', 'E', 'R', 'A', 'X'])
        elif text[i].isalpha():
                c.append(text[i]) 
    return ''.join(c)

def Filterdecode(Ot):
    Tabulka = str.maketrans({
        'á': 'a', 'č': 'c', 'ď': 'd', 'é': 'e', 'ě': 'e', 'í': 'i', 
        'ň': 'n', 'ó': 'o', 'ř': 'r', 'š': 's', 'ť': 't', 'ú': 'u', 
        'ů': 'u', 'ý': 'y', 'ž': 'z','Á': 'A', 'Č': 'C', 'Ď': 'D', 'É': 'E', 'Ě': 'E', 'Í': 'I',
        'Ň': 'N', 'Ó': 'O', 'Ř': 'R', 'Š': 'S', 'Ť': 'T', 'Ú': 'U',
        'Ů': 'U', 'Ý': 'Y', 'Ž': 'Z'
    })

    number_words = {
        '1': ['X', 'O', 'N', 'E', 'X'],
        '2': ['X', 'T', 'W', 'O', 'X'],
        '3': ['X', 'T', 'H', 'R', 'E', 'E', 'X'],
        '4': ['X', 'F', 'O', 'U', 'R', 'X'],
        '5': ['X', 'F', 'I', 'V', 'E', 'X'],
        '6': ['X', 'S', 'I', 'X', 'X'],
        '7': ['X', 'S', 'E', 'V', 'E', 'N', 'X'],
        '8': ['X', 'E', 'I', 'G', 'H', 'T', 'X'],
        '9': ['X', 'N', 'I', 'N', 'E', 'X'],
        '0': ['X', 'Z', 'E', 'R', 'O', 'X']
    }

    text = Ot.translate(Tabulka)
    text = text.upper()

    n = len(text)
    c = []
    for i in range(n):
        if text[i].isalpha():  # Opraveno přidáním 'if'
            c.append(text[i])
    return ''.join(c)

def Destruct(Text):
    result = []
    n = len(Text)
    for i in range(n):
        result.append(Text[i])
    return result


def Matrix5x5(jazyk):
    if jazyk == True:
        abeceda = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    else:
        abeceda = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    random.shuffle(abeceda)
    Matrix = []
    index = 0
    
    for i in range(5):
        row = []
        for j in range(5):
            row.append(abeceda[index])
            index += 1
        Matrix.append(row)
    print(Matrix)
    return Matrix


def Matrix6x6(jazyk):
    if jazyk == True:
        abeceda = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    else:
        abeceda = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


    random.shuffle(abeceda)
    Matrix = []
    index = 0
    
    for i in range(6):
        row = []
        for j in range(6):
            row.append(abeceda[index])
            index += 1
        Matrix.append(row)
    print(Matrix)
    return Matrix

def MatrixDecider(roz, jazyk):
    if roz == True:
        result = Matrix6x6(jazyk)
    else: 
        result = Matrix5x5(jazyk)

    return result


def MatrixFind(Matrix, Text):
    Result = []
    for i in range(len(Text)):
        for a in range(len(Matrix)):
            for b in range(len(Matrix)):
                if Text[i] == Matrix[a][b]:
                    Result.append([a, b])
    return Result

def PrvniCoder(Souradnice, co):
    result = []
    if co == False:
        Slovnik = {0: 'A', 1: 'D', 2: 'F', 3: 'G', 4: 'X'}
    else:
        Slovnik = {0: 'A', 1: 'D', 2: 'F', 3: 'G', 4: 'V', 5: 'X'}
    for pair in Souradnice:
        transformed_pair = [Slovnik[p] for p in pair]
        result.append(transformed_pair)
    
    return result

def PrvniDecoder(Souradnice, co):
    result = []
    if co == False:
        Slovnik = {'A': 0, 'D': 1, 'F': 2, 'G': 3, 'X': 4}
    else:
        Slovnik = {'A': 0, 'D': 1, 'F': 2, 'G': 3, 'V': 4, 'X': 5}

    for pair in Souradnice:
        transformed_pair = [Slovnik[p] for p in pair]
        result.append(transformed_pair)
    
    return result



def Koded(Slovo, souradnice):
    # Flatten the list of coordinates (souradnice) into a single list
    listek = sum(souradnice, [])  # This flattens the nested list

    Matrix = []  # Initialize the matrix

    x = len(Slovo)  # Length of the word (number of columns)
    y = len(listek)  # Number of total coordinates

    # Calculate how many complete rows can be formed
    cele = y // x
    zbytek = y % x

    for i in range(cele):
        row = []  
        for j in range(x):
            row.append(listek[i * x + j])
        Matrix.append(row)  # Add the full row to the matrix

    # Add the remaining cells in a new row, if any
    if zbytek > 0:
        last_row = []
        for j in range(x):
            if j < zbytek:
                last_row.append(listek[cele * x + j])
            else:
                last_row.append("_")  # Fill with "_" if no coordinate is available
        Matrix.append(last_row)  # Add the last row to the matrix

    # Fill remaining rows with underscores if the total number of cells is less than expected
    total_rows = (len(Slovo) + len(Matrix[0]) - 1) // len(Slovo)
    while len(Matrix) < total_rows:
        Matrix.append(["_"] * x)


    return Matrix


def poradimaker(kod):
    # Rozložení vstupního řetězce na písmena
    pismena = list(kod)
    
    # Slovník pro mapování písmen na jejich pořadí v abecedě
    abc = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
        'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
        'Y': 25, 'Z': 26
    }
    
    # Převedení písmen na jejich hodnoty v abecedě
    hodnoty = []
    for pismeno in pismena:
        if pismeno.upper() in abc:
            hodnoty.append(abc[pismeno.upper()])
    
    # Vytvoření seznamu indexů seřazených podle hodnot
    poradi = list(range(len(hodnoty)))
    poradi.sort(key=lambda i: hodnoty[i])
    
    # Vytvoření výsledného pořadí

    vysledek = [0] * len(hodnoty)
    for i, pozice in enumerate(poradi):
        vysledek[pozice] = i + 1
        
    return vysledek


def Rozrazeni(poradi, matice):
    # Vytvoříme seznam sloupců z matice
    sloupce = [[radek[i] for radek in matice] for i in range(len(matice[0]))]
    
    # Výsledek podle pořadí
    result = [''] * len(poradi)
    for pozice, index in enumerate(poradi):
        result[index - 1] = ''.join(sloupce[pozice])
    
    return ''.join(result)
def RozdeleniTextu(text, kod):
    # Délka buňky
    cell_size = len(text) // len(kod)
    
    # Pokud délka textu není násobkem kódu, zvyšte cell_size o 1
    if len(text) % len(kod) != 0:
        cell_size += 1

    # Rozdělený text do buněk
    SortedText = []

    # Iterace přes text po cell_size krocích
    for i in range(0, len(text), cell_size):
        chunk = text[i:i + cell_size]
        
        # Doplnění podtržítky, pokud je poslední buňka kratší
        if len(chunk) < cell_size:
            chunk += '_' * (cell_size - len(chunk))
        
        SortedText.append(chunk)
    
    return SortedText

def sniz_prvky(seznam):
    return [prvek - 1 for prvek in seznam]

def DeMatrixa(text, poradi):
        i = 0
        b = 0
        poradi = sniz_prvky(poradi)
        matice = [["_"] * len(text) for _ in range(len(text[0]))]
        while i < len(poradi):
            if b == poradi[i]:
                    for c in range(len(text[0])):
                            matice[c][i] = text[b][c]
                    i = 0
                    b += 1
            else: i += 1            
        return matice
def SouradniceDecrypt(matice):
    a = [prvek for radek in matice for prvek in radek]
    a = [prvek for prvek in a if prvek != '_']
    return [a[i:i+2] for i in range(0, len(a), 2)]

def  Decode(coordinates, matrix):
    vysledky = []
    for (radek, sloupec) in coordinates:
        if 0 <= radek < len(matrix) and 0 <= sloupec < len(matrix[0]):
            vysledky.append(matrix[radek][sloupec])
        else:
            vysledky.append(None)  # pokud jsou souřadnice mimo matici, přidej None
    

    return ''.join(vysledky)


import tkinter as tk
import random
import string

# Funkce pro kontrolu chybějících písmen ve vlastní matici
def kontrola_matici(input_text, alphabet=None):
    if alphabet is None:
        alphabet = string.ascii_uppercase
    
    input_text = input_text.replace(" ", "").upper()
    input_set = set(input_text)
    alphabet_set = set(alphabet)
    missing_letters = sorted(alphabet_set - input_set)
    
    return missing_letters

def Zakodovani(OpenText, kodoveslovo, jazyke, advg, user_matrix=None):
    kodoveslovo = Filter(kodoveslovo, None)
    FiltedText = Filter(OpenText, jazyke)
    FiltedText = Destruct(FiltedText)
    
    Maxtrix = user_matrix if user_matrix else MatrixDecider(advg, jazyke)
    Souradnice = MatrixFind(Maxtrix, FiltedText)
    MatrixCoded = PrvniCoder(Souradnice, advg)
    poradi = poradimaker(kodoveslovo)
    Pokracovani = Koded(kodoveslovo, MatrixCoded)
    Pokracovani = Rozrazeni(poradi, Pokracovani)
    
    return Pokracovani, Maxtrix 

def odstran_mezery(veta):
    return veta.replace("   ", "")

def Odkodovani(OpenText, kodoveslovo, jazyke, advg, user_matrix):
    kodoveslovo = Filterdecode(kodoveslovo)
    FiltedText = OpenText.strip()
    FiltedText = Destruct(FiltedText)
    
    Maxtrix = user_matrix
    poradi = poradimaker(kodoveslovo)
    FilterArray = RozdeleniTextu(FiltedText, kodoveslovo)
    DeMatrix = DeMatrixa(FilterArray, poradi)
    Kodsouradnic = SouradniceDecrypt(DeMatrix)
    Kodsouradnic = PrvniDecoder(Kodsouradnic, advg)
    Result = Decode(Kodsouradnic, Maxtrix)
    
    replacements = {
        "XMEZERAX": " ",
        "XZEROX": "0",
        "XONEX": "1",
        "XTWOX": "2",
        "XTHREEX": "3",
        "XFOURX": "4",
        "XFIVEX": "5",
        "XSIXX": "6",
        "XSEVENX": "7",
        "XEIGHTX": "8",
        "XNINEX": "9"
    }
    for key, value in replacements.items():
        Result = Result.replace(key, value)

    return Result, Maxtrix

def missing_letters(matrix):
    all_letters = set(string.ascii_uppercase)
    matrix_letters = set("".join("".join(row) for row in matrix))
    missing = all_letters - matrix_letters
    return sorted(missing)





# GUI aplikace
root = tk.Tk()
root.title("Kódování a Dekódování")
root.geometry("800x800")

# Vstupní pole a tlačítka
open_text_label = tk.Label(root, text="Text:")
open_text_label.pack()
open_text_entry = tk.Entry(root, width=50)
open_text_entry.pack()

code_word_label = tk.Label(root, text="Kódovací slovo:")
code_word_label.pack()
code_word_entry = tk.Entry(root)
code_word_entry.pack()

# Přidání pole pro zadání vlastní matice
user_matrix_label = tk.Label(root, text="Zadejte vlastní matici (např. pro kódování/dekódování):")
user_matrix_label.pack()
user_matrix_entry = tk.Text(root, height=10, width=25)
user_matrix_entry.pack()

# Jazyk a velikost matice
jazyk_var = tk.BooleanVar()
advg_var = tk.BooleanVar()

jazyk_check = tk.Checkbutton(root, text="Český jazyk", variable=jazyk_var)
jazyk_check.pack()
advg_check = tk.Checkbutton(root, text="6x6 matice", variable=advg_var)
advg_check.pack()

# Výstupní pole pro zakódovaný/odkódovaný text
output_label = tk.Label(root, text="Zakódovaný/Odkódovaný text:")
output_label.pack()
output_text = tk.Text(root, height=2, width=40)
output_text.pack()

# Výstupní pole pro matici
matrix_label = tk.Label(root, text="Matice:")
matrix_label.pack()
matrix_text = tk.Text(root, height=10, width=25)
matrix_text.pack()

# Výstupní pole pro chybějící písmena
missing_label = tk.Label(root, text="Chybějící písmena:")
missing_label.pack()
missing_text = tk.Text(root, height=1, width=50)
missing_text.pack()

# Funkce pro tlačítka
def on_encode():
    open_text = open_text_entry.get()
    code_word = code_word_entry.get()
    jazyk = jazyk_var.get()
    advg = advg_var.get()
    
    # Načtení uživatelské matice z textového pole
    user_matrix_text = user_matrix_entry.get("1.0", tk.END).strip().splitlines()
    user_matrix = [line.split() for line in user_matrix_text] if user_matrix_text else None
    
    zakodovany_text, matice = Zakodovani(open_text, code_word, jazyk, advg, user_matrix)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, zakodovany_text)
    
    matrix_text.delete("1.0", tk.END)
    matrix_text.insert(tk.END, "\n".join([" ".join(row) for row in matice]))

def on_decode():
    open_text = open_text_entry.get()
    code_word = code_word_entry.get()
    jazyk = jazyk_var.get()
    advg = advg_var.get()
    
    user_matrix_text = user_matrix_entry.get("1.0", tk.END).strip().splitlines()
    user_matrix = [line.split() for line in user_matrix_text]
    
    odkodovany_text, _ = Odkodovani(open_text, code_word, jazyk, advg, user_matrix)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, odkodovany_text)
    
    matrix_text.delete("1.0", tk.END)
    matrix_text.insert(tk.END, "\n".join([" ".join(row) for row in user_matrix]))

def on_check_missing_letters():
    user_matrix_text = user_matrix_entry.get("1.0", tk.END).replace("\n", "")
    missing_letters = kontrola_matici(user_matrix_text)
    missing_text.delete("1.0", tk.END)
    missing_text.insert(tk.END, ", ".join(missing_letters))

# Tlačítka
encode_button = tk.Button(root, text="Zakódovat", command=on_encode)
encode_button.pack()

decode_button = tk.Button(root, text="Odkódovat", command=on_decode)
decode_button.pack()

check_missing_button = tk.Button(root, text="Zkontrolovat chybějící písmena", command=on_check_missing_letters)
check_missing_button.pack()

root.mainloop()
