#Escreva uma função que receba como parâmetro um número N e retorna
#True se esse número for primo, e False caso não seja primo.

def m(n):
    if n <2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
               return False
        return True
    

n = int(input("Digite o valor de n: "))
f = m(n)    
print(f)