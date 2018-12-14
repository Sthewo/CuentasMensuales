from tkinter import *

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

height = 5
width = 7
for i in range(height): #Rows
	j = 0
	while j < 7: #Columns
		b = Label(gridFrame, text=str(i)+":"+str(j))
		b.grid(row=i,column=j)
		j = j + 1

labelStringMes 			= Label(topFrame, text="Mes: Enero")
labelDineroTotal 		= Label(botFrame1, text="Dinero: 1500")
labelCambiarImporte = Label(botFrame1, text="CambiarDinero", anchor=W)
entryDia 						= Entry(botFrame2)
entryImporte 				= Entry(botFrame2)
buttonAceptar 			= Button(botFrame3, text="Aceptar")
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
