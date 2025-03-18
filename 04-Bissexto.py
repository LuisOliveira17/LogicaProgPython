ano=int(input("Digite o ano:"))

if ano%4==0 or ano%400==0 and ano%100!=0:
    print("Eh Bissexto")

else:
    print("Nao eh Bissexto")