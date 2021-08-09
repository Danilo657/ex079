numeros = list()
resp = ''
while True:
    valores = int(input('diga um valor: '))
    if valores not in numeros:
        numeros.append(valores)
        print('valor inserido  com sucessos')
    else:
        print('valor duplicado !!!')
    resp = str(input('Quer continuar ? Sim ou Não ?')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Os valores ditos foram {sorted(numeros)}')
