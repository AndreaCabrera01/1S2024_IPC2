import tkinter as tk
import tkinter.filedialog
from tkinter import messagebox
from tkinter import ttk
import xml.etree.ElementTree as ET
from ListaEnlazada import ListaEnlazada
from imagen import Imagen
from PIL import Image, ImageTk
# PROGRAMA:


class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initSize() # Dimensiones de la ventana
        self.title('Clase 8 - Test') # Titulo de la ventana
        self.panelPrincipal() # Crear panel principal
        self.archivo = None
        self.texto = None  
        self.listado = ListaEnlazada()
        self.nombresCombobox = []

    def abrirArchivo(self):
        fileTypes = (('XML files', '*.xml'), ('All files', '*.*'))
        try:
            filename = tk.filedialog.askopenfilename(title='Abrir archivo', initialdir='/', filetypes=fileTypes)
            if filename:
                self.archivo = filename

                self.file = open(filename, 'r')
                self.texto = self.file.read()
                self.file.close()

                self.editorTexto.delete('1.0', tk.END)
                self.editorTexto.insert(tk.END, self.texto)

        except Exception as e:
            print(f'Error: {e}')

    def leerArchivo(self, archivo):
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()
            
            for img in root.findall('imagen'):
                nombre = img.find('nombre').text
                self.nombresCombobox.append(nombre)
                url = img.find('url').text
                imagen = Imagen(nombre, url)
                self.listado.insertar(imagen)
            self.successMessage = messagebox.showinfo('Exito', 'Archivo leido correctamente')

            self.listado.imprimir()

        except Exception as e:
           self.mensajeError = messagebox.showerror('Error', f'Error al leer el archivo: {e}')
    
    def initSize(self):
        width = 1200
        height = 650
        screenWidth = self.winfo_screenwidth()
        screenHeight = self.winfo_screenheight()
        centerX = int(screenWidth / 2 - width / 2)
        centerY = int(screenHeight / 2 - height / 2)
        self.geometry(f'{width}x{height}+{centerX}+{centerY}')

    def panelPrincipal(self):
        self.panel = tk.Frame(self, bg='#000000')
        self.panel.pack(expand=True, fill='both')
        self.divisionesPaneles()
    
    def divisionesPaneles(self):
        self.panel1 = tk.PanedWindow(self.panel,height=650, width=300, bg='blue')
        self.panel1.place(x=0, y=0)

        self.panel2 = tk.PanedWindow(self.panel,height=650, width=900, bg='red')
        self.panel2.place(x=300, y=0)

        self.editorTexto = tkinter.Text(self.panel2, wrap='word', height=42, width=132)
        self.editorTexto.config(font=('consolas', 8), bg='white', fg='black')
        self.editorTexto.place(x=50, y=50)
        self.botonesPanel1()

    def comboImagenes(self):
        self.combo = ttk.Combobox(self.ventana, values=self.nombresCombobox, width=50)
        self.combo.place(x=50, y=50)
        self.combo.current(0)
        self.image_label = tk.Label(self.ventana)

        self.botonSeleccionar = tk.Button(self.ventana, text='Seleccionar', bg='white', fg='black', font=('Century Gothic', 12), width=15, height=2, command=self.mostrarImagen)
        self.botonSeleccionar.place(x=50, y=100)

    def mostrarImagen(self):
        nombre = self.combo.get()
        imagen = self.listado.buscar(nombre)
        try:
            self.imagen = Image.open(imagen.URL)
            width = self.imagen.width
            height = self.imagen.height

            new_width = width//5
            new_height = height//5

            # Resize the image
            self.imagen = self.imagen.resize((new_width, new_height))
            photo = ImageTk.PhotoImage(self.imagen)

            
            self.image_label.config(image=None)
            self.image_label.config(image=photo)
            self.image_label.image = photo
            self.image_label.place(x=100, y=180)

        except Exception as e:
            print(f'Error: {e}')

    def nuevaVentana(self):
        self.ventana = tk.Toplevel(self)
        self.ventana.title('Procesar archivo')
        self.ventana.geometry('1280x650')
        self.ventana.config(bg='white')
        self.comboImagenes()

    def botonesPanel1(self):
        self.btnAbrir = tk.Button(self.panel1, text='Abrir archivo', command=self.abrirArchivo, bg='white', fg='black', font=('Century Gothic', 12), width=15, height=2)
        self.btnAbrir.place(x=80, y=150)

        self.btnProcesar = tk.Button(self.panel1, text='Procesar archivo', bg='white', fg='black', font=('Century Gothic', 12), width=15, height=2, command=lambda: self.leerArchivo(self.archivo))
        self.btnProcesar.place(x=80, y=250)

        self.btnMostrar = tk.Button(self.panel1, text='Mostrar datos', bg='white', fg='black', font=('Century Gothic', 12), width=15, height=2, command=self.nuevaVentana)
        self.btnMostrar.place(x=80, y=350)

if __name__ == '__main__':
    app = Interfaz()
    app.mainloop() # Mostrar la ventana