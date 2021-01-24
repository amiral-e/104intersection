##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_print
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.print import *


class vector:
    def __init__(self, x: float = 0.0, y: float = 0.0, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z


class avc:
    def __init__(self, av):
        self.opt = int(av[1])
        self.xp = int(av[2])
        self.yp = int(av[3])
        self.zp = int(av[4])
        self.xv = int(av[5])
        self.yv = int(av[6])
        self.zv = int(av[7])
        self.p = int(av[8])


class TestPrint(TestCase):
    def test_print_surface_sphere(self):
        av = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        avs = avc(av)
        expected = "Sphere of radius 8\n"
        expected += "Line passing through the point (2, 3, 4)"
        expected += " and parallel to the vector (5, 6, 7)\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print_surface(avs)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_surface_cylinder(self):
        av = [0, 2, 2, 3, 4, 5, 6, 7, 8]
        avs = avc(av)
        expected = "Cylinder of radius 8\n"
        expected += "Line passing through the point (2, 3, 4)"
        expected += " and parallel to the vector (5, 6, 7)\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print_surface(avs)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_surface_cone(self):
        av = [0, 3, 2, 3, 4, 5, 6, 7, 8]
        avs = avc(av)
        expected = "Cone with a 8 degree angle\n"
        expected += "Line passing through the point (2, 3, 4)"
        expected += " and parallel to the vector (5, 6, 7)\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print_surface(avs)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_inters1(self):
        v0 = vector(0, 0, 0)
        expected = "1 intersection point:\n"
        expected += "(0.000, 0.000, 0.000)\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print_inters1(v0)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_print_inters2(self):
        v1 = vector(0, 0, 0)
        v2 = vector(1, 1, 1)
        expected = "2 intersection points:\n"
        expected += "(0.000, 0.000, 0.000)\n"
        expected += "(1.000, 1.000, 1.000)\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            print_inters2(v1, v2)
        self.assertEqual(mock_stdout.getvalue(), expected)
