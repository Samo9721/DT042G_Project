# length_converter.py in the models directory

from .base_converter import BaseConverter
from converter.data.units import SUPPORTED_UNITS

class WeightConverter(BaseConverter):
    def __init__(self):
        # Initialize the base class with the conversion factors for length
        super().__init__(SUPPORTED_UNITS['weight']['units'])
