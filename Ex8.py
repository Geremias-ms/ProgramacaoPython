#Escreva uma função que receba como parâmetro um número N
#e exibe todos os número primos menores que N.
def ehprimo(n):
    soma = 0
    for i in range(1, n +1):
        if n % i == 0:
            soma += 1
    if soma == 2:
        return True
    else:
        return False

def primomenores(num):
    for i in range(1, num + 1):
        if ehprimo(i) == True:
            print (i)

num = int(input("informe um numero: "))
primomenores(num)
