'''
visualize the 2 slices to be interpolated, as well as the 5 interpolated slices in individual figures and make the
figures open in full screen size (to make it easier to compare them when switching through the window tabs)
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

# Extract the slices
slice_1 = vol[slice_index_1, :, :]
slice_2 = vol[slice_index_2, :, :]

# Specify the number of slices to be interpolated
num_slices = 5

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

# Plot the first slice
plt.figure(figsize=(12, 9))
plt.imshow(slice_1, cmap='gray')
plt.title('Slice 1')
plt.show()

# Plot the second slice
plt.figure(figsize=(12, 9))
plt.imshow(slice_2, cmap='gray')
plt.title('Slice 2')
plt.show()

# Plot the interpolated slices
for i in range(num_slices):
    plt.figure(figsize=(12, 9))
    plt.imshow(interpolated_slices[i], cmap='gray')
    plt.title(f'Interpolated Slice {i + 1}')
    plt.show()
