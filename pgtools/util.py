
import csv

def writecsv(lot,fname):
    with open(fname,"w") as f:
        w = csv.writer(f)
        for r in lot:
            w.writerow(r)

