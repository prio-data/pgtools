
import csv
import numpy as np

def writecsv(lot,fname):
    with open(fname,"w") as f:
        w = csv.writer(f)
        for r in lot:
            w.writerow(r)

def correctRow(row):
    return tuple((int(float(v)) for v in row))

def serialChunks(series):
    prev = (series-np.roll(series,1))
    chunkstarts = ((prev)!=1).nonzero()[0]
    chunkends = np.concatenate([
        np.roll(chunkstarts,-1)[:-1],
        [series.shape[0]]
        ])
    chunks = [(s,e) for s,e in zip(chunkstarts,chunkends)]
    return [series[slice(*ch)] for ch in chunks]

def moduloChunks(series,n):
    chunkends = ((series % n) == 0).nonzero()[0]
    chunkstarts = np.concatenate([[0],chunkends+1])
    chunkends = np.concatenate([chunkends+1,[series.shape[0]]])
    chunks = [(s,e) for s,e in zip(chunkstarts,chunkends)]
    if chunkends[-1] == series.shape[0]:
        chunks = chunks[:-1]
    return [series[slice(*ch)] for ch in chunks]
