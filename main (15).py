#analizador sintactico "parser" que procese adecuadamente las cadenas FEN , despues
#que se pinte el tablero de ajedrez en la interfaz grafica con fichas unicode 

import tkinter as tk

fen = input("codigo fen: ")
fen = fen.split("/")

def crear_cuadro(tablero, posicion, color):
    cuadro = tk.Frame(tablero, width=62, height=62, bg=color, borderwidth=2, relief="groove")
    cuadro.grid(
        row=posicion[0], column=posicion[1], padx=1, pady=1, sticky="nsew"
    )
    return cuadro


def crear_pieza(cuadro, nombre_pieza, posicion):
    Label = tk.Label(cuadro, text=nombre_pieza, font=("Times", 44, "bold"), bg=cuadro["bg"])
    Label.grid(row=posicion[0], column=posicion[1])

def crear_tablero():
    root = tk.Tk()
    root.title("Ajedrez")
    tablero = tk.Frame(root, bg="white", width=500, height=500)
    tablero.pack()
    return root, tablero

def pintar_tablero(fen, tablero):
    cuadros = []
    for i in range(8):
        cuadros.append([])
        for j in range(8):
            if (i + j) % 2:
                color = "white"
            else:
                color = "gray"
            cuadros[i].append(crear_cuadro(tablero, (i, j), color))
    return cuadros

def pintar_piezas(fen, cuadros):
    piezas = {
        "p": "♙",
        "r": "♖",
        "n": "♘",
        "b": "♗",
        "k": "♔",
        "q": "♕",
        "P": "♟",
        "R": "♜",
        "N": "♞",
        "B": "♝",
        "K": "♚",
        "Q": "♛",
    }
    tablero = fen[0]
    posicion = 0
    for linea in tablero.split("/"):
        columna = 0 
        for caracter in linea:
            if caracter.isdigit():
                columna += int(caracter)
            
            else:
                crear_pieza(cuadros[posicion][columna], piezas[caracter], (0, 0))
                columna += 1
    posicion += 1




root, tablero = crear_tablero()
cuadros = pintar_tablero(fen, tablero)
pintar_piezas(fen, cuadros)
root.mainloop()