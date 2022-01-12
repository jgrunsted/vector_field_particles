import numpy as np
from particle import Particle
from timeit import default_timer as timer
import cexprtk

class Particles:
    def __init__(self, vector_field, num_particles):
        self.positions_data = {}
        self.num_particles = num_particles
        self.vector_field = vector_field
        self.particles = np.array([Particle()])
        for i in range(num_particles - 1):
            self.particles = np.append(self.particles, Particle())
            self.positions_data[str(i)] = "[" + str(self.particles[i].position[0]) + "," + str(self.particles[i].position[1]) + "]"
        self.x = 0.0
        self.y = 0.0
        self.st = cexprtk.Symbol_Table({"x":self.x, "y":self.y}, add_constants = True)
        self.uExpr = cexprtk.Expression(self.vector_field[0], self.st)
        self.vExpr = cexprtk.Expression(self.vector_field[1], self.st)

    def get_force(self, position):
        # vfield = np.copy(self.vector_field)
        # self.aeval("x=" + str((position[0] - 500)))
        # self.aeval("y=" + str((position[1] - 500)))
        
        self.st.variables["x"] = (position[0] - 500) / 10
        self.st.variables["y"] = (position[1] - 500) / 10

        return np.array([self.uExpr(), self.vExpr()])

    def update_particles(self):
        # start = timer()
        for i, p in enumerate(self.particles):
            if p.updated != True:
                p.apply_force(self.get_force(p.position))
                p.update_position()
                if p.is_alive != True:
                    self.particles[i] = Particle()
                p.updated = True
            else:
                p.updated = False
            self.positions_data[str(i)] = "[[" + str(p.position[0]) + "," + str(p.position[1]) + "]," + str(p.lifespan) + "]"
        # end = timer() - start
        # print(end)

        return self.positions_data