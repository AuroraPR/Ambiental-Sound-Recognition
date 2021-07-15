import os
import re
import sys

raiz='.'


file=open("./"+sys.argv[1],"w")

file.write("name,target,category\n")

switcher = {
        "aspirador": 1,
        "cisterna": 2,
        "conversacion": 3,
        "cubiertos_sartenes": 4,
        "despertador": 5,
        "ducha": 6,


        "grifo_cocina": 7,
        "impresora": 8,
        "microondas": 9,

		"puerta": 10,
		"telefono":11,
		"timbre":12
		}

for dirName, subdirList, fileList in os.walk(raiz):
	#print("Direcotrio "+dirName)
	for fname in fileList:
		#print(dirName+','+fname)
		#print(dirName)
		category=dirName.split(".\\")
		#print(category)
		#print(fname)
		name=re.split('(\d+)',fname)
		#print(name)
		
		if(category[0]!='.'):#Quitamos los archivos de la raiz
			target=switcher.get(dirName[2:])
			#print(name[1])
			#if(len(name[1])==2):
			file.write(name[0]+name[1]+name[2]+','+str(target)+',"'+dirName[2:]+'"\n')
			#else:
			#	file.write(name[0]+name[1][1:]+name[2]+','+str(target)+',"'+dirName[2:]+'"\n')
file.close()