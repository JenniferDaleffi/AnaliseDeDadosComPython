# Para rodar meu programa escreva no terminal python analise.py (numero do algarismo) numeros.txt ordenados.txt
# Um exemplo para rodar o bubble sort python analise.py 1 numeros.txt ordenados.txt
# Declarei o numero do algarismo, depois o arquivo de entrada e depois o de saida

# Os testes dos algoritmos com as listas grandes estão no arquivo testes.py :D

# imports de bibliotecas que usei
import time
import sys

# função para medir o tempo de execução
def medir_tempo(funcao, arr):
    inicio = time.perf_counter()  
    resultado = funcao(arr.copy())  
    fim = time.perf_counter()  
    return resultado, fim - inicio  

# função para o algoritmo bubble sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# função para o algoritmo selection sort 
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Função para o algoritmo insertion sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# função para o algoritmo merge sort 
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# função para ler números do arquivo
def ler_arquivo(arquivo_entrada):
    with open(arquivo_entrada, 'r') as f:
        arr = list(map(int, f.readlines()))  
    return arr

# função para gravar a lista ordenada no arquivo
def gravar_arquivo(arquivo_saida, arr):
    with open(arquivo_saida, 'w') as f:
        for numero in arr:
            f.write(f"{numero}\n")  

# função main
def main():
    if len(sys.argv) != 4:
        print("Uso correto: python programa.py <algoritmo> <arquivo_entrada> <arquivo_saida>")
        sys.exit(1)

    escolha = sys.argv[1]
    arquivo_entrada = sys.argv[2]
    arquivo_saida = sys.argv[3]

    algoritmos = {
        '1': ("Bubble Sort", bubble_sort),
        '2': ("Selection Sort", selection_sort),
        '3': ("Insertion Sort", insertion_sort),
        '4': ("Merge Sort", merge_sort)
    }

    if escolha not in algoritmos:
        print("Algoritmo inválido! Escolha entre 1 (Bubble Sort), 2 (Selection Sort), 3 (Insertion Sort), 4 (Merge Sort)")
        sys.exit(1)

    nome_algoritmo, funcao_ordenacao = algoritmos[escolha]

    # ler os números do arquivo de entrada
    lista = ler_arquivo(arquivo_entrada)

    # ordenar a lista e medir o tempo
    lista_ordenada, tempo_execucao = medir_tempo(funcao_ordenacao, lista)

    # gravar a lista ordenada no arquivo da saida
    gravar_arquivo(arquivo_saida, lista_ordenada)

    print(f"Algoritmo: {nome_algoritmo}")
    print(f"Tempo de execução: {tempo_execucao:.3f} segundos")


main()





