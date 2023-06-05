from sympy import *
import math
import pickle
import os.path
from os import path



#These two functions put and load in memory. Additionally,
#They memoize to avoid stupid retrievals during program
#runtime. All mems are expected to be globally invairant

resources = {}

def mem_get(file_name):
    if file_name in resources:
        return resources[file_name]
    else:
        if path.exists(file_name):
            with open(file_name) as file:
                temp = pickle.load(file)
                resources[file_name] = temp
                return temp
        else:
            return 0


def mem_put(obj, file_name):
    if file_name not in resources and not path.exists(file_name):
        resources[file_name] = obj
        with open(file_name, 'wb') as file:
            pickle.dump(obj, file)
    

    return 0
