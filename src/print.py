##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## print
##


def print_surface(avs):
    if avs.opt == 1:
        print(f"Sphere of radius {avs.p}")
    elif avs.opt == 2:
        print(f"Cylinder of radius {avs.p}")
    else:
        print(f"Cone with a {avs.p} degree angle")
    print("Line passing through the point ", end="")
    print(f"({avs.xp}, {avs.yp}, {avs.zp}) ", end="")
    print("and parallel to the vector ", end="")
    print(f"({avs.xv}, {avs.yv}, {avs.zv})")


def print_inters1(v0):
    print("1 intersection point:")
    print(f"({v0.x:.3f}, {v0.y:.3f}, {v0.z:.3f})")


def print_inters2(v1, v2):
    print("2 intersection points:")
    print(f"({v1.x:.3f}, {v1.y:.3f}, {v1.z:.3f})")
    print(f"({v2.x:.3f}, {v2.y:.3f}, {v2.z:.3f})")
