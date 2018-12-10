import os
"""
class Mes:
	def __init__(self, dias, saldoTotal):
		self.dias = dias
		self.saldoTotal = saldoTotal
	def setSaldoTotal(self, saldoTotal):
		self.saldoTotal = saldoTotal
	def setDias(self, dias):
		self.dias = dias
"""
"""
	Esta clase sirve para guardar el importe de un dia concreto dentro del mesArray,
	donde indica el valor que dispones y si ese es por defecto o modicifaco manualmente
"""

class Mes:
	def __init__(self, saldo, modificado):
		self.saldo = saldo
		self.modificado = modificado
	def setSaldo(self,saldo):
		self.saldo = saldo
	def setModificado(self, modificado):
		self.modificado = modificado


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
def getDiasMes(mes):
	diasPorMes = {'ENERO': 31, 'FEBRERO': 28, 'MARZO': 31, 'ABRIL': 30, 'MAYO': 31, 'JUNIO': 30, 'JULIO': 31, 'AGOSTO': 31, ' SEPTIEMBRE': 30, 'OCTUBRE': 31, 'NOVIEMBRE': 30, 'DICIEMBRE': 31}

	return diasPorMes[mes.upper()]

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
		dias.append(Mes(saldoDiario, False))
	

	return dias

"""
	Dado mes, dia, importe, dinero del que se dispone en ese Mes
	modifica el importe de ese dia en concreto y recalcula el valor
	de los dias que no se modificaron
"""
def cambiarImporte(mes, dia, importe, dineroTotal):
	mes[dias].saldo = importe
	mes[dia].modificado = True
	count = 0
	for i in range(len(mes)):
		if mes[i].modificado == True:
			dineroTotal -= mes[i].saldo
			count += 1

	saldoDiario = dineroTotal/(len(mes)-count)
	for i in range(len(mes)):
		if mes[i].modificado == False:
			mes[i].saldo = saldoDiario

	return mes

## Dado el Mes nos imprime los valores en forma de calendario
def printCalendar(mes):
	print('')
	print('')
	print('    L    |      M    |      X    |      J    |      V    |      S    |      D')
	for i in range(len(mes)):
		if i < 9:
			print(' ',end='')

		saldo = str(round(mes[i].saldo,2))
		while len(saldo) < 5:
			saldo = "0"+saldo
		print(str(i+1)+': '+str(saldo)+'|  ', end='')
		if i%7==6:
			print('')
			print('---------|-----------|-----------|-----------|-----------|-----------|-----------|')
	print('')
	print('')
	print('')

## Dado mes, año y Mes, nos guarda en .txt los datos e.g. 2018Enero.txt
def guardarMes(mesString, anoString, mes):
	file = open( anoString+mesString+".txt", "w")
	for dia in mes:
		file.write(str(dia.saldo)+",")
		file.write(str(dia.modificado))
		file.write("\n")

	file.close()

def getMes(mesString, anoString):
	file = open( anoString+mesString+".txt", "r")
	lines = file.readlines()
	dias = []

	for line in lines:
		line = line.split(",")
		dias.append(Dia( float(line[0]) , bool(line[1].replace("\n","")) ) )

	
	return dias




keep = True
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
			respuesta = "N"
		while respuesta.upper() != "Y" and respuesta.upper() != "N":
			respuesta = input("That month already exist. Do you want overwrite it?(Y/N)")
		if respuesta.upper() == "Y":
			dineroMensual = setDinero()
			Mes = setDineroDiarioDefault(dineroMensual, getDiasMes(mesString))
			printCalendar(Mes)
		elif respuesta.upper() == "N":
			Mes = getMes(mesString,anoString)
			printCalendar(Mes)

	if choose == 2:
		keep = False
	


