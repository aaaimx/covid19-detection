"""
===============
Eggs Boiling Example
===============

This is a simple example of Fuzzy enference system to determinate the boiling time of eggs given
the size/weight.

https://github.com/calidev/presentaciones/blob/master/Pyday_2018/Truth%20is%20always%20Strange%20-%20Fuzzy%20logic%20in%20Python/Truth%20is%20always%20strange.pdf
"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Symptoms Universe
Fi = np.arange(-13.5, 39.1, 0.01)
DC = np.arange(-30, 0.3, 0.01)
Mi = np.arange(-30, 0.3, 0.01)
Fa = np.arange(-64, 0.2, 0.01)
CN = np.arange(-30, 0.3, 0.01)
Es = np.arange(-30, 0.3, 0.01)
DG = np.arange(-30, 0.67, 0.01)
DR = np.arange(-30, 0.3, 0.01)
Ri = np.arange(-30, 0.3, 0.01)

# symptoms are the antecedents (inputs)
Fi_Antecedent = ctrl.Antecedent(Fi, 'Fi')
DC_Antecedent = ctrl.Antecedent(DC, 'DC')
Mi_Antecedent = ctrl.Antecedent(Mi, 'Mi')
Fa_Antecedent = ctrl.Antecedent(Fa, 'Fa')
CN_Antecedent = ctrl.Antecedent(CN, 'CN')
Es_Antecedent = ctrl.Antecedent(Es, 'Es')
DG_Antecedent = ctrl.Antecedent(DG, 'DG')
DR_Antecedent = ctrl.Antecedent(DR, 'DR')
Ri_Antecedent = ctrl.Antecedent(Ri, 'Ri')

# the diagnosis is the consequent (outputs)
diagno_Consequent = ctrl.Consequent(np.arange(-50, 0.8, 0.01), 'diagnosis')

Fi_Antecedent.automf(3)
DC_Antecedent.automf(3)
Mi_Antecedent.automf(3)
Fa_Antecedent.automf(3)
CN_Antecedent.automf(3)
Es_Antecedent.automf(3)
DG_Antecedent.automf(3)
DR_Antecedent.automf(3)
Ri_Antecedent.automf(3)

# fuzzy sets
diagno_Consequent.automf(3)

# Fiber fuzzy sets
diagno_Consequent['low'] = fuzz.trimf(diagno_Consequent.universe, [-50, 0.2])
diagno_Consequent['medium'] = fuzz.trimf(diagno_Consequent.universe, [0.14, 2.5, 0.66])
diagno_Consequent['high'] = fuzz.trimf(diagno_Consequent.universe, [50, 0.8])

Fi_Antecedent['average'].view()

# view the fuzzy set.
# eggSize.view()  # uncoment to view graphic (it can fails in windows)

# Simple conditipnal rules "IF antecendent THEN consequence"
rule1 = ctrl.Rule(eggSize['large'], boilTime['long'])
rule2 = ctrl.Rule(eggSize['small'], boilTime['short'])

# view the fuzzy set.
# boilTime.view()

# controller
boilerController = ctrl.ControlSystem([rule1, rule2])

# simulation
boilerSimulator = ctrl.ControlSystemSimulation(boilerController)

# input
# rawEggSize = input("please input the weight of the egg (from 40 to 70 grams)")
rawEggSize = 60

# ensure that is in range
clippeEggSize = float(np.clip(rawEggSize, 40, 70))

# load the value in the simulator
boilerSimulator.input['size'] = rawEggSize

# process
boilerSimulator.compute()

# output
resultTime = boilerSimulator.output['time']

print("you need %1.2f minutes to boil that egg" % resultTime)