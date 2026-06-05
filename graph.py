import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
n = 50
G.add_nodes_from(range(n))

# -------------------------
# 1. Левая слабая цепь (0–14)
# -------------------------
for i in range(0, 14):
    G.add_edge(i, i + 1)

# -------------------------
# 2. ЯМА (15–24): почти изолированная цепь
# -------------------------
for i in range(15, 24):
    G.add_edge(i, i + 1)

# слабое соединение с остальной частью
G.add_edge(14, 15)

# -------------------------
# 3. ГОРБ (25–34): ПОЛНЫЙ ГРАФ (clique)
# -------------------------
for i in range(25, 35):
    for j in range(25, 35):
        if i != j:
            G.add_edge(i, j)

# соединяем ядро с окружением
G.add_edge(24, 25)
G.add_edge(34, 35)

# -------------------------
# 4. Правая слабая цепь (35–49)
# -------------------------
for i in range(35, 49):
    G.add_edge(i, i + 1)

# -------------------------
# Eigenvector centrality
# -------------------------
centrality = nx.eigenvector_centrality(G, max_iter=5000)

values = [centrality[i] for i in range(n)]

print(values)

plt.plot(range(n), values, marker='o')
plt.title("Deterministic eigenvector centrality shape")
plt.xlabel("Node")
plt.ylabel("Centrality")
plt.grid(True)
plt.show()