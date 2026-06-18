# Eliminador de Strings Duplicadas - RISC-V Assembly

## 📋 Descrição do Projeto

Este projeto consiste em um programa desenvolvido em **Assembly RISC-V** que processa uma string de entrada, identifica palavras duplicadas e gera um arquivo de saída (`resultado.txt`). 

O diferencial desta versão é que o programa:
1. **Filtra a String Original**: Mantém apenas a primeira ocorrência de cada palavra.
2. **Identifica Duplicatas com Índice**: Lista as palavras que se repetiram e indica em qual posição (índice) do texto original elas foram encontradas.
3. **Preserva Pontuação**: Mantém os separadores originais na string filtrada.

## 🎯 Funcionalidades

- ✅ **Processamento de Strings**: Identifica palavras alfanuméricas (A-Z, a-z, 0-9).
- ✅ **Comparação Case-Insensitive**: Reconhece que "GUSTAVO" e "gustavo" são a mesma palavra.
- ✅ **Geração de Arquivo**: Cria um arquivo `resultado.txt` com os resultados.
- ✅ **Rastreamento de Posição**: Adiciona o índice de onde a palavra duplicada foi encontrada na string original.

## 🏗️ Estrutura do Código

### Seção de Dados (`.data`)

```assembly
msg:              # String de exemplo para processamento
string_final:     # Buffer para a string filtrada
string_repetidos: # Buffer para palavras duplicadas + índices
write:            # Nome do arquivo de saída ("resultado.txt")
dash:             # Caractere separador ("-") para os índices
```

### Registradores Principais

- `t0`: Ponteiro da string de entrada.
- `s9`: Ponteiro para `string_final`.
- `s10`: Ponteiro para `string_repetidos`.
- `t4`: Contador de caracteres (índice global).
- `s8`: Tamanho da palavra atual.
- `s4`: Tamanho da palavra anterior (para comparação rápida).

## 💻 Fluxo de Lógica

1. **Varredura**: O programa lê a `msg` caractere por caractere.
2. **Filtro Alfanumérico**: Ignora símbolos para delimitar palavras, mas os preserva na `string_final`.
3. **Comparação**:
   - Se a palavra atual é diferente da anterior (tamanho ou conteúdo), ela é copiada para `string_final`.
   - Se for igual (mesmo ignorando case), ela é enviada para `string_repetidos`.
4. **Indexação**: Quando uma duplicata é achada, o programa calcula sua posição inicial na string original e anexa ao lado da palavra (ex: `palavra-15`).
5. **Saída em Arquivo**: Utiliza as syscalls RISC-V para abrir, escrever e fechar o arquivo `resultado.txt`.

## 📝 Exemplo

**Entrada (`msg`):**
`"luz luz e diogo,diogo,gustavo GUSTAVO sao da computacao"`

**Arquivo de Saída (`resultado.txt`):**
1. **Parte 1 (Filtrada):** `luz  e diogo,,gustavo  sao da computacao`
2. **Parte 2 (Repetidos):** `luz-5 diogo-17 GUSTAVO-31`

*(Nota: Os separadores e espaços são mantidos na primeira parte para preservar a estrutura do texto original).*

## 🚀 Como Executar

1. Utilize um simulador RISC-V que suporte syscalls de arquivo (como o **RARS** ou **MARS**).
2. Carregue o arquivo `trabalhoplnassembly.asm`.
3. Monte (Assemble) e Execute (Run).
4. Verifique o arquivo `resultado.txt` gerado no mesmo diretório.

## 👥 Autores

- [**Gustavo de Sousa**](https://github.com/Gustasssdev)
- [**Diogo Rangel**](https://github.com/DiogoRangel11)
- [**Pedro Luz Lima**](https://github.com/pLuzLim)

**Projeto de Arquitetura de Computadores - RISC-V Assembly**

---

**Última atualização:** 2026-06-18
