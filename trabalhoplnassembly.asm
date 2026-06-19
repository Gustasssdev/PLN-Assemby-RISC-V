.data
msg: .asciz "luz luz e diogo,diogo,gustavo GUSTAVO sao da computacao" #string exemplo
string_final: .space 600 # string filtrada de repetidos 
string_repetidos: .space 600 # string de repetidos 
string_atual: .space 100
string_prev: .space 100
write: .asciz "resultado.txt"
dash: .ascii "-"
endl: .byte 10


.text
.globl main

main:
la t0, msg #Recebe o ponteiro da String
la s9, string_final #String tratada sem repetidos
la s10, string_repetidos #String para colocar os repetidos quando for se comparando
li s8, 0 #Controle
la s1 , string_atual # Carrega o endereco da string atual
la s2 , string_prev # Carrega o endereco da string anterior 
li s4, 0 # Carrega o tamanho da string anterior 
li t4, 0 #indice


loop:
addi t4, t4, 1
lb s11, 0(t0)#
li t2, 48 #Intervalo final de caracteres
blt s11,t2,comparacao # if string.bit < 48 vai tratar string 
li t2, 122
bgt s11, t2, comparacao # if string.bit > 122
j comp_alfanum

leitura_bit_string:
sb s11, 0(s1)
addi s1, s1, 1
addi t0, t0, 1
addi s8, s8, 1
j loop

comparacao:
mv s0 , s8 # copia o tamanho da string atual pra minha variavel
bne s0 , s4 , copiar_string_final # se o tamanho for diferente coloca na string final 
la s1 , string_atual # endereco da string atual
la s2 , string_prev # endereco da string
   
while: # tamanho iguais, comeca a comparar bit a bit  
lb s5 , 0(s1) # carrega o valor do char da string
lb s6 , 0(s2) # carrega o valor do char da string
beq s5 , s6 , continue # compara byte abyte e vai para decrementar, garantindo que o caso de serem o ascii igual
sub s7 , s5 , s6
li t2 , 32 
beq s7 , t2 , continue
li t2 , -32
beq s7 , t2 , continue 

copiar_string_final:
mv s0, s8 #copiar para contar de novo
la s1 , string_atual #comeca a carregar para a string final
loopcopia:
beqz s0, copiar_prev
lb t6, 0(s1)
sb t6, 0(s9)  
addi s1, s1, 1
addi s9, s9, 1
addi s0, s0, -1
j loopcopia
copiar_prev:
mv s0, s8
mv s4, s8
la s1, string_atual #preparando para copiar pra string anterior
la s2, string_prev
copialoop:
beqz s0, addfinal
lb t6, 0(s1)
sb t6, 0(s2)
addi s1, s1, 1
addi s2, s2, 1
addi s0, s0, -1 
j copialoop
copiar_string_repetida:
mv s0, s8
la s1, string_atual
reploop:
beqz s0, indice
lb t6, 0(s1)
sb t6, 0(s10)
addi s1, s1, 1
addi s10, s10, 1
addi s0, s0, -1
j reploop


continue: # decrementa coma=parando byte a byte 
addi s5 , s5 , 1
addi s6 , s6 , 1
addi s0 , s0 , -1
beqz s0 , copiar_string_repetida # se terminar a string e tudo for igual vai copiar no vector hj 
j while

comp_alfanum:
li t2, 58 # comparar intervalo entre 9 e A
blt s11,t2,leitura_bit_string
li t2,65 # comparar intervalo entre 9 e A
blt s11,t2,comparacao
li t2,91
blt s11,t2,leitura_bit_string # comparar intervalo entre 90 e 97
li t2,96
bgt s11,t2,leitura_bit_string
j comparacao

ascii_gt10ind: #no caso que o indice fica maior que 10, transforma para imprimir
div t5, t6, t3
rem t2, t6, t3
addi t5, t5,  48
addi t2, t2, 48
sb t5, 0(s10)
addi s10, s10, 1
sb t2, 0(s10)
addi s10, s10, 2
j preloop

indice: #coloca o índice na lista dos repetidos
la t5, dash
lb t6, 0(t5)
sb t6, 0(s10)
addi s10, s10, 1
li t3, 10
mv t6, t4
sub t6, t6, s8
bgt t6, t3, ascii_gt10ind #caso que seja maior que 10
addi t6, t6, 48
sb t6, 0(s10)
addi s10, s10, 2
j preloop

addfinal: # preserva os separadores das palavras
sb s11, 0(s9)
addi s9, s9, 1
beqz s11, fim
preloop:
la s1, string_atual
li s8, 0
addi t0, t0, 1
beqz s11, fimtrata # Quando a string acabar salta para o final 
j loop

fimtrata: # exclui os separadores das palavras repetidas
addi s9, s9, -1
sb x0, 0(s9)

fim: #coloca tudo em um arquivo de saída

li a7, 1024
la a0, write
li a1, 1
ecall
mv t3, a0


li a7, 64
mv a0, t3
la a1, string_final
mv a2, t4
ecall

mv a0, t3
la a1, endl
li a2, 1
ecall

mv a0, t3
la a1, string_repetidos
mv a2, t4
ecall

li a7, 57
ecall

li a7, 10
ecall
