#frutas = ["maçã", "banana", "uva", "manga", "abacaxi", "melancia"]

#primeiras_frutas = frutas[0:3]

#frutas.remove("uva")

#ultima_fruta = frutas.pop(4)

#print(f"as frutas são{frutas}, a ultima fruta é {ultima_fruta}, e as primeiras frutas são {primeiras_frutas}.")

dias_semana = ("domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado")

for dia in dias_semana:
    print(dia)

perfil = {
    "nome": "Guilherme", "idade": 18, "cidade": "Rio de Janeiro", "profissão": "Dev"
}

print(perfil["cidade"])

perfil["linguagem"] = "Python"
perfil["idade"] = 19

for chaves, valor in perfil.items():
    print(f"{chaves}: {valor}")