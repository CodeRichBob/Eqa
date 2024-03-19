# Ergo Quantum Coding Assignment

## This repo contains solutions for the Ergo Quantum coding assignment.

### Challenge 1

- In the first part of challenge 1, we find the square root of a number, using an iterative procedure to obtain the result.

- We use the following formula;

        xn+1 = xn - ((xn2 -a)/2xn)

- Since it is rare for to reach exact 0 while using floating point arithmetic, we set the **threshhold** = 1e-10
- As a stopping criteria, we also set a maximum number of iterations, and limit it to 100.

- On the second part of challenge 1, we solve the problem
  sin(x) + (3/4)x = 1

- The domain of the problem is restricted to x in (0.0, 6.0)
- We use the following initial values to obtain the solution

  - x0 = 1.0
  - x0 = 2.0
  - x0 = 4.0

- We use matplotlib to plot the function, using plot.py script.

- Run the python script another.py, to view the results

### Challenge 2

- In this challenge, we are working on Matrix Product State
- The code pads the input vector with zeros to make its length a power of 2 and then normalizes it.
- It reshapes the normalized vector into a matrix of dimensions 2*N-1* x 2 where _N_ is the nearest power of 2.
- Singular Value Decomposition (SVD) is performed on the matrix to obtain _U_,_s_, and _V_ matrices.
- We construct the _A_ matrix and reshapes it accordingly
- Finally, we reshape the _V_ matrix into a tensor, swaps the axes, and stores it in a list called psi.
- To view the results navigate to the folder named challenge2 and run the python script mpssolution.py

## Set up and How to use

- Clone the repository to your local host:

  `git clone https://github.com/CodeRichBob/Eqa.git`

- Navigate to the relevant folder for each challenge
- Run the python scripts to view the solution

## License

[Click to view License](LICENSE)
