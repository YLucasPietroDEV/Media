# Ler as notas dos quatro bimestres
N1 = float(input("Digite a nota do primeiro bimestre: "))
N2 = float(input("Digite a nota do segundo bimestre: "))
N3 = float(input("Digite a nota do terceiro bimestre: "))
N4 = float(input("Digite a nota do quarto bimestre: "))

# Calcular a média aritmética
MD = (N1 + N2 + N3 + N4) / 4

# Verificar se o aluno foi aprovado ou reprovado
if MD >= 5:
    print("Aluno Aprovado com média:", MD)
else:
    print("Aluno Reprovado com média:", MD)