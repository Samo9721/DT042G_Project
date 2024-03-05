import argparse
import sys
from converter.controllers.conversion_controller import ConversionController
from converter.views.cli_view import ConversionView


def main():
    controller = ConversionController()
    view = ConversionView()

    # Command line mode
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Convert between units of measurement.")
        parser.add_argument("conversion_type", choices=['currency', 'length', 'temperature', 'weight', 'volume'],
                            help="Type of conversion: currency, length, temperature, weight, or volume")
        parser.add_argument("--from", dest='from_unit', required=True, help="Unit to convert from")
        parser.add_argument("--to", dest='to_unit', required=True, help="Unit to convert to")
        parser.add_argument("--amount", type=float, required=True, help="Amount to convert")

        args = parser.parse_args()

        # Convert the input conversion type to the one expected by the controller
        conversion_type = view.conversion_options.get(args.conversion_type, args.conversion_type)

        controller.perform_conversion(view, conversion_type, args.from_unit, args.to_unit, args.amount)

    # Interactive mode
    else:
        conversion_type, from_unit, to_unit, amount = view.get_user_input()
        controller.perform_conversion(view, conversion_type, from_unit, to_unit, amount)

if __name__ == "__main__":
    main()
