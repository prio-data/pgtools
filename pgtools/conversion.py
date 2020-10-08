from operator import mul
from functools import reduce
import math

import numpy as np
from scipy.sparse import lil_matrix,csc_matrix

from pgtools.constants import EXTENT 

def idToIdx(id,extent):
    xext,yext = extent
    x = (xext - (id-1) // yext)-1
    y = ((id-1) % yext)
    return (x,y)

pgidToIdx = lambda pgid: idToIdx(pgid,EXTENT)

def longformToSparseMatrices(iterable):
    """
    Convert long form data (list of tuples, where each tuple corresponds to a
    "coordinate" of pgid,val,year) into a year-dict of sparse matrices. 
    """
    blank = lambda: lil_matrix(EXTENT)
    matrices = {}
    for r in iterable:
        pgid,val,year = (int(v) for v in r)
        try:
            base = matrices[year]
        except KeyError:
            base = blank()
            matrices[year] = base 
        base[pgidToIdx(pgid)] = val

    matrices = {k:csc_matrix(v) for k,v in matrices.items()}
    return matrices

def domToDense(dom):
    """
    Dictionary of sparse matrices to dense matrix
    """
    zmin,zmax = min(dom.keys()),max(dom.keys())

    base = []

    for i in range(zmin,zmax+1):
        try:
            base.append(dom[i].todense())
        except KeyError:
            base.append(np.zeros(EXTENT))

    return np.array(base)


