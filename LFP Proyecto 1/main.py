from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from analizadorlexico import instruccion, operar2
import tkinter as tk
import os



class Pantalla_Principal():
    
    def __init__(self):
        self.PP = Tk()
        self.PP.title("Pantalla Principal")
        self.PP.geometry("1000x700")
        self.PP.configure(bg="#102027")
        self.pantalla_1()
        
    def pantalla_1(self):
        self.Frame = Frame()
        self.Frame.config(bg="gray")
        self.Frame.config(bd=15)
        self.Frame.config(relief="sunken")  # Le da el borde
        self.Frame.config(cursor="hand2")
        self.Frame.pack(side=tk.LEFT, fill="x")
        self.Frame.configure(height=800, width=600)
        self.text = ""

        Button(self.Frame, command=self.abrir_archivo, text="Abrir Archivo", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=50)

        Button(self.Frame, text="Guardar", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=150)

        Button(self.Frame, command=self.guardar_como, text="Guardar Como", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=250)

        Button(self.Frame, command=self.ejecutar, text="Ejecutar", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=350)

        Button(self.Frame, text="Errores", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=450)

        Button(self.Frame, text="Cerrar Ventana", command=self.PP.destroy, font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=200, y=550)

        self.Frame = Frame()
        self.Frame.config(bg="tan")
        self.Frame.config(bd=15)
        self.Frame.config(relief="sunken")  # Le da el borde
        self.Frame.config(cursor="hand2")
        self.Frame.pack(side=tk.RIGHT, fill="x")
        self.Frame.configure(height=800, width=600)
        self.text = ""

        Button(self.Frame, text="Manual Tecnico", font=("Arial Black Italic", 18), fg="AntiqueWhite2", bg="azure4", width=10).place(x=200, y=50)

        Button(self.Frame, command=self.abrir_manual_usuario, text="Manual de Usuario", font=("Arial Black Italic", 18), fg="AntiqueWhite1", bg="azure4", width=10).place(x=200, y=150)

        Button(self.Frame, text="Ayuda", font=("Arial Black Italic", 18), fg="AntiqueWhite1", bg="azure4", width=10).place(x=200, y=250)

        self.Frame.mainloop()

        #Text(self.Frame,font=("Arial", 15), fg="black", width=60, height=5).place(x=100,y=250)
        self.Frame = Frame()
        self.Frame.config(bg = "tan")
        self.Frame.config(bd=15)
        self.Frame.config(relief="sunken")  #Le da el borde
        self.Frame.config(cursor="hand2")
        self.Frame.pack(side=tk.RIGHT, fill="x")
        self.Frame.configure(height=800, width=600)
        self.text = ''
        
        Button(self.Frame,text="Manual Tecnico", font=("Arial Black", 18), fg="AntiqueWhite2", bg="azure4", width=10).place(x=200, y=50)
        
        Button(self.Frame ,text="Manual de Usuario", command=self.abrir_manual_usuario, font=("Arial Black", 18),fg="AntiqueWhite1", bg="azure4", width=10).place(x=200, y=150)
        
        Button(self.Frame,text="Ayuda", font=("Arial Black", 18), fg="AntiqueWhite1", bg="azure4", width=10).place(x=200, y=250)
        self.Frame.mainloop()
        

        
    def abrir_archivo(self):
        x = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Seleciona un archivo', filetypes=[('Archivos', f'*.json')])
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
                                            
        except: 
            print("Error, no se ha seleccionado ningun archivo")
            return
        
        self.texto = x
        print(self.texto)
        
        
    def ejecutar(self):
        instruccion(self.texto)
        respuestas = operar2()                         
        for respuesta in respuestas:
            print(respuesta.operar(None))
            
    def abrir_manual_usuario(self):
        try:
            os.startfile("./manual_de_Usuario.pdf")
        except:
            print("No se pudo abrir el archivo")
            
    def guardar_como(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if filename:
            with open(filename, "w", encoding="utf-8") as outfile:
                outfile.write(self.texto)

                
r = Pantalla_Principal()