from tkinter import * 
import socket #Importamos la librería socket para poder comunicarnos con nuestro ESP8266



#+++++++++++++++++++CONEXION A ESP32+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#ESP_IP = '192.168.1.116'
#ESP_PORT = 8266 #Puerto que hemos configurado para que abra el ESP
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos el objeto socket para conectarnos.
#s.connect((ESP_IP , ESP_PORT)) #Nos conectamos a la IP y el puerto que hemos declarado al inicio.






#++++++++++++++++++++++++++++++FUNCIONES DE LAS LUCES DE ENCENDIDO Y APAGADO +++++++++++++++++++++++++++++++++++++++++++++

def enciendeLED():              #Función para encender el LED
    print("Encendiendo LED")
    dato = '1'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 1 al modulo ESP

def sala():
	pass

def cocina():
	pass

def habitacion1():
	pass

def habitacion2():
	pass

def bodega():
	pass


def apagaLED():                #Función para apagar el LED
    print("Apagando LED")
    dato = '0'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 0 al modulo ESP

#++++++++++++++++++++++++++++++++++++++++++++++++++FINDE LA PROGRAMACION DE LAS LUCES+++++++++++++++++++++++++++++++++++++++


#-----------------------------------------INCIO DE LAS FUCIONES DE LAS PUERTAS------------------------------------------------

def puertap():
	pass

def cuartop():
	pass

def puertaco():
	pass

def puertah1():
	pass

def puertah2():
	pass

def pertabog():
	pass

def puertac():
	pass


#+++++++++++++++++++++++++++++VENTANA PRINCIPAL DE LA APLICACION++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
ventana = Tk()
ventana.title("Smart House ")
ventana.geometry("1333x700")
#ventana.resizable(0,0)
ancho_titulo = 80
alto_titulo = 2
#++++++++++++++++++++++++++DISEÑO+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
imagenL=PhotoImage(file="fondo.png")
lnlImagen=Label(ventana,image=imagenL).place(x=0,y=0)
#ventana.config(bg="#737373")






#++++++++++++++++++++++++++++++++CONFIGURACIONES DE PRIMERA PAGUINA+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
etiqueta = Label(ventana,text="SMART HOUSE ",width=ancho_titulo,height=alto_titulo,bg="#bc8e47",justify="right",font=("verdana",20)).pack(anchor=CENTER)
#++++++++++++++++++++++++++++++CONFIUGURACIONES DE PRIMER TITULO++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



#++++++++++++++++++++++++++++++++++++++++Incio de cabezeras++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Luz     = Label (ventana,text=" LUCES  ",width=10,height=1,bg="#FF8C00",justify="right",font=("verdana",20)).place(x=80,y=100)
Puerta  = Label (ventana,text=" PUERTAS  ",width=10,height=1,bg="#FF8C00",justify="right",font=("verdana",20)).place(x=400,y=100)
Jardin  = Label (ventana,text=" JARDIN  ",width=10,height=1,bg="#FF8C00",justify="right",font=("verdana",20)).place(x=750,y=100)
Ventanas= Label (ventana,text=" VENTANAS  ",width=10,height=1,bg="#FF8C00",justify="right",font=("verdana",20)).place(x=1080,y=100)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++ INICIO DE FUNCIONES DE LUCES++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
luzPrincipal   = Label(ventana,text="Cuarto Principal",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=25,y=160)
luzSALA        = Label(ventana,text=" Sala",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=25,y=230)
luzCocina      = Label(ventana,text=" Cocina",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=25,y=300)
luzHabitacion1 = Label(ventana,text=" Habitacion 1",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=25,y=370)
luzHabitacion2 = Label(ventana,text=" Habitacion 2",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=25,y=440)
luzBodega      = Label(ventana,text=" Bodega",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=25,y=510)
#+++++++++++++++++++++++++++FINAL DE LAS LUCES++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#++++++++++++++++++++++++++++ INICIO DE LAS PUERTAS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PuertacuartoPrincipal = Label (ventana,text="Puerta Principal",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=370,y=160)
PuertaCuertoPrincipal = Label (ventana,text="Cuarto Principal",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=370,y=230)
Puertacocina          = Label (ventana,text="Puerta Cocina",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=370,y=300)
PuertaHabitacion1     = Label (ventana,text="Puerta Habitacion 1",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=370,y=370)
PuertaHabitacion2     = Label (ventana,text="Puerta Hanitacion 2",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=370,y=440)
PuertaBodega          = Label (ventana,text="Puerta Bodega",width=15,height=2,bg="#ffb02f",justify="right",font=("verdana",14)).place(x=370,y=510)
#++++++++++++++++++++++++++++++++FINAL DE LAS PUERTAS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++      



#++++++++++++++++++++++++++++++++INICIOS DE BOTONES DE LUCES++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
CPLUZ     =Button(ventana,command=enciendeLED,height=3,width=5).place(x=300, y=160)  #LLUZ CUARTO PRINCIPAL 1 ENCENDIDO
CPLUZOF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=230, y=160)     #LUZ CUARTO PRINCIPAL  1 APAGADO 
LUZSA     =Button(ventana,command=enciendeLED,height=3,width=5).place(x=230, y=230)  #LLUZ SALA 1 ENCENDIDO
CPLUZOF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=300, y=230)     #LUZ SALA   1 APAGADO 
LUZCO     =Button(ventana,command=enciendeLED,height=3,width=5).place(x=230, y=300)  #LLUZ COCINA 1 ENCENDIDO
LUZCOOF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=300, y=300)     #LUZ COCINA  1 APAGADO 
LUBA1     =Button(ventana,command=enciendeLED,height=3,width=5).place(x=300, y=370)  #LLUZ Habitacion 1 1 1 ENCENDIDO
LUBA1OF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=230, y=370)     #LUZ HABITACION 1  1 APAGADO 
LUBA2     =Button(ventana,command=enciendeLED,height=3,width=5).place(x=300, y=440)  #LLUZ HABITACION 2 1 ENCENDIDO
LUBA2OF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=230, y=440)     #LUZ HABITACION 2   1 APAGADO
LUBOG     =Button(ventana,command=enciendeLED,height=3,width=5).place(x=300, y=510)  #LLUZ  BODEGA 1 ENCENDIDO
LUBOGOF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=230, y=510)     #LUZ BODEGA  1 APAGADO }
#+++++++++++++++++++++++++++FIN DE BOTONES DE LUCES+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#+++++++++++++++++++++++++++++++INICIO DE PROGRAMACION DE PUERTAS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
PUERPON   =Button(ventana,command=enciendeLED,height=3,width=5).place(x=570, y=160) #PUERTA ABIERTA PRINCIPAL 
PUERTOF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=630, y=160)    #PUERTA PRINCIPAL CERRADA
PUERCON   =Button(ventana,command=enciendeLED,height=3,width=5).place(x=570, y=230) #PUERTA ABIERTA CUARTO 
PUERCOF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=630, y=230)    #PUERTA cuarto PRINCIPAL CERRADA
PUECION   =Button(ventana,command=enciendeLED,height=3,width=5).place(x=570, y=300) #PUERTA COCINA ABIERTA 
PUECIOF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=630, y=300)    #PUERTA COCIN CERRADA
PUEH1ON   =Button(ventana,command=enciendeLED,height=3,width=5).place(x=570, y=370) #PUERTA PERTA HABITACION 1 ABIERTA
PUEH1OF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=630, y=370)    #PUERTA HABITACION 1 CERRADA
PUEH2ON   =Button(ventana,command=enciendeLED,height=3,width=5).place(x=570, y=440) #PUERTA HABITACION 2 ABIERTA
PUEH2OF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=630, y=440)    #PUERTA HABITACION 2 CERRADA
PUEBOON   =Button(ventana,command=enciendeLED,height=3,width=5).place(x=570, y=510) #PUERTA BODEGA ABIERTA 
PUEBOOF   =Button(ventana,command=apagaLED,height=3,width=5).place(x=630, y=510)    #PUERTA BODEGA CERRADA 
#++++++++++++++++++++++++++++++++++FIN DE LOS BOTONES PARA LAS PUERTAS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++







#++++++++++++++++++++++++++++++++++++++++++Jardin LUCES+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
LucesJardin = Label (ventana,text="L C P ",width=15,height=2,bg="#FF8C00",justify="right",font=("verdana",14)).place(x=700,y=160)












ventana.mainloop()

