from pulp import *

# Create the 'prob' variable to contain the problem data
prob = LpProblem("Fixed_Charge_Model",LpMaximize)

#Define variables
x1 = LpVariable("ShirtsProd", 0, cat = LpInteger)
x2 = LpVariable("ShortsProd", 0, cat = LpInteger)
x3 = LpVariable("PantsProd", 0, cat = LpInteger)
y1 = LpVariable("ShirtMachine", 0, cat = LpBinary)
y2 = LpVariable("ShortMachine", 0, cat = LpBinary)
y3 = LpVariable("PantsMachine", 0,  cat = LpBinary)

#Objective Function
prob += 6*x1 + 4*x2 + 7*x3 - 200*y1 - 150*y2 - 100*y3
# The five constraints are entered
prob += 3*x1 + 2*x2 + 6*x3 <= 150, "LaborConstraint"
prob += 4*x1 + 3*x2 + 4*x3 <= 160, "ClothConstraint"


BigM = 1000
prob += x1 - BigM*y1 <= 0, "ShirtMachine"
prob += x2 - BigM*y2 <= 0, "ShortMachine"
prob += x3 - BigM*y3 <= 0, "PantsMachine"

prob.writeLP("FixedCharge.lp")


# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)
# The optimised objective function value is printed to the screen
print("Total Profit of the Process = ", value(prob.objective))
