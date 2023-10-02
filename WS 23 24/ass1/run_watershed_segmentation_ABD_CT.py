import cv2
import matplotlib.pyplot as plt

from segmentation_watershed import *

# load ABD_CT.jpg image (with grayscale conversion, data type conversion to floating-point datatype and downscaling)
img = cv2.imread('ABD_CT.jpg', cv2.IMREAD_UNCHANGED).astype(np.float32)
img = img[90:img.shape[0]-50, 160:img.shape[1]-170] # we just crop out a roi and use it as whole image

# compute gradient images with normalized Sobel filter kernels (this resembles step 1 from slide #31)
g_y = np.array([[0.25, 0.5, 0.25], [0, 0, 0], [-0.25, -0.5, -0.25]])
g_x = g_y.transpose()
gradX = cv2.filter2D(img, -1, np.flip(g_x), borderType=cv2.BORDER_REPLICATE) # flip -> convolution, since filter2D computes correlation
gradY = cv2.filter2D(img, -1, np.flip(g_y), borderType=cv2.BORDER_REPLICATE) # flip -> convolution, since filter2D computes correlation
# compute gradient magnitude image
gradMag = np.sqrt(gradX**2 + gradY**2)

# TODO: initialize seedMap with seed points [y: 68, x: 38] and [y: 62, x: 50] - this will substitute step 3 from slide #31
seedMap = np.zeros_like(img, dtype=np.uint8)
seedMap[68, 38] = 1
seedMap[62, 50] = 1
# perform watershed segmentation
labelMap = computeWatershedSegmentation(gradMag, seedMap)

# TODO: plot original grayscale image
plt.figure(figsize=(12, 12))
plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Grayscale Image')
plt.axis('off')

# TODO: plot gradient magnitude image
plt.subplot(2, 2, 2)
plt.imshow(gradMag, cmap='gray')
plt.title('Gradient Magnitude Image')
plt.axis('off')

# TODO: plot labelMap
plt.subplot(2, 2, 3)
plt.imshow(np.where(labelMap == -1, 0, labelMap), cmap='jet')
plt.title('Label Map')
plt.axis('off')

# TODO: plot binary map with dam pixels
binaryMap = (labelMap == -1).astype(np.uint8)
plt.subplot(2, 2, 4)
plt.imshow(binaryMap, cmap='gray')
plt.title('Binary Map (Dam Pixels)')
plt.axis('off')

plt.tight_layout()
plt.show()
