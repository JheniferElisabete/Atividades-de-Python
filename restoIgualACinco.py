'''
faça um programa que verifique e mostre os numeros entre 1000 e 2000(inclusive) que, quando dividido por 11 produz resto igual a 5
'''
#o % é o resto da divisão
for i in range (1000, 2001):
    if i%11 == 5:
        print(i)