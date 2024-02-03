from pulp import *

prob = LpProblem("Simple LP Problem", LpMaximize)

x1 = LpVariable("x1")
x2 = LpVariable("x2")

prob += x1 + x2

prob += 2 * x1 + x2 <= 100
prob += x1 <= 50
prob += x1 <= 30
prob += 2 * x2 <= 40

prob += x1 >= 0
prob += x2 >= 0

prob.solve()

print ("Максимальна кількість лимонаду: ", x1.varValue)
print ("Максимальна кількість фруктового соку: ", x2.varValue)
