from tkinter import * #importar la libreria tkinter
raiz =Tk()  # contruir la raiz utilizando una variable

raiz.title("Ventana de pruebas")# si queremos poner un titulo a nuestra raiz
raiz.resizable(1,1) # Para poder hacerla mas grande en lo ancho y lo alto (width,heigh)
#raiz.iconbitmat(gato.ico)# para poder cambiar el icono de pluma debes tener una imagen con terminacion .ico
raiz.geometry("650x350")#poner a un solo tamano a la ventana
raiz.config(bg="blue")#este metodo nos ayuda hacer muchas cosas como cambiar el color de fordo 
raiz.config(bd=35)# aplicarle un borde a la raiz
raiz.config(relief="groove")
raiz.config(cursor="hand2")

# COMO CREAR FRAMES 
#tkinter python3 documentacion de python 
miframe=Frame()
#miframe.pack(side="bottom") #empaquetar el frame dentro de la raiz
#miframe.pack(side="left",ancho="n")#para tener nuestro objeto con dos coordenadas
miframe.pack()#wxpandir en dos direcciones
miframe.config(bg="red")#para ver el frame podemos dar un color de fondo
miframe.config(width="30",height=30)#darle taman al frame
miframe.config(bd=5) # tamano del borde
miframe.config(relief="groove")# cambiar las caracteristicas del borde
miframe.config(cursor="pirate")#cambiar en el frame el cursor por un pirta

raiz.mainloop() # metodo main loop es necesario porque debe estar en un bucle infinito asi se crea la primera ventana en python
