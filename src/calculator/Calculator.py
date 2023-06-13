"""A class to compute numbers."""

class Calculator:
    """Concrete class holding various arithmetic operations."""
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers.

        Parameters
        ----------
        a: float, required
            First number.
        b: float, required
            Second number

        Returns
        -------
        Sum of two numbers.
        """
        return a + b