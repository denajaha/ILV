'''
The process of interpolating between slices is relatively easy – since it comes down to computing intermediate slices by linearly interpolating pixelwise between the pixels at the corresponding pixel positions of the first and second slice (this way, the only axis along which a linear interpolation needs to be performed is the z-axis (note: instead of a bilinear interpolation)):
a) start with picking two (ideally consecutive) slices and compute interpolated slices (pick the 128th and 129th slice as the slices to be interpolated)
b) decide on the number of slices to be generated between those 2 slices, so use a variable to specify this number – a good starting point is to use 5 slices to be interpolated.
c) compute the interpolation weight for every of the slices to be interpolated (your weights have to span the range [0, 1] and need to increase linearly (you can use the np.arange or np.linspace function for this task)
d) a value of 0 will mean that the first picked slice will be weighted with 100% and the
second picked slice with 0%
e) a value of 1 will mean that the first picked slice weighted with 0% and the second
picked slice with 100%
f) a value in between 0 and 1 will weight the 2 slices according to the interpolation
weight.
g) Since the first weight will be 0 and the last weight will be 1, this means the first
interpolated slice should be the same as the 128th slice and the last interpolated slice should be the same as the 129th slice, slices in between should be mixture slices
h) the formula for linear interpolation along one axis is defined as (𝑤 being the weight): 𝑣𝑎𝑙𝑢𝑒(𝑖𝑛𝑡𝑒𝑟𝑝𝑜𝑙𝑎𝑡𝑒𝑑) = (1 − 𝑤) × 𝑣𝑎𝑙𝑢𝑒1 + 𝑤 × 𝑣𝑎𝑙𝑢𝑒2
i) for every slice to be interpolated, compute its interpolated pixel values by performing the linear interpolation pixelwise (use numpy’s vectorized capabilities if possible)
'''

import numpy as np
import matplotlib.pyplot as plt

# Load the volume dataset
npz = np.load('volume.npz')
vol = npz['arr_0']
vol = vol.transpose((2, 0, 1))

# Select the slices for interpolation
slice_index_1 = 127  # 128th slice
slice_index_2 = 128  # 129th slice

# Specify the number of slices to be interpolated
num_slices = 5

# Extract the slices
slice_1 = vol[slice_index_1, :, :]
slice_2 = vol[slice_index_2, :, :]

# Compute the interpolation weight for each slice
weights = np.linspace(0, 1, num_slices + 2)[1:-1]  # Exclude the endpoints

# Initialize the list to store interpolated slices
interpolated_slices = []

# Perform linear interpolation between the slices
for weight in weights:
    # Compute the interpolated slice
    interpolated_slice = (1 - weight) * slice_1 + weight * slice_2

    # Append the interpolated slice to the list
    interpolated_slices.append(interpolated_slice)

# Insert the first and last slices into the list
interpolated_slices.insert(0, slice_1)
interpolated_slices.append(slice_2)

# Plot original slices and interpolated slices
fig, axs = plt.subplots(1, num_slices + 2, figsize=(4 * (num_slices + 2), 4))

# Plot the first slice
axs[0].imshow(slice_1, cmap='gray')
axs[0].set_title('Slice 1')

# Plot the interpolated slices
for i in range(num_slices):
    axs[i + 1].imshow(interpolated_slices[i], cmap='gray')
    axs[i + 1].set_title(f'Interpolated Slice {i + 1}')

# Plot the last slice
axs[-1].imshow(slice_2, cmap='gray')
axs[-1].set_title('Slice 2')

fig.tight_layout()
plt.show()

