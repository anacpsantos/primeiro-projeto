# Leitura do valor da compra
valor_compra = float(input("Digite o valor total da compra: R$ "))

# Cálculo do desconto
if valor_compra <= 100:
    desconto = 0

elif valor_compra <= 300:
    desconto = valor_compra * 0.05

elif valor_compra <= 500:
    desconto = valor_compra * 0.10

else:
    desconto = valor_compra * 0.15

# Valor final
total_pagar = valor_compra - desconto

# Exibição dos resultados
print(f" \n Valor original: R$ {valor_compra:.2f}")
print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_pagar:.2f}")


