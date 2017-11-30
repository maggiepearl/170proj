
from __future__ import print_function
import sys
from ortools.constraint_solver import pywrapcp
def dianarox(fname):
  with open(fname) as f:
    content = f.readlines()
  content = [x.strip() for x in content]
  num_constraints = int(content[1])
  num_people = int(content[0])
  content = content[2:]
  constraints = []
  s = set()
  for elem in content:
    t = elem.split()
    constraints.append(t)
    for x in t:
      s.add(x)
  s = list(s)
  variables = []
  domains = []
  for i in range(num_people):
    domains.append(i)
  solver = pywrapcp.Solver("simple_example")
  real_vars = []
  for i in range(len(domains)):
    variables.append([solver.IntVar(0, num_people-1, s[i]), s[i]])
    real_vars.append(variables[i][0])
  solver.Add(solver.AllDifferent(real_vars))
  for c in constraints:
    for var in variables:
      if (c[0] == var[1]):
        first_index = var[0]
      if (c[1] == var[1]):
        second_index = var[0]
      if (c[2] == var[1]):
        third_index = var[0]
    solver.Add(solver.Max(first_index < third_index, second_index > third_index)==1 )
    solver.Add(solver.Max(first_index > third_index, second_index < third_index)==1 )
  db = solver.Phase(real_vars, solver.CHOOSE_FIRST_UNBOUND, solver.ASSIGN_MIN_VALUE)
  solver.Solve(db)
  res = domains
  while solver.NextSolution():
    for i in range(num_people):
      res[int(variables[i][0].Value())] = variables[i][1]
    ret = ""
    for st in res:
      ret += st + " "
    print(ret)
