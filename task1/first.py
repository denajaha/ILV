'''
@Author: Uros Miljkovic 123598
load the provided image ABD_CT.jpg and check the datatype – decide if you need to convert the
values to a different numerical datatype and value range given the above requirements.
'''

import cv2

# Load the image
image = cv2.imread('ABD_CT.jpg', cv2.IMREAD_GRAYSCALE)

# Check the datatype of the image
data_type = image.dtype

# Check the value range of the image
min_value = image.min()
max_value = image.max()

# Determine if conversion is needed
conversion_needed = False
if data_type != float or min_value < 0 or max_value > 1:
    conversion_needed = True

# Print the results
print(f"Image datatype: {data_type}")
print(f"Min value: {min_value}")
print(f"Max value: {max_value}")
print(f"Conversion needed: {conversion_needed}")
