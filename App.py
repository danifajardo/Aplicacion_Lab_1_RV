# Importo librerias
# Libreria para manejo de imagenes para interfaz de usuario
from PIL import Image, ImageTk
# Libreria
# Libreria para Interfaz de usuario
import tkinter as tk
# importamos el modulo ttk para dar estilos a los componentes
from tkinter import Label, ttk
# importamos modulo para ventana de guardado
from tkinter import filedialog, messagebox
# Importar libreria opencv
import cv2 as cv
# importamos el modulo numpy
import numpy as np

# Clase principal (contenedor)

#Mi nombre es Joseph 
class App(tk.Tk):
    # método de iniciación
    def __init__(self, *args, **kwargs):
        # Iniciamos un frame
        tk.Tk.__init__(self, *args, **kwargs)
        # Seleccionamos geometria
        tk.Tk.geometry(self, "1500x720")
        # Ponemos un titulo
        tk.Tk.title(self, 'Laboratorio Realidad Virtual')

        # hacemos un contendor
        Contenedor = tk.Frame(self, bg='#99A3A4')
        # Cada fila de contenedor tendra un ancho de 1
        Contenedor.grid_rowconfigure(0, weight=1)
        # Cada columna de contenedor tendra un ancho de 1
        Contenedor.grid_columnconfigure(0, weight=1)
        # Posicionamos contenedor
        Contenedor.pack(side="top", expand=True, fill=tk.BOTH)

        # Creamos un menú barra

        # creamos el objeto Menu
        menu_app = tk.Menu(self)
        # le decimos a tkinter que este será nuestro menú
        self.config(menu=menu_app)
        # Creamos un nuevo menú tomando como contenedor el menú anterior
        item_archivo = tk.Menu(menu_app)
        # Añadimos item_archivo al menú principal
        menu_app.add_cascade(label="Archivo", menu=item_archivo)
        # Añadimos un item de al sub menú de archivo
        item_archivo.add_command(
            label="Cargar imagenes", command=self.fun_selec_img)

    # función que se activa con el botón "Escoger Imagen"
    def fun_selec_img(self):
        ruta_imagen = filedialog.askopenfile(title="Abrir imagen para prueba")
        print(ruta_imagen.name)

if __name__ == '__main__':
    main = App()
    main.mainloop()
