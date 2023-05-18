'''
task 1 – applying the power function as intensity transfer function to an image
an intensity transfer function (ITF) we did not talk about in the lecture is the power function. It can be used for
non-linear contrast stretching or contrast compression. To make the power function work for this one must bring
the intensity value range into the range of 0 and 1.

Interpreting this function as an ITF, 𝑥 denotes the input intensity value, 𝑦 is the output intensity value and 𝛾
(gamma) is the correction parameter taking positive values and resulting in a non-linear contrast compression
for values below 1 and a non-linear contrast expansion for values >1

'''
import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('ABD_CT', cv2.IMREAD_GRAYSCALE)


#Normalize the image intensity values to the range of 0 to 1:
normalized_image = image.astype(float) / 255.0

#Define the power function as the ITF:
def power_function(x, gamma):
    return np.power(x, gamma)

#Apply the power function to the normalized image:
gamma = 1.5  # Adjust this parameter as desired
output_image = power_function(normalized_image, gamma)

#Rescale the output image back to the range of 0 to 255:
rescaled_image = (output_image * 255).astype(np.uint8)


#Display the original and processed images using matplotlib:
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(rescaled_image, cmap='gray')
plt.title('Processed Image (Power Function)')
plt.axis('off')

plt.tight_layout()
plt.show()



