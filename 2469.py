# =================== Convert the Temperature


# You are given a number celsius (float)
# Convert it into :- 
# Kelvin = celsius + 273.15
# Fahrenheit = celsius * 1.80 + 32


# --- Solution 1 :- Simple Conversion


def convertTemperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32

    return [kelvin, fahrenheit]

celsius = 36.50
print(convertTemperature(celsius))