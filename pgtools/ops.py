import textwrap
import csv
import numpy as np
from pgtools.remote import getvar,getmeta
from pgtools.util import writecsv,correctRow
from pgtools.conversion import longformToSparseMatrices,domToDense
import sys

_FORMATS = {
   "long": (lambda x: x, writecsv) 
}

def download(vname,out=sys.stdout,format=None):
   if format is None:
      format = "long"

   converter,writer = _FORMATS[format]

   data = getvar(vname)
   data = converter(data)
   writer(data,out)

def convert(infile,outfile,tofmt="numpy"):
    with open(infile) as f:
        reader = csv.reader(f)
        _ = next(reader)
        reader = (correctRow(r) for r in reader)
        sparsemat = longformToSparseMatrices(reader)
        dense = domToDense(sparsemat)
    np.save(outfile,dense)

def list():
    def formatMeta(m):
        delim = "#"*52
        sep = "="*32
        need = [
                "unit","type","category",
                "startYear","endYear",
                "sourceName","sourceUrl","version"
                ]
        rep = ""
        for s in need:
            rep += f"\t{s}: {m[s]}\n"

        descr = "\n".join(["\t"+ln for ln in textwrap.wrap(m['description'],52)])
        return (
            f"\t{delim}\n\n"
            f"\t*** {m['displayName']} ({m['name']}) - {m['id']}\n\n"
            f"\t{sep}\n\n"
            f"{descr}\n\n"
            f"\t{sep}\n\n"
            f"{rep}"
        )
    for e in getmeta():
        print(formatMeta(e))
