 # Programa que armazena os nomes e idades de 10 pessoas em uma matriz,
  # e imprime o nome da pessoa mais nova.

matriz_pessoas = []

for _ in range(10):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    matriz_pessoas.append([nome, idade])

pessoa_mais_nova = min(matriz_pessoas, key=lambda x: x[1])

print(f"\nA pessoa mais nova é: {pessoa_mais_nova[0]} com {pessoa_mais_nova[1]} anos.")