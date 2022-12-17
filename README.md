# Finding the depth and dimension of the spherical ore body under the Surface 

## Using Guass-Newton method for non-linear inverse problem
The gravity_plot_guass_newton.py implements the Guass-Newton method to find the model parameters, it requres a initial guess for the model parameters. The model in question is the value of gravitational acceleration from a spherical body given by

$g = \frac{4\pi R^3 \Delta \rho G z }{3(x^2 + z^2)^{3/2}}$

where z is the depth to the spherical ore body and x is the horizontal distance. G is the gravitational constant and $\rho$ is the average crust density. R is the dimention of the ore body. Here R,Z are the model parameters.

Following diagram show the effectiveness of the method as it plots the error with respect to the iteration number and converges very fast for a very bad initial guess

![Gravity_guass_newton_300_700](https://user-images.githubusercontent.com/120786270/208243451-50eae25d-2e7e-4a77-865d-6eb7d5bfe220.png)



---
## Using least square approach by converting into linear problem

The least_square_approach.py solves the same non-linear problem after converting the equations to a linear system of eqautions and then apply the least square method. It requires an input data file which includes the observed data and it tries to fit the model with that data and gives the best fit model parameters as output.
