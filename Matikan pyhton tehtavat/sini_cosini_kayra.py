import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6.4 * 3, 4.8))

X = np.linspace(-np.pi*3, np.pi*3, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X, C, color='blue', linestyle='--', label='Cosini')
plt.plot(X, S, color='orange', linestyle='--', label='Sini')

plt.xticks(
    [-3 * np.pi, -2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi, 3 * np.pi],
    [r'$-3\pi$', r'$-2\pi$', r'$-\pi$', r'$0$', r'$\pi$', r'$2\pi$', r'$3\pi$']
)

plt.show()