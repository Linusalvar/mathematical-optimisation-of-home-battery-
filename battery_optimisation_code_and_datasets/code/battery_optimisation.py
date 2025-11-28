import numpy as np
import matplotlib.pyplot as plt
from random import randint
from random import choice
import gurobipy as gp
from gurobipy import GRB

#battery specific slopes
current_load_dict = {2:-1.2194749695604454, 4:-0.9539072039011061, 6: -0.76388888892, 8:-0.5738705739560475}
charging_slope = 0.9310134757692252

#how many data points(time points)
time_points_count = 24

#load .txt files
load_list_file = np.loadtxt(r"C:\Users\linus\OneDrive\Techxperience_studyweek\battery_simulation\datasets\resistance_2468.txt")
electric_cost_file = np.loadtxt(r"C:\Users\linus\OneDrive\Techxperience_studyweek\battery_simulation\datasets\price.txt")

# Get right part of data 
load_list = load_list_file[:, 1]
electric_cost = electric_cost_file[:, 1]

#initialize model
model = gp.Model("battery_optimisation")

#add variables which should be found
Z = model.addVars(time_points_count, vtype=GRB.BINARY, name="Z")
state_of_charge = model.addVars(time_points_count, lb=85, ub=90, vtype=GRB.CONTINUOUS, name = "state_of_charge")

#SoC change for every k(time)
for k in range(time_points_count - 1):
    model.addConstr(
        state_of_charge[k + 1] == state_of_charge[k] + (Z[k] * current_load_dict[int(load_list[k])]) + ((1 - Z[k]) * charging_slope)
    )

#add SoC constraints for first SoC and last SoC
model.addConstr(89.5 <= state_of_charge[time_points_count - 1])
model.addConstr(state_of_charge[time_points_count - 1] <= 90.5)
model.addConstr(89.5 <= state_of_charge[0])
model.addConstr(state_of_charge[0] <= 90.5)

#set objective function, minimize the electricity cost
model.setObjective(
    gp.quicksum(
        electric_cost[k] * (1 + (abs(current_load_dict[int(load_list[k])]) / charging_slope)) * (1 - Z[k])
        for k in range(time_points_count)
    ), 
    GRB.MINIMIZE
)

#optimize
model.optimize()


#make python lists of solutions for easier output
z_solutions = []
state_of_charge_solutions = []
for k in range(time_points_count):
    z_solutions.append(int(Z[k].X))
    state_of_charge_solutions.append(float(state_of_charge[k].X))


if model.status == GRB.OPTIMAL:
    print("Objective value(optimal cost in Rappen per Watt):", model.ObjVal/120, "Rp./W")
"""
    print("\nZ decisions (0 = charge, 1 = discharge):")
    for k in range(time_points_count):
        print(f"t={k}: {z_solutions[k]}")

    print("\nState of Charge:")
    for k in range(time_points_count):
        print(f"t={k}: {state_of_charge_solutions[k]:.2f}")
else:
    print("No optimal solution found.")
"""

#Plotting results
fig, axes = plt.subplots(4, 1, figsize=(12, 10))

#Time axis (assuming each period is 1h, max 24h)
time_axis = np.arange(time_points_count)

#Price graph
axes[0].plot(time_axis, electric_cost, "b-", linewidth=2, label="Electricity Price")
axes[0].set_xlabel("Time (min)")
axes[0].set_ylabel("Price")
axes[0].set_title("Electricity Price Over Time")
axes[0].grid(True, alpha=0.3)
axes[0].legend()

#resistance over time
axes[1].step(time_axis, load_list, "m-", linewidth=2, marker="", markersize=6, where="post", label="Resistance")
axes[1].set_xlabel("Time (min)")
axes[1].set_ylabel("Resistance in Ohms(Ω)")
axes[1].set_title("Resistance over time")
axes[1].set_ylim(1.5, 8.5)
axes[1].set_yticks([2, 4, 6, 8])
axes[1].grid(True, alpha=0.3)
axes[1].legend()


#battery on/off graph
axes[2].step(time_axis, z_solutions, "g-", linewidth=2, marker="", markersize=6, label="Battery Usage (z)", where="post")
axes[2].set_xlabel("Time (min)")
axes[2].set_ylabel("Battery Usage (1=on, 0=off)")
axes[2].set_title("Battery Usage Decision Over Time (Binary: 0 or 1)")
axes[2].set_ylim(-0.1, 1.1)
axes[2].set_yticks([0, 1])
axes[2].grid(True, alpha=0.3)
axes[2].legend()

#Battery SoC graph
axes[3].plot(range(time_points_count), state_of_charge_solutions, "r-", linewidth=2, marker="", markersize=4, label="State of Charge")
axes[3].axhline(y=90, color="k", linestyle="--", alpha=0.5, label=f"Max SOC ({90}%)")
axes[3].axhline(y=85, color="k", linestyle="--", alpha=0.5, label=f"Min SOC ({85}%)")
axes[3].set_xlabel("Time (min)")
axes[3].set_ylabel("SOC")
axes[3].set_title("Battery State of Charge Over Time")
axes[3].grid(True, alpha=0.3)
axes[3].legend()

#plot
plt.tight_layout()
plt.show()
