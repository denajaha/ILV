'''
@Author: Uros Miljkovic 123598
create 5 different instances of the ITFs (create 5 different lookup tables by calling the function 5 times
with the given different parameter) and map the image with these 5 ITFs, with these values for
parameter 𝛾: 0.25, 0.5, 1.0, 1.5, 2.0
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
from second import compute_itf

# Load the image
image = cv2.imread('ABD_CT.jpg', cv2.IMREAD_GRAYSCALE)

# Define intensity values
intensity_values = np.arange(256) / 255.0  # Range of 0 to 1 with 256 values

# Define gamma values
gamma_values = [0.25, 0.5, 1.0, 1.5, 2.0]

# Create a subplot grid for displaying the images
num_plots = len(gamma_values) + 1
rows = (num_plots // 2) + (num_plots % 2)
cols = 2
fig, axes = plt.subplots(rows, cols, figsize=(10, 10))

# Display the original image
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

# Iterate over the gamma values
for i, gamma in enumerate(gamma_values):
    # Compute ITF lookup table
    itf_lookup_table = compute_itf(intensity_values, gamma)

    # Map intensity values of the image using ITF lookup table
    mapped_image = itf_lookup_table[image]

    # Convert mapped image back to appropriate datatype and value range
    mapped_image = (mapped_image * 255).astype(np.uint8)

    # Display the mapped image
    row = (i + 1) // cols
    col = (i + 1) % cols
    axes[row, col].imshow(mapped_image, cmap='gray')
    axes[row, col].set_title(f'Gamma = {gamma}')
    axes[row, col].axis('off')

# Hide empty subplots if any
if num_plots < rows * cols:
    for i in range(num_plots, rows * cols):
        axes[i // cols, i % cols].axis('off')

# Adjust spacing and display the plots
plt.tight_layout()
plt.show()

'''
In this updated code, we iterate over the gamma values [0.25, 0.5, 1.0, 1.5, 2.0]. 
For each gamma value, we compute a new ITF lookup table, map the intensity values of the image using that ITF, and display the resulting mapped image alongside the original image.

The images will be displayed in a grid layout, with the first column reserved for the original image. 
Each subsequent column will display the mapped image corresponding to a specific gamma value.
'''