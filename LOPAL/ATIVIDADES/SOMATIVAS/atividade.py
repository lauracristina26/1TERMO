# 8. Ano de Nascimento: Peça o ano atual e a idade do aluno. Calcule e exiba o ano em que ele nasceu.

ano1 = int(input("Digite o ano atual:"))
idade = int(input("Digite a idade do aluno:"))
total = ano1 - idade
print("O aluno nasceu em", total)

# 9. Filtro de Idade (TikTok): Peça a idade do usuário. Se for menor que 13, exiba "Acesso restrito". Se tiver entre 13 e 17, "Acesso moderado". Se for 18 ou mais, "Acesso liberado".

idade = int(input("Digite a idade do usuário: "))
if idade <= 13:
    print("Acesso restrito")
elif 13 < idade < 17:
    print("Acesso moderado")
elif idade >= 18:
    print("Acesso liberado")

# 10.Bateria do Celular: Crie um while que começa com a bateria em 100. A cada repetição, subtraia 10 e mostre: "Bateria em [valor]%". O loop para quando chegar em 10 e exibe: "Por favor, conecte o carregador!".

valor = 100
while valor <= 100:
        print(f"Bateria em {valor-10}%")
        valor += 10
        break
print("Por favor, conecte o carregador!")

# 11.Contagem de Curtidas: Use um for para simular a contagem de curtidas em uma foto. Peça ao usuário o limite de curtidas (ex: 5). O programa deve contar de 1 até esse número, printando: "Curtida no [i] recebida!".

for curtida in range(1,6):
   print(f"Curtida no {curtida} recebida")

# 12.Carrinho de Compras Online: Use um while para pedir nomes de produtos que o aluno quer comprar. O loop só para quando ele digitar "sair". No final, mostre quantas vezes ele adiciona itens ao carrinho (use um contador).

produtos = ["farinha","feijão","arroz","alface","milho"]

input("Digite o produto desejado:")
for item in produtos:
    if item == produtos:
        print(f"O {item} produto foi colocado no carrinho")
    print("Fim da escolha no carinho de compras")