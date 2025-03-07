# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LPIsQHyd-Pp9w34qg_366LhIRosmRD35
"""

# prompt: grafica del espectro de cuerpo negro

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import h, c, k

def planck_law(wavelength, temperature):
  """Calculates the spectral radiance of a black body.

  Args:
    wavelength: Wavelength in meters.
    temperature: Temperature in Kelvin.

  Returns:
    Spectral radiance in W sr^-1 m^-3.
  """
  a = 2 * h * c**2
  b = h * c / (k * temperature)
  intensity = a / (wavelength**5 * (np.exp(b / wavelength) - 1))
  return intensity

# Set the temperature (in Kelvin)
temperature = 5800  # Example: Temperature of the Sun

# Define the wavelength range (in meters)
wavelengths = np.linspace(1e-9, 3e-6, 500)  # Visible and near-infrared

# Calculate the spectral radiance
intensities = planck_law(wavelengths, temperature)

# Convert wavelength to nanometers
wavelengths_nm = wavelengths * 1e9

# Plot the black body spectrum ttttttt
plt.figure(figsize=(10, 6))
plt.plot(wavelengths_nm, intensities, color='blue')
plt.xlabel("Wavelength (nm)", fontsize=18)
plt.ylabel("Spectral Radiance (W sr$^{-1}$ m$^{-3}$)", fontsize=14)
plt.title(f"Black Body Spectrum (T = {temperature} K)", fontsize=16)
plt.grid(True)
plt.xlim(0, 3000) # Limit x-axis to visible range

# optional add a secondary axis to show microns
# plt.gca().secondary_xaxis('top', functions=(lambda x: x/1000, lambda x: x*1000))

plt.show()