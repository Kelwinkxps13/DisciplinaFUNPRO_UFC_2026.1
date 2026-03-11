# ALGORITMO

#     DEFINA
#         salario, pct_aumento, aumento, sal_aumentado real

#     ESCREVA("Digite o salario: ")
#     LEIA salario
#     ESCREVA("Digite o aumento em porcentagem: ")
#     LEIA pct_aumento

#     aumento <- (salario*pct_aumento)/100
#     sal_aumentado <- salario + aumento

#     ESCREVA("O aumento sera: ", aumento)
#     ESCREVA("E o salario com aumento sera: ", sal_aumentado)

# FIM_ALGORITMO

# definindo as variáveis
salario=0;
pct_aumento=0;
aumento=0;
sal_aumentado=0;

# tratando as entradas
while(True):
    
    # pedindo a entrada
    salario = float(input("Digite o salário: "));
    pct_aumento = float(input("Digite o aumento em porcentagem: "));
    
    # condicao de inexistência
    if(salario<=0 or pct_aumento<=0):
        
        # mostrando a mensagem de erro
        print("Alguma entrada esta invalida!");
    else:
        
        # saindo do loop
        break;

#calculando a porcentagem de aumento
aumento = (salario*pct_aumento)/100;

#calcula o salario acrescido da porcentagem de aumento
sal_aumentado = salario+aumento;

#exibindo os resultados na tela
print(f'O aumento será: {aumento}');
print(f'E o salário aumentado será: {sal_aumentado}');