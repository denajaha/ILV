'''
@Author: Uros Miljkovic 123598
summarize and interpret your results in your report/protocol document (you may also try out different
values for 𝛾), also do not forget to add comments to your code (those lines starting with that # sign in
the beginning of the line and comment what you did in the code)
'''

'''
Report Summary: Application of Gamma Correction in Different Technical Fields

Gamma correction, also known as gamma adjustment or power-law transformation, is a widely used technique in various technical fields for image and signal processing. It involves applying a power function to the intensity values to modify the brightness and contrast characteristics of an image. In this report, we investigated the application of gamma correction in different domains and summarized our findings.

We first implemented the gamma correction algorithm in Python using the provided image "ABD_CT.jpg" and the ITF function. We loaded the image and checked its datatype, ensuring that it was grayscale. We then created a separate Python script, itf_function.py, to compute the intensity transfer function (ITF) values and generate the lookup table. The compute_itf function took the intensity values and gamma parameter as inputs and returned the mapped intensity values.

To visualize the results, we applied gamma correction with different gamma values (0.25, 0.5, 1.0, 1.5, and 2.0) to the image. Each gamma value represented a different level of non-linear contrast compression or expansion. We created a subplot grid and displayed the original image, plotted the ITFs using matplotlib's plot function, and displayed the resulting images mapped with the corresponding ITFs.

Our findings indicate that gamma correction has widespread applications in various technical fields. Some of the notable areas where gamma correction is used include:

1. Photography and Imaging: Gamma correction is essential in image processing pipelines to compensate for the non-linear response of image sensors and display devices, ensuring accurate color reproduction and tonal range representation.

2. Computer Graphics and Gaming: Gamma correction is employed in computer-generated images and video games to achieve consistent color reproduction and brightness levels across different display devices.

3. Display Technology and Calibration: Gamma correction is necessary for calibrating display devices such as monitors and televisions to ensure accurate and uniform brightness levels throughout the grayscale range.

4. Medical Imaging: Gamma correction is applied in medical imaging modalities, including X-ray, CT, and MRI, to enhance image contrast and improve the visibility of anatomical structures, aiding in diagnostic interpretation.

5. Video Processing and Broadcasting: Gamma correction plays a crucial role in video workflows, ensuring consistent and optimal luminance levels during video capture, editing, compression, transmission, and display.

6. Remote Sensing and Satellite Imagery: Gamma correction is used in satellite and aerial imagery to enhance the visual appearance, reveal valuable information, and facilitate accurate analysis of Earth's surface features.

7. Color Correction and Color Grading: Gamma correction is an integral part of color correction and grading workflows in photography, cinematography, and post-production, allowing adjustment of overall brightness and contrast for desired artistic effects and visual consistency.

In conclusion, gamma correction is a versatile technique used in various technical domains for enhancing image quality, achieving accurate color reproduction, and ensuring consistent brightness and contrast characteristics. The ability to adjust gamma values provides flexibility in tailoring the visual appearance and achieving desired results in different applications.
'''