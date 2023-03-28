from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from analizadorlexico import instruccion, operando, getErrores
import tkinter as tk
import os
from tkinter import messagebox
import graphviz
from graphviz import Digraph
from Instrucciones.Errores import Errores

class Pantalla_Principal():
    
    def __init__(self):
        self.PP = Tk()
        self.PP.title("Pantalla Principal")
        self.PP.geometry("1300x900")
        self.PP.configure(bg="#102027")
        self.pantalla_1()
        
    def pantalla_1(self):
        self.Frame = Frame()
        self.Frame.config(bg="gray")
        self.Frame.config(bd=15)
        self.Frame.config(relief="sunken")  # Le da el borde
        self.Frame.config(cursor="hand2")
        self.Frame.pack(side=tk.LEFT, fill="x")
        self.Frame.configure(height=1500, width=1600)
        self.text = ""

        Button(self.Frame, command=self.abrir_archivo, text="Cargar", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="green2", width=15).place(x=50, y=50)

        Button(self.Frame, text="Guardar", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=50, y=150)

        Button(self.Frame, command=self.guardar_como, text="Guardar Como", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=50, y=250)

        Button(self.Frame, command=self.ejecutar, text="Ejecutar", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="blue4", width=15).place(x=50, y=350)

        Button(self.Frame, text="Errores", font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="red1", width=15).place(x=50, y=450)

        Button(self.Frame, text="Cerrar Ventana", command=self.PP.destroy, font=("Arial Black Italic", 18), fg="AntiqueWhite3", bg="red2", width=15).place(x=50, y=550)

        Button(self.Frame, command = self.abrir_manual_tecnico,text="Manual Tecnico", font=("Arial Black Italic", 18), fg="AntiqueWhite2", bg="azure4", width=14).place(x=400, y=50)

        Button(self.Frame, command=self.abrir_manual_usuario, text="Manual de Usuario", font=("Arial Black Italic", 18), fg="AntiqueWhite1", bg="azure4", width=14).place(x=400, y=150)

        Button(self.Frame, text="Ayuda", font=("Arial Black Italic", 18), fg="AntiqueWhite1", bg="azure4", width=10).place(x=425, y=250)

        Button(self.Frame, command = self.mostrarAST, text="Mostrar AST", font=("Arial Black Italic", 18), fg="AntiqueWhite1", bg="azure4", width=10).place(x=425, y=350)
       
        self.text = Text(self.Frame, font=("Arial", 15), fg="black", width=45, height=8)
        self.text.place(x=700, y=100)
       
        self.resultado_text = Text(self.Frame, font=("Arial", 15), fg="black", width=30, height=6)
        self.resultado_text.place(x=775, y=300)
       
        self.Frame.mainloop()

        
    def abrir_archivo(self):
        x = ""
        Tk().withdraw()
        try:
            filename = askopenfilename(title='Selecciona un archivo', filetypes=[('Archivos', f'*.json')])
            with open(filename, encoding='utf-8') as infile:
                x = infile.read()
                                            
        except: 
            print("Error, no se ha seleccionado ningun archivo")
            return
        
        self.texto = x
        self.text.insert('1.0', x)
        
    def ejecutar(self):
        instruccion(self.texto)
        respuestas = operando()
        resultado = ""
        for respuesta in respuestas:
            resultado += str(respuesta.operar(None)) + "\n"
        self.resultado_text.insert('1.0',format(resultado))
            
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
    def abrir_manual_tecnico(self):
        try:
            os.startfile("./manual_tecnico.pdf")
        except:
            print("No se pudo abrir el archivo")




    def mostrarAST(self):
        try:
            s = self.graficarAST()
            graph = graphviz.Source(s)
            graph.view()
        except Exception as e:
            messagebox.showerror("Error", str(e))


r = Pantalla_Principal()