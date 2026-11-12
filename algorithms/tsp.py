
from algorithms.dijkstra import dijkstra, get_path


def nearest_neighbor_tsp(graph, start, destinations):

    unvisited = set(destinations)
    unvisited.discard(start)

    current = start

    route_order = [start]
    full_path = [start]

    total_distance = 0

    while unvisited:

        # Calculate shortest distances from current location
        distances, previous = dijkstra(graph, current)

        # Find nearest unvisited customer
        next_location = min(
            unvisited,
            key=lambda node: distances[node]
        )

        # Add shortest distance
        total_distance += distances[next_location]

        # Reconstruct shortest path
        path = get_path(previous, next_location)

        full_path.extend(path[1:])

        # Update current location
        current = next_location

        route_order.append(current)
        unvisited.remove(current)

    # Return to warehouse
    distances, previous = dijkstra(graph, current)

    return_distance = distances[start]

    return_path = get_path(previous, start)

    total_distance += return_distance

    full_path.extend(return_path[1:])

    route_order.append(start)

    return route_order, full_path, total_distance
