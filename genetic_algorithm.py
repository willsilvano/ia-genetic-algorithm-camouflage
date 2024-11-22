import random
import numpy as np


class CamouFlagGeneticAlgorithm:
    # Class-level attributes
    generations = 0
    population_size = 0
    keep_population_num = 0
    target_color = (0, 0, 0)
    mutation_rate = 0
    mutation_intensity = 0
    population = []

    def __init__(
        self,
        mutation_rate,
        mutation_intensity,
        generations,
        population_size,
        keep_population_num,
        target_color,
    ):
        """
        Initializes the genetic algorithm with the given parameters.

        Args:
            mutation_rate (float): Probability of mutation for each gene.
            mutation_intensity (float): Intensity of mutation.
            generations (int): Number of generations to evolve.
            population_size (int): Number of individuals in the population.
            keep_population_num (int): Number of top individuals to keep each generation.
            target_color (tuple, optional): The RGB color tuple to evolve towards.
        """
        self.mutation_rate = mutation_rate
        self.mutation_intensity = mutation_intensity
        self.generations = generations
        self.target_color = target_color
        self.population_size = population_size
        self.keep_population_num = keep_population_num

        if self.target_color is None:
            self.target_color = self.__generate_random_color()

    def __generate_random_color(self):
        """Generates a random RGB color tuple."""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def __generate_random_population(self):
        """Generates an initial random population of colors."""
        print("Generating random population...")
        random_population = [
            self.__generate_random_color() for _ in range(self.population_size)
        ]
        return random_population

    def __calculate_fitness(self, individual):
        """
        Calculates the fitness of an individual.

        Fitness is defined as the sum of absolute differences from the target color.
        Lower fitness values are better.

        Args:
            individual (tuple): RGB color tuple of the individual.

        Returns:
            int: Fitness score.
        """
        return sum(abs(individual[i] - self.target_color[i]) for i in range(3))

    def __get_population_sorted_by_fitness(self):
        """Sorts the population based on fitness in ascending order."""
        return sorted(self.population, key=self.__calculate_fitness)

    def __apply_one_point_crossover(self, crossover_point, parent1, parent2):
        """
        Performs one-point crossover between two parents at the specified point.

        Args:
            crossover_point (int): The point at which crossover occurs.
            parent1 (tuple): First parent RGB tuple.
            parent2 (tuple): Second parent RGB tuple.

        Returns:
            tuple: Child RGB tuple after crossover.
        """
        return parent1[:crossover_point] + parent2[crossover_point:]

    def __apply_crossover(self, parent1, parent2):
        """
        Applies crossover between two parents to produce two children.

        Args:
            parent1 (tuple): First parent RGB tuple.
            parent2 (tuple): Second parent RGB tuple.

        Returns:
            tuple: Two child RGB tuples.
        """
        crossover_point = random.randint(1, 2)  # Crossover after first or second gene
        child1 = self.__apply_one_point_crossover(crossover_point, parent1, parent2)
        child2 = self.__apply_one_point_crossover(crossover_point, parent2, parent1)
        return child1, child2

    def __apply_mutation(self, individual, sigma=1):
        """
        Applies mutation to an individual based on mutation rate and intensity.

        Args:
            individual (tuple): RGB color tuple of the individual.
            sigma (float, optional): Standard deviation for Gaussian mutation. Defaults to 1.

        Returns:
            tuple: Mutated RGB color tuple.
        """
        mutated_individual = list(individual)
        for i in range(3):
            if random.random() < self.mutation_rate:
                # Apply Gaussian noise
                mutated_individual[i] += round(np.random.normal(0, sigma))
                # Apply mutation intensity
                mutated_individual[i] = int(
                    mutated_individual[i]
                    * (1 + random.choice([-1, 1]) * self.mutation_intensity)
                )
                # Ensure RGB values are within valid range
                mutated_individual[i] = max(0, min(mutated_individual[i], 255))
        return tuple(mutated_individual)

    def start_evolution(self, func):
        """
        Starts the genetic algorithm evolution process.

        Args:
            func (callable): Callback function to update visualization each generation.
        """
        print(f"Starting evolution for:\n{self}")
        self.population = self.__generate_random_population()

        for generation in range(1, self.generations + 1):
            # Sort population by fitness
            self.population = self.__get_population_sorted_by_fitness()

            # Select the best individual
            best_individual = self.population[0]
            best_fitness = self.__calculate_fitness(best_individual)

            # Callback to update visualization
            func(self.population, generation, best_fitness)

            # Check if the best individual matches the target color
            if best_individual == self.target_color:
                print(f"Generation {generation}: Solution found!")
                break

            print(
                f"Generation {generation}: "
                f"Best fitness: {best_fitness}, "
                f"Best individual: {best_individual}, "
                f"Target color: {self.target_color}"
            )

            # Create new population starting with the best individual
            new_population = [best_individual]
            while len(new_population) < self.population_size:
                # Select two parents from the top keep_population_num individuals
                parent1, parent2 = random.choices(
                    self.population[: self.keep_population_num], k=2
                )
                # Apply crossover to produce two children
                child1, child2 = self.__apply_crossover(parent1, parent2)
                # Apply mutation to children
                child1 = self.__apply_mutation(child1)
                child2 = self.__apply_mutation(child2)
                # Add children to the new population
                new_population.extend([child1, child2])

            # Update population for next generation
            self.population = new_population[: self.population_size]

    def __str__(self):
        """Returns a string representation of the algorithm's parameters."""
        return (
            "CamouFlagGeneticAlgorithm("
            f"generations={self.generations},"
            f"population_size={self.population_size},"
            f"keep_population_num={self.keep_population_num},"
            f"target_color={self.target_color},"
            f"mutation_rate={self.mutation_rate},"
            f"mutation_intensity={self.mutation_intensity},"
            ")"
        )
