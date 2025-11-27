import matplotlib.pyplot as plt
import numpy as np

#set up lists for data
y_values = []
x_values = np.linspace(0, 360, 13)

#get y values as input
for _ in range(13):
    y_values.append(float(input("")))

#turn y_values into 
y_values = np.array(y_values)

#find trendline
m, b = np.polyfit(x_values, y_values, 1)

#print trendline gradient
print(str(30 * m) + "%/30s")