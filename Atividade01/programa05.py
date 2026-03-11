# ALGORITMO

#     DEFINA
#         numero, quadrado, cubo real

#     ENQUANTO (Verdadeiro)

#         ESCREVA("Digite um numero maior que zero: ")
#         leia numero
        
#         SE (numero<=0)
#             ENTAO
#                 ESCREVA("Digite um numero maior que zero!!")
#         SENAO
#             QUEBRE

#     quadrado <- numero*numero
#     cubo <- numero*numero*numero

#     ESCREVA("Seu número ao quadrado é: ", quadrado)
#     ESCREVA("Seu número ao cubo é: ", cubo)

# FIM_ALGORITMO

# definindo as variáveis
numero=0;
quadrado=0;
cubo=0;

# loop para quando o usuario digitar um numero menor ou igual a zero
while(True):
    
    # pedindo a entrada
    numero = float(input("Digite um número maior que zero: "));

    # condição para verificar se o numero digitado é maior que zero
    if(numero<=0):
        # caso seja, exibe uma mensagem e repete o loop
        print("Escreva um numero maior que zero!");
    else:
        
        # caso seja um numero maior que zero, quebra o loop while
        break;

# calculando o quadrado e o cubo do numero digitado
quadrado = numero*numero;
cubo = numero*numero*numero;

# mostrando o resultado na tela
print(f'O quadrado de {numero} é: {quadrado}');
print(f'O cubo de {numero} é: {cubo}');