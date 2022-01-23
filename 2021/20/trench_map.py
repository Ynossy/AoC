#%%
import numpy as np
from scipy.signal import convolve2d
from time import perf_counter

file = "input.txt"
# file = "example.txt"


def enhance(file, t):
    start = perf_counter()

    with open(file) as f:
        lines = f.readlines()
    enhancement = np.array([1 if y == "#" else 0 for y in lines[0].strip()])
    image = np.array([[1 if y == "#" else 0 for y in x.strip()] for x in lines[2:]])

    # flipped bit mask for convolution
    kernel = np.reshape([2 ** x for x in range(9)], (3, 3))

    # TASK enhancement: index 0 = LIGHT, index 511 = DARK-> need to flip fillvalue every time
    for i in range(t):
        fill = i % 2 if file == "input.txt" else 0  # fillvalue=0 for example
        enhancement_index = convolve2d(
            image, kernel, "full", boundary="fill", fillvalue=fill
        )
        image = enhancement[enhancement_index]

    print(f"Runtime: {perf_counter()-start}")
    return image


# part 1
image = enhance(file, 2)
print(f"Part 1 - Pixels Lit: {np.sum(image)}")

# part 2
image = enhance(file, 50)
print(f"Part 2 - Pixels Lit: {np.sum(image)}")

# %%
