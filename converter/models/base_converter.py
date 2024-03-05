from converter.exceptions.conversion_exceptions import InvalidUnitError, NonNumericValueError, NegativeValueError

class BaseConverter:
    def __init__(self, conversion_factors):
        self.conversion_factors = conversion_factors

    def convert(self, from_unit, to_unit, value):
        self._validate_units(from_unit, to_unit)
        self._validate_value(value)
        return self._perform_conversion(from_unit, to_unit, value)

    def _validate_units(self, from_unit, to_unit):
        # Normalize the units for validation.
        from_unit =  str(from_unit).lower()
        to_unit = str(to_unit).lower()
        if from_unit not in self.conversion_factors or to_unit not in self.conversion_factors:
            raise InvalidUnitError(f"Invalid or unsupported unit: {from_unit} or {to_unit}")
    @staticmethod
    def _validate_value(value):
        if not isinstance(value, (int, float)):
            raise NonNumericValueError()
        if value < 0:
            raise NegativeValueError()

    def _perform_conversion(self, from_unit, to_unit, value):
        if from_unit == to_unit:
            return value  # No conversion necessary if units are the same
        base_value = value * self.conversion_factors[from_unit]
        return base_value / self.conversion_factors[to_unit]
