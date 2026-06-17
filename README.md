# Eliminador de Strings Duplicadas - RISC-V Assembly

## 📋 Descrição do Projeto

Este projeto implementa um programa em **Assembly RISC-V** que processa uma string de entrada, identifica e elimina palavras duplicadas, gerando um arquivo de saída contendo:

1. **String Filtrada**: Contém as palavras originais sem repetições
2. **String de Duplicatas**: Lista as palavras que foram encontradas repetidas

## 🎯 Funcionalidade Principal

O programa realiza as seguintes operações:

- ✅ Lê uma string de entrada
- ✅ Percorre caractere por caractere identificando palavras
- ✅ Compara palavras novas com as já processadas
- ✅ Filtra palavras duplicadas (considerando variações maiúsculas/minúsculas)
- ✅ Gera saída com palavras únicas
- ✅ Registra palavras duplicadas encontradas

## 🏗️ Estrutura do Código

### Seção de Dados (`.data`)

```assembly
msg:              # String de entrada
string_final:     # String filtrada (sem repetidos)
string_repetidos: # String contendo os repetidos
string_atual:     # Buffer para a palavra atual sendo processada
string_prev:      # Buffer para a palavra anterior para comparação
```

### Seção de Código (`.text`)

O programa implementa um algoritmo que:

1. **Leitura de Bits**: Extrai caracteres alpanuméricos (A-Z, a-z, 0-9)
2. **Comparação**: Compara a palavra atual com palavras anteriores
3. **Filtro**: Remove palavras já processadas
4. **Saída**: Exibe as strings processadas

## 💻 Fluxo de Execução

```
Início
  ↓
Lê caractere da entrada
  ↓
É alfanumérico?
  ├─ Sim: Adiciona à string atual
  └─ Não: Processa a palavra
    ↓
Compara com palavras anteriores
  ├─ Duplicada: Adiciona a string_repetidos
  └─ Única: Adiciona a string_final
    ↓
Fim da entrada?
  ├─ Não: Volta ao início
  └─ Sim: Exibe resultado
```

## 📝 Exemplo de Uso

**Entrada:**
```
"aa.aa/ds ds,fd*gt.gt"
```

**Saída esperada:**
- **String Final**: `aa`, `ds`, `fd`, `gt` (sem repetições)
- **String Repetidos**: `aa`, `ds`, `gt` (palavras que se repetiram)

## 🔤 Detalhes Técnicos

### Faixa de Caracteres Suportados

- **0-9**: ASCII 48-57
- **A-Z**: ASCII 65-90
- **a-z**: ASCII 97-122

### Comparação Case-Insensitive

O programa implementa comparação que considera variações entre maiúsculas e minúsculas:
- Diferença de 32 entre maiúscula e minúscula é ignorada
- Exemplo: `"Palavra"` e `"palavra"` são consideradas iguais

## 🚀 Como Executar

1. Utilize um simulador ou assembler RISC-V
2. Carregue o arquivo `trabalhoplnassembly.asm`
3. Execute o programa
4. O resultado será exibido através de syscall (a7=4)

### Requisitos

- Simulador RISC-V (ex: MARS, Spike, ou similar)
- Suporte a syscalls para I/O (print, exit)

## 📁 Arquivos

- `trabalhoplnassembly.asm` - Código fonte em Assembly RISC-V
- `README.md` - Este arquivo

## 🛠️ Componentes Principais

| Componente | Descrição |
|-----------|-----------|
| `msg` | String de entrada a ser processada |
| `string_final` | Buffer de 600 bytes para palavras únicas |
| `string_repetidos` | Buffer de 600 bytes para palavras duplicadas |
| `string_atual` | Buffer de 100 bytes para a palavra em processamento |
| `string_prev` | Buffer de 100 bytes para comparação com palavra anterior |

## 📊 Registradores Utilizados

- `t0` - Ponteiro da string de entrada
- `t3` - Ponteiro da string final
- `t5` - Ponteiro da string de repetidos
- `t4` - Contador de tamanho
- `s0-s6` - Registradores de propósito geral
- `a0, a1, a3` - Registradores de argumentos
- `a7` - Número da syscall

## 🔄 Algoritmo de Comparação

1. Verifica se tamanhos das palavras são diferentes
2. Se diferentes → palavra é única, adiciona à string_final
3. Se iguais → compara byte a byte:
   - Verifica igualdade exata
   - Verifica diferença de 32 (case-insensitive)
4. Se todas as comparações forem iguais → palavra é duplicada

## 📌 Notas Importantes

- O programa assume palavras separadas por caracteres não-alfanuméricos
- A comparação é case-insensitive
- O tamanho máximo de buffers é 600 bytes
- Cada palavra pode ter até 100 caracteres

## 👥 Autores

- [**Gustavo de Sousa**](https://github.com/Gustasssdev)
- [**Diogo Rangel**](https://github.com/DiogoRangel11)

**Projeto de Arquitetura de Computadores - RISC-V Assembly**

---

**Última atualização:** 2026-06-17
