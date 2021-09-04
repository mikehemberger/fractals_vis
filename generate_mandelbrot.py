""" 
Generate mandelbrot set using complex matrices 
(see https://de.wikipedia.org/wiki/Mandelbrot-Menge)

"""

# Imports 
import numpy as np
import matplotlib.pyplot as plt

# Pixeldensity, width and height (original example)
w, h = 800, 600
w, h = 128-1, 64-1  # adjusted for oled display

# Max number iterations and "Fluchtradius" (r > 2) (original example)
n, r = 100, 2.5
n, r = 10, 2.5  # adjusted for faster testing

# Evaluation grid
x = np.linspace(0, 2, num=w+1)
y = np.linspace(0, 2 * h / w, num=h+1)

A, B = np.meshgrid(x - 1, y - h / w)
C = 2.0 * (A + B * 1j) - 0.5

Z = np.zeros_like(C)
T = np.zeros(C.shape)

# Iteration
for k in range(n):
    M = abs(Z) < r
    T[M] = T[M] + 1
    Z[M] = Z[M] ** 2 + C[M]

# Normalize (min-max > [0,1])
T_norm = T ** 0.5
T_norm = (T_norm - np.min(T_norm)) / (np.max(T_norm) - np.min(T_norm))
T_norm = T_norm.astype("int")

# Visualize Mandelbrot
figsize = (4, 4)
cmap = plt.cm.twilight_shifted  # plt.cm.magma_r / plt.cm.twilight_shifted

plt.figure(figsize=figsize)
plt.imshow(T_norm, interpolation="nearest", cmap=cmap)
plt.axis("off")

# Save to image file
plt.imsave("mandelbrot_img_128x64.jpg", T_norm)
