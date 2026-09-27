"""
converter.py
Core temperature conversion logic for Celsius, Fahrenheit, and Kelvin.
Kept separate from the GUI so the math can be tested/reused on its own.
"""

ABSOLUTE_ZERO_C = -273.15


class InvalidTemperatureError(ValueError):
    """Raised when a temperature is below absolute zero for its scale."""
    pass


def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    return k - 273.15


def fahrenheit_to_kelvin(f: float) -> float:
    return celsius_to_kelvin(fahrenheit_to_celsius(f))


def kelvin_to_fahrenheit(k: float) -> float:
    return celsius_to_fahrenheit(kelvin_to_celsius(k))


def _validate(value: float, unit: str) -> None:
    """Raise InvalidTemperatureError if value is below absolute zero."""
    if unit == "Celsius" and value < ABSOLUTE_ZERO_C:
        raise InvalidTemperatureError(
            f"{value}°C is below absolute zero ({ABSOLUTE_ZERO_C}°C)."
        )
    if unit == "Fahrenheit" and value < celsius_to_fahrenheit(ABSOLUTE_ZERO_C):
        raise InvalidTemperatureError(
            f"{value}°F is below absolute zero "
            f"({celsius_to_fahrenheit(ABSOLUTE_ZERO_C):.2f}°F)."
        )
    if unit == "Kelvin" and value < 0:
        raise InvalidTemperatureError(f"{value}K is below absolute zero (0K).")


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert `value` from `from_unit` to `to_unit`.
    Units must be one of: "Celsius", "Fahrenheit", "Kelvin".
    """
    _validate(value, from_unit)

    if from_unit == to_unit:
        return value

    # First normalize to Celsius, then go to the target unit.
    if from_unit == "Celsius":
        c = value
    elif from_unit == "Fahrenheit":
        c = fahrenheit_to_celsius(value)
    elif from_unit == "Kelvin":
        c = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unknown source unit: {from_unit}")

    if to_unit == "Celsius":
        return c
    elif to_unit == "Fahrenheit":
        return celsius_to_fahrenheit(c)
    elif to_unit == "Kelvin":
        return celsius_to_kelvin(c)
    else:
        raise ValueError(f"Unknown target unit: {to_unit}")


UNIT_SYMBOLS = {"Celsius": "°C", "Fahrenheit": "°F", "Kelvin": "K"}
