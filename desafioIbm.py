x = int(input('Informe o numero para saber se é multiplo de 3 e/ou 5'))
n = x
for i in range (0,x):
    if n%3 == 0 and n%5 == 0:
        print('FizzBuzz')
    elif n%3 == 0:
        print('Fizz')
    elif n%5 == 0:
        print('Buzz')
    else:
        print(n)
    n = n - 1

