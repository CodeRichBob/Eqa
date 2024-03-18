# Ergo Quantum Coding Assignment

## This repo contains solutions for the Ergo Quantum coding assignment.

### Challenge 1

- In the first part of challenge 1, we find the square root of a number, using an iterative procedure to obtain the result.

- We use the following formula;

x\_{n+1} = x_n - \frac{(x_n^2 - a)}{2x_n}

- Since it is rare for to reach exact 0 while using floating point arithmetic, we set the **threshhold** = 1e-10
- As a stopping criteria, we also set a maximum number of iterations, and limit it to 100.
