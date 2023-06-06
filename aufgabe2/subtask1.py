'''
Write a Python script that does linear interpolation between slices of the provided volume dataset:
• Load the volume dataset provided named volume.npz (which is a compressed numpy file format for
storing ndarrays) by using these commands:
npz = np.load('volume.npz')
vol = npz.f.arr_0
vol = vol.transpose((2, 0, 1))
This will give you the volume in a 3-dimensional ndarray, where the 1st axis is the z-axis, the 2nd axis
is the y-axis and the 3rd axis is the x-axis – therefore allowing you to select the e.g. 64th slice by
indexing with vol[63, :, :]
'''

import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the volume dataset
npz = np.load('volume.npz')
vol = npz['arr_0']
vol = vol.transpose((2, 0, 1))

# Select the 64th slice
slice_index = 63
slice_data = vol[slice_index, :, :]

# Perform linear interpolation between adjacent slices
previous_slice = vol[slice_index - 1, :, :]
next_slice = vol[slice_index + 1, :, :]

# Perform linear interpolation
'''
For linear interpolation, the addWeighted function from Python-OpenCV is used, which blends the intensity values of the 
previous and next slices with equal weights (0.5 each). Feel free to adjust the interpolation parameters based on your 
requirements.
'''
interpolated_slice = cv2.addWeighted(previous_slice, 0.5, next_slice, 0.5, 0)

# Plot original and interpolated slices
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(previous_slice, cmap='gray')
axs[0].set_title('Previous Slice')

axs[1].imshow(slice_data, cmap='gray')
axs[1].set_title('Selected Slice')

axs[2].imshow(next_slice, cmap='gray')
axs[2].set_title('Next Slice')

fig.tight_layout()
plt.show()
