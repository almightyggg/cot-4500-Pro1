def newton_method(f, df, p0, tol, N0):
    """
    Newton's Method for finding roots of a function.

    Parameters:
    f  : function  -> The function whose root we are trying to find.
    df : function  -> The derivative of the function.
    p0 : float     -> Initial approximation.
    tol: float     -> Tolerance (stopping criterion).
    N0 : int       -> Maximum number of iterations.

    Returns:
    root : float   -> Approximate root if successful, or None if unsuccessful.
    """
    i = 1  # Iteration counter

    while i <= N0:
        if df(p0) == 0:
            print("Unsuccessful: Derivative is zero")
            return None
        
        p_next = p0 - f(p0) / df(p0)  # Newton's iteration formula

        if abs(p_next - p0) < tol:  # Convergence check
            print(f"Success: Root found at {p_next} after {i} iterations")
            return p_next

        i += 1
        p0 = p_next  # Update previous approximation

    print("Unsuccessful: Maximum iterations reached")
    return None  # If max iterations are reached without convergence

# Example usage:
import math

# Define the function f(x) and its derivative f'(x)
def f(x):
    return x**3 - 4*x + 10  # Example function

def df(x):
    return 3*x**2 - 4  # Derivative of the function

# Initial guess, tolerance, and max iterations
p0 = 1.5
tol = 1e-6
N0 = 50

# Run Newton's Method
newton_method(f, df, p0, tol, N0)

