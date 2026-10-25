"""
jaimo - Python library and toolkit for data science applications.
"""

# Current Version Number
__version__ = "0.1.1"

# Import the main functions into the top-level namespace.
from .core import f     # Function Compute

from . import num       # Numerical Function

# Content permitted for secondary import / wildcard import.
__all__ = [
    "f", 
    "num"
]