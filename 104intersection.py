#!/usr/bin/python3

##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## 104intersection
##

import os
from sys import argv
from src.errors_man import errors
from src.constants import NB_ARGS, EXIT_FAILURE
from src.classes import avc, vector
from src.calcs import get_vect, sphere, cylinder, cone
from src.print import print_surface


def check_args(ac, av):
    if ac == 1 or (ac == 2 and av[1] == "-h"):
        exit(errors(1, ac))
    elif ac != NB_ARGS:
        exit(errors(2, ac))
    avs = avc(av)
    if avs.opt not in [1, 2, 3]:
        exit(errors(4, ac))
    if avs.xp == 0 and avs.yp == 0 and avs.zp == 0:
        exit(errors(5, ac))
    if avs.opt in [1, 2, 3] and avs.p <= 0:
        exit(errors(6, ac))
    return avs


def main(ac, av):
    avs = check_args(ac, av)
    print_surface(avs)
    if avs.opt == 1:
        sphere(avs)
    elif avs.opt == 2:
        cylinder(avs)
    else:
        cone(avs)


main(len(argv), argv)
