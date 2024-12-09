import tkinter as tk
from tkinter import font

# Função para incrementar o número
def increment():
    global count
    if count < 99:  # Limite superior opcional
        count += 1
        update_display()

# Função para decrementar o número
def decrement():
    global count
    if count > 1:  # Evita que o número seja menor que 1
        count -= 1
        update_display()

# Atualiza o número exibido na tela
def update_display():
    display_label.config(text=f"{count:02}")

# Criação da janela principal
root = tk.Tk()
root.title("Increment & Decrement")
root.geometry("350x200")
root.configure(bg="orange")

# Estilo para botões e display
font_style = font.Font(family="Helvetica", size=24, weight="bold")

# Variável inicial
count = 1

# Container principal
frame = tk.Frame(root, bg="white", bd=10, relief="raised")
frame.pack(expand=True, padx=20, pady=20)

# Botão de decremento
minus_button = tk.Button(
    frame, text="-", font=font_style, fg="blue", bg="orange",
    width=3, height=1, command=decrement
)
minus_button.grid(row=0, column=0, padx=10, pady=10)

# Display do número
display_label = tk.Label(
    frame, text=f"{count:02}", font=font_style, fg="black", bg="white",
    width=4, height=1, relief="sunken"
)
display_label.grid(row=0, column=1, padx=10)

# Botão de incremento
plus_button = tk.Button(
    frame, text="+", font=font_style, fg="blue", bg="orange",
    width=3, height=1, command=increment
)
plus_button.grid(row=0, column=2, padx=10, pady=10)

# Inicia o loop principal da aplicação
root.mainloop()
