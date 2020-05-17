
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from rules import rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10

system = ctrl.ControlSystem(rules=[rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10])
diagnosis = ctrl.ControlSystemSimulation(system)

"""

COVID-19=[40.28, 0.4128, 0.5805, 0.4942, 0.1437, 0.1802, 0.4195, 0.9128, 0.1782]

Alergias=[36.78, 0.1105, 0.08621, 0.1453, 0.8563, 0.8314, 0.1437, 0.5523, 0.6264]

Resfriado=[37.7, 0.3779, 0.3161, 0.1686, 0.9138, 0.8779, 0.8563, 0.2151, 0.9138]

Influenza=[40.22, 0.8779, 0.8908, 0.9012, 0.3046, 0.1337, 0.4425, 0.1221, 0.4655]

COVID-19=[38.4, 0, 0, 1, 0, 0, 0, 1, 0]
"""

inputs = [37.7, 0.3779, 0.3161, 0.1686, 0.9138, 0.8779, 0.8563, 0.2151, 0.9138]
diagnosis.input['Fiebre'] = inputs[0]
diagnosis.input['DolorCabeza'] = inputs[1]
diagnosis.input['Mialgia'] = inputs[2]
diagnosis.input['Fatiga'] = inputs[3]
diagnosis.input['CongestionNasal'] = inputs[4]
diagnosis.input['Estornudos'] = inputs[5]
diagnosis.input['DolorGarganta'] = inputs[6]
diagnosis.input['Diarrea'] = inputs[7]
diagnosis.input['Rinorrea'] = inputs[8]
print(diagnosis.input)
diagnosis.compute()
print('Co:', diagnosis.output['Co'])
print('Al:', diagnosis.output['Al'])
print('Re:', diagnosis.output['Re'])
print('In:', diagnosis.output['In'])
#diagno.view(sim=diagnosis)

