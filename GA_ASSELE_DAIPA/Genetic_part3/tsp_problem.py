# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving TSP example)
"""
#from ga_solver import GAProblem
from genetic_part2 import cities as ct
import random
from ga_solver import *
class TSProblem(GAProblem):
    """Implementation of GAProblem for the traveling salesperson problem"""
    def __init__(self, city_dict):
        super().__init__()
        self.city_dict = city_dict
        self.threshold_fitness = None

    def how_to_compute_fitness(self, chromosome):
        return - ct.road_length(self.city_dict, chromosome)

    def new_individual_from_2_parents(self, first_parent, second_parent):
        possible_cities = ct.default_road(self.city_dict)
        new_chrom = first_parent.chromosome[0:len(first_parent.chromosome) // 2]
        new_chrom += [chrom for chrom in second_parent.chromosome[len(second_parent.chromosome) // 2:] if
                      chrom not in new_chrom]
        while len(new_chrom) < len(first_parent.chromosome):
            u = random.choice(possible_cities)
            if u not in new_chrom:
                new_chrom.append(u)
        return Individual(new_chrom, - ct.road_length(self.city_dict, new_chrom))

    def mutation(self, parent):
        pos_1 = random.randint(0, len(parent.chromosome) - 1)
        pos_2 = random.randint(0, len(parent.chromosome) - 1)
        new_chrom = parent.chromosome
        new_chrom[pos_1], new_chrom[pos_2] = new_chrom[pos_2], new_chrom[pos_1]
        return Individual(new_chrom, - ct.road_length(self.city_dict, new_chrom))

    def how_to_generate_one_random_chromosome(self):
        chrom_initial = ct.default_road(self.city_dict)
        return ct.generate_random_chrosome(chrom_initial)


if __name__ == '__main__':

    from ga_solver import GASolver

    city_dict = ct.load_cities("cities.txt")
    problem = TSProblem(city_dict)
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()
    ct.draw_cities(city_dict, solver.get_best_individual().chromosome)
