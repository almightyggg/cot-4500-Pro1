def bisection_method(f, left, right, tol, max_iter):
    if f(left) * f(right) >= 0:
        print("Bisection method fails. The function must have opposite signs at the endpoints.")
        return None
    
    i = 0  # Iteration counter
    while abs(right - left) > tol and i < max_iter:
        i += 1
        p = (left + right) / 2  # Midpoint
        
        if f(p) == 0 or abs(right - left) < tol:
            return p  # Root found
        
        # Determine which subinterval to keep
        if (f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0):
            right = p
        else:
            left = p

    return (left + right) / 2  # Return the final approximation

# Example usage:
import math
f = lambda x: x**3 - x - 2  # Example function
root = bisection_method(f, 1, 2, 1e-6, 100)
print("Root:", root)

