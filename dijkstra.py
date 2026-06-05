import heapq
import math


def dijkstra(graph, start):
    """
    graph: dict, где ключ — вершина,
           значение — список (сосед, вес)
    start: начальная вершина
    """

    # расстояния до всех вершин
    distances = {vertex: math.inf for vertex in graph}
    distances[start] = 0

    # очередь приоритетов (расстояние, вершина)
    pq = [(0, start)]

    # для восстановления пути (по желанию)
    previous = {vertex: None for vertex in graph}

    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        # если нашли более короткий путь — пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # проверяем соседей
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # если нашли лучший путь
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    return distances, previous


def get_path(previous, start, end):
    """Восстановление пути от start до end"""
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == start:
        return path
    return []


# ---------------------------
# Пример графа (список смежности)
# ---------------------------
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

start_vertex = 'A'

distances, previous = dijkstra(graph, start_vertex)

print("Кратчайшие расстояния:")
for v, d in distances.items():
    print(f"{start_vertex} → {v} = {d}")

print("\nПример пути A → D:", get_path(previous, 'A', 'D'))