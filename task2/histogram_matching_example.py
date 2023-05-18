#everything is commented in order to remove confusion for the py compiler

'''
import numpy as np
import cv2
import matplotlib.pyplot as plt

def compute_cdf(pdf):
    # computes the cdf out of the pdf (normalized histogram) of the source image
    numBins = len(pdf+1)
    cdf = np.zeros(numBins)
    sum_value = 0
    for i in range(numBins):
        sum_value += pdf[i]
        cdf[i] = sum_value
    return cdf


source = cv2.imread('./source.jpeg', cv2.IMREAD_GRAYSCALE)
reference = cv2.imread('./reference.jpeg', cv2.IMREAD_GRAYSCALE)

numBins = 256

# compute the normalized histogram
hist1, edges1 = np.histogram(source.flat, bins=numBins, range=(0,numBins), density=True)
hist2, edges2 = np.histogram(reference.flat, bins=numBins, range=(0,numBins), density=True)

cdf1 = compute_cdf(hist1)
cdf2 = compute_cdf(hist2) # used as lut

# then computes mapping function for histogram matching (just another lut)
# search for smallest matching index in lookup table for every entry in cdf
mapping = np.zeros(numBins)
for i in range(numBins):
    for indexFound in range(numBins):
        if cdf1[i] <= cdf2[indexFound]:
           break
    mapping[i] = indexFound


# finally apply mapping of values
mapped_img = mapping[source].astype(np.uint8)

# compute normalized histogram
histMapped, edgesMapped = np.histogram(mapped_img.flat, bins=numBins, range=(0,numBins), density=True)
'''