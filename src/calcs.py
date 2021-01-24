##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## calcs
##

from math import sqrt, tan, radians
from src.classes import vector
from src.errors_man import errors
from src.print import print_inters1, print_inters2


def get_vect(avs, x):
    return vector(avs.xv * x + avs.xp, avs.yv * x + avs.yp,
        avs.zv * x + avs.zp)


def sphere(avs):
    a = (avs.xv ** 2) + (avs.yv ** 2) + (avs.zv ** 2)
    b = (2 * avs.xv * avs.xp) + (2 * avs.yv * avs.yp) + (2 * avs.zv * avs.zp)
    c = ((avs.xp ** 2) + (avs.yp ** 2) + (avs.zp ** 2)) - (avs.p ** 2)
    delta = b ** 2 - (4 * a * c)

    if delta > 0:
        v1 = get_vect(avs, (float(-b) + float(sqrt(delta))) / (2 * float(a)))
        v2 = get_vect(avs, (float(-b) - float(sqrt(delta))) / (2 * float(a)))
        print_inters2(v1, v2)
    elif delta == 0:
        if ((2 * float(a)) == 0):
            exit(errors(8, 1))
        v0 = get_vect(avs, (-float(b)) / (2 * float(a)))
        print_inters1(v0)
    else:
        print("No intersection point.")


def cylinder(avs):
    a = (avs.xv ** 2) + (avs.yv ** 2)
    b = (2 * avs.xv * avs.xp) + (2 * avs.yv * avs.yp)
    c = ((avs.xp ** 2) + (avs.yp ** 2)) - (avs.p ** 2)
    delta = (b) ** 2 - (4 * a * c)

    if delta > 0:
        v1 = get_vect(avs, float(-b + sqrt(delta)) / (2 * a))
        v2 = get_vect(avs, float(-b - sqrt(delta)) / (2 * a))
        print_inters2(v1, v2)
    elif delta == 0:
        if float(a) != 0:
            v0 = get_vect(avs, (-float(b)) / (2 * float(a)))
            print_inters1(v0)
        else:
            print("There is an infinite number of intersection points.")
    else:
        print("No intersection point.")


def cone(avs):
    a = (avs.xv) ** 2 + (avs.yv) ** 2
    a -= (avs.zv) ** 2 * tan(radians(avs.p)) ** 2
    b = (2 * avs.xv * avs.xp) + (2 * avs.yv * avs.yp)
    b -= (2 * avs.zv * avs.zp) * tan(radians(avs.p)) ** 2
    c = (avs.xp) ** 2 + (avs.yp) ** 2
    c -= (avs.zp) ** 2 * tan(radians(avs.p)) ** 2
    delta = (b) ** 2 - (4 * a * c)

    if delta > 0:
        v1 = get_vect(avs, float(-b + sqrt(delta)) / (2 * a))
        v2 = get_vect(avs, float(-b - sqrt(delta)) / (2 * a))
        print_inters2(v1, v2)
    elif delta == 0:
        if float(a) != 0:
            v0 = get_vect(avs, (-float(b)) / (2 * float(a)))
            print_inters1(v0)
        else:
            print("There is an infinite number of intersection points.")
    else:
        print("No intersection point.")
