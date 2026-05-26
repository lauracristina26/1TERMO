# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

print("Bem-vindo ao Elevador de Prédio!")
elevador = input("Aperte o botão para iniciar o elevador!")
andaratual = 0 

while True: 
    try:
        elevador1 = int(input("Digite o andar desejado (0-10): "))
        if elevador1 < 0 or elevador1 > 10: 
            raise ValueError("Andar inválido. Por favor, digite um número entre 0 a 10 para garantir o funcionamento do elevador!")
        print(f"Elevador em funcionamento, mudando {andaratual} para o andar desejado {elevador1}")
        andaratual = elevador1
        print(f"Chegamos ao seu andar {elevador1}!")
        capacidade1 = int(input("Digite quantas pessoas estão no elevador:"))
        if capacidade1 < 0 or capacidade1 > 5: 
            raise ValueError("Número inválido. Por favor, respeite a capacidade do Elevador para o seu funcionamento!")
        print(f"Elevador em funcionamento, mudando {andaratual} para o andar desejado {elevador1}, com {capacidade1} pessoas")
        andaratual = capacidade1 
        print(f"Chegamos ao seu andar {elevador1} com {capacidade1} de pessoas!")
        break
             
    except ValueError:
        print("Erro: Número Inválido: Por Favor, digite um número que não comprometa o funcionamento do Elevador!")
    