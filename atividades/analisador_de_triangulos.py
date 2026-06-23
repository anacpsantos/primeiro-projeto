A = float(input("Digite o comprimento da reta A: "))
B = float(input("Digite o comprimento da reta B: "))
C = float(input("Digite o comprimento da reta C: "))


if A + B > C or A + C > B or B + C > A:
    print("As retas podem formar um triângulo!")


    if A == B == C:
        print("Tipo: Triângulo Equilátero")
    elif A == B or A == C or B == C:
        print("Tipo: Triângulo Isósceles")
    else:
        print("Tipo: Triângulo Escaleno")
else:
    print("As retas NÃO podem formar um triângulo.")