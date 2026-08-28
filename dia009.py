def apresentar(nome, profissao="estudante", cidade="Rio de Janeiro"):
    print(f"Sou {nome}, {profissao}, moro em {cidade}")

for _ in range(1):
    nome = input("Seu nome: ")
    apresentar(nome)
    nome = input("Seu nome: ")
    cidade = input("Sua cidade: ")
    apresentar(nome, cidade=cidade)
    nome = input("Seu nome: ")
    cidade = input("Sua cidade: ")
    profissao = input("Sua profissão: ")
    apresentar(nome, cidade=cidade, profissao=profissao)

