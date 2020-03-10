#Escreva uma função que recebe como parâmetro um número N e 
#exibe todos os divisores desse número.

def main(n):
   for i in range(1,n+1):
       if (n % i ) == 0:
           print(i)
            

n = int(input("Digite o valor de n: "))
main(n)
