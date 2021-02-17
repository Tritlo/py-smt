


def mono_solve(cnf):
  """ mono_solve only works for the simplest of CNFs,
      namely when there is only one equation. This is
      the trivial case, and a solution is given by
      returning the solution"""
  if len(cnf) == 1:
    return cnf[0]
  raise ValueError("mono_solve only works for one equation")

