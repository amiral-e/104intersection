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
from src.constants import *


class TestConstants(TestCase):
    def test_constants(self):
        self.assertEqual(EXIT_SUCCESS, 0)
        self.assertEqual(EXIT_FAILURE, 84)
        self.assertEqual(NB_ARGS, 9)
        self.assertEqual(INVALID_NB_ARGS, "Invalid number of arguments")
        self.assertEqual(INVALID_SURF, "Invalid surface")
        self.assertEqual(INVALID_ARG, "Invalid argument")
        self.assertEqual(INVALID_VECT, "Invalid vector, can't be null")
        self.assertEqual(INVALID_P, "Invalid p, can't be lower or equal to 0")
        self.assertEqual(INVALID_P2,
            "Invalid p, can't be lower than -90 or higher than 90")
