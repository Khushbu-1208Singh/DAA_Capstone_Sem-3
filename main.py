import json

from algorithms.sorting import merge_sort
from algorithms.knapsack import knapsack
from algorithms.dijkstra import build_graph, dijkstra, get_path
from algorithms.tsp import nearest_neighbor_tsp

# Load parcel data
with open("data/parcels.json", "r") as file:
    parcel_data = json.load(file)

# Load location data
with open("data/locations.json", "r") as file:
    location_data = json.load(file)

# Load road network
with open("data/road_network.json", "r") as file:
    road_data = json.load(file)


print("================================")
print("     MINI COURIER PLANNER       ")
print("================================")

print("\nVehicle Capacity:",
      parcel_data["vehicle_capacity"], "kg")

print("\nTotal Parcels:",
      len(parcel_data["parcels"]))

print("\nDelivery Locations:",
      location_data["locations"])

print("\nTotal Roads:",
      len(road_data["roads"]))

print("\nProject setup successful!")

# Sort parcels by priority
sorted_parcels = merge_sort(parcel_data["parcels"])

print("\nPARCELS SORTED BY PRIORITY")

for parcel in sorted_parcels:
    print(
        parcel["id"],
        "Priority:", parcel["priority"],
        "Weight:", parcel["weight"], "kg"
    )

# Knapsack optimization
capacity = parcel_data["vehicle_capacity"]

selected_parcels, dp = knapsack(
    parcel_data["parcels"],
    capacity
)

print("\nOPTIMAL PACKING PLAN")

total_weight = sum(
    parcel["weight"] for parcel in selected_parcels
)

total_priority = sum(
    parcel["priority"] for parcel in selected_parcels
)

for parcel in selected_parcels:
    print(
        parcel["id"],
        "Weight:", parcel["weight"], "kg",
        "Priority:", parcel["priority"]
    )

print("\nTotal Weight:", total_weight, "kg")
print("Vehicle Capacity:", capacity, "kg")
print("Total Priority Score:", total_priority)


# Build delivery graph
graph = build_graph(road_data["roads"])

# Find shortest paths from warehouse
distances, previous = dijkstra(graph, "W")

print("\nDIJKSTRA SHORTEST PATHS")

for location in location_data["locations"]:

    path = get_path(previous, location)

    print(
        "W ->", location,
        "| Path:", " -> ".join(path),
        "| Distance:", distances[location], "km"
    )


# Get destinations of selected parcels
delivery_destinations = list(dict.fromkeys(
    parcel["destination"] for parcel in selected_parcels
))

# Generate optimized delivery route
route_order, full_path, total_distance = nearest_neighbor_tsp(
    graph,
    "W",
    delivery_destinations
)

print("\nNEAREST NEIGHBOR DELIVERY ROUTE")

print("Delivery Stops:", " -> ".join(route_order))

print("Actual Road Path:", " -> ".join(full_path))

print("Total Route Distance:", total_distance, "km")
