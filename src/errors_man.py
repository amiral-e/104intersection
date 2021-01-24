##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## errors_man.py
##

import os
from sys import argv, stderr
from src.constants import (
    INVALID_NB_ARGS,
    INVALID_ARG,
    INVALID_SURF,
    INVALID_VECT,
    INVALID_P,
    INVALID_P2,
    DIV_ZERO,
)


def usage(choice):
    if choice == 1:
        print("Usage: ./104intersection opt xp yp zp xv yv zv p")
        return 84
    else:
        S1 = "\t\t    "
        S2 = "    "
        print(f"USAGE\n{S2}./104intersection opt xp yp zp xv yv zv p\n")
        print("DESCRIPTION")
        print(f"{S2}opt{S1}surface option: 1 for a sphere, ", end="")
        print("2 for a cylinder, 3 for a cone")
        print(f"{S2}(xp, yp, zp){S2}coordinates of a point by ", end="")
        print("which the light ray passes through")
        print(f"{S2}(xv, yv, zv){S2}coordinates of a vector ", end="")
        print("parallel to the light ray")
        print(f"{S2}p{S1}parameter: radius of the sphere, radius ", end="")
        print("of the cylinder, or angle formed by the cone and the Z-axis")
        return 0


def errors(choice, ac):
    if choice == 1:
        return usage(ac)
    error_mess = [
        INVALID_NB_ARGS,
        INVALID_ARG,
        INVALID_SURF,
        INVALID_VECT,
        INVALID_P,
        INVALID_P2,
        DIV_ZERO,
    ]
    print(error_mess[choice - 2], file=stderr)
    return 84
