# EOS_fitting


## Task1- Equation of State (EOS) Fitting
In this Task, the program will:

1. Read Data: Import the volume (V) and energy (E) data from a CSV file.
2. Define EOS Function: Utilize the simplified Birch-Murnaghan EOS, ```E(V) = a + bV^-2/3 + cV^-4/3 + dV^-6/3```, where a, b, c, and d are fitting parameters to be determined.
3. Parameter Optimization: Use `curve_fit` to fit the equation and get the estimated parameters: `a_fit, b_fit, c_fit, d_fit`.
4. Calculate Equilibrium Volume: Use `minimize_scalar` to minimize the energy function with the estimated parameters. `equilibrium_volume` is the volume at which the energy is minimized, and `equilibrium_energy` is the resulting minimized energy.
5. Output Results: Print the optimized parameters and the equilibrium volume to the console.

## Task2-Visualizing Results
In this Task, the visualization task aims to：
1. Plot Energy-Volume Curve: Generate a plot of the fitted energy-volume curve using matplotlib.
2. Highlight Equilibrium Volume: Indicate the equilibrium volume on the plot.
3. Quality of Fit: Display the quality of the fit by plotting the actual data points against the fitted curve, allowing for visual assessment of the EOS model's performance.
