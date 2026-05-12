# Lógica de Programação com Python 🐍

Este guia aborda os fundamentos da lógica de programação, desde a captura de dados até estruturas de repetição e boas práticas de desenvolvimento.

---

## 1. Entrada, Saída e Tipos de Dados
Para interagir com o usuário e processar informações, utilizamos funções de entrada/saída e conversão de tipos.

- `print()`: Exibe informações no console.
- `input()`: Captura dados digitados pelo usuário (sempre retorna uma *string*).
- `int()`: Converte um valor para número inteiro.
- `float()`: Converte um valor para número decimal.

**Exemplo:**
```python
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura (ex: 1.75): "))

print(f"Olá {nome}, você tem {idade} anos.")
```

---

## 2. Estruturas Condicionais (`if`, `elif`, `else`)
Utilizadas para a tomada de decisão no código baseada em condições lógicas.

```python
nota = float(input("Digite a nota final: "))

if nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")
```

---

## 3. Estruturas de Repetição e Controle
Servem para executar um bloco de código várias vezes.

### `while`
Executa enquanto uma condição for verdadeira. Útil quando não sabemos exatamente quantas vezes o código deve rodar.
```python
contador = 0
while contador < 5:
    print(f"Contagem: {contador}")
    contador += 1
```

### `for`
Utilizado para percorrer sequências (como listas ou intervalos).
```python
for i in range(1, 6):
    print(f"Número {i}")
```

### `break` e `import time`
- `break`: Interrompe o loop imediatamente.
- `import time`: Biblioteca para manipulação de tempo (ex: pausas).

```python
import time

while True:
    print("Processando...")
    time.sleep(1) # Pausa de 1 segundo
    break # Sai do loop infinito
```

---

## 4. Clean Code (Código Limpo)
Escrever código que humanos consigam entender, não apenas máquinas.

- **Nomes Significativos:** Use `soma_total` em vez de `s`.
- **Funções Pequenas:** Cada função deve fazer apenas uma coisa.
- **Comentários Necessários:** Comente o "porquê", não o "o quê".
- **DRY (Don't Repeat Yourself):** Evite repetição de código.

---

## 5. Versionamento com GitHub
O GitHub é a plataforma para hospedar seus repositórios e colaborar com outros desenvolvedores.

**Comandos essenciais do Git:**
1. `git init`: Inicia um repositório local.
2. `git add .`: Prepara os arquivos para o salvamento.
3. `git commit -m "mensagem"`: Salva as alterações com uma descrição.
4. `git push`: Envia as alterações para o GitHub.
