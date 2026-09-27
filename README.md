# 🌡 Temperature Converter

A desktop Temperature Converter built with Python and Tkinter, supporting Celsius, Fahrenheit, and Kelvin.

## Features

- Celsius ⇄ Fahrenheit ⇄ Kelvin conversion (any unit to any unit)
- Clean, light-theme GUI with a sky-blue background
- Swap-units button
- Input validation (rejects empty/non-numeric input)
- Physical validation (rejects temperatures below absolute zero)
- Conversion history list
- Clear button
- Enter key support
- No external libraries required — pure Python standard library

## Conversion Formulas

### Celsius to Fahrenheit
`F = (C × 9/5) + 32`

### Fahrenheit to Celsius
`C = (F − 32) × 5/9`

### Celsius to Kelvin
`K = C + 273.15`

### Kelvin to Celsius
`C = K − 273.15`

## Technologies Used

- Python 3
- Tkinter (standard library, ships with Python)

## Project Structure

```
temp_converter/
├── main.py           # GUI (entry point)
├── converter.py       # Conversion logic (unit-tested independently of the GUI)
├── requirements.txt
└── README.md
```

## How to Run

1. Clone/download the repository
2. Open the project folder
3. Run:

```
python main.py
```

## Running the conversion logic without the GUI

```python
from converter import convert
convert(100, "Celsius", "Fahrenheit")  # -> 212.0
```
