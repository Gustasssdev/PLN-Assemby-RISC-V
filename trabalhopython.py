#Trabalho de Arquitetura:
texto = "marcos. marcos. julia julia e thiago thiago thiago sao da fisica fisica experimental"
i = 0
<<<<<<< HEAD
palavra_prev = ""
palavra_atual = ""
texto_final = ""
resultado = ""
palavras_repetidas = list()

for letra in texto:
    if (ord(letra) >= 32 and ord(letra) <= 47) or (ord(letra) >= 58 and ord(letra) <= 64) or (ord(letra) >= 91 and ord(letra) <= 96) or (ord(letra) >= 123 and ord(letra) <=127):
        if palavra_atual.lower() == palavra_prev.lower():
            if palavra_atual.capitalize()  not in palavras_repetidas:
                palavras_repetidas.append(palavra_atual.capitalize())
            palavra_atual = ""
=======
resultado = None
pontuacao = 1
palavras_repetidas = dict()
texto = "Pedro,Pedro Diogo,Gustavo,Gus"
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
        if palavra in pontuacoes:
            if pontuacao == 1:
                msg_final += palavra
                pontuacao = 0
>>>>>>> 21c7d1c (Algo)
        else:
            texto_final += palavra_atual + letra
            if i == 0:
                palavra_prev = palavra_atual
                palavra_atual = ""
            i = 1
    else:
        palavra_atual += letra
        i = 0

if palavra_atual.lower() == palavra_prev.lower():
    if palavra_atual.capitalize()  not in palavras_repetidas:
            palavras_repetidas.append(palavra_atual.capitalize())
else:        
    texto_final += palavra_atual

for word in palavras_repetidas:
    resultado += f"{word} "


print(texto_final)
print(palavras_repetidas)


with open("Resultado.txt", "w") as file:
    file.write(f"{texto_final}\n")
    file.write(f"{resultado}\n")

