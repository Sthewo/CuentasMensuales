from tkinter import *
from funcionesCuentasMensuales import *

MES = getMes("Enero","2019")

def borrarTabla():
  list = gridFrame.grid_slaves()
  for l in list:
    l.destroy()

def onClickAceptar():
	dia = int(Entry.get(entryDia))
	importe = int(Entry.get(entryImporte))
	entryDia.delete(0, 'end')
	entryImporte.delete(0, 'end')
	borrarTabla()

	cambiarImporte(MES, dia, importe)
	guardarMes("Enero","2019",MES)
	printCalendar(gridFrame,MES)

def borrarCampos():
	entryDia.delete(0, 'end')
	entryImporte.delete(0, 'end')

def cargarMes():
	loadFrame.pack_forget()
	mesString = Entry.get(entryMes)
	anoString = Entry.get(entryAno)
	MES = getMes(mesString, anoString)
	monthFrame.pack(fill = BOTH)
	printCalendar(gridFrame,MES)

def Volver():
	monthFrame.pack_forget()
	loadFrame.pack(fill = BOTH)

root = Tk()

loadFrame = Frame(root)
loadFrame.pack(fill = BOTH)

mainFrame = Frame(loadFrame)
mainFrame.pack(fill= X)

buttonFrame = Frame(loadFrame)
buttonFrame.pack(fill = X)

entryMes = Entry(mainFrame)
entryAno = Entry(mainFrame)
buttonCargar = Button(buttonFrame, command=cargarMes, text="Cargar")

Label(mainFrame, text = "Mes: ").pack(side = LEFT)
entryMes.pack(side = LEFT)
Label(mainFrame, text = "Año: ").pack(side = LEFT)
entryAno.pack(side = LEFT)
buttonCargar.pack()






monthFrame = Frame(root)
##monthFrame.pack(fill = BOTH)

topFrame = Frame(monthFrame)
topFrame.pack(fill = X)

gridFrame = Frame(monthFrame)
gridFrame.pack()

botFrame1 = Frame(monthFrame)
botFrame1.pack(fill = X)

botFrame2 = Frame(monthFrame)
botFrame2.pack(fill = X)

botFrame3 = Frame(monthFrame)
botFrame3.pack(fill = X,pady=(5,5))


printCalendar(gridFrame,MES)


labelStringMes 			= Label(topFrame, text="Mes: Enero")
labelDineroTotal 		= Label(botFrame1, text="Dinero: 1500")
labelCambiarImporte 	= Label(botFrame1, text="Cambiar Importe", anchor=W)
entryDia 				= Entry(botFrame2)
entryImporte 			= Entry(botFrame2)
buttonAceptar 			= Button(botFrame3, command=onClickAceptar, text="Cambiar")
buttonCancelar 			= Button(botFrame3, command=borrarCampos, text="Cancelar")
buttonVolver 			= Button(botFrame3, command=Volver, text="Atras")

labelStringMes.pack(side = TOP, fill = X, anchor = W)
labelDineroTotal.pack(side = TOP, fill = X,)
labelCambiarImporte.pack(side = TOP, fill = X)
Label(botFrame2, text = "Dia: ").pack(side = LEFT)
entryDia.pack(side = LEFT)
Label(botFrame2, text = "Importe: ").pack(side = LEFT)
entryImporte.pack(side = LEFT)
buttonAceptar.pack(side = LEFT, padx=(10, 0))
buttonCancelar.pack(side = LEFT, padx=(5, 0))
buttonVolver.pack(side = LEFT, padx=(5, 0))









root.mainloop()
