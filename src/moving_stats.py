from collections import deque
import numpy as np

def div(x, y):
    if y == 0:
        return 0
    return x / y

class MovingStats:
    """
        Classe que computa estatísticas de uma população de agentes
        a cada etapa da simulação.

        As estatísticas calculadas atualmente são:
        - avg: média móvel
        - stdev: espécie de desvio padrão, calculado a cada etapa com base
                 na média móvel e no valor da população
        - osc: medida de oscilação da população
    """

    moving_avg_len = 50

    def __init__(self):
        self.values = deque()
        self.sum = 0 # soma dos últimos `moving_avg_len` valores de população

        self.osc_up = 0
        self.osc_up_steps = 0
        self.osc_down = 0
        self.osc_down_steps = 0

    def update_step(self, population):
        self.values.append(population)
        self.sum += population
        if len(self.values) > self.moving_avg_len:
            self.sum -= self.values[0]
            self.values.popleft()

        # Atualizamos a medida de oscilação, dependendo de se a população
        # atual é maior ou menor que a média móvel
        if population >= self.avg():
            self.osc_up += population - self.avg()
            self.osc_up_steps += 1
        else:
            self.osc_down += self.avg() - population
            self.osc_down_steps += 1

    def avg(self):
        """ Média móvel dos últimos `moving_avg_len` passos """
        return div(self.sum, len(self.values))

    def osc(self):
        """
            Retorna uma medida de oscilação da população, calculada pela média geométrica
            de osc_up_avg e osc_down_avg.

            Essa medida é maximizada quando a população passa tempos similares acima e
            abaixo da média, o que indica uma alta amplitude de oscilação.
        """
        osc_up_avg = div(self.osc_up, self.osc_up_steps)
        osc_down_avg = div(self.osc_down, self.osc_down_steps)
        return np.sqrt(osc_up_avg * osc_down_avg)

