quebrar_loop = False #variável para quebra do loop principal

while not quebrar_loop : #loop responsável pelo funcionamento contínuo do programa
    nome = input("Insira o nome do aluno:")
    for i in range(1): # Pega o nome, calcula a média e imprime
        nota = list(map(float, input("Insira suas quatro  notas, separadas por espaço: ").split()))
        media = sum(nota)/ len(nota)
        print(f"O aluno {nome} tem como média: {media}")
        
        if media < 6:
            print('Sua média não foi o suficiente, você foi reprovado.')
        else:
            print("Sua média foi maior que 6, parabéns você foi aprovado!")
        
       
    quebrador_Loop_MaisALuno = False       
    while not quebrador_Loop_MaisALuno: #Loop para inserção contínua de mais um aluno
            maisAluno =  input('Deseja inserir mais um aluno e suas respectivas notas? ')
            if maisAluno == "sim":
               quebrador_Loop_MaisALuno = False
            else:
                break
                
            nome2 = input("Insira o nome do outro aluno: ")
            nota2 = list(map(float, input("Insira suas quatro  notas, separadas por espaço: ").split()))
            media2 = sum(nota2)/ len(nota2)
            print(f"O aluno {nome2} tem como média: {media2}")
        
            if media2 < 6:
                print('Sua média não foi o suficiente, você foi reprovado.')
            else:
                print("Sua média foi maior que 6, parabéns você foi aprovado!")                   
            
    quebrador_Loop_Encerramento = False
            
    while not quebrador_Loop_Encerramento: #Loop para encerramento ou continuação  do programa
        encerrar_prog = input("Deseja encerrar o programa? (sim/não) ")
        if encerrar_prog.lower() == "sim":  
            quebrar_loop = True
            quebrador_Loop_Encerramento = True
            break
        elif encerrar_prog.lower() == "não":
             quebrador_Loop_Encerramento = True
        else:
            print("Opção inválida. Digite 'sim' ou 'não'. ")
            continue
        