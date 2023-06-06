'''
Another thing you should try out is to pick 2 slices which are 2 slices apart (meaning in between them
is exactly one other slice), e.g., slice number 73 and 75, and reconstruct the in-between slice by
interpolating the two slices, since you also have the original slice 74 (which can be considered the
ground truth) you can compare your reconstructed slice to the true slice and draw conclusions from it.
What are your findings?
'''

import numpy as np
import matplotlib.pyplot as plt

# Load the volume dataset
npz = np.load('volume.npz')
vol = npz['arr_0']
vol = vol.transpose((2, 0, 1))

# Select the slices for interpolation
slice_index_1 = 72  # First slice
slice_index_2 = 74  # Second slice
slice_index_3 = 76  # Third slice (ground truth)

# Extract the slices
slice_1 = vol[slice_index_1, :, :]
slice_2 = vol[slice_index_2, :, :]
slice_ground_truth = vol[slice_index_3, :, :]

# Perform linear interpolation between the slices
interpolated_slice = 0.5 * (slice_1 + slice_2)

# Plot the original slices
plt.figure(figsize=(12, 9))
plt.subplot(131)
plt.imshow(slice_1, cmap='gray')
plt.title('Slice 1')

plt.subplot(132)
plt.imshow(slice_2, cmap='gray')
plt.title('Slice 2')

plt.subplot(133)
plt.imshow(slice_ground_truth, cmap='gray')
plt.title('Ground Truth (Slice 3)')
plt.tight_layout()
plt.show()

# Plot the interpolated slice
plt.figure(figsize=(12, 9))
plt.subplot(121)
plt.imshow(interpolated_slice, cmap='gray')
plt.title('Interpolated Slice')

plt.subplot(122)
plt.imshow(slice_ground_truth, cmap='gray')
plt.title('Ground Truth (Slice 3)')
plt.tight_layout()
plt.show()

# Compute the mean squared error (MSE) between the interpolated slice and the ground truth
mse = np.mean((interpolated_slice - slice_ground_truth) ** 2)
print(f"Mean Squared Error (MSE): {mse}")

'''
In this modified script, we interpolate between slice 72 and slice 74, and compare the reconstructed slice with the 
ground truth slice, which is slice 76. We use linear interpolation to estimate the in-between slice.

The script will display three figures:

The first figure shows slice 72.
The second figure shows slice 74.
The third figure shows the ground truth slice, which is slice 76.
The fourth figure compares the interpolated slice with the ground truth slice.

By comparing the interpolated slice with the ground truth slice, we can draw conclusions about the accuracy of the 
interpolation. A lower mean squared error (MSE) value indicates a closer match between the interpolated slice and the 
ground truth slice. A higher MSE value indicates a larger discrepancy between the two.

You can examine the MSE value printed in the console to quantify the difference between the interpolated slice and 
the ground truth slice. A lower MSE suggests a better estimate, while a higher MSE indicates a larger deviation.

Feel free to modify the slice indices to explore different pairs of slices and observe the results.
'''