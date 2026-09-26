# Smart Travel Planner

A beginner-friendly Python console program that collects trip details, calculates estimated costs, and prints a formatted travel summary.

## Requirements

- Python 3
- No external libraries, database, files, or API access

## Run the program

From this folder, run:

```console
python smart_travel_planner.py
```

## What it collects

- Travel name and destination
- Number of travelers and travel days
- Transportation cost per traveler for the trip
- Hotel cost per traveler per day
- Food cost per traveler per day
- Activity cost per traveler for the trip

Food cost is collected separately because the program needs an amount to calculate the requested total food cost. Enter cost amounts in the same currency.

## Calculations

The program uses separate functions that return each calculated value:

- Transportation total = cost per traveler x travelers
- Hotel total = cost per traveler per day x days x travelers
- Food total = cost per traveler per day x days x travelers
- Activity total = cost per traveler x travelers
- Overall trip cost = transportation + hotel + food + activities
- Cost per traveler = overall trip cost / travelers
- Average daily cost = overall trip cost / days

It validates that traveler and day counts are positive whole numbers and that costs are non-negative. A dictionary keeps the related trip details organized. The program also demonstrates variables, data types, input, type conversion, functions, parameters, return values, arithmetic, validation, and formatted output.