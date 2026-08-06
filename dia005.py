numero_secreto = 7

tentativas = 0

while True: 
    numero = int(input("Digite um número aqui: "))
    tentativas += 1
    if numero == numero_secreto:
        print("Acertou! Parabéns chefe!")
        print(f"Acertou em {tentativas} tentativas!")

        break
    print("Errou! Tente novamente!")
    
   
