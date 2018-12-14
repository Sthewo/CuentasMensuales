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

root = Tk()

topFrame = Frame(root)
topFrame.pack(fill = X)

gridFrame = Frame(root)
gridFrame.pack()

botFrame1 = Frame(root)
botFrame1.pack(fill = X)

botFrame2 = Frame(root)
botFrame2.pack(fill = X)

botFrame3 = Frame(root)
botFrame3.pack(fill = X,pady=(5,5))


printCalendar(gridFrame,MES)


labelStringMes 			= Label(topFrame, text="Mes: Enero")
labelDineroTotal 		= Label(botFrame1, text="Dinero: 1500")
labelCambiarImporte = Label(botFrame1, text="Cambiar Importe", anchor=W)
entryDia 						= Entry(botFrame2)
entryImporte 				= Entry(botFrame2)
buttonAceptar 			= Button(botFrame3, command=onClickAceptar, text="Cambiar")
buttonCancelar 			= Button(botFrame3, command=borrarCampos, text="Cancelar")

labelStringMes.pack(side = TOP, fill = X, anchor = W)
labelDineroTotal.pack(side = TOP, fill = X,)
labelCambiarImporte.pack(side = TOP, fill = X)
Label(botFrame2, text = "Dia: ").pack(side = LEFT)
entryDia.pack(side = LEFT)
Label(botFrame2, text = "Importe: ").pack(side = LEFT)
entryImporte.pack(side = LEFT)
buttonAceptar.pack(side = LEFT, padx=(10, 0))
buttonCancelar.pack(side = LEFT, padx=(5, 0))

root.mainloop()
