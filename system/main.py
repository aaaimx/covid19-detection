
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from rules import rule1, rule2, rule3, rule4, rule5, rule6

system = ctrl.ControlSystem(rules=[rule1, rule2, rule3, rule4, rule5, rule6])
diagnosis = ctrl.ControlSystemSimulation(system)

