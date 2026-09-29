import numpy as np
import matplotlib.pyplot as plt

LAMBDA = 0.3

# TODO 1
data = np.loadtxt("decay_observed.csv", delimiter=",", skiprows=1)
t = data[:, 0]
observed = data[:, 1]

# TODO 2
N0 = observed[0]
analytical = N0 * np.exp(-LAMBDA * t)

# TODO 3
fig, ax = plt.subplots(1, 2, sharex=True, sharey=True)

ax[0].scatter(t, observed)
ax[0].set_title("Observed data")

ax[1].plot(t, analytical)
ax[1].set_title("Analytical")

ax[0].set_xlabel("Time")
ax[1].set_xlabel("Time")
ax[0].set_ylabel("Count")

# TODO 4
plt.savefig("figure.png")