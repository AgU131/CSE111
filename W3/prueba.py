# trying

"""
I should get this
> python test_water_flow.py
======================== test session starts ==========================
platform win32 -- Python 3.11.1, pytest-7.2.1, pluggy-1.0.0 --
rootdir: C:\Users\cse111\week03
collected 3 items
test_water_flow.py::test_water_column_height PASSED              [ 33%]
test_water_flow.py::test_pressure_gain_from_water_height PASSED  [ 66%]
test_water_flow.py::test_pressure_loss_from_pipe PASSED          [100%]
========================= 3 passed in 0.07s ===========================
"""
import pytest

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    pressure_kilopascals = (-0.04 * 998.2 * fluid_velocity ** 2 * quantity_fittings)

    return pressure_kilopascals