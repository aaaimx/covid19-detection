import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from antecedents import Fi, DC, Mi, Fa, CN, Es, DG, DR, Ri
from consequents import Co, Al, Re, In

# -------------------------------------
# Inference rules
# -------------------------------------
rule1 = ctrl.Rule(antecedent=(Fi['No'] & DG['No']), consequent=(Co['PP'], Al['MP'], Re['PP'], In['PP']))
rule2 = ctrl.Rule(antecedent=(Fi['No'] & DG['Leve']), consequent=(Co['PP'], Re['MP'], In['PP']))
rule3 = ctrl.Rule(antecedent=(Fi['Alta'] & DC['~No'] & Mi['~No'] & Fa['~No'] & DR['No']), consequent=Re['MP'])
rule4 = ctrl.Rule(antecedent=(Fi['Alta'] & DR['~No']), consequent=(Co['MP'], Al['PP'], Re['PP']))
rule5 = ctrl.Rule(antecedent=(Fi['Leve'] & DR['~No']), consequent=Co['Pr'])
rule6 = ctrl.Rule(antecedent=(Fi['Leve'] & CN['~No'] & Es['~No'] & DG['~No'] & DR['No'] & Ri['~No']), consequent=Re['MP'])
rule7 = ctrl.Rule(antecedent=(Fi['~No'] & DC['~No'] & Mi['~No'] & Fa['~No'] & DR['~No']), consequent=In['MP'])
rule8 = ctrl.Rule(antecedent=(Fi['Leve'] & DR['No']), consequent=(Re['Pr'], In['Po']))
rule9 = ctrl.Rule(antecedent=(Fi['Alta'] & DC['~No'] & Mi['~No'] & Fa['~No'] & DR['~No']), consequent=(Co['MP'], Al['PP'], Re['PP'], In['PP']))
rule10 = ctrl.Rule(antecedent=(Fi['No'] & DG['Severo']), consequent=(Co['PP'], Al['PP'], Re['MP'], In['PP']))