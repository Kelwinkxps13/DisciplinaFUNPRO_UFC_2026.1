# ALGORITMO

#     DEFINA
#         nota1,nota2,media,peso1,peso2 real

#     ESCREVA("Digite sua nota1: ")
#     LEIA nota1
#     ESCREVA("Digite seu peso da nota1: ")
#     LEIA peso1
#     ESCREVA("Digite sua nota2: ")
#     LEIA nota2
#     ESCREVA("Digite sua peso da nota2: ")
#     LEIA peso2

#     media <- (peso1*nota1 + peso2*nota2)/(peso1+peso2)

#     ESCREVA("Sua média ponderada é: ", media)

# FIM_ALGORITMO

# definindo as variáveis
nota1=0;
nota2=0;
media=0;
peso1=0;
peso2=0;


# tratando as entradas
while(True):
    
    # pedindo a entrada
    nota1 = float(input("Digite sua nota1: "));
    peso1 = float(input("Digite seu peso da nota1: "));
    nota2 = float(input("Digite sua nota2: "));
    peso2 = float(input("Digite seu peso da nota2: "));
    
    # testando condicoes de inexistencia
    if(nota1<0 or nota2<0 or peso1<0 or peso2<0 or nota1>10 or nota2>10):
        
        # caso a condição seja atendida
        print("alguma entrada esta invalida!");
    else:
        
        # quebra e continua o codigo (sai do loop while)
        break;



# calculando a mnedia com pesos
media = (peso1*nota1 + peso2*nota2)/(peso1+peso2);

# mostrando na tela o resultado
print(f'Sua média ponderada é: {media}');