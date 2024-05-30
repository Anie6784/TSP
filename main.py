from genetic import TSP

# input txt files
file = {
    1: "indiana.txt",
    2: "tsp.txt",
    3: "tsp9.txt",
    4: "tsp21.txt",
    5: "tsp99.txt",
    6: "us.txt"
}

# Prompts and Inputs
map_num = int(input(
    "Welcome to the Traveling Salesman Problem. Choose map number: 1.Indiana, or 2.TSP, or 3.TSP9, or 4.TSP21, "
    "or 5.TSP99, or 6.US: "))
while map_num not in range(1, 7):
    map_num = int(input("Invalid map! Choose again: "))
f = open(f'inputs/{file[map_num]}', "r").readlines()
v = int(f[0])

print("\nLocation names: ")
gene = []
for i in range(1, v + 1):
    s = f[i][:-1]
    print(str(i-1) + ". " + s)
    gene.append(s)

print("\nGrid of costs: ")
w = []
for i in range(v + 1, 2 * v + 1):
    s = f[i][:-1]
    print(s)
    w.append([int(obj) for obj in s.split(' ')])

s = TSP(v, gene, w)
s.solve()
