from tkinter import Tk, Label, Entry, Button, PhotoImage, StringVar, N, S, E, W
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle


def conferir():
    vCPF = var_CPF.get()

    if vCPF == '111.111.111-11' or vCPF == '11111111111':
        status.configure(image=unchecked)

    n10 = int(vCPF[0]) * 10
    n9 = int(vCPF[1]) * 9
    n8 = int(vCPF[2]) * 8
    n7 = int(vCPF[3]) * 7
    n6 = int(vCPF[4]) * 6
    n5 = int(vCPF[5]) * 5
    n4 = int(vCPF[6]) * 4
    n3 = int(vCPF[7]) * 3
    n2 = int(vCPF[8]) * 2

    primeiro_verificador = (
        ((n10 + n9 + n8 + n7 + n6 + n5 + n4 + n3 + n2) * 10) % 11)

    n11_2 = int(vCPF[0]) * 11
    n10_2 = int(vCPF[1]) * 10
    n9_2 = int(vCPF[2]) * 9
    n8_2 = int(vCPF[3]) * 8
    n7_2 = int(vCPF[4]) * 7
    n6_2 = int(vCPF[5]) * 6
    n5_2 = int(vCPF[6]) * 5
    n4_2 = int(vCPF[7]) * 4
    n3_2 = int(vCPF[8]) * 3
    n2_2 = primeiro_verificador * 2

    segundo_verificador = (
        ((n11_2 + n10_2 + n9_2 + n8_2 + n7_2 + n6_2 + n5_2 + n4_2 + n3_2 + n2_2) * 10) % 11)

    if ((str(primeiro_verificador == vCPF[9]) and (str(segundo_verificador) == vCPF[10]))):
        status.configure(image=checked)
    else:
        status.configure(image=unchecked)


root = Tk()
root.title('Validador de CPF')
root.geometry('280x100')
root.configure(bg='#464646')

style = ThemedStyle(root)
style.set_theme('equilux')

# IMAGENS
checked = PhotoImage(file='img/checked.png')
unchecked = PhotoImage(file='img/unchecked.png')
teclado = PhotoImage(file='img/teclado.png')

cpf_label = ttk.Label(root, text='Digite o CPF abaixo',
                      font=('Arial', 12, 'bold'))
cpf_label.grid(row=0, column=0)

var_CPF = StringVar()

cpf_input = ttk.Entry(root, font=('Arial', 12, 'bold'), textvariable=var_CPF)
cpf_input.grid(row=1, column=0)

status = ttk.Label(root, image=teclado)
status.grid(row=0, rowspan=2, column=1, padx=10)

bt_conferir = ttk.Button(root, text='Conferir', command=conferir, width=15)
bt_conferir.grid(row=2, columnspan=2, sticky=N+S+E+W)


root.mainloop()
