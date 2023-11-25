
def criar_matriz():
    matriz = []
    for i in range(3):
        linha = []
        for j in range(3):
            elemento = int(input(f"Digite o elemento da posição ({i + 1}, {j + 1}): "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def multiplicar_diagonal_principal(matriz, k):
    for i in range(3):
        matriz[i][i] *= k

def imprimir_matriz(matriz, mensagem):
    print(mensagem)
    for linha in matriz:
        print(linha)

matriz_original = criar_matriz()

k = int(input("Digite o valor de k para multiplicar os elementos da diagonal principal: "))

multiplicar_diagonal_principal(matriz_original, k)


imprimir_matriz(matriz_original, "Matriz Original:")
imprimir_matriz(matriz_original, f"Matriz Após Multiplicação da Diagonal Principal por {k}:")