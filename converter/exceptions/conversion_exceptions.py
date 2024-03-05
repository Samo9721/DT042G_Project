
class ConversionError(Exception):
    """Base exception class for all conversion-related errors."""
    def __init__(self, message="An error occurred during conversion"):
        super().__init__(message)

class InvalidUnitError(ConversionError):
    """Exception raised for specifying an unsupported unit for conversion."""
    def __init__(self, unit, message="Invalid or unsupported unit"):
        self.unit = unit
        self.message = f"{message}: {unit}"
        super().__init__(self.message)

class NegativeValueError(ConversionError):
    """Exception raised for specifying a negative value for conversion."""
    def __init__(self, message="Negative values are not allowed"):
        super().__init__(message)

class NonNumericValueError(ConversionError):
    """Exception raised for specifying a non-numeric value for conversion."""
    def __init__(self, message="Value must be numeric"):
        super().__init__(message)

class InvalidCurrencyError(Exception):
    """Exception raised for invalid currency codes."""
    def __init__(self, message="Invalid or unsupported currency code provided"):
        super().__init__(message)

class NetworkError(Exception):
    """Exception raised when there's a network error or no internet connection."""
    def __init__(self, message="Network error, please check your internet connection"):
        super().__init__(message)