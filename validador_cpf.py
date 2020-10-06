import tkinter.ttk as ttk
from tkinter import Tk, StringVar, N, S, E, W, PhotoImage

from ttkthemes import ThemedStyle

from uteis import validador

checked = PhotoImage(file='img/checked.png')
unchecked = PhotoImage(file='img/unchecked.png')

root = Tk()
root.title('Validador de CPF')
root.geometry('280x100')
root.configure(bg='#464646')

style = ThemedStyle(root)
style.set_theme('equilux')

cpf_label = ttk.Label(root, text='Digite o CPF abaixo', font=('Arial', 12, 'bold'))
cpf_label.grid(row=0, column=0)

var_CPF = StringVar()

cpf_input = ttk.Entry(root, font=('Arial', 12, 'bold'), textvariable=var_CPF)
cpf_input.grid(row=1, column=0)

teclado = PhotoImage(file='img/teclado.png')

status = ttk.Label(root, image=teclado)
status.grid(row=0, rowspan=2, column=1, padx=10)

bt_conferir = ttk.Button(root, text='Conferir', command=validador.verificar(var_CPF), width=15)
bt_conferir.grid(row=2, columnspan=2, sticky=N + S + E + W)


root.mainloop()
