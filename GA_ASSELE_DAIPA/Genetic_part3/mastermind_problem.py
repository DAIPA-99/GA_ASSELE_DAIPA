# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 2022

@author: tdrumond & agademer

Template file for your Exercise 3 submission 
(GA solving Mastermind example)
"""
#from ga_solver import GAProblem
from ga_solver import *
from genetic_part1 import mastermind as mm
import random

class MastermindProblem(GAProblem):
    """Implementation of GAProblem for the mastermind problem"""
    def __init__(self, match):
        super().__init__()
        self.match = match
        self.threshold_fitness = self.match.max_score()

    def how_to_compute_fitness(self, chromosome):
        return match.rate_guess(chromosome)

    def new_individual_from_2_parents(self, first_parent, second_parent):
        x_point = random.randrange(0, len(first_parent.chromosome))
        new_chromose = first_parent.chromosome[0:x_point] + second_parent.chromosome[x_point:]
        return Individual(new_chromose, match.rate_guess(new_chromose))

    def mutation(self, parent):
        possibles_colors = mm.get_possible_colors()
        new_gene = random.choice(possibles_colors)
        pos = random.randint(0, len(parent.chromosome) - 1)
        new_chrom = parent.chromosome[0:pos] + [new_gene] + parent.chromosome[pos + 1:]
        return Individual(new_chrom, match.rate_guess(new_chrom))

    def how_to_generate_one_random_chromosome(self):
        return match.generate_random_guess()


if __name__ == '__main__':
    from ga_solver import GASolver
    match = mm.MastermindMatch(secret_size=6)
    problem = MastermindProblem(match)
    solver = GASolver(problem)
    solver.reset_population()
    solver.evolve_until()

    #print(
        #f"Best guess {mm.decode_guess(solver.getBestDNA())} {solver.get_best_individual()}")
    print(
        f"Best guess {solver.get_best_individual().chromosome}"
    )
    print(
        f"Problem solved? {match.is_correct(solver.get_best_individual().chromosome)}")
