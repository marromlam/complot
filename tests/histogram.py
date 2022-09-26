import numpy as np
from complot import hist


x = np.random.rand(10000)


h1 = np.histogram(x)
h2 = hist(x)
if np.sum(h1[0]-h2.counts) > 1e-8:
  raise ValueError("Histogram function is not working properly.")


h1 = np.histogram(x, density=True)
h2 = hist(x, density=True)
if np.sum(h1[0]-h2.counts) > 1e-8:
  raise ValueError("Histogram function with density is not working properly.")
