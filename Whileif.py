
while True:
    valor = int(input("Insira um número: "))
    analise = valor%2

    if valor < 0:
        print("\nNúmero negativo")
        break
    elif analise == 0:
        print("\nNúmero par!!")
    elif analise > 0:
        print("\nNúmero ímpar!")
