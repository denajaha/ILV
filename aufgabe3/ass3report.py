'''
In today's tasks, we focused on image processing and manipulation using the OpenCV, NumPy, and Matplotlib libraries in Python.

In task one, we implemented the "unsharp masking" algorithm on an image called "MouseCT.jpg".
The algorithm involves spatial image filtering to enhance the sharpness of an image.
We started by loading the image using OpenCV's imread function and converted it to grayscale.
Then, we applied a Gaussian blur using the GaussianBlur function to create a smoothed version of the image.
Next, we computed the unsharp mask by subtracting the smoothed image from the original image.
We defined a factor to adjust the mask's intensity and added it back to the original image using the addWeighted function.
Finally, we used Matplotlib to visualize the input image, smoothed image, unsharp mask, and the resulting image.



In task two, we explored the Fourier Transform and its application in image processing.
We loaded an image called "MouseCT.jpg" and performed a 2-dimensional Fast Fourier Transform (FFT) using NumPy's fft2 function.
The FFT transformed the image from the spatial domain to the frequency domain, resulting in a complex spectrum.
We then applied a shift to bring the zero-frequency component to the center of the spectrum using fftshift.
Next, we computed the magnitude spectrum by taking the absolute value of the complex spectrum.
To visualize the spectrum, we applied a logarithm to compress the dynamic range and scaled the values for visualization.
Finally, we implemented a circular mask to suppress high-frequency components beyond a certain distance from the center.
We obtained the resulting image by performing an inverse FFT using ifft2 and visualized it using Matplotlib.

Both tasks allowed us to understand fundamental image processing techniques and the capabilities of libraries like OpenCV, NumPy, and Matplotlib.
We gained insights into spatial filtering, frequency domain analysis, and visualization of image transformations.
These tasks provided hands-on experience in manipulating images, applying filters, and understanding the effects of different operations on image enhancement and analysis.



'''