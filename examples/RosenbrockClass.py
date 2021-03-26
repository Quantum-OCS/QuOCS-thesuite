from quocs_optlib.figureofmeritevaluation.AbstractFom import AbstractFom
from scipy import optimize
import numpy as np
import time


class Rosenbrock(AbstractFom):
    def __init__(self, args_dict: dict = None):
        pass

    def get_FoM(self, pulses, parameters, timegrids):
        # time.sleep(0.2)
        return {"FoM": optimize.rosen(np.asarray(parameters))}
