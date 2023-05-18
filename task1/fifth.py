'''
@Author: Uros Miljkovic 123598
visualize the following things:
1. original image
2. the 5 ITFs as plot (use matplotlib’s plot function, either use the subplot command to put
the 5 plots in different subplots of the same figure or plot all 5 functions in one figure with
different colors, consider also putting a text label next to the curve of the corresponding ITF)
3. the result images (consider using the subplot command)
4.  add titles to the plots and images with the title command

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

# Create a subplot grid for displaying the plots and images
num_plots = len(gamma_values) + 2
rows = (num_plots // 2) + (num_plots % 2)
cols = 2
fig, axes = plt.subplots(rows, cols, figsize=(12, 16))

# Display the original image
axes[0, 0].imshow(image, cmap='gray')
axes[0, 0].set_title('Original Image')
axes[0, 0].axis('off')

# Plot the ITFs
itf_colors = ['r', 'g', 'b', 'c', 'm']
for i, gamma in enumerate(gamma_values):
    # Compute ITF lookup table
    itf_lookup_table = compute_itf(intensity_values, gamma)

    # Plot the ITF
    axes[0, 1].plot(intensity_values, itf_lookup_table, color=itf_colors[i], label=f'Gamma = {gamma}')

axes[0, 1].set_title('Intensity Transfer Functions (ITFs)')
axes[0, 1].legend(loc='lower right')

# Iterate over the gamma values and display the mapped images
for i, gamma in enumerate(gamma_values):
    # Compute ITF lookup table
    itf_lookup_table = compute_itf(intensity_values, gamma)

    # Map intensity values of the image using ITF lookup table
    mapped_image = itf_lookup_table[image]

    # Convert mapped image back to appropriate datatype and value range
    mapped_image = (mapped_image * 255).astype(np.uint8)

    # Display the mapped image
    row = (i + 1) // cols + 1
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
In this updated code, the original image is displayed in the first subplot, 
the ITFs are plotted in the second subplot, and the resulting mapped images are displayed in the subsequent subplots.
Each subplot has an appropriate title using the set_title function. The ITF plots are labeled with the corresponding 
gamma values using different colors for distinction.
Make sure the "ABD_CT.jpg" file is in the same directory as your script, or provide the correct path to the image file.
'''