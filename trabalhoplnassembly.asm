.data
msg: .asciz "aa.aa/ds ds,fd*gt.gt"
string_final: .space 600 # string filtrada de repetidos 
string_repetidos: .space 600 # string de repetidos 
string_atual: .space 100
string_prev: .space 100

.text
.globl main

main:
la t0, msg #Recebe o ponteiro da String
la t3, string_final #String tratada sem repetidos
la t5, string_repetidos #String para colocar os repetidos quando for se comparando
li t4, 0 #Controle
la s1 , string_atual # Carrega o endereço da string atual
la s2 , string_prev # Carrega o endereço da string anterior 
li s4, 0 # Carrega o tamanho da string anterior 

loop:
lb a0, 0(t0)#
lb a1, 0(t3) # Da linha 19 a 21 carrega os espaçoes reservados 
lb a3, 0(t5)#
beqz a0, fim # Quando a string acabar salta para o final 
li t2, 48 #Intervalo final de caracteres
blt a0,t2,comparação # if string.bit < 48 vai tratar string 
li t2, 122
bgt a0, t2, comparação # if string.bit > 122
j comp_alfanum

leitura_bit_string:
sb a0, 0(s1)
addi s1, s1, 1
addi t0, t0, 1
addi t4, t4, 1
j loop

comparação:
mv s0 , t4 # copia o tamanho da string atual pra minha variavel
bne s0 , s4 , copiar_string_final # se o tamanho for diferente coloca na string final 
la s1 , string_atual # endereço da string atual
la s2 , string_prev # endereço da string
   
while: # tamanho iguais, começa a comparar bit a bit  
lb s5 , 0(s1) # carrega o valor do char da string
lb s6 , 0(s2) # carrega o valor do char da string
beq s5 , s6 , continue # compara byte abyte e vai para decrementar, garantindo que o caso de serem o ascii igual
sub s7 , s5 , s6
li t2 , 32 
beq s7 , t2 , continue
li t2 , -32
beq s7 , t2 , continue 
copiar_string_final:


continue: # decrementa coma=parando byte a byte 
addi s5 , s5 , 1
addi s6 , s6 , 1
addi s0 , s0 , -1
bnez s0 , copiar_string_repetida # se terminar a string e tudo for igual vai copiar no vector hj 
j while

comp_alfanum:
li t2, 57 # comparar intervalo entre 9 e A
bgt a0,t2,mini_pulo
j comparação

mini_pulo:
li t2,65 # comparar intervalo entre 9 e A
blt a0,t2,comparação
li t2,90
bgt a0,t2,mini_pulo2 # comparar intervalo entre 90 e 97
j comparação

mini_pulo2: # comparar intervalo entre 97 
li t2,97
blt a0,t2,comparação
j leitura_bit_string

fim:
la a0, string_final
li a7, 4
ecall
li a7, 10
ecall

