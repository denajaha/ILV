import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('MouseCT.jpg', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian blur to the image
smoothed = cv2.GaussianBlur(image, (0, 0), 3)

# Calculate the unsharp mask
mask = cv2.subtract(image, smoothed)

# Define the amount/factor to adjust the mask
factor = 1.5

# Combine the mask with the original image
result = cv2.addWeighted(image, 1 + factor, mask, -factor, 0)

# Display the images
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Input Image')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(smoothed, cmap='gray')
plt.title('Smoothed Image')
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(mask, cmap='gray')
plt.title('Unsharp Mask')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(result, cmap='gray')
plt.title('Result Image')
plt.axis('off')

plt.tight_layout()
plt.show()
'''
This code will display four separate figures showing the input image, the smoothed image, the unsharp mask, 
and the resulting image. The unsharp mask is not a binary mask, but a grayscale image representing the difference
between the original and smoothed images. The result image is obtained by combining the original image with the 
adjusted unsharp mask.
'''