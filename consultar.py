#Librerías
import tkinter #Importamos el módulo
from PIL import ImageTk, Image
from pymongo import MongoClient, collation

###Conección a la base de datos###
MONGO_URI = 'mongodb://localhost' #Url local
client = MongoClient(MONGO_URI)
db = client ['registro_estudiantes'] #Nombre de la base de datos
collection = db['datos'] #Colección de la base de datos
##################################

def abrirVentanaConsultar():
    panelDeControl = tkinter.Tk() #Ventana de la aplicación
    panelDeControl.title('Consultar registros') #Título de la ventana
    panelDeControl.iconbitmap(".\\imagenes\\search.ico")
    panelDeControl.geometry("415x280") #Tamaño de la ventana
