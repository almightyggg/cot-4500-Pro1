# Fixed Point Iteration Method in Python

# Constants
p0 = 1.5  # Initial guess
tol = 1e-6  # Tolerance
N0 = 8  # Now set to fail after 8 iterations
result = "Failure"  # Default result

def fixed_point_iteration():
    global p0, result
    i = 1
    p = 0

    while i <= N0:
        p = -p0**3 + 5 * p0 - 10  # Fixed-point iteration formula

        if p != p:  # Check if p is NaN (divergence)
            print("\nResult diverges")
            break

        print(f"{i} : {p}")

        if abs(p - p0) < tol:  # Convergence check
            result = "Success"
            break

        i += 1
        p0 = p  # Update p0 for next iteration

    if i >= N0:  # Force failure after 8 iterations
        result = "Failure"

    print(f"\n{result} after {i} iterations\n")

# Run the function
fixed_point_iteration()

