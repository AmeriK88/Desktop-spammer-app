import pyautogui as pg
import time
import tkinter as tk
from tkinter import messagebox

# Función para obtener la posición del clic del usuario
def obtener_posicion():
    messagebox.showinfo("Instrucciones", "Haz clic en la parte de la pantalla donde quieras que se escriba el mensaje.")
    time.sleep(3)  # Espera 3 segundos antes de obtener la posición
    global input_position
    input_position = pg.position()
    posicion_label.config(text=f"Posición seleccionada: {input_position}")

# Función para ejecutar el script
def ejecutar_script():
    try:
        mensaje = mensaje_entry.get()
        repeticiones = int(repeticiones_entry.get())
        tiempo_espera = float(tiempo_entry.get())
        
        # Verifica que la posición ha sido seleccionada
        if not input_position:
            messagebox.showerror("Error", "Debes seleccionar una posición en la pantalla.")
            return
        
        # Espera antes de comenzar el script
        time.sleep(tiempo_espera)
        
        # Repite el envío del mensaje
        for _ in range(repeticiones):
            # Mueve el cursor al input y hace clic
            pg.click(input_position)
            
            # Escribe el mensaje
            pg.typewrite(mensaje, interval=0.05)  # Aumenta ligeramente el intervalo
            
            # Envía el mensaje 
            pg.press('enter')
            
            # Tiempo de espera entre mensajes
            time.sleep(0.1)
            
        messagebox.showinfo("Finalizado", "El script ha terminado de ejecutar.")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Interfaz gráfica
root = tk.Tk()
root.title("Automatización de Mensajes")

# Etiquetas y entradas de texto
mensaje_label = tk.Label(root, text="Mensaje:")
mensaje_label.pack()
mensaje_entry = tk.Entry(root, width=50)
mensaje_entry.pack()

repeticiones_label = tk.Label(root, text="Número de repeticiones:")
repeticiones_label.pack()
repeticiones_entry = tk.Entry(root)
repeticiones_entry.pack()

tiempo_label = tk.Label(root, text="Tiempo de espera antes de comenzar (segundos):")
tiempo_label.pack()
tiempo_entry = tk.Entry(root)
tiempo_entry.pack()

# Botón para seleccionar la posición
posicion_btn = tk.Button(root, text="Seleccionar posición", command=obtener_posicion)
posicion_btn.pack()

posicion_label = tk.Label(root, text="Posición seleccionada: Ninguna")
posicion_label.pack()

# Botón para ejecutar el script
ejecutar_btn = tk.Button(root, text="Ejecutar", command=ejecutar_script)
ejecutar_btn.pack()


root.mainloop()
