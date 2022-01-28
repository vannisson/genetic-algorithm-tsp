import numpy as random
import matplotlib.pyplot as plt

from functions import City, Fitness, createRoute, initialPopulation, rankRoutes, selection, matingPool, breed, breedPopulation, mutate, mutatePopulation, nextGeneration, geneticAlgorithm

cityList = []

for i in range(0,25):
    cityList.append(City(x=int(random.random() * 200), y=int(random.random() * 200)))

geneticAlgorithm(population=cityList, popSize=100, eliteSize=20, mutationRate=0.01, generations=500)
