
from pysmt.solve import mono_solve
import pytest

def test_mono_solve():
  assert(mono_solve([[1]]) == [1])
  assert(mono_solve([[1,2,-3]])) == [1,2,-3]

  with pytest.raises(ValueError) as err:
    mono_solve([[1],[1,2]])
  assert("mono_solve only works for one equation" == str(err.value))

