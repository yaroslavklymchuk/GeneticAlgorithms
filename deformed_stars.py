import random
import numpy as np
import itertools
import math


class Deformed_Star:

    def __init__(self, function, lower_bounds, upper_bounds):
        self.function = function
        self.lower_bounds = lower_bounds
        self.upper_bounds = upper_bounds

    def _calculate_fitness(self, population):
        return [self.function(*ind) for ind in population]

    def _parallel_transfer(self, population):
        new_population = np.array(population).copy()
        condition = sum([any([el[i] < self.lower_bounds[i] or el[i] > self.upper_bounds[i]
                              for el in new_population]) for i in range(len(self.lower_bounds))])
        while condition:
            alpha = random.random()
            a = [np.random.uniform(self.lower_bounds[i], self.upper_bounds[i]) for i in range(len(self.upper_bounds))]
            a1, a2 = a
            new_population = [(el + a1 * math.cos(math.pi * alpha), el1 + a2 * math.sin(math.pi * alpha))
                              for el, el1 in new_population]
            condition = sum([any([el[i] < self.lower_bounds[i] or el[i] > self.upper_bounds[i]
                                  for el in new_population]) for i in range(len(self.lower_bounds))])
        return new_population

    def _generate_random_population(self, qty_individuals, qty_variables):
        population = [x for x in zip(*[np.random.random(qty_individuals) for i in range(qty_variables)])]
        return population

    def _generate_population_t(self, qty_individuals):
        t_population = [x for x in zip(*[np.random.uniform(self.lower_bounds[i], self.upper_bounds[i], qty_individuals)
                                         for i in range(len(self.lower_bounds))])]
        t_values = self._calculate_fitness(t_population)
        return t_population, t_values

    def _generate_population_z(self, population):
        z_population = self._parallel_transfer(population)
        z_values = self._calculate_fitness(z_population)

        return z_population, z_values

    def _simple_rotation(self, operand1, operand2, alpha):
        new_operand = np.zeros(len(operand1))
        new_operand[0] = operand1[0] + \
                         (operand1[0] - operand2[0]) * math.cos(math.pi * alpha) - \
                         (operand1[1] - operand2[1]) * math.sin(math.pi * alpha)
        new_operand[1] = operand1[1] + \
                         (operand1[0] - operand2[0]) * math.sin(math.pi * alpha) - \
                         (operand1[1] - operand2[1]) * math.cos(math.pi * alpha)
        return tuple(new_operand)

    def _compress(self, operand1, operand2, compression_rate):
        return tuple([(operand1[i] + operand2[i]) / compression_rate for i in range(len(operand1))])

    def _rotate(self, population, is_compress=False, compression_rate=2):

        alpha = random.random()
        for i in range(len(population) - 1):
            if self.function(*population[i]) < self.function(*population[i + 1]):
                if is_compress:
                    population[i] = self._compress(population[i], population[i + 1], compression_rate)
                population[i + 1] = self._simple_rotation(population[i + 1], population[i], alpha)
            else:
                if is_compress:
                    population[i + 1] = self._compress(population[i], population[i + 1], compression_rate)
                population[i] = self._simple_rotation(population[i], population[i + 1], alpha)
        return self._parallel_transfer(population)

    def _generate_population_s(self, population):

        s_population = self._rotate(population)
        s_values = self._calculate_fitness(s_population)

        return s_population, s_values

    def _generate_population_w(self, population, compression_rate=2):

        w_population = self._rotate(population, True, compression_rate)
        w_values = self._calculate_fitness(w_population)
        return w_population, w_values

    def evolution(self, qty_individuals, qty_variables=2, maxiterations=100, compression_rate=2):
        random_population = self._generate_random_population(qty_individuals, qty_variables)
        whole_population = [self._generate_population_t(qty_individuals)[0],
                            self._generate_population_s(random_population)[0],
                            self._generate_population_w(random_population, compression_rate)[0],
                            self._generate_population_z(random_population)[0]]

        whole_population = list(map(lambda x: tuple(x), whole_population))
        whole_population_values = np.array(list(itertools.chain(*[self._calculate_fitness(pop)
                                                                  for pop in whole_population])))
        whole_population_values.sort()
        iteration = 1
        selected_population = [el for el in list(itertools.chain(*whole_population))
                               if self.function(*el) in whole_population_values[:qty_individuals]]
        while iteration < maxiterations:
            whole_population = [self._generate_population_t(qty_individuals)[0],
                                self._generate_population_s(selected_population)[0],
                                self._generate_population_w(selected_population, compression_rate)[0],
                                self._generate_population_z(selected_population)[0]]

            whole_population = list(map(lambda x: tuple(x), whole_population))
            whole_population_values = np.array(list(itertools.chain(*[self._calculate_fitness(pop)
                                                                      for pop in whole_population])))
            whole_population_values.sort()

            selected_population = [el for el in list(itertools.chain(*whole_population))
                                   if self.function(*el) in whole_population_values[:qty_individuals]]
            iteration += 1

        return selected_population[0], whole_population_values[0]