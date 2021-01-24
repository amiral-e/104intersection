##
## EPITECH PROJECT, 2020
## Untitled (Workspace)
## File description:
## test_classes
##

import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from src.classes import *


class TestClasses(TestCase):
    def test_vector(self):
        v0 = vector(1, 2, 3)

        self.assertEqual(v0.x, 1)
        self.assertEqual(v0.y, 2)
        self.assertEqual(v0.z, 3)

    def test_avc(self):
        av = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        avs = avc(av)

        self.assertEqual(avs.opt, 1)
        self.assertEqual(avs.xp, 2)
        self.assertEqual(avs.yp, 3)
        self.assertEqual(avs.zp, 4)
        self.assertEqual(avs.xv, 5)
        self.assertEqual(avs.yv, 6)
        self.assertEqual(avs.zv, 7)
        self.assertEqual(avs.p, 8)

    def test_avc_error(self):
        av = [0, 1, 2, "c", 4, 5, 6, 7, 8]

        with self.assertRaises(SystemExit) as cm:
            avc(av)
        self.assertEqual(cm.exception.code, 84)
