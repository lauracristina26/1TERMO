# Projeto Cancela Automatica 
# Criar um algoritmo para que:

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.

# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código

print("Bem-vindo ao Estacionamento do Shopping!")
entrada = input("Qual a placa do carro?")
tempo = float(input("Digite por quanto tempo o carro permaneceu no estacionamento: "))
valor = 5 
formaacesso = input("Escolha uma forma de acesso: ")

if formaacesso == "Ticket":
    print("Aperte o botão para emitir o seu Ticket!")
    total = valor * tempo
    print("O valor cobrado é de:", total)
    print("Devolva o ticket com o pagamento na portaria do estacionamento. Pagamento em dinheiro, utilize o interfone.")
if formaacesso == "TAG":
    total = valor * tempo
    print("O valor cobrado é de:", total)
    print("Acesso liberado! O valor será cobrado na folha de pagamento!")
if formaacesso == "Interfone":
    print("Caso ocorra algum erro, ligue o interfone, o atendimento completo irá ser feito pelo interfone.")
else:
    print("Agradecemos por ter escolhido nossos serviços e volte sempre!")


relatoriosaida = input("Deseja receber o relatório do processo?")
if relatoriosaida == "Sim":
    print(f"Placa do carro {entrada}; Tempo de permanência {tempo}; Forma de acesso {formaacesso}; Valor pago {total}.")
elif relatoriosaida == "Não":
    print("Volte sempre!")
else: 
    print("Obrigada por confiar e escolher nossos serviços!")