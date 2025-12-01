# Explanation
Optimisation of a home battery storage system.</br>
A learning project for "TechXperience" study week of Schweizer Jugend Forscht. Supervised by Francisco Escobar (PSL, ETH Zurich)</br>
Mathematical optimisation of simplified model. Programmed in python with library gurobipy. Battery specific variables got determined experimentally.

# Credits
Nikolas Lamprecht</br>
Aksel Iberrakene</br>
Linus Hollnagel</br>
Francisco Escobar (PSL, ETH Zurich)

# Important file explanation:

## battery_optimisation.py : This contains the mathematical model for the optimisation, open folder in an editor and you can run it there.
- python script utilising numpy and matplotlib.
- contains a mathematical model with certain constraints.
- contains graphs for price, resistance, z (battery usage) and SoC (State of Charge).
- calculations for model.

### price.txt : A text file containing the data for the price curve illustrating the price change over time.
- contains realistic independent data for price from https://www.ekz.ch/de/blue/wissen/2025/dynamische-wahltarife-2026.html

### resistance_2468.txt : A text file containing the data for the resistance curve
- simplified realistic data from https://www.ekz.ch/de/blue/wissen/2025/dynamische-wahltarife-2026.html.
- illustrating the resistance change over time (cycling through 2, 4, 6 and 8 Ohms).

### rest of files : additional data for illustration and quick calculations.
