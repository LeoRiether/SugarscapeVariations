"""
Sugarscape Constant Growback Model
================================

Replication of the model found in Netlogo:
Li, J. and Wilensky, U. (2009). NetLogo Sugarscape 2 Constant Growback model.
http://ccl.northwestern.edu/netlogo/models/Sugarscape2ConstantGrowback.
Center for Connected Learning and Computer-Based Modeling,
Northwestern University, Evanston, IL.
"""

from datetime import datetime

from mesa import Model
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

from .agents import SsAgent, Sugar
from .schedule import RandomActivationByBreed

from .moving_stats import MovingStats

class SugarscapeCg(Model):
    """
    Sugarscape 2 Constant Growback
    """

    verbose = False  # Print-monitoring

    def __init__(
        self, height=50, width=50, initial_population=100,
        reproduce_prob=0.5, growback_factor=1,
    ):
        """
        Create a new Constant Growback model with the given parameters.

        Args:
            initial_population: Number of population to start with
            reproduce_prob: Probabilidade de que uma formiga se reproduza
                            em um passo da simulação
            growback_factor: Amount that every sugarcane grows by each step
            growback_factor: Quantidade de açúcar que cada cana 

        """

        # Set parameters
        self.height = height
        self.width = width
        self.initial_population = initial_population
        self.reproduce_prob = reproduce_prob
        self.growback_factor = growback_factor

        self.stats = MovingStats()
        self.schedule = RandomActivationByBreed(self)
        self.grid = MultiGrid(self.height, self.width, torus=False)
        self.datacollector = DataCollector(
            model_reporters = {
                "SsAgent"     : lambda m: m.schedule.get_breed_count(SsAgent),
                "Average"     : lambda m: m.stats.avg(),
                "Oscillation" : lambda m: m.stats.osc(),
            },
        )

        self.children = []
        self.removals = []

        # Create sugar
        import numpy as np

        sugar_distribution = np.genfromtxt("src/sugar-map.txt")
        self.sugar_agent_at = np.ndarray((self.height, self.width), dtype=Sugar)
        for _, x, y in self.grid.coord_iter():
            max_sugar = sugar_distribution[x, y]
            sugar = Sugar((x, y), self, max_sugar)
            self.sugar_agent_at[x, y] = sugar
            self.grid.place_agent(sugar, (x, y))
            self.schedule.add(sugar)

        # Create agent:
        for i in range(self.initial_population):
            x = self.random.randrange(self.width)
            y = self.random.randrange(self.height)
            sugar = self.random.randrange(6, 25)
            metabolism = self.random.randrange(2, 4)
            vision = self.random.randrange(1, 6)
            ssa = SsAgent((x, y), self, False, sugar, metabolism, vision, reproduce_prob)
            self.grid.place_agent(ssa, (x, y))
            self.schedule.add(ssa)

        self.running = True
        self.datacollector.collect(self)

    def schedule_add_child(self, child):
        self.children.append(child)

    def schedule_removal(self, agent):
        self.removals.append(agent)

    def step(self):
        self.schedule.step()
        self.stats.update_step(self.schedule.get_breed_count(SsAgent))
        self.datacollector.collect(self)
        if self.verbose:
            print([self.schedule.time, self.schedule.get_breed_count(SsAgent)])

        for child in self.children:
            self.grid.place_agent(child, child.pos)
            self.schedule.add(child)

        for agent in self.removals:
            self.grid._remove_agent(agent.pos, agent)
            self.schedule.remove(agent)

        self.children = []
        self.removals = []

        if len(self.schedule.agents_by_breed[SsAgent]) == 0:
            self.running = False

        if self.schedule.steps == 100 or (self.schedule.steps < 100 and not self.running):
            timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
            suffix = "_data_rp{}_gf{}_t{}.csv".format(
                self.reproduce_prob,
                self.growback_factor,
                timestamp
            )
            import os
            os.makedirs("csv", exist_ok=True)
            self.datacollector \
                .get_agent_vars_dataframe() \
                .to_csv("csv/agent" + suffix)
            self.datacollector \
                .get_model_vars_dataframe() \
                .to_csv("csv/model" + suffix)


    def run_model(self, step_count=200):

        if self.verbose:
            print(
                "Initial number Sugarscape Agent: ",
                self.schedule.get_breed_count(SsAgent),
            )

        for i in range(step_count):
            self.step()
            if not self.running:
                break

        if self.verbose:
            print("")
            print(
                "Final number Sugarscape Agent: ",
                self.schedule.get_breed_count(SsAgent),
            )

