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


        


graph = {
    'Ginnery' : {'Victoria Avenue': 4, 'Limbe' : 6},
    'Limbe' : {'Ginnery' : 6, 'Zomba' : 62},
    'Victoria Avenue' : {'Ginnery' : 4, 'Zalewa' : 54},
    'Zalewa' : {'Victoria Avenue' : 54, 'Ntcheu': 98, 'Balaka' : 90},
    'Balaka' : {'Zalewa' : 90, 'Ntcheu' : 42, 'Liwonde' : 33, 'Monkeybay': 147},
    'Zomba' : {'Limbe' : 62, 'Liwonde' : 51},
    'Liwonde' : {'Zomba' : 51, 'Balaka' : 33, 'Monkeybay' : 136},
    'Monkeybay' : {'Liwonde' : 136, 'Balaka' : 147, 'Salima' : 133},
    'Ntcheu' : {'Zalewa' : 98, 'Balaka' : 42, 'Dedza' : 73},
    'Dedza' : {'Ntcheu' : 73, 'Gateway' : 90},
    'Gateway' : {'Dedza' : 90, 'Area 49' : 6},
    'Area 49' : {'Gateway' : 6, 'Dowa' : 48},
    'Dowa' : {'Area 49' : 48, 'Kasungu' : 118, 'Salima' : 67},
    'Kasungu' : {'Dowa' : 118, 'Nkhotakota' : 112, 'Mzuzu' : 230},
    'Nkhotakota' : {'Salima' : 112, 'Nkhatabay' : 194, 'Kasungu' : 112},
    'Salima' : {'Monkeybay' : 133, 'Dowa' : 67, 'Nkhotakota' : 112},
    'Nkhatabay' : {'Nkhotakota' : 194, 'Mzuzu' : 47},
    'Mzuzu' : {'Nkhatabay' : 47, 'Rhumpi' : 68, 'Kasungu' : 230},
    'Rhumpi' : {'Mzuzu' : 68, 'Karonga' : 173},
    'Karonga' : {'Rhumpi' : 173}

}

dijkstra(graph, "Karonga", "Dedza")


