"""
Functions for interacting with the Priogrid API
"""

import textwrap
import csv
import os
import requests

BASE_URL = "http://grid.prio.org/api/"

def lodToLot(lod):
    """
    list of dicts to list of tuples
    """
    lot = []
    lot.append(tuple(lod[0].keys()))
    for d in lod[1:]:
        lot.append(tuple(d.values()))
    return lot


def getvar(vname):
    dest = os.path.join(BASE_URL,"data",vname)
    r = requests.get(dest)

    if r.status_code != 200:
        raise requests.exceptions.HTTPError(r.status_code)

    
    data = r.json()

    return lodToLot(data["cells"]) 

def getmeta():
    dest = os.path.join(BASE_URL,"variables")
    r = requests.get(dest)
    return r.json()


