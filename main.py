import utility as utility
import loader as loader
import numpy as np


def main():

    # Paths to the data and solution files.
    vrp_file = "data/n32-k5.vrp"  # "data/n80-k10.vrp"
    sol_file = "data/n32-k5.sol"  # "data/n80-k10.sol"

    # Loading the VRP data file.
    px, py, demand, capacity, depot = loader.load_data(vrp_file)

    # Displaying to console the distance and visualizing the optimal VRP solution.
    vrp_best_sol = loader.load_solution(sol_file)
    best_distance = utility.calculate_total_distance(vrp_best_sol, px, py, depot)
    print("Best VRP Distance:", best_distance)
    utility.visualise_solution(vrp_best_sol, px, py, depot, "Optimal Solution")

    # Executing and visualizing the nearest neighbour VRP heuristic.
    # Uncomment it to do your assignment!

    nnh_solution = nearest_neighbour_heuristic(px, py, demand, capacity, depot)
    nnh_distance = utility.calculate_total_distance(nnh_solution, px, py, depot)
    print("Nearest Neighbour VRP Heuristic Distance:", nnh_distance)
    utility.visualise_solution(nnh_solution, px, py, depot, "Nearest Neighbour Heuristic")

    # Executing and visualizing the saving VRP heuristic.
    # Uncomment it to do your assignment!

    # sh_solution = savings_heuristic(px, py, demand, capacity, depot)
    # sh_distance = utility.calculate_total_distance(sh_solution, px, py, depot)
    # print("Saving VRP Heuristic Distance:", sh_distance)
    # utility.visualise_solution(sh_solution, px, py, depot, "Savings Heuristic")

#Returns a list of routes that visits each node, nodes are represented by their index and are referred to as such
def nearest_neighbour_heuristic(px, py, demand, capacity, depot):
    """
    Algorithm for the nearest neighbour heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """
    routes = []
    visitedIndexes = []
    visitedIndexes.append(depot)
    while len(visitedIndexes) < len(px):
        capacityUsed = 0
        route = []
        route.append(depot)
        while 1==1:
            sortedUnvisitedIndexes = sort_unvisited_by_distance(px, py, visitedIndexes, route[-1])
            found = False
            for i in sortedUnvisitedIndexes:
                if(capacityUsed + demand[i] <= capacity):
                    capacityUsed += demand[i]
                    visitedIndexes.append(i)
                    route.append(i)
                    found = True
                    break
            if(not found):
                del route[0] #remove depot to match .sol format
                routes.append(route)
                break
    return routes

#Returns a list of indexes sorted by their distances from the current node
def sort_unvisited_by_distance(px, py, visited, current):
    indexes = []
    distances = []
    for n in range(len(px)):
        if(n not in visited):
            indexes.append(n)
            distances.append(utility.calculate_euclidean_distance(px, py, n, current))
    return [indexes for _, indexes in sorted(zip(distances, indexes))]

def savings_heuristic(px, py, demand, capacity, depot):

    """
    Algorithm for Implementing the savings heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """
    routes = []
    #initial routes everything but (depot,depot,depot)
    for(n in range(1, len(px))):
        route = []
        route.append(0)
        route.append(n)
        route.append(0)
        routes.append(route)
    #calculate route merge savings
    savings = [[0] * (len(routes)-1) for i in range(len(routes))]
    for(i in range(len(routes))):
        for(j in range(len(routes))):
            if(i is not j):


    return None

def compute_savings(px, py, node1, node2):
    return ((utility.calculate_euclidean_distance(px,py,node1,1)
    + utility.calculate_euclidean_distance(px,py,1,node2))
    - utility.calculate_euclidean_distance(px,py,node1,node2))

if __name__ == '__main__':
    main()
