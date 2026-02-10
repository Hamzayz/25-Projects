UNITS = {
    'length': {
        'km': 'Kilometers',
        'm': 'Meters',
        'cm': 'Centimeters',
        'mm': 'Millimeters',
        'mile': 'Miles',
        'yard': 'Yards',
        'foot': 'Feet',
        'inch': 'Inches'
    },
    'weight': {
        'kg': 'Kilograms',
        'g': 'Grams',
        'mg': 'Milligrams',
        'ton': 'Tons',
        'lb': 'Pounds',
        'oz': 'Ounces'
    },
    'temperature': {
        'C': 'Celsius',
        'F': 'Fahrenheit',
        'K': 'Kelvin'
    }
}

def convert_length(value, from_unit, to_unit):
    to_meters = {
        'km': 1000,
        'm': 1,
        'cm': 0.01,
        'mm': 0.001,
        'mile': 1609.34,
        'yard': 0.9144,
        'foot': 0.3048,
        'inch': 0.0254
    }
    meters = value * to_meters[from_unit]
    result = meters / to_meters[to_unit]
    return result

def convert_weight(value, form_unit, to_unit):
    to_kg={
        'kg': 1,
        'g': 0.001,
        'mg': 0.000001,
        'ton': 1000,
        'lb': 0.453592,
        'oz': 0.0283495
    }
    kg = value * to_kg[form_unit]
    result = kg / to_kg[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    """Convert between temperature units"""
    # Convert to Celsius first
    if from_unit == 'C':
        celsius = value
    elif from_unit == 'F':
        celsius = (value - 32) * 5/9
    elif from_unit == 'K':
        celsius = value - 273.15
    
    # Convert from Celsius to target
    if to_unit == 'C':
        result = celsius
    elif to_unit == 'F':
        result = (celsius * 9/5) + 32
    elif to_unit == 'K':
        result = celsius + 273.15
    
    return result