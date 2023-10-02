import cv2
import matplotlib.pyplot as plt
import numpy as np

import segmentation_watershed as seg

# load yellowlily.jpg image (with grayscale conversion, data type conversion to floating-point datatype and downscaling)
img = cv2.imread('yellowlily.jpg', cv2.IMREAD_GRAYSCALE).astype(np.float32)
scaleFactor = 0.125
dims = (int(img.shape[1] * scaleFactor), int(img.shape[0] * scaleFactor))
img = cv2.resize(img, dims, cv2.INTER_LINEAR)

# compute gradient images with normalized Sobel filter kernels (this resembles step 1 from slide #31)
g_y = np.array([[0.25, 0.5, 0.25], [0, 0, 0], [-0.25, -0.5, -0.25]])
g_x = g_y.transpose()
gradX = cv2.filter2D(img, -1, np.flip(g_x), borderType=cv2.BORDER_REPLICATE) # flip -> convolution, since filter2D computes correlation
gradY = cv2.filter2D(img, -1, np.flip(g_y), borderType=cv2.BORDER_REPLICATE) # flip -> convolution, since filter2D computes correlation
# compute gradient magnitude image
gradMag = np.sqrt(gradX**2 + gradY**2)

# TODO: initialize seed map - seed points should be those pixels that are zero (or almost zero, e.g. < 0.25) in the gradient magnitude image - this will resemble step 3 from slide #31
seedMap = (gradMag < 0.25).astype(np.uint8)

# perform watershed segmentation
labelMap = seg.computeWatershedSegmentation(gradMag, seedMap)

# TODO: plot original grayscale image

plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

# TODO: plot gradient magnitude image

plt.subplot(2, 2, 2)
plt.imshow(gradMag, cmap='gray')
plt.title('Gradient Magnitude Image')
plt.axis('off')

# TODO: plot labelMap (set -1 values to 0 before you visualize)

plt.subplot(2, 2, 3)
plt.imshow(np.where(labelMap == -1, 0, labelMap), cmap='jet')
plt.title('Label Map')
plt.axis('off')

# TODO: plot binary map with dam pixels being set to 1 and 0 otherwise

binaryMap = (labelMap == -1).astype(np.uint8)
plt.subplot(2, 2, 4)
plt.imshow(binaryMap, cmap='gray')
plt.title('Binary Map (Dam Pixels)')
plt.axis('off')

plt.tight_layout()
plt.show()
