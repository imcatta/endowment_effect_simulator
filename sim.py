import math
import random


class Sim:

    def __init__(self, alpha=2, m=44, k=22, value_dist={'distribution': 'uniform'}):
        self.n_swaps = None
        self.alpha = alpha
        self._init_prior_values(m, value_dist)
        ones = [1 for _ in range(k)]
        zeros = [0 for _ in range(m - k)]
        self.mugs = random.sample(ones + zeros, m)
        

    def _init_prior_values(self, m, value_dist):
        if value_dist['distribution'] == 'uniform':
            self.prior_values = [random.uniform(0, 1) for _ in range(m)]
        elif value_dist['distribution'] == 'triangular':
            c = value_dist['c']
            self.prior_values = [random.triangular(0, 1, c) for _ in range(m)]
        else:
            raise ValueError(
                'The value of `distribution` must be `uniform` or `triangular`')

    def _utility_func(self, x):
        return x if x >= 0 else self.alpha * x

    def run(self):
        asks = []
        bids = []
        for value, mug in zip(self.prior_values, self.mugs):
            sign = 1 if mug else -1
            utility = self._utility_func(sign * value)
            if mug:
                asks.append(-utility)
            else:
                bids.append(utility)

        asks.sort()
        bids.sort(reverse=True)

        self.n_swaps = 0
        for ask, bid in zip(asks, bids):
            if ask > bid:
                break
            self.n_swaps += 1
