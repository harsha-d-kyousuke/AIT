import random

def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]]
    return cost

def get_neighbors(path):
    neighbors = []
    for i in range(1, len(path)):
        for j in range(i + 1, len(path)):
            neighbor = path.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing_tsp(graph):
    V = len(graph)
    current_path = list(range(V))
    random.shuffle(current_path)
    current_cost = calculate_cost(graph, current_path)

    while True:
        neighbors = get_neighbors(current_path)
        next_path = current_path
        next_cost = current_cost

        for neighbor in neighbors:
            cost = calculate_cost(graph, neighbor)
            if cost < next_cost:
                next_path = neighbor
                next_cost = cost

        if next_cost >= current_cost:
            break

        current_path = next_path
        current_cost = next_cost

    return current_path, current_cost

if __name__ == "__main__":
    graph = [[0, 12, 10, 19],
             [12, 0, 3, 7],
             [10, 3, 0, 6],
             [19, 7, 6, 0]]
    
    best_path, best_cost = hill_climbing_tsp(graph)
    print("Best path found:", best_path)
    print("Cost of path:", best_cost)
