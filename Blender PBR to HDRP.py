#!/usr/bin/env python
import cv2
import glob
import numpy as np

#interfaz GTK con Python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys

archivo = ""
ruta = ""
mylist = ""
material = ""
tipo = ""
encontrado = False
numero = 0
roughness = False
metallic = False
ao = False

#Definicion que convierte la imagen
def conversion():
    global archivo
    global ruta
    global mylist
    global material
    global tipo
    global encontrado
    global numero
    global roughness
    global metallic
    global ao

    #crea una textura blanca usando cualquier textura existente
    if roughness:
        black = cv2.imread(ruta+"/"+material+"_Roughness.exr",  -cv2.IMREAD_ANYDEPTH)
        white = cv2.imread(ruta+"/"+material+"_Roughness.exr",  -cv2.IMREAD_ANYDEPTH)        
    elif metallic:
        black = cv2.imread(ruta+"/"+material+"_Metallic.exr",  -cv2.IMREAD_ANYDEPTH)
        white = cv2.imread(ruta+"/"+material+"_Metallic.exr",  -cv2.IMREAD_ANYDEPTH)
    else:
        black = cv2.imread(ruta+"/"+material+"_AO.exr",  -cv2.IMREAD_ANYDEPTH)
        white = cv2.imread(ruta+"/"+material+"_AO.exr",  -cv2.IMREAD_ANYDEPTH)
    
    #Convierte a 8bits
    black_bit8 = (black) * 255
    white_bit8 = (white) * 255
    #lo pasa a escala de grises
    black_gray = cv2.cvtColor(black_bit8, cv2.COLOR_BGR2GRAY)
    white_gray = cv2.cvtColor(white_bit8, cv2.COLOR_BGR2GRAY)
    #puede rellenar la imagen de uin solo color
    black_gray[:] = (0) #puede tener 3 valores (0,0,0)
    white_gray[:] = (255)

    #Lee el mapa de rugosidad, metalico y AmbientOclusion (si hay)
    #las convierte a 8bit. los exr van del 0 a 1
    #la convierte a escala de grises
    if roughness:
        img_roughness = cv2.imread(ruta+"/"+material+"_Roughness.exr",  -cv2.IMREAD_ANYDEPTH)
        roughness_bit8 = (img_roughness) * 255
        #hay que invertir el mapa de roughness porque unity tiene un mapa de "suavidad", no de rugosidad
        roughness_invert = 255 - roughness_bit8
        roughness_gray = cv2.cvtColor(roughness_invert, cv2.COLOR_BGR2GRAY)
    else:
        roughness_invert = white_gray
    if metallic:
        img_metallic = cv2.imread(ruta+"/"+material+"_Metallic.exr",  -cv2.IMREAD_ANYDEPTH)
        metallic_bit8 = (img_metallic) * 255
        metallic_gray = cv2.cvtColor(metallic_bit8, cv2.COLOR_BGR2GRAY)
    else:
        metallic_gray = black_gray
    if ao:
        img_ao = cv2.imread(ruta+"/"+material+"_AO.exr",  -cv2.IMREAD_ANYDEPTH)
        ao_bit8 = (img_ao) * 255
        ao_gray = cv2.cvtColor(ao_bit8, cv2.COLOR_BGR2GRAY)
    else:
        ao_gray = white_gray

    #une las imagenes + un canal alpha (BGR A)
    img_BGRA = cv2.merge((black_gray, ao_gray, metallic_gray, roughness_gray))

    #guarda la imagen
    cv2.imwrite(ruta+"/"+material+"_MaskMap.png", img_BGRA)
    print(str(material)+"_MaskMap.png creado con exito!")

def revision(text):
    global archivo
    global ruta
    global mylist
    global material
    global tipo
    global encontrado
    global numero
    global roughness
    global metallic
    global ao
    
    archivo = ""
    ruta = ""
    mylist = ""
    material = ""
    tipo = ""
    encontrado = False
    archivo = os.path.basename(text)
    ruta = os.path.dirname(text)[7:]
    mylist = os.listdir(ruta)
    numero = 0
    roughness = False
    metallic = False
    ao = False

    try:
    	material = archivo.rsplit('_',1)[0]
    except:
    	print("material no valido")
    try:
    	tipo = archivo.rsplit('_',1)[1]
    except:
    	print("tipo no valido")
	
    #print ("Ubicacion: " + ruta)
    #print ("Nombre de Fichero: " + archivo)
    #print ("Material: " + str(material))
    #print ("Tipo: " + str(tipo))
    #print (str(len(mylist)) +" Archivos en la carpeta") # + str(mylist))

    for x in mylist:
        try:
            tipo = x.rsplit('_',1)[1]
        except:
            print("ignorar este error")
        if x.rsplit('_',1)[0] == material and tipo == "Metallic.exr" or x.rsplit('_',1)[0] == material and tipo == "Roughness.exr" or x.rsplit('_',1)[0] == material and tipo == "AO.exr":
            encontrado = True
            if tipo == "Roughness.exr":
                roughness = True
            elif tipo == "Metallic.exr":
                metallic = True
            elif tipo == "AO.exr":
                ao = True
            numero +=1

    return encontrado
		

class LabelWindow(Gtk.Window):	
    def __init__(self):
        Gtk.Window.__init__(self, title="Blender PBR a Unity HDRP")
        self.set_default_size(800,200)

        #se crea una "caja"
        verticalbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        verticalbox.set_homogeneous(False)

        #Conecta la caja con la funcion de arrastre
        enforce_target = Gtk.TargetEntry.new('text/plain', Gtk.TargetFlags(4), 129)
        verticalbox.drag_dest_set(Gtk.DestDefaults.ALL, [enforce_target], Gdk.DragAction.COPY)
        verticalbox.connect("drag-data-received", self.on_drag_data_received)

        #Crea una etiqueta
        self.label = Gtk.Label()
        self.label.set_markup("Arrastre una imagen <b>EXR</b> creada con el <b>BAKE PBR</b> en la ventana \n")
        self.label.set_justify(Gtk.Justification.LEFT)
        self.label.set_line_wrap(True)
        verticalbox.pack_start(self.label, True, True, 0)

        #Crea un boton
        self.button = Gtk.Button("Esperando imagen...")
        self.button.connect("clicked", self.button_pressed)
        verticalbox.pack_start(self.button, True, True, 0)

        self.add(verticalbox)

    def button_pressed(self, widget):
        if encontrado == False and archivo == "":
            self.button.set_label("¡No hay imagenes!")
        elif encontrado == True:
            conversion()

    def on_drag_data_received(self, widget, drag_context, x,y, data,info, time):
        if True == revision(data.get_text()):
            self.button.set_label("Crear MaskMap")
            self.label.set_markup("Hay <b>"+ str(len(mylist)) + "</b> archivos en <b>" +ruta +"</b>\n"
                                  "Archivo arrastrado: <b>"+archivo+"</b>\n"
                                  "<b>"+ str(numero) +"</b> materiales <b>"+material+"</b> encontrados\n"
                                  "Roughness: <b>"+ str(roughness) + "</b>\nMetallic: <b>" + str(metallic) + "</b>\nAO: <b>" + str(ao) +"</b>"
                                  )
            
        else:
            self.button.set_label("¡archivo no compatible!")
            self.label.set_markup("¡El archivo <b>"+archivo+"</b> No es compatible!\n"
            "Arrastre una imagen <b>EXR</b> creada con el <b>BAKE PBR</b> en la ventana")

    


window = LabelWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()