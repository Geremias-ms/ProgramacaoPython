#Escreva um programa que leia o salário de um funcionário  e exiba na 
#tela o valor do salário com um reajuste de aumento, sendo que:
#Caso o salário atual seja maior que R$ 2.000,00 receberá 7% de aumento.
#Caso contrário, receberá 15% de aumento.

sal = float(input('Digite seu salario: '))
if sal > 2000:
    s1= sal*0.07
    aum= sal + s1
else:
    s= sal*0.15
    aum = sal + s

print('O salario com aumento é: ', aum)