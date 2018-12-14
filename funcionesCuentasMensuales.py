import os
from tkinter import *

root = Tk()
root.geometry("500x500")

"""
	Esta clase sirve para guardar el importe de un dia concreto dentro del mesArray,
	donde indica el valor que dispones y si ese es por defecto o modicifaco manualmente
"""

class Dia:
	saldo = 0
	modificado = False
	def __init__(self, saldo, modificado):
		self.saldo = saldo
		self.modificado = modificado

class Mes:
	dias = [Dia(0,False)]
	saldoTotal = 0
	mesString = ""
	def __init__(self, dias = [Dia(0,False)], saldoTotal = 0, mesString = ""):
		self.dias = dias
		self.saldoTotal = saldoTotal
		self.mesString = mesString
	

## Establece el mes y comprueba que se ha introducido un mes valido
def setMesString():
	mesesValidos = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', ' SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
	mesValido = False

	while (mesValido == False) :
		mes = input('Introducir mes: ')
		for a in mesesValidos:
			if a == mes.upper():
				mesValido = True
	return mes

## Dado el mes nos devuelve el numero de dias
def getDiasMes(mesString):
	diasPorMes = {'ENERO': 31, 'FEBRERO': 28, 'MARZO': 31, 'ABRIL': 30, 'MAYO': 31, 'JUNIO': 30, 'JULIO': 31, 'AGOSTO': 31, ' SEPTIEMBRE': 30, 'OCTUBRE': 31, 'NOVIEMBRE': 30, 'DICIEMBRE': 31}

	return diasPorMes[mesString.upper()]

## Estable el dinero mensual
def setDinero():
	return int(input('Introducir dinero mensual: '))

""" 
	Dado el mes y el dinero disponible para gastar, devuelve un Mes 
	con el dinero por defecto que dispone para gastar cada dia
"""
def setDineroDiarioDefault(dinero, diasMes):
	saldoDiario = dinero/diasMes
	
	dias = []

	for i in range(diasMes):
		dias.append(Dia(saldoDiario, False))
	
	MES = Mes(dias,dinero)	

	return MES

"""
	Dado mes, dia, importe, dinero del que se dispone en ese Mes
	modifica el importe de ese dia en concreto y recalcula el valor
	de los dias que no se modificaron
"""
def cambiarImporte(MES, dia, importe):
	dia = dia - 1
	MES.dias[dia].saldo = importe
	MES.dias[dia].modificado = True
	count = 0
	dineroTotal = MES.saldoTotal
	for i in range(len(MES.dias)):
		if MES.dias[i].modificado == True:
			dineroTotal -= MES.dias[i].saldo
			count += 1

	saldoDiario = dineroTotal/(len(MES.dias)-count)
	for i in range(len(MES.dias)):
		if MES.dias[i].modificado == False:
			MES.dias[i].saldo = saldoDiario

	return MES

## Dado el Mes nos imprime los valores en forma de calendario
def printCalendar(MES):
	print('')
	print('')
	print('Month: '+MES.mesString)
	print('')
	print('    L    |      M    |      X    |      J    |      V    |      S    |      D')
	for i in range(len(MES.dias)):
		if i < 9:
			print(' ',end='')

		saldo = str(round(MES.dias[i].saldo,2))
		while len(saldo) < 5:
			saldo = " "+saldo
		print(str(i+1)+': '+str(saldo)+'|  ', end='')
		if i%7==6:
			print('')
			print('---------|-----------|-----------|-----------|-----------|-----------|-----------|')
	print('')
	print('')
	print("Total amount: "+str(MES.saldoTotal))
	print('')
	print('')

def printCalendarVentana(frame, MES):
	height = int(len(MES.dias)/7) + (len(MES.dias)/7 > 0)
	width = 7
	for i in range(height): #Rows
		j = 0
		while i*7+j < len(MES.dias) and j < 7: #Columns
			count = i*7+j
			b = Label(frame, text=str(i*7+j+1)+":  "+str(round(MES.dias[i*7+j].saldo,2)))
			b.grid(row = i, column = j)
			j = j + 1

	
	

	


## Dado mes, año y Mes, nos guarda en .txt los datos e.g. 2018Enero.txt
def guardarMes(mesString, anoString, MES):
	file = open( anoString+mesString+".txt", "w")
	file.write(str(MES.saldoTotal))
	file.write("\n")
	for dia in MES.dias:
		file.write(str(dia.saldo)+",")
		file.write(str(dia.modificado))
		file.write("\n")

	file.close()

def getMes(mesString, anoString):
	file = open( anoString+mesString+".txt", "r")
	lines = file.readlines()
	dias = []
	count = 0
	for line in lines:
		if count == 0:
			saldoTotal = int(line.replace("\n",""))
		else:	
			line = line.split(",")
			modificado = False
			if line[1].replace("\n","") == "True":
				modificado = True

			dias.append(Dia( float(line[0]) , modificado ) )
		count += 1


	file.close()	
	MES = Mes(dias, saldoTotal)
	return MES




keep = True
MES = Mes()
print("Hi there! Welcome to your personal economy assistant.")

while keep == True:
	print("1. Load month economy")
	print("2. Exit")
	choose = int(input(""))
	if choose == 1:
		anoString = input("Select Year:")
		mesString = input("Select Month:")
		exist = os.path.isfile('./'+anoString+mesString+'.txt')
		if exist == True:
			respuesta = ""
		else:
			respuesta = "Y"
		while respuesta.upper() != "Y" and respuesta.upper() != "N":
			respuesta = input("That month already exist. Do you want overwrite it?(Y/N)")
		if respuesta.upper() == "Y":
			dineroMensual = setDinero()
			MES = setDineroDiarioDefault(dineroMensual, getDiasMes(mesString))
			MES.mesString = mesString
			printCalendar(MES)
			printCalendarVentana(MES)
			guardarMes(mesString,anoString, MES)
		elif respuesta.upper() == "N":
			MES = getMes(mesString,anoString)
			MES.mesString = mesString
			printCalendar(MES)
			printCalendarVentana(MES)
		keep1 = True
		while keep1 == True:
			print("1. Modify a day amount")
			print("2. Exit")
			choose1 = int(input(""))
			if choose1 == 1:
				dia = int(input("Which day you want to modify: "))
				importe = int(input("How much you go to spend: "))
				cambiarImporte(MES, dia, importe)
				printCalendar(MES)
				printCalendarVentana(MES)
				guardarMes(mesString,anoString,MES)
			elif choose1 == 2:
				keep1 = False

	elif choose == 2:
		keep = False

	


	
	

	