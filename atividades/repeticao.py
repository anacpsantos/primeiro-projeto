continuar = "S"

while continuar.lower() == "s":
    num = float(input("Digite um numero: "))
    print(num % 2)
    if num % 2 == 0:
        print("par")
else:
    print("impar")

    continuar = input("Deseja continuar? ")
    


