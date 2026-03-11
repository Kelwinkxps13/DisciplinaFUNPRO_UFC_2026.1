# ALGORITMO

#     DEFINA
#         nota1,nota2,nota3,media real

#     ESCREVA("Digite a nota1: )
#     LEIA nota1
#     ESCREVA("Digite a nota2: ")
#     LEIA nota2
#     ESCREVA("Digite a nota3: ")
#     LEIA nota3

#     media <- (nota1+nota2+nota3)/3

#     ESCREVA ("A média é: ", media)

# FIM_ALGORITMO

# definindo as variáveis
nota1=0;
nota2=0;
nota3=0;
media=0;

# tratando as entradas
while(True):
    
    # pedindo a entrada
    nota1 = float(input("Digite a nota1: "));
    nota2 = float(input("Digite a nota2: "));
    nota3 = float(input("Digite a nota3: "));
    
    # testando condicoes de inexistencia
    if(nota1<0 or nota2<0 or nota3<0 or nota1>10 or nota2>10 or nota3>10):
        
        # caso a condição seja atendida
        print("alguma entrada esta invalida!");
    else:
        
        # quebra e continua o codigo (sai do loop while)
        break;

# calculando a media
media = (nota1+nota2+nota3)/3;

# mostrando na tela o resultado
print(f'a média é: {media}');