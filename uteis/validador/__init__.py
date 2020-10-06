from validador_cpf import *


def verificar(v_cpf):
    checked = PhotoImage(file='img/checked.png')
    unchecked = PhotoImage(file='img/unchecked.png')

    if v_cpf == '111.111.111-11' or v_cpf == '11111111111':
        return status.configure(image=unchecked)

    n10 = int(v_cpf[0]) * 10
    n9 = int(v_cpf[1]) * 9
    n8 = int(v_cpf[2]) * 8
    n7 = int(v_cpf[3]) * 7
    n6 = int(v_cpf[4]) * 6
    n5 = int(v_cpf[5]) * 5
    n4 = int(v_cpf[6]) * 4
    n3 = int(v_cpf[7]) * 3
    n2 = int(v_cpf[8]) * 2

    primeiro_verificador = (
            ((n10 + n9 + n8 + n7 + n6 + n5 + n4 + n3 + n2) * 10) % 11)

    n11_2 = int(v_cpf[0]) * 11
    n10_2 = int(v_cpf[1]) * 10
    n9_2 = int(v_cpf[2]) * 9
    n8_2 = int(v_cpf[3]) * 8
    n7_2 = int(v_cpf[4]) * 7
    n6_2 = int(v_cpf[5]) * 6
    n5_2 = int(v_cpf[6]) * 5
    n4_2 = int(v_cpf[7]) * 4
    n3_2 = int(v_cpf[8]) * 3
    n2_2 = primeiro_verificador * 2

    segundo_verificador = (
            ((n11_2 + n10_2 + n9_2 + n8_2 + n7_2 + n6_2 + n5_2 + n4_2 + n3_2 + n2_2) * 10) % 11)

    if str(primeiro_verificador == v_cpf[9]) and (str(segundo_verificador) == v_cpf[10]):
        return status.configure(image=checked)
    else:
        return status.configure(image=unchecked)
