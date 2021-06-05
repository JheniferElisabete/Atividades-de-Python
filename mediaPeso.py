'''
Faça um programa que receba o peso de 7 pessoas. Calcule e mostre:
    * a quantidade de pessoas acima de 90kg
    * a meida dos pesos das pessoas
'''
#cria umna lista
x = []
contador = 0
#cria a estrutura de repetição pra rodar 7 vezes
for i in range (0, 7):
    #inicializa na ultima posição da lista o valor que o usuario digitar
    x.append(float(input(f'Informe o peso da {i+1} pessoa\n')))
    if x[i] > 90:
        contador +=1
#sum soma todos os valores
#len retorna o tamanho da lista
#:.2p faz com que a media fique formatada com 2 casas apos a virgula
print(f'Existem {contador} pessoas acima dos 90KG e media dos pesos é {sum(x)/len(x):.2f}')



