# ALGORITMO

#     DEFINA
#         raio, pi, area real

#     pi <- 3.14

#     ESCREVA("Digite o valor do raio do circulo: ")
#     LEIA raio

#     area <- pi*raio*raio

#     ESCREVA("A area do seu circulo é: ", area)

# FIM_ALGORITMO

# importando a biblioteca math para usar o pi
import math;

# definindo as variáveis
raio=0;
area=0;

# tratando a entrada
while(True):
    
    # pedindo a entrada
    raio = float(input("Digite seu raio: "));
    
    # caso a entrada seja inválida
    if(raio<=0):
        
        # mostrando uma mensagem de erro
        print("digite uma entrada válida!");
    else:
        
        # quebrando o loop e voltando pro codigo
        break;

# calculando a area
area = math.pi*raio*raio;

# mostrando o resultado
print(f'Sua área é: {area}');