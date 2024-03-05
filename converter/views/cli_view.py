class ConversionView:
    def __init__(self):
        self.conversion_options = {
            '1': 'currency',
            '2': 'length',
            '3': 'temperature',
            '4': 'weight',
            '5': 'volume'
        }

    def display_menu(self):
        print("Choose the type of conversion:")
        for option, description in self.conversion_options.items():
            print(f"{option}: {description.capitalize()}")

    def get_conversion_type(self):
        self.display_menu()
        while True:
            conversion_type = input("Enter the number of the conversion type: ")
            if conversion_type in self.conversion_options:
                return self.conversion_options[conversion_type]
            print("Invalid conversion type selected. Please try again.")

    @staticmethod
    def get_unit_from():
        return input("Enter the unit you are converting from: ")

    @staticmethod
    def get_unit_to():
        return input("Enter the unit you are converting to: ")

    @staticmethod
    def get_amount():
        while True:
            amount_str = input("Enter the amount to convert: ")
            try:
                return float(amount_str)
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")

    def get_user_input(self):
        conversion_type = self.get_conversion_type()
        from_unit = self.get_unit_from()
        to_unit = self.get_unit_to()
        amount = self.get_amount()
        return conversion_type, from_unit, to_unit, amount

    @staticmethod
    def display_result(from_unit, to_unit, amount, result):
        print(f"{amount} {from_unit} is {result} {to_unit}")

    @staticmethod
    def display_error(error):
        print(f"An error occurred: {error}")
