salario = float(input("Digite o salário bruto?"))
parcelas = float(input("Digite ao valor das parcelas?"))

if parcelas <= salario * 0.30:
    print("crédito aprovado")

else:
    print("crédito reprovado")

