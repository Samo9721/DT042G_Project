from converter.models.currency_converter import CurrencyConverter
from converter.models.length_converter import LengthConverter
from converter.models.temperature_converter import TemperatureConverter
from converter.models.volume_converter import VolumeConverter
from converter.models.weight_converter import WeightConverter


class ConverterFactory:
    converter_classes = {
        'length': LengthConverter,
        'weight': WeightConverter,
        'volume': VolumeConverter,
        'currency': CurrencyConverter,
        'temperature': TemperatureConverter,
    }

    def __init__(self, db_path):
        self.db_path = db_path


    def get_converter(self, unit_type):
        converter_class = self.converter_classes.get(unit_type)
        if not converter_class:
            raise ValueError(f"No converter available for type '{unit_type}'.")
        return converter_class(self.db_path)
