from converter.factories.converter_factory import ConverterFactory

class ConversionController:
    @staticmethod
    def perform_conversion(view, unit_type, from_unit, to_unit, amount):
        try:
            # Get the appropriate converter instance for the given unit type
            converter = ConverterFactory.get_converter(unit_type)
            # Perform the conversion
            result = converter.convert(from_unit, to_unit, amount)
            # Display the result using the view
            view.display_result(from_unit, to_unit, amount, result)
        except Exception as e:
            # If an error occurs, display it using the view
            view.display_error(e)
