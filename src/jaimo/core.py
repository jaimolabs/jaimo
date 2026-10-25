"""
core.py - Core Function
"""

import math

# Function Compute
def f(input_fun: str, **kwargs) -> float:
    """
    Evaluate a mathematical expression string safely within a given environment.

    Args:
        input_fun (str): A mathematical expression as a string (e.g., "x**2 + sin(x)").
        **kwargs: Keyword arguments representing variable values (e.g., x=3.0).

    Returns:
        float: The calculated numerical result.

    Raises:
        ValueError: If the input values fall outside the domain or evaluation fails.
    """
    safe_env = {
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        **kwargs
    }
    try:
        return float(eval(input_fun, {"__builtins__": {}}, safe_env))
    except (ValueError, ZeroDivisionError, OverflowError) as e:
        # Throw a clear prompt when the input falls outside the defined domain.
        raise ValueError(
            f"Calculation error: The input values {kwargs} "
            f"may fall outside the domain of the function '{input_fun}'. "
            f"Details: {e}"
        )