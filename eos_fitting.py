import numpy as np
import pandas as pd
from scipy.optimize import curve_fit, minimize_scalar
import matplotlib.pyplot as plt

# Read data
data = pd.read_csv('eos.csv')
print(data.head())

# Extract volume and energy data
volumes = data['Volume (A^3/atom)'].values
energies = data['Energy (eV/atom)'].values

# Define Birch-Murnaghan equation of state
def birch_murnaghan(V, a, b, c, d):
    return a + b * V**(-2/3) + c * V**(-4/3) + d * V**(-6/3)

# Fit the data using curve_fit
fit_params, covariance = curve_fit(birch_murnaghan, volumes, energies)

# Print the fitting parameters
a_fit, b_fit, c_fit, d_fit = fit_params
print(f"Fitting parameters:a = {a_fit}, b = {b_fit}, c = {c_fit}, d = {d_fit}")

# Find the equilibrium volume by minimizing the energy
result = minimize_scalar(lambda V: birch_murnaghan(V, a_fit, b_fit, c_fit, d_fit), bounds=(0, 100))
equilibrium_volume = result.x
equilibrium_energy = result.fun

print(f"Equilibrium volume: {equilibrium_volume} A^3/atom")
print(f"Corresponding equilibrium energy: {equilibrium_energy} eV/atom")

# Generate a range of volumes for plotting
plot_volumes = np.linspace(min(volumes), max(volumes), 1000)

# Compute corresponding energies using the fitted function
plot_energies = birch_murnaghan(plot_volumes, a_fit, b_fit, c_fit, d_fit)

# Plot energy-volume curve
plt.plot(volumes, energies, 'o', label='Actual Data')
plt.plot(plot_volumes, plot_energies, '-', label='Fitted Curve')
plt.xlabel('Volume(A^3/atom)')
plt.ylabel('Energy (eV/atom)')
plt.legend()
plt.title('Birch-Murnaghan Fit Result')
plt.show()
