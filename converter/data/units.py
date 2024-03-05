
SUPPORTED_UNITS = {
    'length': {
        'base': 'm', # Base unit is meters
        'units':{
            'mm': 0.001,  # Millimeters to meters
            'cm': 0.01,  # Centimeters to meters
            'dm': 0.1,  # Decimeters to meters
            'm': 1.0,  # Meters to meters
            'km': 1000,  # Kilometers to meters
            'in': 0.0254,  # Inches to meters
            'ft': 0.3048,  # Feet to meters
            'yd': 0.9144,  # Yards to meters
            'mi': 1609.34,  # Miles to meters
            'nmi': 1852  # Nautical miles to meters
        }
    },
    'weight': {
        'base': 'kg', # Base unit is kilograms
        'units': {
            'kg': 1,  # Kilogram
            'g': 0.001,  # Gram
            'mg': 0.000001,  # Milligram
            't': 1000,  # Metric ton (tonne)
            'lb': 0.45359237,  # Pound (avoirdupois)
            'oz': 0.0283495231,  # Ounce
            'ct': 0.0002,  # Carat
            'u': 1.66053906660e-27,  # Atomic mass unit (AMU)
            'Eg': 1e18,  # Exagram
            'Pg': 1e15,  # Petagram
            'Tg': 1e12,  # Teragram
            'Gg': 1e9,  # Gigagram
            'Mg': 1e6,  # Megagram
            'hg': 0.1,  # Hectogram
            'dag': 0.01,  # Dekagram
            'dg': 0.0001,  # Decigram
            'cg': 0.00001,  # Centigram
            'µg': 1e-6,  # Microgram
            'ng': 1e-9,  # Nanogram
            'pg': 1e-12,  # Picogram
        }
    },
    'volume': {
        'base': 'l',  # Base unit is liters
        'units': {
            'ml': 0.001,          # Milliliter
            'cl': 0.01,           # Centiliter
            'dl': 0.1,            # Deciliter
            'l': 1,               # Liter
            'dal': 10,            # Dekaliter
            'hl': 100,            # Hectoliter
            'kl': 1000,           # Kiloliter
            'm3': 1000,           # Cubic meter (equivalent to 1000 liters)
        }
    }
}