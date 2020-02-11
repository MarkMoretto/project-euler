
"""
Purpose: Projec-Euler
Date created: 2020-02-10

Problem: 701
Title:Random connected area
URI: https://projecteuler.net/problem=701

Contributor(s):
    Mark M.
"""



def binary_permutations(n):
    # for i in range(1 << n):
    for i in range(2 ** n):
        # s = bin(i)[2:]
        s = bin(i).replace("0b","")
        s ='0' * (n - len(s)) + s
        yield list(map(int, list(s)))

def chunker(iterable, n_values=2):
    start = 0
    end = n_values
    iter_len = len(iterable)
    while start < iter_len:
        yield iterable[start:end]
        start = end
        end = start + n_values

def crawler(iterable):
    """Like the chunker, but predefined for chunk size and step size."""
    chunksize = 2
    step_size = 1
    start = 0
    end = chunksize
    iter_len = len(iterable)
    while end <= iter_len:
        yield iterable[start:end]
        start += step_size # Increment start by step_size
        end = start + chunksize


def transpose(arr):
    return [*map(list, zip(*arr))]


class BinaryGraph:
    def __init__(self, n_rows=2, n_cols=2):
        self.rows = n_rows
        self.cols = n_cols
        self.n_dims = None
        self.grid = None


    def __eval_rc(self):
        self.n_dims = max([self.rows, self.cols])

    def __make_perms(self):
        factor = self.n_dims ** 2
        self.grid = [i[::-1] for i in binary_permutations(factor)]

    def set(self):
        self.__eval_rc()
        self.__make_perms()


## Instantiate class with desired row and column counts
w, h = 4, 4
n_dims = max(w, h) # Number of dimensions in grid
graph_max = n_dims - 1 # Max width or height value
max_dims = n_dims ** 2 # Max squred dimensions
bg = BinaryGraph(w, h)
bg.set()
main_grid = bg.grid # Static grid variable



######################################################################
### Test row
# # tst = bg.grid[100]
# tst = bg.grid[102]
# chunks = [ch for ch in chunker(tst, n_dims)]
# t_chunks = transpose(chunks)

# tst1 = bg.grid[0] # zero 1
# tst2 = bg.grid[1] # single 1
# tst3 = bg.grid[102] # Mixed bag; Should return subtot 2

# def tester(tst_row):

#     tst = tst_row.copy()
#     chunks = [ch for ch in chunker(tst, n_dims)]
#     t_chunks = transpose(chunks)
#     tot = 0
#     subtot = 0

#     while True:
#         if not 1 in tst:
#             print(f"Tot: {tot}\nSubtot: {subtot}")
#             break
#         tot += 1
#         for ch in chunks:
#             for x in crawler(ch):
#                 if sum(x) == 2:
#                     subtot += 1
    
#         for tch in t_chunks:
#             for y in crawler(tch):
#                 if sum(y) == 2:
#                     subtot += 1
#         print(f"Tot: {tot}\nSubtot: {subtot}")
#         break

# tester(tst1)
# tester(tst2)
# tester(tst3)

# tst = bg.grid[100]

# ### For 2, 2 grid
# tst = bg.grid[0] # zero 1
# tst = bg.grid[1] # single 1
# tst = bg.grid[-3] # [1, 0, 1, 1]
# tst = bg.grid[3] # [1, 1, 0, 0]
# tst = bg.grid[6] # [0, 1, 1, 0]
# tst = bg.grid[-6] # [0, 1, 0, 1]
# tst = bg.grid[-1] # [1, 1, 1, 1]


# chunks = [ch for ch in chunker(tst, n_dims)]
# t_chunks = transpose(chunks)
# tot = 0
# subtot = 0

# while True:
#     if not 1 in tst:
#         print(f"Tot: {tot}\nSubtot: {subtot}")
#         break
#     tot += 1
#     for ch in chunks:
#         for x in crawler(ch):
#             if sum(x) == 2:
#                 subtot += 1
#     for tch in t_chunks:
#         for y in crawler(tch):
#             if sum(y) == 2:
#                 subtot += 1
#     print(f"Tot: {tot}\nSubtot: {subtot}")
#     break

# tester(tst1)
# tester(tst2)
# tester(tst3)

### For 4, 4 grid
tst = bg.grid[0] # zero 1
tst = bg.grid[1] # single 1
tst = bg.grid[1000] # [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

tst = bg.grid[-3] # [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

chunks = [ch for ch in chunker(tst, n_dims)]
t_chunks = transpose(chunks)
tot = 0
subtot = 0

while True:
    if not 1 in tst:
        print(f"Tot: {tot}\nSubtot: {subtot}")
        break
    tot += 1
    for ch in chunks:
        for x in crawler(ch):
            if sum(x) == 2:
                subtot += 1
    for tch in t_chunks:
        for y in crawler(tch):
            if sum(y) == 2:
                subtot += 1
    print(f"Tot: {tot}\nSubtot: {subtot}")
    break

tester(tst1)
tester(tst2)
tester(tst3)
######################################################################



def eval_areas(row):

    chunks = [ch for ch in chunker(row, n_dims)]
    t_chunks = transpose(chunks)
    tot = 0
    subtot = 0

    while True:
        if not 1 in row:
            break
        tot += 1
        for ch in chunks:
            for x in crawler(ch):
                if sum(x) == 2:
                    subtot += 1
    
        for tch in t_chunks:
            for y in crawler(tch):
                if sum(y) == 2:
                    subtot += 1
        break

    tot += subtot

    if subtot == max_dims:
        tot = subtot

    return tot








area_list = list()
for row in main_grid:
    res = eval_areas(row)
    area_list.append(res)

tot_area = sum(area_list)
exp_area = round(tot_area / len(main_grid), 8)


# E(2, 2) = 1.875
# E(4, 4) = 5.76487732



# main_list= list()
# coord_list = []
# for r in main_grid:
#     area_list = list()
#     chunks = list(chunker(r, n_dims))
#     tp_chunks = transpose(chunks)
#     for r, chunk in enumerate(chunks):
#         for c, val in enumerate(chunk):
#             area = 0

#             xyz = news_coords((r, c), graph_max)
#             if chunks[r][c] == 1:
#                 area += 1
#                 # print(f"r c area: {area}")
#                 for coord in xyz:
#                     if coord:
#                         area += chunks[coord[0]][coord[1]]
#                         # print(f"{coord}: {area}")
    
#             area_list.append(area)
#     main_list.extend(area_list)










w, h = 3, 3
perms = [i[::-1] for i in binary_permutations(w * h)]

if w == h:
    dim_len = w

tst1 = perms[100]
for i in range(1, len(tst1)):
    if tst1[i] == or tst[i-1] == tst[i + dim_len]:


ddict = {}
for r in range(len(tst1)):
    for c in range(len(tst1)):



# [i for i in chunker(perms[-2])]
tot_count = 0
rn = 0
for r in perms[:3]:
    rn += 1
    chunks = chunker(r)
    for ch in chunks:
        print(rn, ": ", ch)



# for m in perms[:3]:
#     for r in range(2):
#         for c in range(2):

# for m in perms[:3]:
#     for c in len(range(m)):

matrix = [[0. for c in range(w)] for r in range(h)]

for r in range(h):
    cols = [i for i in range(w)]
    print(f"{r}, {cols}")
    for j in range(h):
        for k in range(w):
            print(f"")
            # tot = sum([r1, c1, r2, c2])
            # print(f"[[{r1}, {c1}],\n[{r2}, {c2}]] = {tot}\n")



# for i in [0, 1,]:
#     for j in [0, 1,]:
#         for k in [0, 1,]:
#             for l in [0, 1,]:
#                 print(f"({i}, {j}, {k}, {l})")

# class Matrix:
#     def __init__(self, row, column, default_value = 0.):
#         self.row, self.column = row, column
#         self.array = [[default_value for c in range(column)] for r in range(row)]



# def prob_check(width=2, height=2, p_black = 0.5, n_iters = 1000, value_list = None):
#     rng_ = [i for i in range(width*height)]
#     denom = sum([1 for r in rng_ for c in rng_])
#     if value_list is None:
#         avg_list = list()
#     iters = n_iters
#     while iters > 0:
#         tot_blk = 0
#         for r in rng_:
#             for c in rng_:
#                 randn = random.random()
#                 if randn >= p_black:
#                     tot_blk += 1
#         avg_list.append(round(tot_blk/denom, 8))
#         iters -= 1

#     avg_check = sum(avg_list) / 1000
#     frmt_avg = avg_check * 100
#     print(f"Probability of black area after {n_iters} iterations ~{frmt_avg:0<.2f}%")




# class Graph:
#     def __init__(self, vertex):
#         self.vertex = vertex
#         self.graph = [[0] * vertex for i in range(vertex)]

#     def add_edge(self, u, v):
#         self.graph[u - 1][v - 1] = 1
#         self.graph[v - 1][u - 1] = 1

#     def show(self):

#         for i in self.graph:
#             for j in i:
#                 print(j, end=" ")
#             print(" ")
