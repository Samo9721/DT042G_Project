import argparse
import sys
from converter.controllers.conversion_controller import ConversionController
from converter.data.units import SUPPORTED_UNITS
from converter.database.database_setup import DatabaseSetup
from converter.views.cli_view import ConversionView


def initialize_database(db_path):
    # Ensure that db_path is a file path, not a directory path
    sql_schema_file = 'converter/database/units_table.sql'
    db_file = f'{db_path}/utilities_app.db'  # Complete file path for the database

    # Instantiate DatabaseManager and perform initialization
    db_manager = DatabaseSetup(db_file, sql_schema_file)
    db_manager.create_db_schema()
    db_manager.populate_units_table(SUPPORTED_UNITS)


def main():

    db_path = 'converter/database'
    initialize_database(db_path)
    view = ConversionView()
    controller = ConversionController(db_path + "/utilities_app.db")


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
