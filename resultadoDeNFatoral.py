'''
Faça um progra,a que mostre o resultado de n!
5! = 5*4*3*2*1
'''

x = int(input(f'Informe o numero que sera calculado o valor fatorial\n'))

fatorial = 1
#for começa do vaolor que o usuario digita ate 0
for i in range(x, 0, -1):
#i começa a valer o valor que o usuario digitou, po isso que multiplica ele pelo fatorial
    fatorial = fatorial * i
print(fatorial)