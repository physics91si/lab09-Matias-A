from particle import Particle
import numpy as np

class Molecule:
    """Stores information about a molecule with two particles, spring constant, and equilibrium distance."""
    def __init__(self, pos1, pos2, m1, m2, spr, eq):
        """Create a molecule with 2 positions (numpy array of len 2), 2 masses, spring constant and an equilibrium distance."""
        self.p1=Particle(pos1, m1)
        self.p2=Particle(pos2, m2)
        self.k = spr
        self.L0=eq

    def get_displ(self):
        return self.p2.pos-self.p1.pos
    def get_force(self):
        """Gets the force due to the string on particle 1"""
        displ=self.get_displ()
        distance = np.sqrt(displ[0]**2+displ[1]**2)
        magnitude = (distance-self.L0)*self.k
        return (magnitude/distance)*displ
