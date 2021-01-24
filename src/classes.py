##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## classes
##

from src.errors_man import errors


class vector:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z


class avc:
    def __init__(self, av):
        try:
            self.opt = int(av[1])
            self.xp = int(av[2])
            self.yp = int(av[3])
            self.zp = int(av[4])
            self.xv = int(av[5])
            self.yv = int(av[6])
            self.zv = int(av[7])
            self.p = int(av[8])
        except ValueError:
            exit(errors(3, len(av)))
