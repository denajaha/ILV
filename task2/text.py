'''
@Author: Uros Miljkovic 123598
'''

'''
Summarize in your report what you did and try to understand how the algorithm works – you may add additional comments 
in code or just summarize your findings in your report.
'''


'''
Report: Histogram Matching

In this task, we implemented histogram matching, a technique used to match the histogram of one image to another image.
The goal is to transfer the color distribution from a reference image to a source image while preserving the spatial
information.

We began by loading the source image and the reference image using OpenCV's imread function.
Both images were assumed to be grayscale for simplicity. We then defined a function compute_cdf to compute the
cumulative distribution function (CDF) from the normalized histogram (PDF) of an image.

Next, we calculated the normalized histograms (PDFs) of the source and reference images using NumPy's histogram
function. These histograms represent the probability distribution of intensities in each image. The CDFs of both images were
computed using the compute_cdf function.

To perform histogram matching, we created a mapping function by searching for the closest intensity value in the
reference image's CDF for each intensity value in the source image's CDF. This mapping function represents the desired
transformation for each intensity value in the source image.

Finally, we applied the mapping function to the source image to obtain the mapped result image. We also computed the
normalized histogram (PDF) of the mapped result image.

To visualize the results, we used Matplotlib to plot the source image, normalized histograms (PDFs) of the source and
reference images, CDFs of the source and reference images, mapped result image, and the normalized histogram (PDF) of
the mapped result image. We arranged these visualizations as subplots in a single figure, adding appropriate titles and
labels to each subplot.

Through this implementation and visualization, we observed the following:

The source image represents the original image for which we want to match the histogram.
The normalized histogram (PDF) of the source image shows the probability distribution of intensity values in the
source image.
The reference image serves as the target image, and its histogram is used as a reference for matching.
The normalized histogram (PDF) of the reference image displays the probability distribution of intensity values in the
reference image.
The CDFs of the source and reference images show how the cumulative probabilities change across intensity values.
The mapped result image is the source image after the histogram matching transformation has been applied.
The normalized histogram (PDF) of the mapped result image represents the transformed probability distribution of
intensity values.
Histogram matching is a powerful technique in image processing that allows us to adjust the color distribution of an
image to match a desired target distribution. It finds applications in various fields, including:

Medical imaging: Histogram matching can be used to standardize or enhance the appearance of medical images for better
analysis and diagnosis.
Computer vision: Histogram matching is utilized in image registration, where the goal is to align two images with
different lighting conditions or contrasts.
Photography and image editing: Histogram matching can be employed to adjust the color balance or enhance the overall
appearance of photographs.
Overall, histogram matching provides a means to transfer the color characteristics from one image to another,
facilitating better visual perception or analysis of images across different domains and applications.
'''