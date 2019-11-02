import random
import numpy as np


class EvolutionAlgorithm:

    def __init__(self, fitness_function, lower_bounds, upper_bounds):
        self.fitness_function = fitness_function
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds

    def _calculate_fitness(self, population_result):
        """define the value of fitness function for an individual"""
        fitness_value = self.fitness_function(*population_result)
        return fitness_value

    def _create_individual(self, qty_variables):
        """creates an individual of population"""
        return [self.lower_bounds[i] + random.random() * (self.upper_bounds[i] - self.lower_bounds[i])
                for i in range(qty_variables)]

    def _create_population(self, qty_variables, qty_individuals):
        """creates a population"""
        return [self._create_individual(qty_variables) for i in range(qty_individuals)]

    def _evaluate_population(self, population):
        """evaluates a fitness of whole population"""
        return np.mean([self._calculate_fitness(single_result)
                         for single_result in population])

    def _mutate(self, individual, mutation_probability):
        """mutates an individual"""
        new_individual = []
        if mutation_probability > random.random():
            for i, ind_value in enumerate(individual):
                randomness = np.random.normal(size=1)
                new_value = ind_value + randomness
                while new_value > self.upper_bounds[i] or new_value < self.lower_bounds[i]:
                    randomness = np.random.normal(size=1)
                    new_value = ind_value + randomness
                new_individual.append(new_value)
            return new_individual
        else:
            return individual

    def _get_best_individual(self, population, criterion_function='min'):
        """selects best individual in population, works with 'min' and 'max' criterion functions"""
        population_fitness_results = np.array([self._calculate_fitness(individual) for individual in population])
        if criterion_function == 'min':
            return population_fitness_results.min(), population[population_fitness_results.argmin()]
        else:
            return population_fitness_results.max(), population[population_fitness_results.argmax()]

    def _select_population(self, population, criterion='min', mutation_probability=0.5):
        """selects best individuals for population"""
        new_population = []
        population_avg_score = self._evaluate_population(population)
        for individual in population:
            if criterion == 'min':
                if self._calculate_fitness(individual) < population_avg_score:
                    new_population.append(individual)
                else:
                    new_population.append(self._mutate(individual, mutation_probability))
            else:
                if self._calculate_fitness(individual) > population_avg_score:
                    new_population.append(individual)
                else:
                    new_population.append(self._mutate(individual, mutation_probability))
        return new_population

    def main(self, population_qty, qty_variables_per_individual, max_iterations=1000,
             criterion_function='min', mutation_probability=0.5):
        """main function"""
        population = self._create_population(qty_variables_per_individual, population_qty)
        best_fitness_function_value, best_solution = self._get_best_individual(population, criterion_function)
        iteration_number = 1
        while iteration_number < max_iterations:
            population = self._select_population(population, criterion_function, mutation_probability)
            best_fitness_function_value, best_solution = self._get_best_individual(population,
                                                                                        criterion_function)
            iteration_number += 1

        return best_fitness_function_value, best_solution