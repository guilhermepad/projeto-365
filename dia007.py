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



contatos = [ 
    {"nome": "Luis", "telefone": "(11)998259920", "cidade": "São Paulo"},
    {"nome": "João", "telefone": "(21)975214402", "cidade": "Rio de Janeiro"},
    {"nome": "Pedro", "telefone": "(85)958215052", "cidade": "Fortaleza"}
]

for contato in contatos:
    print(f"{contato['nome']} mora em {contato['cidade']}.")

contatos.append({"nome": "Guilherme", "telefone": "(21)981524715", "cidade": "Rio de Janeiro"})

print(f"Temos {len(contatos)} contatos listados.")

    