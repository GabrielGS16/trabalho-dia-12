hora =  int(input('digite a hora'))
if  0<= hora <=23:
    if 0 <= hora <12:
        horario = 'manhã'
    elif 12 <= hora <18:
        horario = 'tarde'
    else:
        horario = 'noite'
    print(f'é de {horario}')
else:
    print('Horario invalido')
 
