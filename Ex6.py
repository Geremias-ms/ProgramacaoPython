#Escreva uma função que recebe como parâmetro 
#um número N e retorna a soma de todos os divisores desse número.

def main(n):
    j=0
    for i in range(1,n+1):
       if (n % i ) == 0:
           j= j+ i
    return j
            

n = int(input("Digite o valor de n: "))
f=main(n)
print(f)