# Explanation
A learning project for Schweize Jungen F study week of a battery system simulated in a lab at ETH Zurich

# Credits
Nikolas Lamprecht
Aksel Iberrakene
Linus Hollnagel

# Important file explanation:

## battery_optimisation.py: This contains the mathematical model for the optimisation, open folder in an editor and you can run it there.
- python script utilising numpy and matplotlib
- contains a mathematical model with certain constraints
- contains graphs for price, resistance, z (battery usage) and SoC (State of Charge)
- calculations for model

### price.txt: A text file containing the data for the price curve illustrating the price change over time.
- contains realistic independent data for price from https://www.ekz.ch/de/blue/wissen/2025/dynamische-wahltarife-2026.html

### resistance_2345678.tx A text file containing the data for the resistance curve
- realistic data from https://www.ekz.ch/de/blue/wissen/2025/dynamische-wahltarife-2026.html
- illustrating the resistance change over time (cycling through 2, 4 and 8 Ohms)

### rest of files: additional data for illustration and quick calculations.
