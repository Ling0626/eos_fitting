# EOS_fitting

- `eos_fitting.py`: the main program
- `eos.csv`: the data

## Task1 - Equation of State (EOS) Fitting

1. Read Data: Import the volume (V) and energy (E) data from `eos.csv`.
2. Define EOS Function: Utilize the simplified Birch-Murnaghan equation:
$$E(V) = a + bV^{-2/3} + cV^{-4/3} + dV^{-6/3},$$
where $a$, $b$, $c$, and $d$ are fitting parameters to be determined.
4. Parameter Optimization: Use `curve_fit` to fit the equation and get the estimated parameters: `a_fit, b_fit, c_fit, d_fit`.
5. Calculate Equilibrium Volume: Use `minimize_scalar` to minimize the energy function with the estimated parameters. In the program, `equilibrium_volume` is the volume at which the energy is minimized, and `equilibrium_energy` is the resulting minimized energy.
6. Output Results: Print the optimized parameters and the equilibrium volume to the console.

## Task2 - Visualizing Results

1. Plot the actual data points from `eos.csv`.
2. Generate a plot of the fitted energy-volume curve using `matplotlib.pyplot`.

![Figure_1](https://github.com/Ling0626/eos_fitting/assets/148604827/1690b30f-f9fd-4699-b9c0-5529fb1991f4)
