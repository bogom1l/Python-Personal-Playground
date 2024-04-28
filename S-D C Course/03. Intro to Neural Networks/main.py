#classification
#linear model
#perceptions
#weights
####################################################

import numpy as np
import matplotlib.pyplot as plt

number_of_points = 100
np.random.seed(0) # every time generates same random numbers
top_region = np.array([np.random.normal(10, 2, number_of_points), np.random.normal(12, 2, number_of_points)]).T
bottom_region = np.array([np.random.normal(5, 2, number_of_points), np.random.normal(6, 2, number_of_points)]).T
_, ax = plt.subplots(figsize=(4, 4))
ax.scatter(top_region[:, 0], top_region[:, 1], color='r')
ax.scatter(bottom_region[:, 0], top_region[:, 1], color='b')
plt.show()
