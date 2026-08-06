numero_secreto = 7 # define o número secreto previamente

tentativas = 0 # define um comço para a contagem das tentativas

while True: # loop até a condição ser verdadeira
    numero = int(input("Digite um número aqui: ")) # pede um número e guarda ele
    tentativas += 1 # aumenta o número de tentativas a cada loop 
    if numero == numero_secreto: # condição para finalizar o loop
        print("Acertou! Parabéns chefe!") # se a condição for verdadeira essa mensagem irá aparecer
        print(f"Acertou em {tentativas} tentativas!") # pega o número de tentativas e mostra ele
    break # termina o loop se as condições anteriores forem verdadeiras
    print("Errou! Tente novamente!") # se a condição anterior for falsa ele cai direto aqui
    
   
