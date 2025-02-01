# Constants
x0 = 1.5
tol = 0.000001

# Initialization
iter = 0
diff = x0
x = x0

# Print first iteration
print(f"{iter} : {x}")

# Iterative computation
while diff >= tol:
    iter += 1
    y = x  # Store previous value of x
    x = (x / 2) + (1 / x)  # Update x using given formula
    diff = abs(x - y)  # Compute difference

    print(f"{iter} : {x}")

# Final convergence message
print(f"\nConvergence after {iter} iterations.")

