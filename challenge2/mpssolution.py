import numpy as np

def create_mps(vector):
    # Determine the nearest power of 2 for padding
    N = int(np.ceil(np.log2(len(vector))))
    # Pad the input vector with zeros to match the nearest power of 2
    padded_vector = np.pad(vector, (0, 2**N - len(vector)))

    # Normalize the padded vector
    norm = np.linalg.norm(padded_vector)
    normalized_vector = padded_vector / norm

    # Reshape the normalized vector into a matrix
    reshaped_matrix = normalized_vector.reshape((2**(N-1), 2))
    psi = []

    # Perform Singular Value Decomposition (SVD) and store tensors in psi
    for _ in range(N-1):
        U, s, V = np.linalg.svd(reshaped_matrix)
        # Reshape V into a tensor of size [len(s), 2, len(V)//len(s)]
        reshaped_V = V.reshape((len(s), 2, len(V)//len(s)))
        # Swap the axes 0 and 1
        reshaped_V = np.swapaxes(reshaped_V, 0, 1)
        # Append the reshaped tensor to psi
        psi.append(reshaped_V)
        # Update reshaped_matrix for the next iteration
        reshaped_matrix = np.dot(U, np.diag(s))

    # Reverse the order of tensors in psi
    psi.reverse()
    return psi

def verify_state(psi, vector):
    N = len(psi)
    # Iterate through all possible binary representations of indices
    for i in range(2**N):
        # Convert the index i to binary representation with leading zeros to match length N
        b = np.array(list(format(i, f'0{N}b')), dtype=int)
        # Compute the product of tensors corresponding to the binary representation
        val = np.prod([psi[j][b[j]] for j in range(N)])
        # Print the original vector element and the computed value
        print(f"x[{i}] = {vector[i]:.6f}, val = {val:.6f}")

# Example usage
input_vector = np.array([1, 2, 3, 4])
# Create the MPS representation of the input vector
psi_list = create_mps(input_vector)
# Verify the values of the state
verify_state(psi_list, input_vector)
