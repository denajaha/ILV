'''
@Author: Uros Miljkovic 123598
map the intensity values of the image (the intensity value of every pixel) by applying the ITF (LUT)
'''
import cv2
import numpy as np
from second import compute_itf
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('ABD_CT.jpg', cv2.IMREAD_GRAYSCALE)

# Define intensity values
intensity_values = np.arange(256) / 255.0  # Range of 0 to 1 with 256 values

# Define gamma parameter
gamma = 1.5  # Adjust this parameter as desired

# Compute ITF lookup table
itf_lookup_table = compute_itf(intensity_values, gamma)

# Map intensity values of the image using ITF lookup table
mapped_image = itf_lookup_table[image]

# Convert mapped image back to appropriate datatype and value range
mapped_image = (mapped_image * 255).astype(np.uint8)

# Display the original and mapped images using matplotlib


plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(mapped_image, cmap='gray')
plt.title('Mapped Image (ITF)')
plt.axis('off')

plt.tight_layout()
plt.show()

