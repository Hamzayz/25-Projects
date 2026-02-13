value = int(input("Enter the Value: "))
from_unit = input("Enter the form_unit: ")
to_unit = input("Enter the to unit: ")

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
print(result)