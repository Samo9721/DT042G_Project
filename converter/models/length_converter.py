from .base_converter import BaseConverter
from converter.data.units import SUPPORTED_UNITS

class LengthConverter(BaseConverter):
    def __init__(self):
        # Initialize the base class with the conversion factors for length
        super().__init__(SUPPORTED_UNITS['length']['units'])
