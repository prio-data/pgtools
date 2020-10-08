"""
Tests for conversion tools.
"""

import unittest
import numpy as np

from pgtools.conversion import idToIdx,pgidToIdx,longformToSparseMatrices,domToDense
from pgtools.constants import EXTENT

class TestConv(unittest.TestCase):
    def test_id_map(self):
        """
        Test id mapping, from PGid (lower-left id mapped)
        to matrix indices (top left [0,0] bottom right [n,n]) 
        """

        txext = 3
        tyext = 6
        testext = lambda id: idToIdx(id,(txext,tyext))
        self.assertEqual(testext(1),(2,0))
        self.assertEqual(testext(18),(0,5))

        xext,yext = EXTENT
        self.assertEqual(pgidToIdx(1),(xext-1,0))
        self.assertEqual(pgidToIdx(xext*yext),(0,yext-1))


    def test_longform_conv(self):
        maxid = EXTENT[0] * EXTENT[1]

        """
        Spatial positioning
        """

        mockdata = [
                (1,1,1),
                (2,2,1),
                (3,3,1),
                (maxid,9,1),
                (maxid-1,8,1),
        ]
        mat = longformToSparseMatrices(mockdata)
        self.assertEqual(mat[1][-1,0], 1)
        self.assertEqual(mat[1][-1,1], 2)
        self.assertEqual(mat[1][-1,2], 3)
        self.assertEqual(mat[1][0,-1], 9)
        self.assertEqual(mat[1][0,-2], 8)

        """
        Temporal positioning
        """

        mockdata = [
                (1,1,2),
                (maxid,2,2),
                (1,8,4),
                (maxid,9,4),
        ]

        mat = longformToSparseMatrices(mockdata)
        self.assertEqual(mat[2][359,0], 1)
        self.assertEqual(mat[2][0,719], 2)
        self.assertEqual(mat[4][359,0], 8)
        self.assertEqual(mat[4][0,719], 9)

        """
        As dense
        """

        dense = domToDense(mat)

        self.assertEqual(dense[0,-1,0],1)
        self.assertEqual(dense[0,0,-1],2)

        self.assertEqual(dense[2,-1,0],8)
        self.assertEqual(dense[2,0,-1],9)
