v = float(input('informe o valor recebido por hora '))
h = int(input('informe a quantidades de horas trabalhadas no mes '))
s = v * h
print(s)
inss = (8/100*s)
ir = (11/100*s)
sindicato = (5/100*s)
sl = s - (inss + ir + sindicato)
print(f'Seu salario Bruto é de: {s},\n Descontos: \n Inss: {inss} \n Imposto de Renda: {ir} \n Sindicato: {sindicato} \n Salario Liquido {sl}')