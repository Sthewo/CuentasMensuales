from tkinter import *
from funcionesCuentasMensuales import *

MES = getMes("Enero","2019")

def borrarTabla():
  list = gridFrame.grid_slaves()
  for l in list:
    l.destroy()
    
def onClickAceptar():
	borrarTabla()
	dia = int(Entry.get(entryDia))
	importe = int(Entry.get(entryImporte))

	cambiarImporte(MES, dia, importe)
	guardarMes("Enero","2019",MES)
	printCalendarVentana(gridFrame,MES)
	

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


printCalendarVentana(gridFrame,MES)
"""
height = 5
width = 7
for i in range(height): #Rows
	j = 0
	while j < 7: #Columns
		b = Label(gridFrame, text=str(i)+":"+str(j))
		b.grid(row=i,column=j)
		j = j + 1
"""

labelStringMes 			= Label(topFrame, text="Mes: Enero")
labelDineroTotal 		= Label(botFrame1, text="Dinero: 1500")
labelCambiarImporte = Label(botFrame1, text="Cambiar Importe", anchor=W)
entryDia 						= Entry(botFrame2)
entryImporte 				= Entry(botFrame2)
buttonAceptar 			= Button(botFrame3, command=onClickAceptar, text="Cambiar")
buttonCancelar 			= Button(botFrame3, text="Cancelar")

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
