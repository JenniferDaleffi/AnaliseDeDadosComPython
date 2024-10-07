# Aqui é o arquivo dos testes dos algarismos com as listas

# O arquivo analise.py é para a análise e ordenação dos numeros do arquivo de entrada numeros.txt


# Imports das bibliotecas que usei
import matplotlib.pyplot as plt 
import random
import time

# Função para medir o tempo de execução
def medir_tempo(funcao, arr):
    inicio = time.perf_counter()  
    resultado = funcao(arr.copy())  
    fim = time.perf_counter()  
    return resultado, fim - inicio  

# Função para o algoritmo bubble sort 
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Função para o algoritmo selection sort 
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Função para o algoritmo inserction sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Função para o algoritmo merge sort 
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

# Função pra testar os algoritmos em listas grandes
def testar_algoritmos():
    algoritmos = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort
    }

    tamanhos_padrao = [10000, 100000, 500000, 1000000, 5000000]  # Tamanhos das listas
    resultados = {}
    for alg in algoritmos:
        resultados[alg] = []


    for nome_algoritmo, funcao_ordenacao in algoritmos.items():
        print(f"Testando {nome_algoritmo}...")

        # Condição pra ver se o algoritmo é quadrático e limitar os tamanhos da lista para tamanhos menores
        if nome_algoritmo in ["Bubble Sort", "Selection Sort", "Insertion Sort"]:
            tamanhos = [10000]  
        else:
            tamanhos = tamanhos_padrao  
        
        for tamanho in tamanhos:
            tempo_total = 0
            for _ in range(3):
                lista_aleatoria = []
                for i in range(tamanho):
                    lista_aleatoria.append(random.randint(0, 1000000))

                tempo_total += medir_tempo(funcao_ordenacao, lista_aleatoria)[1]

            media_tempo = tempo_total / 3
            resultados[nome_algoritmo].append(media_tempo)

            print(f"{nome_algoritmo} - Tamanho {tamanho}: Média de {media_tempo:.3f} segundos")
    
    return resultados



testar_algoritmos()

# Resultados dos tempos obtidos
resultados = {
    "Bubble Sort": [4.6],  
    "Selection Sort": [2.8],
    "Insertion Sort": [2.6],
    "Merge Sort": [0.02, 0.27, 1.6, 3.5, 21.3]  
}

tamanhos_lista = [10000, 100000, 500000, 1000000, 5000000]

for algoritmo, tempos in resultados.items():
    if len(tempos) == 1:
        plt.plot([10000], tempos, label=algoritmo, marker='o')
    else:
        plt.plot(tamanhos_lista, tempos, label=algoritmo, marker='o')

plt.xlabel("Tamanho da Lista")
plt.ylabel("Tempo Médio (s)")
plt.title("Comparação de Algoritmos de Ordenação")
plt.legend()
plt.grid(True)
plt.show()