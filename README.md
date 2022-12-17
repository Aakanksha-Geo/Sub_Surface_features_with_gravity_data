# Finding the depth and dimension of the spherical ore body under the Surface (Non-Linear Inverse Problem)

The gravity_plot_guass_newton.py implements the Guass-Newton method to find the model parameters, it requres a initial guess for the model parameters. The model in question is the value of gravitational acceleration from a spherical body given by

$g = \frac{4\pi R^3 \Delta \rho G z }{3(x^2 + z^2)^{3/2}}$

where z is the depth to the spherical ore body and x is the horizontal distance. G is the gravitational constant and $\rho$ is the average crust density. R is the dimention of the ore body. Here R,Z are the model parameters.


