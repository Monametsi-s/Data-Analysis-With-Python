#install specific version of libraries used in lab
#! mamba install pandas==1.3.3
#! mamba install numpy=1.21.2

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyodide.http import pyfetch


async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())
    else:
        raise Exception(f"Download failed with status {response.status}")