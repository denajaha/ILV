'''
@Author: Uros Miljkovic 123598
task 2 – add visualizations for images and image statistics to the given algorithm for histogram matching
The provided script (histogram_matching_example.py) computes histogram matching to match the intensity value
distribution of a source image to those of a reference image.
Your task is to extend the script to visualize the results. So, you will have to visualize the images and functions
values of the histograms and the mapping function.
Visualize (at least) these images/functions as subplots in one figure:
• source image
• normalized histogram (pdf) of source image
• reference image
• normalized histogram (pdf) of reference image
• cdf of the intensity values of the source image
• cdf of the intensity values of the reference image
• the mapped result image
• normalized histogram (pdf) of the mapped result image
Use titles for the different subplots, also use labels for the axes whenever plotting statistical functions.
hint: there are several options to visualizing functions with discrete function values, e.g., you can use the bar, hist
or plot function just to give some examples

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

    return mapped_img, hist1, hist2, cdf1, cdf2, hist_mapped


# Load the source and reference images
source_image = cv2.imread('./source.jpeg', cv2.IMREAD_GRAYSCALE)
reference_image = cv2.imread('./reference.jpeg', cv2.IMREAD_GRAYSCALE)

# Perform histogram matching
mapped_image, hist_source, hist_reference, cdf_source, cdf_reference, hist_mapped = histogram_matching(source_image, reference_image)

# Plot the images, histograms, and mapping function
fig, axes = plt.subplots(2, 4, figsize=(16, 8))
fig.tight_layout(pad=4.0)

# Source Image
axes[0, 0].imshow(source_image, cmap='gray')
axes[0, 0].set_title('Source Image')
axes[0, 0].axis('off')

# Normalized Histogram of Source Image
axes[0, 1].bar(range(len(hist_source)), hist_source, width=1, color='red')
axes[0, 1].set_title('Histogram (PDF) of Source Image')
axes[0, 1].set_xlabel('Intensity')
axes[0, 1].set_ylabel('Probability')

# Reference Image
axes[0, 2].imshow(reference_image, cmap='gray')
axes[0, 2].set_title('Reference Image')
axes[0, 2].axis('off')

# Normalized Histogram of Reference Image
axes[0, 3].bar(range(len(hist_reference)), hist_reference, width=1, color='blue')
axes[0, 3].set_title('Histogram (PDF) of Reference Image')
axes[0, 3].set_xlabel('Intensity')
axes[0, 3].set_ylabel('Probability')

# CDF of Source Image
axes[1, 0].plot(range(len(cdf_source)), cdf_source, color='red')
axes[1, 0].set_title('CDF of Source Image')
axes[1, 0].set_xlabel('Intensity')
axes[1, 0].set_ylabel('Cumulative Probability')

# CDF of Reference Image
axes[1, 1].plot(range(len(cdf_reference)), cdf_reference, color='blue')
axes[1, 1].set_title('CDF of Reference Image')
axes[1, 1].set_xlabel('Intensity')
axes[1, 1].set_ylabel('Cumulative Probability')

# Mapped Result Image
axes[1, 2].imshow(mapped_image, cmap='gray')
axes[1, 2].set_title('Mapped Result Image')
axes[1, 2].axis('off')

# Normalized Histogram of Mapped Result Image
axes[1, 3].bar(range(len(hist_mapped)), hist_mapped, width=1, color='green')
axes[1, 3].set_title('Histogram (PDF) of Mapped Result Image')
axes[1, 3].set_xlabel('Intensity')
axes[1, 3].set_ylabel('Probability')

plt.show()

