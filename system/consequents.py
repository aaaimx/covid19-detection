"""
Consequents: outputs definition, membership functions and  universe.

"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# -------------------------------------
# Diagnosis Universe
# -------------------------------------
covid = np.arange(0, 1, 0.001)
resfriado = np.arange(0, 1, 0.001)
alergia = np.arange(0, 1, 0.001)
influenza = np.arange(0, 1, 0.001)

universe = np.arange(0, 1, 0.001)
# -------------------------------------
# Outputs (consequents)
# -------------------------------------
Co = ctrl.Consequent(covid, 'Co')
Re = ctrl.Consequent(resfriado, 'Re')
Al = ctrl.Consequent(alergia, 'Al')
In = ctrl.Consequent(influenza, 'In')

# linguistic values
diagno = ['PP', 'Po', 'X', 'Pr' 'MP']
Co.automf(5, names=diagno)
Re.automf(5, names=diagno)
Al.automf(5, names=diagno)
In.automf(5, names=diagno)

# -------------------------------------
# Generate fuzzy membership functions
# -------------------------------------

# --------------------------------------------------
#  Lambda function to gbell & sigmoid memberships
# --------------------------------------------------

gbellmf = lambda a, b, c: fuzz.gbellmf(universe, a, b, c)
sigmf = lambda a, b: fuzz.sigmf(universe, a, b)

# Covid-19
Co['PP'] = sigmf(-50, 0.2)
Co['Po'] = gbellmf(0.14, 2.5, 0.33)
Co['Pr'] = gbellmf(0.14, 2.5, 0.66)
Co['MP'] = sigmf(50, 0.8)

# Resfriado
Re['PP'] = sigmf(-50, 0.2)
Re['Po'] = gbellmf(0.14, 2.5, 0.33)
Re['Pr'] = gbellmf(0.14, 2.5, 0.66)
Re['MP'] = sigmf(50, 0.8)

# Alergia
Al['PP'] = sigmf(-50, 0.2)
Al['Po'] = gbellmf(0.14, 2.5, 0.33)
Al['Pr'] = gbellmf(0.14, 2.5, 0.66)
Al['MP'] = sigmf(50, 0.8)

# Influenza
In['PP'] = sigmf(-50, 0.2)
In['Po'] = gbellmf(0.14, 2.5, 0.33)
In['Pr'] = gbellmf(0.14, 2.5, 0.66)
In['MP'] = sigmf(50, 0.8)
