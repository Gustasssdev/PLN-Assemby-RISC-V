#Trabalho de Arquitetura:
import re
i = 0
resultado = None
pontuacao = 1
palavras_repetidas = dict()
texto = "luz luz e diogo,diogo,gustavo GUSTAVO sao da computacao"
lista_separada = re.split(r'(\W+)', texto)
pontuacoes = re.findall(r'[^\w\s]', texto)
msg_tratada = [item.strip() for item in lista_separada if item.strip()]

def position(text, palavra, segunda_aparicao):
    inicio = -1
    for i in range(segunda_aparicao):
        inicio = text.find(palavra, inicio + 1)
        if inicio == -1:
            return 0
    return inicio

for palavra in msg_tratada:
     if i == 0:
            palavra_prev = palavra
            msg_final = palavra
     else:
        if len(palavra) == 1:
            if palavra in pontuacoes and pontuacao == 1:
                msg_final += palavra
                pontuacao = 0
        else:
            palavra_atual = palavra
            if palavra_prev.lower() != palavra_atual.lower():
                msg_final += f" {palavra}"
                palavra_prev = palavra
                pontuacao = 1
            else:
                pos = position(texto.lower(), palavra.lower(), 2)
                palavras_repetidas[palavra.lower()] = pos + 1
     i += 1

#Percorrer a lista das palavras repetidas:
i = 0
for word in palavras_repetidas:
    if i == 0:
        resultado = f"{word.capitalize()} - {palavras_repetidas[word]}"
    else:
        resultado += f" {word.capitalize()} - {palavras_repetidas[word]}"
    i += 1

with open("Resultado.txt", "w") as file:
    file.write(f"{msg_final}\n")
    file.write(f"{resultado}\n")
