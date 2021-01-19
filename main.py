import random
import optuna
from sim import Sim

N = 250
M = 44
K = 22
TARGET = 2.25

def objective(trial):
    alpha = trial.suggest_uniform('alpha', 0, 20)
    cum = 0
    for i in range(N):
        random.seed(i)
        sim = Sim(alpha=alpha, m=M, k=K)
        sim.run()
        cum += sim.n_swaps

    mean = cum / N
    return (mean - TARGET) ** 2


study = optuna.create_study()
study.optimize(objective, n_trials=1000)
print(study.best_params)