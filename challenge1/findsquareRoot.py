
def find_square_root(a, initial_guess, threshold = 1e-10, max_iterations = 100):

    # Check to ensure a is non negative

    if a < 0:
        raise ValueError("Cannot find the square root of a negative number")
    
    #initialize x with the initial guess

    x = initial_guess

    #use the given iterative formula to calculate the next guess (x_next_guess)

    for iteration in range(max_iterations):

        x_next_guess = x - ((x**2 - a)/ (2*x))

        #Check if the difference between consecutive iterations is below the threshhold

        if abs(x_next_guess - x)<threshold:
            break #Exit the loop if the stopping criterion is met
        
        #update x with the new guess for the next iteration
        x = x_next_guess
    return x_next_guess

    #Finding the square root of 2, with an initial guess of x = 1

result = find_square_root(2, 1)

    #print the result
print(f"The square root is approximately: {result}")
   