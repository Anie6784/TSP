import heapq
from random import randint
from copy import deepcopy


class individual:
    def __init__(self):
        self.gnome = ""
        self.fitness = 0

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness


class TSP:
    def __init__(self, v, gene, w):
        self.v = v
        self.gene = gene
        self.w = w
        self.pop_size = 15

    def create_gnome(self):
        gnome = [0]
        while True:
            if len(gnome) == self.v:
                gnome.append(0)
                break
            temp = randint(1, self.v - 1)
            if temp not in gnome:
                gnome.append(temp)
        return gnome

    def cal_fitness(self, gnome):
        f = 0
        for i in range(len(gnome)-1):
            f += self.w[gnome[i]][gnome[i+1]]
        return f

    def mutatedGene(self, gnome):
        while True:
            r = randint(1, self.v - 1)
            r1 = randint(1, self.v - 1)
            if r1 != r:
                temp = gnome[r]
                gnome[r] = gnome[r1]
                gnome[r1] = temp
                break
        return gnome

    def solve(self):
        gen = 0
        gen_thres = 10
        population = []

        for i in range(self.pop_size):
            temp = deepcopy(individual())
            temp.gnome = self.create_gnome()
            temp.fitness = self.cal_fitness(temp.gnome)
            population.append(temp)

        while gen <= gen_thres:
            population.sort()
            print("\nGeneration ", gen, " of population ", self.pop_size)
            print(population[0].gnome, "Fitness: ", population[0].fitness)
            print()
            new_pop = [population[0]]
            gen += 1
            for i in range(self.pop_size-1):
                parent = population[i+1]
                while True:
                    new_g = self.mutatedGene(parent.gnome)
                    new_gnome = deepcopy(individual())
                    new_gnome.gnome = new_g
                    new_gnome.fitness = self.cal_fitness(new_gnome.gnome)
                    if new_gnome.fitness <= parent.fitness:
                        new_pop.append(new_gnome)
                        break
            population = new_pop

        population.sort()
        print("Solution: ")
        for i in population[0].gnome:
            print(self.gene[int(i)], end=" ")
        print("\nCost: ", population[0].fitness)
