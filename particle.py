import numpy as np
import random

# from numba import double, boolean
# from numba.experimental import jitclass

# spec = [
#     ("position", double[:]),
#     ("velocity", double[:]),
#     ("lifespan", double),
#     ("degrade_rate", double),
#     ("is_alive", boolean)
# ]

# @jitclass(spec)
class Particle:
    def __init__(self):
        self.position = np.array([float(np.random.randint(0, 1900)), float(np.random.randint(0, 950))])
        self.velocity = np.array([0.0, 0.0])
        self.lifespan = 0.5
        self.degrade_rate = np.random.uniform(0.9, 0.998)
        self.is_alive = True
        self.updated = bool(random.getrandbits)

    def update_position(self):
        self.position += self.velocity
        self.lifespan *= self.degrade_rate
        self.is_alive = (self.lifespan > 0.01)

    def apply_force(self, force):
        self.velocity += force / 1000      # the 100 here is equal to the mass of the particle