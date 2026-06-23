#Trabalho de Arquitetura:
texto = "marcos. marcos. julia julia e thiago thiago thiago sao da fisica fisica experimental"
i = 0
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
