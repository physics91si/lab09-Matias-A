# Physics 91SI
# Spring 2018
# Lab 8

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
from particle import Particle
from molecule import Molecule


def init_molecule():
    pos1 = np.random.rand(2,1)
    pos2 = np.random.rand(2,1)
    pos1[0]=.2
    pos1[1]=.2
    pos2[0]=.8
    pos2[1]=.8
    molecule = Molecule(pos1, pos2, 1, 2, 1, 0.5)
    #molecule.p1.vel[0]=.1
    #molecule.p2.vel[0]=-.1
    return molecule


def time_step(dt, mol):
    force = mol.get_force()
    acc1 = (1/mol.p1.m)*force
    acc2 = -(1/mol.p2.m)*force
    mol.p1.vel += acc1 * dt
    mol.p2.vel += acc2 * dt
    mol.p1.pos += mol.p1.vel*dt
    mol.p2.pos += mol.p2.vel*dt


#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
