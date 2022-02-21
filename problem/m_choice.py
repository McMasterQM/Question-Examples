#!/usr/bin/env python
# coding: utf-8

# # Demonstration of GitHub Classroom Q & A
# 
# ## &#x1f468;&#x200d;&#x1f3eb; Purpose
# GitHub Classroom not only allows us to automatically test programming/code. Other types of questions are supported too.
# 1. &#x1f3b2; Multiple-Choice Questions (one or more answers, separated by spaces or commas)
# 2. &#x1fa99; True/False Questions (write True/False)
# 3. &#x1F5A9; Numerical answers requiring some calculation (write the numerical answer in the requested units; significant figures are not checked)
# 4. &#x1f9ee; Numerical answers requiring no calculation (usually just counting) (write the answer as a number)
# 4. &#x1f500; Matching Questions (write pairs sequentially).
# 
# The way we do it, it is important that you *always* put your answer in the indicated position and never use the bold-faced word "Answer" elsewhere. Other than that restriction, the rest of your notebook is yours to play with.
# 
# -----
# 
# ## &#x1f4dc; Instructions
# The next few questions demonstrate the workflow. For each question type, you are first given an example; then you need to do another question of the same type on your own.
# - You can upload files to show your mathematical work; you can also type mathematics using Markdown.
# - You can use the notebook as a calculator for numerical problems; but you can also just type in your answer computed offline.
# - You may find these [sheets containing reference data and mathematical formulas/identities](https://github.com/QC-Edu/IntroQM2022/blob/master/documents/ReferenceConstantsConversionsMath.pdf) useful.
# 

# -----
# **1. &#x1f3b2; Which of the following phenomena are strongly associated with the particle-like nature of light.** 
# 
# A. Blackbody radiation 
# 
# B. Compton Scattering 
# 
# C. Electron Diffraction 
# 
# D. Stern-Gerlach Experiment 
# 
# E. Photoelectric effect
# 
# **Answer**: A, E, B

# More information can be found in the [course notes](https://qchem.qc-edu.org/ipynb/History.html#how-was-quantum-mechanics-discovered).

# -----
# 
# **2. &#x1f3b2; Which of the following changes would double the energy of a photon:**
# 
# A. Doubling its frequency 
# 
# B. Doubling its wavelength 
# 
# C. Doubling its momentum 
# 
# D. Doubling its speed 
# 
# E. Doubling its effective (relativistic) mass 
# 
# F. Doubling its wavenumber.
# 
# **Answer**: A, C, E, F

# -------
# **3. &#x1fa99; Doubling the wavelength of radiation doubles its frequency. (True/False)**
# 
# **Answer**: False

# The wavelength, $\lambda$, of light is related to frequency, $\nu$ by the equation $\nu = \frac{c}{\lambda}$. So doubling the wavelength halves the frequency.

# -----
# 
# **4. &#x1fa99; Doubling the wavelength of radiation halves its speed. (True/False)**
# 
# **Answer**: False

# --------
# **5. &#x1F5A9; A helium-neon laser emits light at 632.8 nm.  What is the energy of the photons generated by this laser, in Joules?**
# 
# **Answer**: 3.139e-19

# In[1]:


import numpy
import scipy
from scipy import constants

Energy = constants.h*constants.c/632.8e-9
print("Energy of the photon in Joules", Energy)


# Using the formula $E = \frac{h c}{\lambda}$.

# --------
# **6. &#x1F5A9; What is the frequency of light in Hz ($s^{-1}$) of light with wavelength 500 nm?**
# 
# **Answer:** 5.996e+14

# In[5]:


print(f"The frequency, c/wavelength, is: {constants.c/500e-9:.3e} Hz.")


# ------
# **7. &#x1f9ee; Two quantum particles move at the same speed, but particle 2 has half the mass of particle 1. The De Broglie wavelength of particle 2 is greater than that of particle 1 by a factor of ____?**
# 
# **Answer:** 2

# The De Broglie wavelength is $\lambda = \frac{h}{p}$. Halving the mass of a particle halves its momentum and doubles its wavelength.

# ------
# **8. &#x1f9ee; When light with wavelength 600 nm shines on a metal surface, electrons are photoelectrically ejected. Next, a light with wavelength 300 nm is shone on the surface. The kinetic energy of the emitted electrons increases by a factor of ____?**
# 
# **Answer:** 2

# See the [course notes](https://qchem.qc-edu.org/ipynb/History.html#photoelectric-effect).

# ------
# **9. &#x1f500; Assign the following equations to the person most strongly associated with them.**
# 
# |Person|Equation|
# |--|--|
# |**A.** De Broglie | **1.** $\, E=h \nu$ |
# |**B.** Einstein   | **2.** $\, p=\frac{h}{\lambda}$|
# |**C.** Planck     | **3.** $\, \text{Kinetic Energy} = h \nu - W$ |
# |**D.** Rydberg    | **4.** $\, h \nu \propto \frac{1}{m^2} - \frac{1}{n^2}$|
# 
# **Answer:** A, 2, B, 3, C, 1, D, 4

# ------
# **10. &#x1f500; Assign the following types of experiment to the person most strongly associated with them.**
# 
# |Person|Experiment|
# |--|--|
# |**A.** Davisson and Germer | **1.** Electron Scattering |
# |**B.** Compton   | **2.** Photon Scattering|
# 
# **Answer:** A, 1, B, 2