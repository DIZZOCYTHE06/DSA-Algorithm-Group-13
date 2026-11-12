import sys
import heapq

def dijkstra(graph, src, dest):
    inf = sys.maxsize 
    distance = {i : inf for i in graph} # distance between nodes
    predecessor = {j : [] for j in graph} # list of predecessors
    distance[src] = 0 # distance to the source node is 0
    predecessor[src] = [src]

    visited = set() #Note used set instead of [] because it is much faster with larger amounts of data
    min_heap = [(0, src)]

    while min_heap:
        dist, temp = heapq.heappop(min_heap)
        if temp in visited:
            continue   # skips loop if in visited
        visited.add(temp)

        if temp == dest:
            break # ends loop since distancee will just be 0

        for j, w in graph[temp].items():
            if j not in visited:
                cost = dist + w
                if cost < distance[j]:
                    distance[j] = cost
                    predecessor[j] = predecessor[temp] + [j]
                    heapq.heappush(min_heap,  (cost, j))

    print("Shortest Distance:", distance[dest])
    print("Shortest path:", " -> ".join(predecessor[dest]))

def validate_graph(graph):
    for node, neighbours in graph.items():
        for n in neighbours:
            if n not in graph:
                print(f"Problem: '{n}' (listed under '{node}') is not a node in the graph")

def show_locations(graph): #checks if neighbours are nodes in the graph
    print("\nAvailable locations:")
    print("--------------------")

    for location in sorted(graph.keys()):
        print(location.title())

    print("--------------------")
        


graph = {
    'ginnery' : {'victoria avenue': 4, 'limbe' : 6},
    'limbe' : {'ginnery' : 6, 'zomba' : 62},
    'victoria avenue' : {'ginnery' : 4, 'zalewa' : 54},
    'zalewa' : {'victoria avenue' : 54, 'ntcheu': 98, 'balaka' : 90},
    'balaka' : {'zalewa' : 90, 'ntcheu' : 42, 'liwonde' : 33, 'monkeybay': 147},
    'zomba' : {'limbe' : 62, 'liwonde' : 51},
    'liwonde' : {'zomba' : 51, 'balaka' : 33, 'monkeybay' : 136},
    'monkeybay' : {'liwonde' : 136, 'balaka' : 147, 'salima' : 133},
    'ntcheu' : {'zalewa' : 98, 'balaka' : 42, 'dedza' : 73},
    'dedza' : {'ntcheu' : 73, 'gateway' : 90},
    'gateway' : {'dedza' : 90, 'area 49' : 6},
    'area 49' : {'gateway' : 6, 'dowa' : 48},
    'dowa' : {'area 49' : 48, 'kasungu' : 118, 'salima' : 67},
    'kasungu' : {'dowa' : 118, 'nkhotakota' : 112, 'mzuzu' : 230},
    'nkhotakota' : {'salima' : 112, 'nkhatabay' : 194, 'kasungu' : 112},
    'salima' : {'monkeybay' : 133, 'dowa' : 67, 'nkhotakota' : 112},
    'nkhatabay' : {'nkhotakota' : 194, 'mzuzu' : 47},
    'mzuzu' : {'nkhatabay' : 47, 'rhumpi' : 68, 'kasungu' : 230},
    'rhumpi' : {'mzuzu' : 68, 'karonga' : 173},
    'karonga' : {'rhumpi' : 173}

}
validate_graph(graph)

print("welcome to Sana deliveries simulation")

show_locations(graph)

print("What is your point of origin? : ")

origin = input()
origin = origin.lower()

print("What is your destinstion? :")

destination = input()
destination = destination.lower()

if origin not in graph or destination not in graph: 
    if origin not in graph:
        print(f"Sorry, '{origin}' is not a possible location.")

    if destination not in graph:
        print(f"Sorry, '{destination}' is not a possible location.")

else:
        dijkstra(graph, origin, destination)
