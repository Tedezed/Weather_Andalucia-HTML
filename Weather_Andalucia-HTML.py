#Create by: Tedezed
import os
import requests
import json
from jinja2 import Template
ncapital = 0
vdireclist = ['Norte','Noreste','Este','Sureste','Sur','Suroeste','Oeste','Noroeste']
capital = ['Almeria','Cadiz','Cordoba','Granada','Huelva','Jaen','Malaga','Sevilla']
list_cent = []
list_centmax = []
list_vspeed = []
list_vdirec = []

fil= open('Plantilla.html','r')
html = ''
for linea in fil:
	html = html + linea
Plantilla = Template(html)

while ncapital <= 7:
	fichero = requests.get('http://api.openweathermap.org/data/2.5/weather/', params={'q':'%s,spain' %capital[ncapital]})
	dicc=json.loads(fichero.text)

	fel = int(dicc['main']['temp_min'])
	felmax = int(dicc['main']['temp_max'])
	vspeed = dicc['wind']['speed']*1600/1000
	vdirec = int(dicc['wind']['deg'])
	cent=str(fel-273)
	centmax=str(felmax-273)

	if vdirec == 0 or vdirec == 360:
		vdirec = vdireclist[0]
	elif vdirec > 0 and vdirec < 90:
		vdirec = vdireclist[1]
	if vdirec == 90:
		vdirec = vdireclist[2]
	elif vdirec > 90 and vdirec < 180:
		vdirec = vdireclist[3]
	if vdirec == 180:
		vdirec = vdireclist[4]
	elif vdirec > 180 and vdirec < 270: 
		vdirec = vdireclist[5]
	if vdirec == 270:
		vdirec = vdireclist[6]
	elif vdirec > 270 and vdirec < 360:
		vdirec = vdireclist[7]

	list_cent.append(cent)
	list_centmax.append(centmax)
	list_vspeed.append(vspeed)
	list_vdirec.append(vdirec)

	ncapital = ncapital + 1

Plantilla_sal = Plantilla.render(capitalh=capital,centh=list_cent,centmaxh=list_centmax,vspeedh=list_vspeed,vdirech=list_vdirec)
archi=open('Plantilla_sal.html','w')
archi.write(Plantilla_sal)
archi.close()
os.system("firefox Plantilla_sal.html")
