peso = input("Me dê o seu peso aqui: ")
altura = input("Me dê a sua altura agora: ")

peso = float(peso)
altura = float(altura)

print(f"O seu IMC aproximado é {peso / (altura ** 2):.2f}")