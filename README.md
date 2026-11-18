# InternCircle Project 01: Interactive Calculator & Unit Converter

## Project overview
A beginner-friendly Python command-line application that performs basic arithmetic and unit conversions. It also includes currency conversion as an extra feature.

## Features
- Addition, subtraction, multiplication and division
- Safe division (division by zero is handled)
- Kilometers to miles
- Celsius to Fahrenheit
- Kilograms to pounds
- Extra: INR to USD and USD to INR using an exchange rate entered by the user
- Input validation using `while` loops and `try/except ValueError`
- Menu repeats until the user chooses Quit
- Conversion factors are stored in a dictionary

## Requirements
- Python 3.10 or newer
- VS Code or another Python editor
- No external Python packages are required

## How to run in VS Code
1. Extract the ZIP file.
2. Open the extracted `InternCircle_Project_01` folder in VS Code.
3. Open **Terminal → New Terminal**.
4. Check Python: `python --version`
5. Run the program:

```bash
python calculator.py
```

On some Windows installations, use:

```bash
py calculator.py
```

## Main menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Convert Units
6. Quit
7. Extra: Currency Converter

The first six options follow the main menu structure in the InternCircle learner guide. Currency conversion is included as an additional feature mentioned in the project overview.

## Conversion formulas
- Miles = Kilometers × 0.621371
- Fahrenheit = Celsius × 9 / 5 + 32
- Pounds = Kilograms × 2.20462
- INR to USD = INR amount ÷ INR value of 1 USD
- USD to INR = USD amount × INR value of 1 USD

The currency rate is entered by the user and is not fetched live.

## Suggested tests
| Test | Input | Expected result |
|---|---|---|
| Addition | 12 and 8 | 20 |
| Subtraction | 12 and 8 | 4 |
| Multiplication | 6 and 7 | 42 |
| Division | 20 and 5 | 4 |
| Division by zero | 20 and 0 | Cannot divide by zero |
| KM to miles | 10 km | About 6.2137 miles |
| Celsius to Fahrenheit | 0 C | 32 F |
| KG to pounds | 1 kg | About 2.2046 pounds |
| Invalid number | Type `hello` when asked for a number | Program asks again |

## Files
- `calculator.py` — complete Python source code
- `README.md` — project description, setup, formulas and test cases
- `.gitignore` — ignores Python cache and virtual environment files

## Before submitting
1. Run the program yourself in VS Code.
2. Test the operations and invalid input.
3. Take a screenshot of a successful sample run.
4. Upload `calculator.py` and `README.md` to a public GitHub repository (or another link-sharing service).
5. Submit the shareable code link and a short note describing the conversions on the InternCircle My Tasks page.

## Short submission note
I created a Python command-line calculator that supports addition, subtraction, multiplication and division. The unit converter supports kilometers to miles, Celsius to Fahrenheit, and kilograms to pounds. I also added INR/USD currency conversion as an extra feature. Input validation and a repeating menu help the program handle incorrect input safely.
