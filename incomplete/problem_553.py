
"""
Purpose: Project Euler exercises
Date created: 2020-06-20

Problen Number: 553
Name: Power sets of power sets
URL: https://projecteuler.net/problem=553

Set notation: https://www.mathsisfun.com/sets/symbols.html

Contributor(s):
    Mark M.
"""

import itertools as ittr

combinations = ittr.combinations
CFI = ittr.chain.from_iterable

MOD=1000000007


class Node:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.graph = [None] * self.vertex

    # Add edges
    def add_edge(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = Node(s)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.vertex):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")


    def make_adjacency_list(self):
            adj_list = {key: [] for key in range(self.__v)}
            for edge in self.__edge_list:
                # where edge[1] is the destiny and edge[2] the weight
                edge_val = {edge[1]: edge[2]} 
                adj_list[edge[0]].append(edge_val)
            self.__adj_list = adj_list


def graph_ex(V=5):
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.print_agraph()



# Depth-first search
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

# Breath-First search

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

bfs(graph, 'A')



def xrange(n):
    return [i for i in range(1, n+1)]

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    max_rng = len(s) + 1
    return CFI(combinations(s, r) for r in range(1, max_rng))


p = xrange(6)
qs = [list(q) for q in powerset(p)]
rs = set()
for q in qs:
    tmp = [list(r) for r in powerset(q)]
    for i in tmp:
        rs.add(i)

    rs.append(tmp)

rs = [list(r) for r in powerset(qs)]


idx, res = 0, []
for q in powerset(p):
    tmp = [r for r in powerset(q)]
    print(q, tmp)
            if set(q).intersection(r):
                res[idx] = {q: r}
                idx += 1

a = {5, 6}
b = {6, 7}
a.intersection(b) # Upsidedown U


# xyz = [[1], [1,2,3], [3], [5,6], [6,7]]
# res = {}
# for i in xyz:
#     for j in xyz:
#         if i != j:
#             if set(i).intersection(j):




















