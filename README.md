# 🧠 Análise de Algoritmos de Ordenação

## Introdução

Este projeto tem como objetivo manipular e analisar dados através de algoritmos de ordenação. Serão testados diferentes algoritmos em listas de diferentes tamanhos, capturando os tempos de execução e construindo gráficos comparativos das médias dos tempos.

<p align="center">
  <a href="https://icons8.com.br/icons/set/python">
    <img src="https://img.icons8.com/?size=100&id=13441&format=png&color=000000" />
  </a>
</p>

## Descrição dos Algoritmos

- **Bubble Sort**: Método de ordenação simples e prático, mas ineficiente para listas grandes devido à sua complexidade O(n²).

- **Selection Sort**: Este método encontra o menor elemento e o coloca na primeira posição, repetindo o processo para o restante da lista. Também tem complexidade O(n²), tornando-se ineficaz para listas maiores.

- **Insertion Sort**: Eficiente para listas pequenas ou quase ordenadas, este algoritmo insere um elemento de cada vez na posição correta. Sua complexidade é O(n²), mas funciona bem em casos específicos.

- **Merge Sort**: Um algoritmo de ordenação eficiente que divide a lista em subsequências até que cada subsequência contenha apenas um item, e então combina essas subsequências. Possui complexidade O(n log n), sendo muito mais eficiente em listas grandes.

## Tabela de Tempos de Execução

| Algoritmo      | Tamanho 10.000 | Tamanho 100.000 | Tamanho 500.000 | Tamanho 1.000.000 | Tamanho 5.000.000 |
|----------------|-----------------|------------------|------------------|--------------------|--------------------|
| **Bubble Sort** | 4.610s          | x                | x                | x                  | x                  |
| **Selection Sort** | 2.036s       | x                | x                | x                  | x                  |
| **Insertion Sort** | 2.086s       | x                | x                | x                  | x                  |
| **Merge Sort**   | 0.022s         | 0.277s           | 1.685s           | 3.591s             | 21.326s            |

## Discussão dos Resultados

Os resultados demonstraram que o algoritmo **Merge Sort** se mostrou significativamente mais eficiente do que os outros algoritmos em listas maiores, variando de 50.000 a 500.000 elementos.

Os métodos **Bubble Sort**, **Insertion Sort** e **Selection Sort** mostraram-se ineficazes em listas grandes, sendo mais adequados para listas menores devido à sua complexidade computacional.

O **Merge Sort**, por sua natureza de dividir o problema em partes menores, demonstrou uma eficiência notável ao resolver cada parte individualmente e, em seguida, combinar os resultados.
