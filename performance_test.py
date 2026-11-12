
import time
import random
import csv
import os
import matplotlib.pyplot as plt

from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import build_graph, dijkstra
from algorithms.tsp import nearest_neighbor_tsp


random.seed(42)

# Dataset sizes
sizes = [10, 50, 100, 250, 500]

results = []


# Measure average execution time
def measure_time(function, repetitions=3):

    total_time = 0

    for _ in range(repetitions):

        start = time.perf_counter()

        function()

        end = time.perf_counter()

        total_time += end - start

    return total_time / repetitions


# Generate sample parcels
def generate_parcels(n):

    return [
        {
            "id": f"P{i}",
            "weight": random.randint(1, 10),
            "priority": random.randint(1, 100),
            "deadline": "12:00"
        }
        for i in range(n)
    ]


# Generate a connected road graph
def generate_graph(n):

    roads = []

    nodes = ["W"] + [f"L{i}" for i in range(1, n)]

    # Connect consecutive locations
    for i in range(n - 1):

        roads.append(
            (nodes[i], nodes[i + 1],
             random.randint(1, 10))
        )

    # Add additional roads
    for i in range(n - 2):

        roads.append(
            (nodes[i], nodes[i + 2],
             random.randint(1, 10))
        )

    return build_graph(roads), nodes


# Run performance tests
for n in sizes:

    print(f"\nTesting dataset size: {n}")

    parcels = generate_parcels(n)

    graph, nodes = generate_graph(n)

    # 1. Merge Sort
    sorting_time = measure_time(
        lambda: merge_sort(parcels)
    )

    results.append(
        ["Merge Sort", n, sorting_time]
    )

    # 2. Knapsack
    knapsack_time = measure_time(
        lambda: knapsack(parcels, 100)
    )

    results.append(
        ["Knapsack", n, knapsack_time]
    )

    # 3. Dijkstra
    dijkstra_time = measure_time(
        lambda: dijkstra(graph, "W")
    )

    results.append(
        ["Dijkstra", n, dijkstra_time]
    )

    # 4. Nearest Neighbor TSP
    # Limit route destinations to keep tests practical
    destinations = nodes[1:]

    tsp_time = measure_time(
        lambda: nearest_neighbor_tsp(
            graph, "W", destinations
        )
    )

    results.append(
        ["Nearest Neighbor TSP", n, tsp_time]
    )

    print("Merge Sort:", sorting_time)
    print("Knapsack:", knapsack_time)
    print("Dijkstra:", dijkstra_time)
    print("TSP:", tsp_time)


# Save results in CSV
os.makedirs("results", exist_ok=True)

with open("results/runtime_results.csv",
          "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(
        ["Algorithm", "Input Size", "Execution Time (seconds)"]
    )

    writer.writerows(results)


# Generate individual runtime charts
algorithms = [
    "Merge Sort",
    "Knapsack",
    "Dijkstra",
    "Nearest Neighbor TSP"
]

for algorithm in algorithms:

    data = [
        row for row in results
        if row[0] == algorithm
    ]

    x = [row[1] for row in data]
    y = [row[2] for row in data]

    plt.figure()

    plt.plot(x, y, marker="o")

    plt.title(f"{algorithm} Runtime Analysis")

    plt.xlabel("Input Size")

    plt.ylabel("Execution Time (seconds)")

    plt.grid(True)

    filename = algorithm.lower().replace(" ", "_")

    plt.savefig(
        f"results/{filename}_runtime.png"
    )

    plt.close()


print("\n================================")
print("PERFORMANCE TESTING COMPLETED")
print("================================")

print("CSV saved: results/runtime_results.csv")
print("Runtime charts saved in results/")
