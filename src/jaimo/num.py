"""
num.py - Numerical methods module.

Functions:
    - zero: Bisection method for root finding.
"""

from . import core

# Bisection method for root finding.
def zero(
    input_fun: str, 
    min_val: float, 
    max_val: float, 
    epsilon: float = 1e-5, 
    dec_len: int = 4
) -> float:
    """
    Find the zero (root) of a monotonic function within the interval 
    [min_val, max_val] using the bisection method.

    Args:
        input_fun (str): A mathematical expression as a string (e.g., "x**2 - 4").
        min_val (float): The lower bound of the search interval.
        max_val (float): The upper bound of the search interval.
        epsilon (float): Convergence tolerance for the function value.
        dec_len (int): Number of decimal places to round the final result.

    Returns:
        float: The approximated root of the function.

    Raises:
        ValueError: If the function values at the boundaries do not have 
            opposite signs (no root guaranteed in the interval).
    """
    # Calculate boundary values
    val_min = core.f(input_fun, x=min_val)
    val_max = core.f(input_fun, x=max_val)

    # Zero Existence Theorem Check
    if val_min * val_max > 0:
        raise ValueError(
            f"Function values at boundaries must have opposite signs. "
            f"f({min_val}) = {val_min}, f({max_val}) = {val_max}"
        )

    # Determining the monotonicity of a function
    is_increasing = val_min < val_max

    # Bisection method, guessing
    guess = (min_val + max_val) / 2
    guess_val = core.f(input_fun, x=guess)

    # Bisection method for finding zero
    while abs(guess_val) >= epsilon:
        if is_increasing:
            if guess_val > 0:
                max_val = guess
            else:
                min_val = guess
        else:
            if guess_val > 0:
                min_val = guess
            else:
                max_val = guess
                
        guess = (min_val + max_val) / 2
        guess_val = core.f(input_fun, x=guess)
        
    return round(guess, dec_len)