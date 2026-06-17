nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3


if media >= 7:
    print(f"Aluno(a) aprovado(a) com media {media:.2f}")
elif media >= 3 and media < 7:
    print(f"Aluno(a) em Recuperação com media {media:.2f}")
    fez_recuperacao = input("Aluno já fez a recuperação? s/n: ")
    if fez_recuperacao == "s":
        nota_recuperacao = float(input("Digite a nota da recuperação: "))
        if nota_recuperacao >= 5:
            print("Aluno(a) aprovado pela recuperação")
        else:
            print("Aluno(a) não obteve nota o suficiente para ser aprovado após a recuperação ")
else:
    print(f"Aluno(a) Reprovado(a) com media {media:.2f}")

