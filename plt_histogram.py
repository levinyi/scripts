import matplotlib.pyplot as plt
import numpy as np
import matplotlib

data = np.random.randn(10000)
print(data)
plt.hist(data, bins=50, normed=0, facecolor="blue", edgecolor="black", alpha=0.7)
plt.show()
