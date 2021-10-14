import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
print(pd.__doc__)
x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)