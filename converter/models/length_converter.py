from .base_converter import BaseConverter
from converter.data.units import SUPPORTED_UNITS

class LengthConverter(BaseConverter):
    def __init__(self, db_path):
        # Initialize the base class with the conversion factors for length
        super().__init__(db_path, 'length')
