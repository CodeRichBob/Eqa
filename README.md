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

- By running the python script another.py, the following is a snapshot of the results
