# ALGORITMO

#     DEFINA
#         nome, matricula, curso, email literal
#         idade inteiro

#     ESCREVA ("Digite o nome do aluno: ")
#     LEIA nome
#     ESCREVA ("Digite a matricula do aluno: ")
#     LEIA matricula
#     ESCREVA ("Escreva o curso do aluno: ")
#     LEIA curso
#     ESCREVA ("Digite a idade do aluno: ")
#     LEIA idade
#     ESCREVA ("Escreva o email do aluno: ")
#     LEIA email

#     ESCREVA ("O nome do aluno é: ", nome)
#     ESCREVA ("A matricula do aluno é: ", matricula)
#     ESCREVA ("O curso do aluno é: ", curso)
#     ESCREVA ("A idade do aluno é: ", idade)
#     ESCREVA ("O email do aluno é: ", email)

# FIM_ALGORITMO

# definindo as variáveis
nome=0;
matricula=0;
curso=0;
email=0;
idade=0;

# pedindo a entrada
nome = input("Digite o nome do aluno: ");
matricula = input("Digite a matricula do aluno: ");
curso = input("Escreva o curso do aluno: ");
email = input("Escreva o email do aluno: ");

# tratando a idade
while(True):
    
    # pedindo uma entrada de idade
    idade = int(input("Digite a idade do aluno: "));
    
    # condição de inexistência
    if(idade<=0 or idade>=150):
        
        #mensagem de erro caso a condição seja atendida
        print("idade Inválida!");
    else:
        
        # caso a condição retorne falso, a idade atende os requisitos, e o codigo continua
        break;
    

# mostrando na tela os resultados
print("O nome do aluno é: ", nome);
print("A matricula do aluno é: ", matricula);
print("O curso do aluno é: ", curso);
print("A idade do aluno é: ", idade);
print("O email do aluno é: ", email);