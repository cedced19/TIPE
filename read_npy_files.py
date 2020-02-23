import argparse
import numpy as np

np_load_old = np.load
np.load = lambda *a,**k: np_load_old(*a, allow_pickle=True, **k)

parser = argparse.ArgumentParser()
parser.add_argument("path", help="give the path to read",type=str)
args = parser.parse_args()
print(np.load(args.path))