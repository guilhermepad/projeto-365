def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Coletar dados do usuário

meu_peso = float(input("Peso: "))
minha_altura = float(input("Altura: "))

# Calcular e exibir IMC

meu_imc = calcular_imc(meu_peso, minha_altura)
print(f"Seu IMC é {meu_imc:.2f}")

# Saudação personalizada

def saudacao_personalizada(nome, idade):
    print(f"Olá, {nome}! Você tem {idade} anos.")


for _ in range(3):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    saudacao_personalizada(nome, idade) #for range() → quando sabe o número exato de repetições
                                        # while True + break → quando a parada depende de uma condição imprevisível (usuário digitar "sair", número aleatório dar certo, etc.)


