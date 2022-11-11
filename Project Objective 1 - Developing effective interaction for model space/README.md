## The Fitting Procedure for required interaction
For interaction to be effective for a model we need to fit it with the experimental data. Mathmatically we need to minimize the weighted least squares function. 
For chi-square $\chi^2$ fitting we have

$$
\chi^2 = \sum_i w_i (E_{i}^{th} - E^{exp}_i)^2
$$

where $i$ sum over all the energy level of the interest, $w_i$ is the weight factor of each energy level. 
$E_i^{th}, E_i^{exp}$ are the theoretical and experimental energy levels energies. One of the simplest way to minimize $\chi^2$ is to consider it as a nonlinear function of the parameters $x_{\alpha}$ of the model and start the minimization process. 

However this process is very slow becuase it require the evaluation of $\chi^2$ at least $f+1$ times with $f$ the number of adjustable parameters.

A very efficient also exist for the shell model calcuations, in which one guess the starting point for the parameters, then finds the corresponding wavefunction, and then predict a new set of parameters using

$$E^{th}_i = ^0\langle 0 \vert H(x_{\alpha})\vert 0 \rangle^0$$

This will be an exact result when $x_{\alpha} = x^0_{\alpha}$. 

Else if $x_{\alpha} \ne x_{\alpha}^0$ is valid upto first-order perturbation. This leads to a very efficient fitting procedure when H is a linear function of the adjustable parameters. 

Second condition applies on fitting is valid when the wave function changes slowly as the parameters change. However in some case we found that this procedure fails to converge due to rapid changes of the wave functions. 

When ever this happens the code automatically should switches to another procedure in which derivative are evaluated analytically:

$$
\frac{\partial \psi}{\partial x_{\alpha} } = 2 \sum_i w_i (E^{th}_i - E^{exp}_i)\frac{\partial E_i^{th}}{\partial x_{\alpha}}
$$

with $$\frac{\partial E_i^{th}}{\partial x_{\alpha}} = \frac{\partial \langle i \vert H \vert i\rangle}{\partial x_{\alpha}} = \frac{\partial H}{\partial x_{\alpha}} \vert i$$

yielding 

$$
\frac{\partial \phi}{\partial {x_{\alpha}}} =  2\sum_i w_i (E^{exp}_i - E^{th}_i) \langle i \vert \frac{\partial H}{\partial x_{\alpha}} \vert i \rangle
$$

The gradient of $\phi$ at any point $x_{\alpha}$ in the $f$-dimensional parameter space is consequently evaluated with a single calculation of the wave functions. If the Hamiltonian is linear in $x_{alpha}$ 

If Hamiltonian is linear in $x_{\alpha}$ ; $H = \sum_{\alpha} x_{\alpha} H_{\alpha}$ then, 

$$\frac{\partial \phi}{\partial x_{\alpha}} = 2\sum_i w_i (E^{exp}_i - E^{th}_i) \langle i \vert  H_{\alpha} \vert i \rangle
$$

After finding the gradient the new parameter values can be founded as 

$$x_{\alpha} \approx x_{\alpha} - \frac{\partial \phi}{x_{\alpha}}\frac{dx}{\nabla \phi}$$

where $dx$ is the distance between the old new parameter point in the parameter space. This fitting procedure predicts new parameters for every solutions of the Schrodinger equation and is f-times more efficient than procedure which compute the derivative numerically.
