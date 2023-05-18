'''
@Author: Uros Miljkovic 123598
CHANGES:
Add comments: Add comments to explain the purpose of each section of the code and clarify the steps being performed.

Wrap the code in a function: Encapsulate the code within a function to improve reusability and modularity. This will allow you to call the function with different source and reference images.

Use numpy functions efficiently: Replace the loop for finding the matching index with numpy functions such as np.searchsorted for improved performance.

Visualize the histograms: Include a histogram plot to visualize the histograms of the source, reference, and mapped images using matplotlib's plt_hist function.
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

def compute_cdf(pdf):
    # Compute the CDF out of the PDF (normalized histogram) of the source image
    numBins = len(pdf)
    cdf = np.zeros(numBins)
    sum_value = 0
    for i in range(numBins):
        sum_value += pdf[i]
        cdf[i] = sum_value
    return cdf

def histogram_matching(source_image, reference_image):
    numBins = 256

    # Compute the normalized histograms
    hist1, edges1 = np.histogram(source_image.flat, bins=numBins, range=(0, numBins), density=True)
    hist2, edges2 = np.histogram(reference_image.flat, bins=numBins, range=(0, numBins), density=True)

    cdf1 = compute_cdf(hist1)
    cdf2 = compute_cdf(hist2)  # Used as the lookup table (LUT)

    # Compute the mapping function for histogram matching
    mapping = np.zeros(numBins)
    for i in range(numBins):
        indexFound = np.searchsorted(cdf2, cdf1[i])
        mapping[i] = indexFound

    # Apply the mapping of values to the source image
    mapped_img = mapping[source_image].astype(np.uint8)

    # Compute the normalized histogram of the mapped image
    hist_mapped, edges_mapped = np.histogram(mapped_img.flat, bins=numBins, range=(0, numBins), density=True)

    return mapped_img, hist1, hist2, hist_mapped


# Load the source and reference images
source_image = cv2.imread('./source.jpeg', cv2.IMREAD_GRAYSCALE)
reference_image = cv2.imread('./reference.jpeg', cv2.IMREAD_GRAYSCALE)

# Perform histogram matching
mapped_image, hist_source, hist_reference, hist_mapped = histogram_matching(source_image, reference_image)

# Plot the histograms
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(source_image.ravel(), bins=256, range=(0, 256), color='red', alpha=0.5, label='Source')
plt.title('Source Image Histogram')
plt.legend()

plt.subplot(1, 3, 2)
plt.hist(reference_image.ravel(), bins=256, range=(0, 256), color='blue', alpha=0.5, label='Reference')
plt.title('Reference Image Histogram')
plt.legend()

plt.subplot(1, 3, 3)
plt.hist(mapped_image.ravel(), bins=256, range=(0, 256), color='green', alpha=0.5)
