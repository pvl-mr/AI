from deap import base, algorithms
from deap import creator
from deap import tools

import algelitism
from graph_show import show_graph, show_ships

import random
import matplotlib.pyplot as plt
import numpy as np

POLE_SIZE = 10
SHIPS = 10
LENGTH_CHROM = 3*SHIPS

POPULATION_SIZE = 200
P_CROSSOVER = 0.9
P_MUTATION = 0.2
MAX_GENERATIONS = 50
HALL_OF_FAME_SIZE = 1

hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

RANDOM_SEED = 42
random.seed(RANDOM_SEED)

creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

def randomShip(total):
    ships = []
    for n in range(total):
        ships.extend([random.randint(1, POLE_SIZE), random.randint(1, POLE_SIZE), random.randint(0, 1)])

    return creator.Individual(ships)

toolbox = base.Toolbox()
toolbox.register("randomShip", randomShip, SHIPS)
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.randomShip)

population = toolbox.populationCreator(n=POPULATION_SIZE)

