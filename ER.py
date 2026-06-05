import networkx as nx

# параметры задачи
n = 40
p = 0.45

# генерация графа Эрдёша–Реньи
G = nx.erdos_renyi_graph(n, p)

# вычисление средней степени вершины (эмпирически)
total_degree = 0
for node in G.nodes():
    total_degree += G.degree(node)

avg_degree_empirical = total_degree / len(G.nodes())

# теоретическая средняя степень
avg_degree_theoretical = (n - 1) * p

# вывод результатов
print("Средняя степень (эмпирическая):", avg_degree_empirical)
print("Средняя степень (теоретическая):", avg_degree_theoretical)
print("Разница:", abs(avg_degree_empirical - avg_degree_theoretical))