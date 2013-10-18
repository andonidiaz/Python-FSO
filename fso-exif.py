#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#fso-exif.py
#
#Copyright 2013 
#Marc Ruiz <marc.ruiz@estudiants.urv.cat> 
#Andoni Diaz <andoni.diaz@estudiants.urv.cat>
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#MA 02110-1301, USA.
#
#

from Tkinter import *
import tkMessageBox
import tkFileDialog
import os
import fnmatch
import pyexiv2
import datetime
import shutil
import ImageTk
from PIL import Image

def change_date(d,m,y):
	
	day=StringVar()
	month=StringVar()
	year=StringVar()
		
	window_date=Toplevel()
	window_date.title("Canvi Data Captura")
	window_date.focus_set()
	imglist=Listbox(images_list,yscrollcommand=scrollist.set,selectmode='multiple')
	data_frame=Frame(window_date)
	data_label=Label(data_frame,text="Data captura (dia/mes/any):",anchor=W)
	data_label.pack(side=LEFT)
	dia_label=Label(data_frame,textvariable=d,borderwidth=1,relief=SUNKEN,bg="#FFFFC4",anchor=W, width=2)
	dia_label.pack(side=LEFT, expand=TRUE, fill=X)
	barra_label=Label(data_frame,text="/",anchor=W)
	barra_label.pack(side=LEFT)
	mes_label=Label(data_frame,textvariable=m,borderwidth=1,relief=SUNKEN,bg="#FFFFC4",anchor=W, width=2)
	mes_label.pack(side=LEFT, expand=TRUE, fill=X)
	barra_label=Label(data_frame,text="/",anchor=W)
	barra_label.pack(side=LEFT)
	year_label=Label(data_frame,textvariable=y,borderwidth=1,relief=SUNKEN,bg="#FFFFC4",anchor=W, width=4)
	year_label.pack(side=LEFT, expand=TRUE, fill=X)
	a_label=Label(data_frame,text="a ",anchor=W)
	a_label.pack(side=LEFT)
	new_d=Entry(data_frame,textvariable=day, width=2, bg="#FFFFC4")
	new_d.pack(side=LEFT, expand=TRUE, fill=X)
	barra_label=Label(data_frame,text="/",anchor=W)
	barra_label.pack(side=LEFT)
	new_m=Entry(data_frame,textvariable=month,width=2, bg="#FFFFC4")
	new_m.pack(side=LEFT,expand=TRUE, fill=X)
	barra_label=Label(data_frame,text="/",anchor=W)
	barra_label.pack(side=LEFT)
	new_y=Entry(data_frame,textvariable=year,width=4, bg="#FFFFC4")
	new_y.pack(side=LEFT, expand=TRUE, fill=X)
	data_button_change=Button(data_frame,text="Canviar",command=window_date.destroy)
	data_button_change.pack(side=LEFT, anchor=E)
	data_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2, anchor=N)
	
def movedirectory():
		
	newdir=StringVar()
		
	window_newdir=Toplevel()
	window_newdir.title("Escollir nou Directori")
	imagenes_copiar = imglist.curselection()
		
	newdir_frame=Frame(window_newdir)
	newdir_label=Label(newdir_frame,text="Nom directori desti:",anchor=W)
	newdir_label.pack(side=LEFT)
	new_dir=Entry(newdir_frame,textvariable=newdir, width=20)
	new_dir.pack(side=LEFT, expand=TRUE, fill=X)
	newdir_button_change=Button(newdir_frame,text="Crear",command=lambda: choose_new_dir(window_newdir,newdir,imagenes_copiar))
	newdir_button_change.pack(side=LEFT, anchor=E)
	newdir_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2, anchor=N)
		
def choose_new_dir(window_newdir,newdir,imagenes_copiar):
	window_newdir.destroy()
	dirname=tkFileDialog.askdirectory()
	for i in xrange(len(imagenes_copiar)):
		shutil.copy2(imglist.get(i), dirname)
		
def changecopyright(mycopy):
		
	newCopy=StringVar()
		
	window_copy=Toplevel()
	window_copy.title("Canvi Copyright")
	window_copy.focus_set()
	
	newcopy_frame=Frame(window_copy)
	newcopy_label=Label(newcopy_frame,text="Modifica Copyright:",anchor=W)
	newcopy_label.pack(side=LEFT)
	copy_label=Label(newcopy_frame,textvariable=mycopy,anchor=W, width=10, borderwidth=1,relief=SUNKEN,bg="#FFFFFF")
	copy_label.pack(side=LEFT, expand=TRUE, fill=X)
	a_label=Label(newcopy_frame,text="a: ",anchor=W)
	a_label.pack(side=LEFT)
	new_copy=Entry(newcopy_frame,textvariable=newCopy, width=10)
	new_copy.pack(side=LEFT,expand=TRUE, fill=X)
	newcopy_button_change=Button(newcopy_frame,text="Canviar",command=window_copy.destroy)
	newcopy_button_change.pack(side=LEFT, anchor=E)
	newcopy_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2, anchor=N)
def cleanList():
	imglist.delete(0,imglist.size())
	hide_move_directory()

def loadFiles(path):
	cleanList()
	for root, dirnames, filenames in os.walk(path):
		for filename in fnmatch.filter(filenames, '*.jpg'):
			#Ruta entera: os.path.join(root, filename)
			imglist.insert(END, os.path.join(root, filename))
	
def hide_move_directory():
	selected.pack_forget()
	mov_directory.pack_forget()
	camera.set("")
	objectiu.set("")
	longitud.set("")
	exposicio.set("")
	diafragma.set("")
	iso.set("")
	midax.set("")
	miday.set("")
	copyr.set("")
	dia.set("")
	mes.set("")
	year.set("")
	thumb_img.pack_forget()
	
def show_move_directory():
	selected.pack(side=LEFT)
	mov_directory.pack(side=LEFT)
	
def mensaje_ventana(cabecera, mensaje):
	
	tkMessageBox.showinfo(title=cabecera,message=mensaje)
	
	"""
	Hay un ejemplo de funcionamiento de esta función en la linia 177
	
	Esto podría ser una alternativa eliminando un parámetro:
	
	window_newdir=Toplevel()
	window_newdir.title("Missatge d'estat")
	window_newdir.minsize(400, 75)
	newdir_frame=Frame(window_newdir)
	newdir_label=Label(newdir_frame,textvariable=mensaje)
	newdir_label.pack()
	accept_button=Button(newdir_frame,text="Acceptar",command=window_newdir.destroy)
	accept_button.pack(side=BOTTOM)
	newdir_frame.pack(side=TOP,expand=TRUE, fill=X)"""
	
#MAIN

window=Tk()
window.title("Tractament Imatge EXIF")
window.minsize(750, 475)

"""
Ejemplo de funcionamiento de la función mensaje_ventana
cabecera='Hola'
mensaje='Estoy informando'
mensaje_ventana(cabecera,mensaje)"""

#HEADER

directory=StringVar()
header=Frame(window)

#MENU

menu=Frame(header)
body=Frame(window)

#IMG LIST
images_list=Frame(body)
scrollist=Scrollbar(images_list,orient=VERTICAL)
scrollistx=Scrollbar(images_list,orient=HORIZONTAL)

imglist=Listbox(images_list,yscrollcommand=scrollist.set,xscrollcommand=scrollistx.set,selectmode='multiple')

scrollistx.config(command=imglist.xview)
scrollistx.pack(side=BOTTOM,expand=FALSE,fill=X,anchor=N)

scrollist.config(command=imglist.yview)
scrollist.pack(side=RIGHT,expand=TRUE,fill=Y,anchor=W)

imglist.pack(side=TOP,expand=TRUE,fill=Y,anchor=N)

images_list.pack(side=LEFT,expand=TRUE,fill=Y, anchor=NW)


def ocultarSeleccionats():
	imatges_seleccionades =imglist.curselection()
	for i in reversed(xrange(len(imatges_seleccionades))):
		imglist.delete(imatges_seleccionades[i])
	hide_move_directory()

def ocultarNoSeleccionats():
	imatges_seleccionades = imglist.curselection()
	while imglist.size() != len(imatges_seleccionades):
		for j in xrange(imglist.size()):
			if(not(str(j) in imatges_seleccionades)):
				imglist.delete(j)
				imatges_seleccionades = imglist.curselection()


hide_selected=Button(menu,text="Ocultar seleccionats",command=ocultarSeleccionats)
hide_selected.pack(side=RIGHT,anchor=CENTER)

hide_non_selected=Button(menu,text="Ocultar NO seleccionats",command=ocultarNoSeleccionats)
hide_non_selected.pack(side=RIGHT,anchor=CENTER)

clean_list=Button(menu,text="Netejar",command=cleanList)
clean_list.pack(side=RIGHT,anchor=CENTER)

def getList():
	loadFiles(directory.get())
	hide_move_directory()

fill_list=Button(menu,text="Omplir",command=getList)
fill_list.pack(side=RIGHT,anchor=CENTER)

list_label=Label(menu,text="Llista:")
list_label.pack(side=RIGHT,anchor=CENTER)

menu.pack(side=BOTTOM,anchor=CENTER)
#END MENU

actual_directory=Label(header,textvariable=directory,borderwidth=1,relief=SUNKEN)
actual_directory.pack(side=RIGHT, expand=TRUE, fill=X)
actual_directory.bind()

choose_directory=Button(header,text="Escollir directori de treball",command=lambda: current_dir(directory))

choose_directory.pack(side=TOP)

header.pack(side=TOP, fill=X, anchor=N)

#END HEADER

#END IMG LIST

#IMG INFORMATION

img_info=Frame(body)

#SELECTED IMAGE

img=StringVar()

img_selected=Frame(img_info)

selected_img_label=Label(img_selected,text="Seleccionat:")
selected_img_label.pack(side=LEFT)

actual_img=Label(img_selected,textvariable=img,borderwidth=1,relief=SUNKEN,bg="#D2F5D2")
actual_img.pack(side=LEFT, expand=TRUE, fill=X)

img_selected.pack(side=TOP, expand=TRUE, fill=X, padx=10, pady=10)

#END SELECTED IMAGE

#IMG_THUMB 

thumb=Frame(img_info)

thumb_img = Canvas(thumb,width=250, height=300)
thumb_img.pack()

thumb.pack(side=LEFT)

#END IMG_THUMB

#IMG EXIF 

exif=Frame(img_info)

camera=StringVar()

objectiu=StringVar()

longitud=StringVar()

exposicio=StringVar()

diafragma=StringVar()

iso=StringVar()

midax=StringVar()

miday=StringVar()

copyr=StringVar()

dia=StringVar()

mes=StringVar()

year=StringVar()

camera_frame=Frame(exif)
camera_button=Button(camera_frame,text="Càmera:",command=window.quit, width=10)
camera_button.pack(side=LEFT)
camera_label=Entry(camera_frame,textvariable=camera,borderwidth=1,bg="#FFFFC4",width=4)
camera_label.pack(side=LEFT, expand=TRUE, fill=X)
camera_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)

objectiu_frame=Frame(exif)
objectiu_button=Button(objectiu_frame,text="Objectiu:",command=window.quit, width=10)
objectiu_button.pack(side=LEFT)
objectiu_label=Entry(objectiu_frame,textvariable=objectiu,borderwidth=1,bg="#FFFFC4",width=4)
objectiu_label.pack(side=LEFT, expand=TRUE, fill=X)
objectiu_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)

longitud_frame=Frame(exif)
longitud_button=Button(longitud_frame,text="Longitud Focal:",command=window.quit, width=10)
longitud_button.pack(side=LEFT)
longitud_label=Entry(longitud_frame,textvariable=longitud,borderwidth=1,relief=SUNKEN,bg="#FFFFC4",width=4)
longitud_label.pack(side=LEFT, expand=TRUE, fill=X)
longitud_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)

exposicio_frame=Frame(exif)
exposicio_button=Button(exposicio_frame,text="Exposició:",command=window.quit, width=10)
exposicio_button.pack(side=LEFT)
exposicio_label=Entry(exposicio_frame,textvariable=exposicio,borderwidth=1,bg="#FFFFC4",width=4)
exposicio_label.pack(side=LEFT, expand=TRUE, fill=X)
exposicio_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)

diafragma_frame=Frame(exif)
diafragma_button=Button(diafragma_frame,text="Diafragma:",command=window.quit, width=10)
diafragma_button.pack(side=LEFT)
diafragma_label=Entry(diafragma_frame,textvariable=diafragma,borderwidth=1,bg="#FFFFC4",width=4)
diafragma_label.pack(side=LEFT, expand=TRUE, fill=X)
diafragma_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)

iso_frame=Frame(exif)
iso_button=Button(iso_frame,text="ISO:",command=window.quit, width=10, pady=5)
iso_button.pack(side=LEFT)
iso_label=Entry(iso_frame,textvariable=iso,borderwidth=1,bg="#FFFFC4",width=4)
iso_label.pack(side=LEFT, expand=TRUE, fill=X)
iso_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)

mida_frame=Frame(exif)
mida_button=Button(mida_frame,text="Mida:",command=window.quit, width=10)
mida_button.pack(side=LEFT)
midax_label=Entry(mida_frame,textvariable=midax,borderwidth=1,bg="#FFFFC4",width=4)
midax_label.pack(side=LEFT, expand=TRUE, fill=X)
x_label=Label(mida_frame,text="x",anchor=W)
x_label.pack(side=LEFT)
miday_label=Entry(mida_frame,textvariable=miday,borderwidth=1,bg="#FFFFC4",width=4)
miday_label.pack(side=LEFT, expand=TRUE, fill=X)
mida_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)

copyr_frame=Frame(exif)
copyr_button=Button(copyr_frame,text="Copyright:",command=window.quit, width=10)
copyr_button.pack(side=LEFT)
copyr_label=Entry(copyr_frame,textvariable=copyr,borderwidth=1,bg="#FFFFC4",width=4)
copyr_label.pack(side=LEFT, expand=TRUE, fill=X)
copyr_button_change=Button(copyr_frame,text="Canviar",command=lambda: changecopyright(copyr))
copyr_button_change.pack(side=LEFT)
copyr_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)

data_frame=Frame(exif)
data_button_change=Button(data_frame,text="Canviar data",command=lambda: change_date(dia,mes,year))
data_button_change.pack(side=BOTTOM, anchor=E)
data_button=Button(data_frame,text="Data captura",command=window.quit, width=10)
data_button.pack(side=LEFT)
data_label=Label(data_frame,text="(dia/mes/any):",anchor=W)
data_label.pack(side=LEFT)
dia_label=Entry(data_frame,textvariable=dia,borderwidth=1,bg="#FFFFC4",width=2)
dia_label.pack(side=LEFT, expand=TRUE, fill=X)
barra_label=Label(data_frame,text="/",anchor=W)
barra_label.pack(side=LEFT)
mes_label=Entry(data_frame,textvariable=mes,borderwidth=1,bg="#FFFFC4",width=2)
mes_label.pack(side=LEFT, expand=TRUE, fill=X)
barra_label=Label(data_frame,text="/",anchor=W)
barra_label.pack(side=LEFT)
year_label=Entry(data_frame,textvariable=year,borderwidth=1,bg="#FFFFC4",width=4)
year_label.pack(side=LEFT, expand=TRUE, fill=X)
data_frame.pack(side=TOP,expand=TRUE, fill=X, padx=10, pady=2)


exif.pack(side=LEFT, expand=TRUE, fill=X)

#END EXIF

img_info.pack(side=LEFT,expand=TRUE,fill=X,anchor=N)

#END IMG INFORMATION

body.pack(side=TOP,expand=TRUE,fill=BOTH)

#END BODY


#FOOTER

footer=Frame(window)
def seleccionarTots():
	imglist.selection_set(0, imglist.size())
	show_move_directory()

def deseleccionarTots():
	imglist.selection_clear(0, imglist.size())
	hide_move_directory()

close_window=Button(footer,text="Sortir",command=window.quit)
close_window.pack(side=BOTTOM,anchor=W)
select_all=Button(footer,text="Tots",command=seleccionarTots)
select_all.pack(side=LEFT)

select_all=Button(footer,text="Cap",command=deseleccionarTots)
select_all.pack(side=LEFT)


selected=Label(footer,text="Als seleccionats")
selected.pack(side=LEFT)
mov_directory=Button(footer,text="Moure a un nou directori",command=movedirectory)
mov_directory.pack(side=LEFT)

selected.pack_forget()
mov_directory.pack_forget()



footer.pack(side=BOTTOM,anchor=W)

#END FOOTER

def current_dir(dirname):
	newdir=tkFileDialog.askdirectory()
	dirname.set(newdir)
	loadFiles(dirname.get())

# Obtiene los metadatos de la imagen y los escribe en la gui
def loadMetadata(images):
	metadades = pyexiv2.ImageMetadata(images)
	metadades.read()
	objectiu.set(getLensModel(metadades))
	camera.set(getCameraModel(metadades))
	longitud.set(getFocalLength(metadades))
	exposicio.set(getExposureTime(metadades))
	diafragma.set(getFNumber(metadades))
	iso.set(getISOSpeedRating(metadades))
	copyr.set(getCopyright(metadades))
	dia.set(getDay(metadades))
	mes.set(getMonth(metadades))
	year.set(getYear(metadades))
	midax.set(getX(metadades))
	miday.set(getY(metadades))


def getCameraModel(metadades):
	# Obtención del modelo de la cámara 
	try:
		return metadades['Exif.Image.Model'].value
	except KeyError:
		return ("No Model found.")

	# Obtención del tipo de lente
def getLensModel(metadades):
	try:
		return metadades['Exif.Photo.LensModel'].value
	except KeyError:
		return ("No LensModel found.")

	# Obtención de la longitud focal
def getFocalLength(metadades):
	try:
		return metadades['Exif.Photo.FocalLength'].value
	except KeyError:
		return("No FocalLength found.")

	# Obtención de la exposición
def getExposureTime(metadades):
	try:
		return metadades['Exif.Photo.ExposureTime'].value
	except KeyError:
		return("No ExposureTime found.")

	# Obtención del diafragma
def getFNumber(metadades):
	try:
		return metadades['Exif.Photo.FNumber'].value
	except KeyError:
		return("No FNumber found.")

	# Obtención del ISO
def getISOSpeedRating(metadades):
	try:
		return metadades['Exif.Photo.ISOSpeedRatings'].value
	except KeyError:
		return("No ISOSpeedRatings found.")

	# Obtención del copypright
def getCopyright(metadades):
	try:
		return metadades['Exif.Image.Copyright'].value
	except KeyError:
		return("No Copyright found.")

def getDay(metadades):
	try:
		data = metadades['Exif.Photo.DateTimeOriginal']
		return data.value.day
	except KeyError:
		return("-")
def getMonth(metadades):
	try:
		data = metadades['Exif.Photo.DateTimeOriginal']
		return data.value.month
	except KeyError:
		return("-")
def getYear(metadades):
	try:
		data = metadades['Exif.Photo.DateTimeOriginal']
		return data.value.year
	except KeyError:
		return("-")

def getX(metadades):
	try:
		return metadades.dimensions[0]
	except KeyError:
		return("-")

def getY(metadades):
	try:
		return metadades.dimensions[1]
	except KeyError:
		return("-")

def showbutton_selected(event):
	
	if imglist.curselection():
		show_move_directory()
		
		index = imglist.curselection()
		longitud_llista = len(index)
		if(longitud == 1):
			if not(index==""):
				images = imglist.get(index)
				img.set(images)
				loadMetadata(images)
			else:
				selected.pack_forget()
				mov_directory.pack_forget()
		else:
			# Comprovamos el primer metadato
			images = imglist.get(index[0])
			metadades_primera = pyexiv2.ImageMetadata(images)
			metadades_primera.read()
			contador = [0 for x in range(13)]
			for i in range(longitud_llista):
				images = imglist.get(index[i])
				metadades = pyexiv2.ImageMetadata(images)
				metadades.read()
				#Carguem la preview de la imatge
				preview = metadades.previews[0]				
				preview.write_to_file("//tmp//thumb_temp")
				imagen = Image.open("//tmp//thumb_temp.jpg")
				imagen = imagen.resize((250,300),Image.ANTIALIAS)
				global preview_final
				preview_final = ImageTk.PhotoImage(imagen)
				thumb_img.create_image(130,150,image=preview_final)
				thumb_img.pack()
				# Camera comú
				if (getCameraModel(metadades_primera) == getCameraModel(metadades)):
					i = longitud_llista
					contador[0]+=1
				if(contador[0] == longitud_llista):
					camera.set(getCameraModel(metadades))
				else:
					camera.set("-")

				# Objectiu comú
				if (getLensModel(metadades_primera) == getLensModel(metadades)):
					i = longitud_llista
					contador[1]+=1
				if(contador[1] == longitud_llista):
					objectiu.set(getLensModel(metadades))
				else:
					objectiu.set("-")

				if (getFocalLength(metadades_primera) == getFocalLength(metadades)):
					i = longitud_llista
					contador[2]+=1
				if(contador[2] == longitud_llista):
					longitud.set(getFocalLength(metadades))
				else:
					longitud.set("-")

				if (getExposureTime(metadades_primera) == getExposureTime(metadades)):
					i = longitud_llista
					contador[3]+=1
				if(contador[3] == longitud_llista):
					exposicio.set(getExposureTime(metadades))
				else:
					exposicio.set("-")

				if (getFNumber(metadades_primera) == getFNumber(metadades)):
					i = longitud_llista
					contador[4]+=1
				if(contador[4] == longitud_llista):
					diafragma.set(getFNumber(metadades))
				else:
					diafragma.set("-")

				if (getISOSpeedRating(metadades_primera) == getISOSpeedRating(metadades)):
					i = longitud_llista
					contador[5]+=1
				if(contador[5] == longitud_llista):
					iso.set(getISOSpeedRating(metadades))
				else:
					iso.set("-")

				if (getCopyright(metadades_primera) == getCopyright(metadades)):
					i = longitud_llista
					contador[6]+=1
				if(contador[6] == longitud_llista):
					copyr.set(getCopyright(metadades))
				else:
					copyr.set("-")

				if (getDay(metadades_primera) == getDay(metadades) and getMonth(metadades_primera) == getMonth(metadades) and getYear(metadades_primera) == getYear(metadades)):
					i = longitud_llista
					contador[7]+=1
				if(contador[7] == longitud_llista):
					dia.set(getDay(metadades))
					mes.set(getMonth(metadades))
					year.set(getYear(metadades))
				else:
					dia.set("-")
					mes.set("-")
					year.set("-")

				if (getX(metadades_primera) == getX(metadades) and getY(metadades_primera) == getY(metadades)):
					i = longitud_llista
					contador[8]+=1
				if(contador[8] == longitud_llista):
					midax.set(getX(metadades))
					miday.set(getY(metadades))
					
				else:
					midax.set("-")
					miday.set("-")
	else:
		hide_move_directory()
				

imglist.bind('<<ListboxSelect>>', showbutton_selected)
window.mainloop()
