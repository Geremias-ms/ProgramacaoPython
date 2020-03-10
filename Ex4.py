#Escreva uma função que recebe como parâmetro de entrada um número N
#positivo, e retorna o fatorial de n 

def func(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    print("O valor de %d! eh =" %n, fat)

n = float(input("Digite o valor de n: "))
func(n)
