
import heapq


def build_graph(roads):

    graph = {}

    for source, destination, distance in roads:

        if source not in graph:
            graph[source] = {}

        if destination not in graph:
            graph[destination] = {}

        # Undirected graph
        graph[source][destination] = distance
        graph[destination][source] = distance

    return graph


def dijkstra(graph, start):

    # Initialize distances
    distances = {
        node: float("inf") for node in graph
    }

    previous = {
        node: None for node in graph
    }

    distances[start] = 0

    # Priority queue
    pq = [(0, start)]

    while pq:

        current_distance, current_node = heapq.heappop(pq)

        # Ignore outdated entries
        if current_distance > distances[current_node]:
            continue

        # Visit neighbors
        for neighbor, weight in graph[current_node].items():

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:

                distances[neighbor] = new_distance
                previous[neighbor] = current_node

                heapq.heappush(
                    pq, (new_distance, neighbor)
                )

    return distances, previous


def get_path(previous, destination):

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    return path[::-1]