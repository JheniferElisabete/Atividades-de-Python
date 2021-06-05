'''
Faça um programa que receba varias idades e calcule e mostre a media das idades. Finalize o programa quano a entrada for igual a -1
'''
soma = 0
i = 0
x = 0
while x != -1:
    x = (int(input('Informe a idade ou utilize o -1 para sair\n')))
    if x != -1:
        soma += x
        i +=1

print(f'A media das idades é {(soma)/i}')