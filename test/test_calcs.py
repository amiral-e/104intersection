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
from src.calcs import *
from src.classes import avc


class TestCalcs(TestCase):
    def test_get_vect(self):
        av = [0, 1, 0, 0, 2, 1, 1, 0, 1]
        avs = avc(av)
        vect = get_vect(avs, 2)

        self.assertEqual(vect.x, 2)
        self.assertEqual(vect.y, 2)
        self.assertEqual(vect.z, 2)

    def test_sphere_0(self):
        av = [0, 1, 0, 0, 2, 1, 1, 0, 1]
        avs = avc(av)
        expected = "No intersection point.\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            sphere(avs)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_sphere_1(self):
        av = [0, 1, 4, 0, 3, 0, 0, -2, 4]
        avs = avc(av)
        expected = "1 intersection point:\n"
        expected += "(4.000, 0.000, 0.000)\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            sphere(avs)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_cylinder_2(self):
        av = [0, 2, 0, 0, 2, 1, 1, 0, 1]
        avs = avc(av)
        expected = "2 intersection points:\n"
        expected += "(0.707, 0.707, 2.000)\n"
        expected += "(-0.707, -0.707, 2.000)\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            cylinder(avs)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_cylinder_f(self):
        av = [0, 2, 1, 0, 0, 0, 0, 1, 1]
        avs = avc(av)
        expected = "There is an infinite number of intersection points.\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            cylinder(avs)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_cone_2(self):
        av = [0, 3, -1, -1, -1, 1, 1, 5, 30]
        avs = avc(av)
        expected = "2 intersection points:\n"
        expected += "(-1.568, -1.568, -3.842)\n"
        expected += "(-0.537, -0.537, 1.315)\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            cone(avs)
        self.assertEqual(mock_stdout.getvalue(), expected)
