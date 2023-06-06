'''
also try out 2 slices that are non-consecutive, e.g. 20 slices apart – what do the interpolated slices
look like – are the interpolated pixel values good estimates for the intermediate intensity values of
the volume? Why is it a good or bad estimate?
'''

'''
When selecting two slices that are non-consecutive and further apart, the interpolated slices may not provide accurate
 estimates for the intermediate intensity values of the volume. This is because linear interpolation assumes a linear 
 relationship between the two slices, which may not hold true for non-consecutive slices that are distant from each 
 other.'''

import numpy as np
import matplotlib.pyplot as plt

# Load the volume dataset
npz = np.load('volume.npz')
vol = npz['arr_0']
vol = vol.transpose((2, 0, 1))

# Select the slices for interpolation
slice_index_1 = 50  # Starting slice
slice_index_2 = 70  # Non-consecutive slice

# Specify the number of slices to be interpolated
num_slices = 8

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

'''
In this modified script (in regards to subtask 4), we have selected two slices that are 20 slices apart 
(slice_index_1 = 50 and slice_index_2 = 70).
You can observe that the interpolated slices between these non-consecutive slices may not accurately represent the 
intermediate intensity values of the volume. The reason for this is that the assumption of a linear relationship 
between distant slices may not hold true for the underlying data.

Linear interpolation assumes a linear change in intensity values between the two slices, which may not capture the 
complex and non-linear variations that can occur in volumetric data. Therefore, the interpolated pixel values may
not be good estimates for the intermediate intensity values in such cases.

It's important to note that the effectiveness of linear interpolation depends on the nature of the data and the 
specific context of the application. In some cases, linear interpolation may provide reasonable estimates, 
while in others, more advanced interpolation techniques or domain-specific knowledge may be required.

If the interpolation between non-consecutive slices is necessary, alternative interpolation methods like spline 
interpolation or higher-order interpolation techniques could be explored to potentially achieve better results.'''