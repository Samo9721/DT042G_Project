from .base_converter import BaseConverter
from converter.exceptions.conversion_exceptions import InvalidUnitError


class TemperatureConverter(BaseConverter):
    def __init__(self):
        super().__init__(None)

    def convert(self, from_unit, to_unit, value):
        #validate the units since temperature conversions have unique units
        self._validate_units(from_unit, to_unit)

        # Call the specific conversion method based on the from and to units
        if from_unit == 'C' and to_unit == 'F':
            return self._celsius_to_fahrenheit(value)
        elif from_unit == 'F' and to_unit == 'C':
            return self._fahrenheit_to_celsius(value)
        elif from_unit == 'C' and to_unit == 'K':
            return self._celsius_to_kelvin(value)
        elif from_unit == 'K' and to_unit == 'C':
            return self._kelvin_to_celsius(value)
        else:
            raise InvalidUnitError(f"Cannot convert temperature from {from_unit} to {to_unit}")

    def _validate_units(self, from_unit, to_unit):
        valid_units = ['C', 'F', 'K']
        if from_unit not in valid_units or to_unit not in valid_units:
            raise InvalidUnitError(f"Invalid unit for temperature conversion: {from_unit} or {to_unit}")

    @staticmethod
    def _celsius_to_fahrenheit(celsius):
        return (celsius * 9 / 5) + 32

    @staticmethod
    def _fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def _celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def _kelvin_to_celsius(kelvin):
        return kelvin - 273.15

