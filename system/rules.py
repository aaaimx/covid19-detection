import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from antecedents import Fi, DC, Mi, Fa, CN, Es, DG, DR, Ri
from consequents import Co, Al, Re, In

# -------------------------------------
# Inference rules
# -------------------------------------

# TODO: redefine rules
rule1 = ctrl.Rule(antecedent=(Fi['No'] & DG['No']), consequent=(Co['PP'] & Al['MP'] & Re['PP'] & In['PP']))
rule2 = ctrl.Rule(antecedent=(Fi['poor'] & DG['average']), consequent=(Co['PP']))
rule3 = ctrl.Rule(antecedent=(Fi['good'] & DR['poor'] & Mi['~No']), consequent=Co['PP'])
rule4 = ctrl.Rule(antecedent=(Fi['good']), consequent=Co['MP'])
rule5 = ctrl.Rule(antecedent=(Fi['average']), consequent=Co['PO'])
rule6 = ctrl.Rule(antecedent=(Fi['poor'] & DG['good']), consequent=Co['PP'])

# TODO: rule7, rule9, rule10