import tkinter as tk
from tkinter import messagebox
import random

# Crear la ventana principal
root = tk.Tk()
root.title("Adivina el Número")
root.geometry("300x200")

# Número aleatorio a adivinar
numero_secreto = random.randint(1, 100)
intentos = 0

# Etiqueta de instrucciones
label_instr = tk.Label(root, text="Adivina un número entre 1 y 100:")
label_instr.pack()

# Entrada para el número
entry_numero = tk.Entry(root)
entry_numero.pack()

# Etiqueta para mostrar las pistas
label_pista = tk.Label(root, text="")
label_pista.pack()

# Función para comprobar el número
def comprobar():
    global intentos
    try:
        num = int(entry_numero.get())
        intentos += 1
        
        if num < numero_secreto:
            label_pista.config(text="El número es mayor")
        elif num > numero_secreto:
            label_pista.config(text="El número es menor")
        else:
            messagebox.showinfo("¡Felicidades!", f"Adivinaste el número en {intentos} intentos.")
            reiniciar()
        
        # Limpiar la entrada después de cada intento
        entry_numero.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Error", "Por favor, ingresa un número válido.")
        entry_numero.delete(0, tk.END)

# Botón para adivinar
btn_adivinar = tk.Button(root, text="Adivinar", command=comprobar)
btn_adivinar.pack()

# Función para reiniciar el juego
def reiniciar():
    global numero_secreto, intentos
    numero_secreto = random.randint(1, 100)
    intentos = 0
    label_pista.config(text="")
    entry_numero.delete(0, tk.END)

# Botón para reiniciar el juego
btn_reiniciar = tk.Button(root, text="Reiniciar", command=reiniciar)
btn_reiniciar.pack()

# Ejecutar la aplicación
root.mainloop()
