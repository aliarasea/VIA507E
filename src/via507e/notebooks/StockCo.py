from pulp import *

Investments = ['1', '2', '3', '4']

# A dictionary of the net present value of 4 different investments
NPV = {"1": 16000,
       "2": 22000,
       "3": 12000,
       "4": 8000}
# A dictionary of the cash outflow required for 4 different investments
Outflow = {"1": 5000,
           "2": 7000,
           "3": 4000,
           "4": 3000}

# Create the 'prob' variable to contain the problem data
prob = LpProblem("StockCo_Model", LpMaximize)

#A binary variable 'InvVar' is created (lower bound zero, upper bound 1, and category integer
InvVar = LpVariable.dicts("Inv", Investments, cat= LpBinary)
# The objective function is added to 'prob' first
prob += lpSum([NPV[i] * InvVar[i] for i in Investments])

# The constraints are entered
prob += lpSum([Outflow[i] * InvVar[i] for i in Investments]) <= 14000, "Budget_Constraint"
prob += lpSum([InvVar[i] for i in Investments]) <= 2, "At_most_two_investments"
prob += InvVar["2"] - InvVar["1"] <= 0
prob += InvVar["2"] + InvVar["4"] <= 1
prob.writeLP("StockCo.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()

# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)
# The optimised objective function value is printed to the screen
print("Total Cost of the Process = ", value(prob.objective))
