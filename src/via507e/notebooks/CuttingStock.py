from pulp import *

Pattern = ['1', '2', '3', '4', '5', '6']

EndItem = ['12in', '15in', '30in']

Scrap = {"1": 5,
         "2": 5,
         "3": 8,
         "4": 2,
         "5": 11,
         "6": 11}

Demand = {"12in": 500,
         "15in": 715,
         "30in": 630}

EndItemSize = [[0, 7, 0],
           [0, 1, 3],
           [1, 0, 3],
           [9, 0, 0],
           [2, 1, 2],
           [7, 1, 0]]

EndItemSize = makeDict([Pattern,EndItem],EndItemSize,0)


# Create the 'prob' variable to contain the problem data
prob = LpProblem("Cutting_Stock_Model", LpMinimize)

#Note the variables are defined to be integers (cat=LpInteger)
Var = LpVariable.dicts("RollNumberPattern", Pattern, 0, cat = LpInteger)

# The objective function is added to 'prob' first
prob += lpSum([Scrap[i] * Var[i] for i in Pattern])

# The constraints are entered
for j in EndItem:
    prob += lpSum([EndItemSize[i][j] * Var[i] for i in Pattern]) >= Demand[j]

prob.writeLP("CuttingStock.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)
# The optimised objective function value is printed to the screen
print("Total Cost of the Process = ", value(prob.objective))
