'''
@Author: Uros Miljkovic 123598
write a separate function (in a separate .py-file) that computes the ITF values and allow to specify the
parameter value 𝛾 as function parameter, a few suggestions from my side:
--> you may consider using a vector of all possible intensity values as main input to this function
--> the output then would be a vector of the mapped (transferred) intensity values – this would
resemble already the lookup table (LUT) that is needed for the actual mapping
'''

import numpy as np

def compute_itf(intensity_values, gamma):
    """
    Compute the ITF values for a given gamma parameter.

    Args:
        intensity_values (numpy.ndarray): Vector of intensity values.
        gamma (float): Gamma parameter for the power function.

    Returns:
        numpy.ndarray: Vector of mapped intensity values (ITF values).
    """
    # Apply power function to the intensity values
    itf_values = np.power(intensity_values, gamma)

    return itf_values

'''
This function takes the input vector of intensity values and the gamma parameter as arguments. It applies the power function to each intensity value and returns the resulting mapped intensity values.
You can then use this function in your main script by importing it:
CODE START
#################################################
from itf_function import compute_itf

# Define intensity values
intensity_values = np.linspace(0, 1, 256)  # Example: Range of 0 to 1 with 256 values

# Define gamma parameter
gamma = 1.5  # Example: Adjust this parameter as desired

# Compute ITF values
itf_values = compute_itf(intensity_values, gamma)

# Print the ITF values
print(itf_values)
#################################################
CODE END

Make sure the "itf_function.py" file is in the same directory as your main script. Adjust the range and number of intensity values as needed for your specific use case.

By separating the ITF computation into a separate function, you can easily reuse it and provide different gamma values to generate different lookup tables.
'''

