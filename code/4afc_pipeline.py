import os
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from modules.prepro import prepro

dataroot = Path("../data/test/4afc")
prepro(dataroot)

data = pd.read_csv(f"{dataroot}/4afc_all.csv")
