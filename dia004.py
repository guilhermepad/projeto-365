##Classificador de idade
#idade_do_usuario = int(input("Diga sua idade para classificação aqui: ")) # Pergunta a idade do usuário e guarda esse número
#if idade_do_usuario < 12: # Faz o uso da condicional para a classificação da idade
    #print("Criança!")
    #print("Tá no começo da vida ainda!")
#elif idade_do_usuario >= 12 and idade_do_usuario < 18:
    #print("Adolescente!")
    #print("Cuidado com as espinhas na cara!")
#elif idade_do_usuario >= 18 and idade_do_usuario < 60:
  #  print("Adulto!")
  #  print("CLT, INSS, e imposto de renda vão te perseguir agora!")
#elif idade_do_usuario >= 60:
   # print("Idoso!")
 #   print("Se levantar os braços Jesus leva!")



##Identificador de Pares e Ímpares

#number = int(input("Digite um número aqui: ")) # Guarda o número para a verificação
#if number % 2 == 0: # Identifica se o número guardado é par
 #   print(f"{number} é par!") # Imprime uma mensagem caso o número seja par
#else:
 #   print(f"{number} é ímpar!") # Caso o número não seja par imprime uma mensagem dizendo que ele é ímpar
#print("Esse comando será sempre executado") # Redundante

##Conversão de Temperatura melhorado
value = input("Você quer converter a temperatura para Celsius ou Fahrenheit? ") #pergunta para qual indicador o usuario quer converter
temp = float(input("Qual a temperatura de Hoje? ")) # pergunta a temperatura de hoje
if value.lower() == 'fahrenheit': 
    print(f"A temperatura de hoje em Fahrenheit é: {(temp * 1.8) + 32}F") # se o usuario digitar fahrenheit ele fara a conversão de celsius pra fahrenheit
elif value.lower() == 'celsius':
    print(f"A temperatura de hoje em Celsius é: {(temp - 32) * 5/9}C") # se o usuario digitar celsius ele fará a conversão contrária
else: 
    print("Erro operação inválida!") # se o usuario digitar qualquer coisa além disso, o comando dará como inválido