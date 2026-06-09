def menu():
    while True:

        print("\n===== LISTA DE EXERCÍCIOS =====")
        print("1  - Questão 1")
        print("2  - Questão 2")
        print("3  - Questão 3")
        print("4  - Questão 4")
        print("5  - Questão 5")
        print("6  - Questão 6")
        print("7  - Questão 7")
        print("8  - Questão 8")
        print("9  - Questão 9")
        print("10 - Questão 10")
        print("11 - Questão 11")
        print("12 - Questão 12")
        print("13 - Questão 13")
        print("14 - Questão 14")
        print("15 - Questão 15")
        print("16 - Questão 16")
        print("17 - Questão 17")
        print("18 - Questão 18")
        print("19 - Questão 19")
        print("20 - Questão 20")
        print("0  - Sair")

        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            q1()

        elif opcao == 2:
            q2()

        elif opcao == 3:
            q3()

        elif opcao == 4:
            q4()

        elif opcao == 5:
            q5()

        elif opcao == 6:
            q6()

        elif opcao == 7:
            q7()

        elif opcao == 8:
            q8()

        elif opcao == 9:
            q9()

        elif opcao == 10:
            q10()

        elif opcao == 11:
            q11()

        elif opcao == 12:
            q12()

        elif opcao == 13:
            q13()

        elif opcao == 14:
            q14()

        elif opcao == 15:
            q15()

        elif opcao == 16:
            q16()

        elif opcao == 17:
            q17()

        elif opcao == 18:
            q18()

        elif opcao == 19:
            q19()

        elif opcao == 20:
            q20()

        elif opcao == 0:
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")

menu()
# =========================
# QUESTÃO 1
# =========================

n = int(input("Digite um número: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)


# =========================
# QUESTÃO 2
# =========================

n = int(input("Digite um número: "))

fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print("Fatorial =", fatorial)


# =========================
# QUESTÃO 3
# =========================

n = int(input("Digite um número: "))

soma = 0

for i in range(1, n + 1):
    soma += i

print("Soma =", soma)


# =========================
# QUESTÃO 4
# =========================

n = int(input("Digite a quantidade de termos: "))

a = 0
b = 1

for i in range(n):
    print(a)

    prox = a + b
    a = b
    b = prox


# =========================
# QUESTÃO 5
# =========================

n = int(input("Digite um número: "))

primo = True

if n <= 1:
    primo = False

for i in range(2, n):

    if n % i == 0:
        primo = False

if primo:
    print("É primo")
else:
    print("Não é primo")


# =========================
# QUESTÃO 6
# =========================

n = int(input("Digite um número: "))

for i in range(1, n + 1):

    if n % i == 0:
        print(i)


# =========================
# QUESTÃO 7
# =========================

n = int(input("Digite um número: "))

soma = 0

for i in range(1, n):

    if n % i == 0:
        soma += i

if soma == n:
    print("Número perfeito")
else:
    print("Não é perfeito")


# =========================
# QUESTÃO 8
# =========================

n = int(input("Digite a quantidade de números: "))

maior = None

for i in range(n):

    valor = int(input("Número: "))

    if maior is None or valor > maior:
        maior = valor

print("Maior valor =", maior)


# =========================
# QUESTÃO 9
# =========================

n = int(input("Digite a quantidade de números: "))

pares = 0

for i in range(n):

    valor = int(input("Número: "))

    if valor % 2 == 0:
        pares += 1

print("Quantidade de pares =", pares)


# =========================
# QUESTÃO 10
# =========================

n = int(input("Digite um número: "))

soma = 0

for i in range(1, n + 1):
    soma += 1 / i

print("Resultado =", soma)
# =========================
# QUESTÃO 11
# =========================

n = int(input("Digite a quantidade de termos: "))

soma = 0
den = 1

for num in range(1, n + 1):
    soma = soma + (num / den)
    den = den + 2

print("Soma =", soma)


# =========================
# QUESTÃO 12
# =========================

n = int(input("Tamanho da matriz: "))

mat = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input("Valor: ")))
    mat.append(linha)

dp = 0
ds = 0

for i in range(n):
    dp += mat[i][i]
    ds += mat[i][n - 1 - i]

print("Diagonal principal =", dp)
print("Diagonal secundária =", ds)


# =========================
# QUESTÃO 13
# =========================

lin = int(input("Linhas: "))
col = int(input("Colunas: "))

mat = []

for i in range(lin):
    linha = []
    for j in range(col):
        linha.append(int(input("Valor: ")))
    mat.append(linha)

x = int(input("Número a procurar: "))

cont = 0

for i in range(lin):
    for j in range(col):
        if mat[i][j] == x:
            cont += 1

print("Quantidade encontrada:", cont)


# =========================
# QUESTÃO 14
# =========================

lin = int(input("Linhas: "))
col = int(input("Colunas: "))

mat = []

for i in range(lin):
    linha = []
    for j in range(col):
        linha.append(int(input("Valor: ")))
    mat.append(linha)

transposta = []

for j in range(col):
    linha = []

    for i in range(lin):
        linha.append(mat[i][j])

    transposta.append(linha)

print("Matriz Transposta:")

for linha in transposta:
    print(linha)


# =========================
# QUESTÃO 15
# =========================

lin = int(input("Linhas: "))
col = int(input("Colunas: "))

mat = []

for i in range(lin):
    linha = []

    for j in range(col):
        linha.append(int(input("Valor: ")))

    mat.append(linha)

maior = mat[0][0]
menor = mat[0][0]

for i in range(lin):
    for j in range(col):

        if mat[i][j] > maior:
            maior = mat[i][j]

        if mat[i][j] < menor:
            menor = mat[i][j]

print("Maior valor:", maior)
print("Menor valor:", menor)


# =========================
# QUESTÃO 16
# =========================

lin = int(input("Linhas: "))
col = int(input("Colunas: "))

mat = []

for i in range(lin):

    linha = []

    for j in range(col):
        linha.append(i * j)

    mat.append(linha)

for linha in mat:
    print(linha)


# =========================
# QUESTÃO 17
# =========================

lin = int(input("Linhas: "))
col = int(input("Colunas: "))

mat = []

for i in range(lin):

    linha = []

    for j in range(col):
        linha.append(int(input("Valor: ")))

    mat.append(linha)

quadrada = True

if lin != col:
    quadrada = False

print("É quadrada?", quadrada)


# =========================
# QUESTÃO 18
# =========================

lin = int(input("Linhas: "))
col = int(input("Colunas: "))

mat = []

for i in range(lin):

    linha = []

    for j in range(col):
        linha.append(int(input("Valor: ")))

    mat.append(linha)

invertida = []

for i in range(lin - 1, -1, -1):
    invertida.append(mat[i])

print("Matriz invertida:")

for linha in invertida:
    print(linha)


# =========================
# QUESTÃO 19
# =========================

frase = input("Digite uma frase: ")

vogais = 0
consoantes = 0

for letra in frase:

    if letra.lower() in "aeiou":
        vogais += 1

    elif letra.isalpha():
        consoantes += 1

print("Quantidade de vogais:", vogais)
print("Quantidade de consoantes:", consoantes)


# =========================
# QUESTÃO 20
# =========================

frase = input("Digite uma frase: ")

invertida = ""

for i in range(len(frase) - 1, -1, -1):
    invertida += frase[i]

print("Frase invertida:", invertida)
