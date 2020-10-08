
import unittest
import numpy as np
from pgtools.util import serialChunks,moduloChunks

class TestChunking(unittest.TestCase):
    def test_serial(self):
        array = np.array([1,2,3,5,6,7,9,10,11])
        chunked = serialChunks(array)
        np.testing.assert_array_equal(chunked,[
            [1,2,3],
            [5,6,7],
            [9,10,11],
            ])

    def test_modulo(self):
        array = np.array([1,2,3,4,5,6,7,8,9])
        chunked = moduloChunks(array,3)
        np.testing.assert_array_equal(chunked,[
            [1,2,3],
            [4,5,6],
            [7,8,9],
            ])



