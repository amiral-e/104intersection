##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_errors.py
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.errors_man import *


class TestErrors(TestCase):
    def test_usage_one(self):
        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            usage(1)
        self.assertEqual(mock_stdout.getvalue(),
            "Usage: ./104intersection opt xp yp zp xv yv zv p\n")

    def test_usage_h(self):
        expected = "USAGE\n    ./104intersection opt xp yp zp xv yv zv p\n"
        expected += "\nDESCRIPTION\n"
        expected += "    opt\t\t    surface option: 1 for a sphere, 2 for a cylinder, 3 for a cone\n"
        expected += "    (xp, yp, zp)    coordinates of a point by which the light ray passes through\n"
        expected += "    (xv, yv, zv)    coordinates of a vector parallel to the light ray\n"
        expected += "    p\t\t    parameter: radius of the sphere, radius of the cylinder, "
        expected += "or angle formed by the cone and the Z-axis\n"

        with patch("sys.stdout", new=StringIO()) as mock_stdout:
            usage(0)
        self.assertEqual(mock_stdout.getvalue(), expected)

    def test_return(self):
        self.assertEqual(errors(1, 1), 84)
        self.assertEqual(errors(1, 2), 0)
        self.assertEqual(errors(2, 0), 84)
        self.assertEqual(errors(3, 0), 84)
        self.assertEqual(errors(4, 0), 84)
        self.assertEqual(errors(5, 0), 84)
        self.assertEqual(errors(6, 0), 84)
        self.assertEqual(errors(7, 0), 84)
