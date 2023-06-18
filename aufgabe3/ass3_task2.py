import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./MouseCT.jpg', cv2.IMREAD_UNCHANGED)

# TODO: explain what this line does DONE
'''
This line performs a 2-dimensional Fast Fourier Transform (FFT) on the input image img. The np.fft.fft2 function 
computes the FFT of the image, converting it from the spatial domain to the frequency domain. The result, fimg, 
represents the image's complex spectrum
'''
fimg = np.fft.fft2(img)

# TODO: explain what this command does and what the purpose is DONE
'''
This command shifts the zero-frequency component (DC component) of the spectrum to the center of the image. 
The np.fft.fftshift function rearranges the quadrants of the frequency spectrum so that the low-frequency components 
are at the center. This operation is done to visualize the spectrum correctly.
'''
fimg = np.fft.fftshift(fimg);

# TODO: compute and visualize (shifted) magnitude spectrum with applied
#  logarithm and scale the values to the used value range for visualization DONE
'''
This TODO is asking to compute and visualize the magnitude spectrum of the image after the FFT operation. 

To compute the magnitude spectrum, you can use the absolute value of the complex spectrum, np.abs(fimg). 
Then, I can apply a logarithm to the magnitude values to compress the dynamic range and scale the values to the 
desired range for visualization purposes. Finally, I can plot the resulting magnitude spectrum.
'''
# Compute the magnitude spectrum
magnitude_spectrum = np.abs(fimg)

# Apply logarithm and scale the values for visualization
magnitude_spectrum_log = np.log(1 + magnitude_spectrum)
magnitude_spectrum_log_scaled = (magnitude_spectrum_log / np.max(magnitude_spectrum_log)) * 255

# Visualize the magnitude spectrum
plt.figure(figsize=(8, 6))
plt.imshow(magnitude_spectrum_log_scaled, cmap='gray')
plt.title('Magnitude Spectrum (Log Scale)')
plt.axis('off')
plt.show()


# TODO: find out what the following code does (HINT: compute again the
#  magnitude spectrum after applying the following operations and analyze
#  what is different, try also to understand what every line of code
#  does) and add visualizations (don't forget to visualize the result image) DONE
'''
This code applies a circular mask to the frequency spectrum to suppress the high-frequency components beyond a 
certain distance from the center. 
Here's a breakdown of what each line does:

dims = fimg.shape: 
Obtains the dimensions (height and width) of the frequency spectrum.

center = np.floor([dims[0]/2, dims[1]/2]): 
Calculates the coordinates of the center of 
the spectrum by halving the dimensions.

maxDist = 60: 
Defines the maximum distance from the center beyond which the frequencies will be suppressed.

for y in range(dims[0]): and for x in range(dims[1]):: Iterate through each pixel in the frequency spectrum.

crad = np.sqrt((y-center[0])**2+(x-center[1])**2): 
Calculates the distance between the current pixel and the center using the Euclidean distance formula.

if crad > maxDist: fimg[y,x] = complex(0,0): 
If the distance is greater than maxDist, the corresponding frequency component is set to zero, effectively suppressing it.

resimg = np.real(np.fft.ifft2(np.fft.ifftshift(fimg))): 
Performs an inverse FFT to obtain the resulting image by shifting the spectrum back, applying the inverse FFT, 
and taking the real part. The resulting image, resimg, represents the spatial domain 
representation of the filtered spectrum.


To analyze the difference, you can compute the magnitude spectrum again after applying the circular mask and 
visualize it, along with the resulting image resimg.
'''
dims = fimg.shape
center = np.floor([dims[0]/2, dims[1]/2])
maxDist = 60
for y in range(dims[0]):
    for x in range(dims[1]):
        crad = np.sqrt((y-center[0])**2+(x-center[1])**2)
        if crad > maxDist:
            fimg[y,x]=complex(0,0)

resimg = np.real(np.fft.ifft2(np.fft.ifftshift(fimg)))


#################################################################
#VISUALISATION

# Convert the result image to the appropriate datatype for visualization
resimg_vis = resimg.astype(np.uint8)

# Visualize the result image
plt.figure(figsize=(8, 6))
plt.imshow(resimg_vis, cmap='gray')
plt.title('Result Image')
plt.axis('off')
plt.show()