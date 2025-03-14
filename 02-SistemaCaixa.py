# Faça um Programa para um caixa eletrônico. 
# O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
import math as mt
saldosaque=0
notasFinais={}

valorSaque=float(input("Digite o valor do saque:"))

while valorSaque<10 or valorSaque>600 :

    if valorSaque <10:
        print("Valor insuficiente, saque pelo menos 10 reais")  
        valorSaque=float(input("Digite o valor do saque acima de 9:"))

    if valorSaque >600:
        print("Valor Ultrapassa, saque menos  de 600 reais")
        valorSaque=float(input("Digite o valor do saque abaixo de 601:"))

if valorSaque>=10 and valorSaque<=600:
     saldosaque=valorSaque

     while True:
        if saldosaque==0:
            print(notasFinais)
            for valor, key in notasFinais.items():
                print(f"{valor}:{key}")
            break
            
        nota100=mt.floor(saldosaque/100)
        if nota100!=0:
            notasFinais["Notas 100"]=nota100

        nota50=mt.floor((saldosaque%100)/50)
        if nota50!=0:
            notasFinais["Notas 50"]=nota50

        nota10=mt.floor((saldosaque%50)/10)
        if nota10!=0:
            notasFinais["Notas 10"]=nota10

        nota5=mt.floor((saldosaque%10)/5)
        if nota5!=0:
            notasFinais["Notas 5"]=nota5

        nota2=mt.floor((saldosaque%5)/2)
        if nota2!=0:
            notasFinais["Notas 2"]=nota2

        nota1=mt.floor((saldosaque%2)/1)
        if nota1!=0:
            notasFinais["Notas 1"]=nota1
        saldosaque=0
        














# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 

# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: 
# Para sacar a quantia de 256 reais, o programa fornece:
# - Duas notas de 100
# - Uma nota de 50
# - Uma nota de 5
# - Uma nota de 1

# Exemplo 2:
# Para sacar a quantia de 399 reais, o programa fornece:
# - Três notas de 100
# - Uma nota de 50
# - Quatro notas de 10
# - Uma nota de 5
# - Quatro notas de 1
