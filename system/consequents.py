"""
Consequents: outputs definition, membership functions and  universe.

"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# -------------------------------------
# Diagnosis Universe
# -------------------------------------
covid = np.arange(0, 10, 0.01)
resfriado = np.arange(0, 10, 0.01)
alergia = np.arange(0, 10, 0.01)
influenza = np.arange(0, 10, 0.01)

# -------------------------------------
# Outputs (consequents)
# -------------------------------------
Co = ctrl.Consequent(np.arange(0, 10, 0.01), 'Co')
Re = ctrl.Consequent(np.arange(0, 10, 0.01), 'Re')
Al = ctrl.Consequent(np.arange(0, 10, 0.01), 'Al')
In = ctrl.Consequent(np.arange(0, 10, 0.01), 'In')

# linguistic values
diagno = ['PP', 'Po', 'Pr' 'MP', 'X']
Co.automf(5, names=diagno)
Re.automf(5, names=diagno)
Al.automf(5, names=diagno)
In.automf(5, names=diagno)

# -------------------------------------
# Generate fuzzy membership functions
# -------------------------------------

# Covid-19
Co['PP'] = fuzz.sigmf(Co.universe, -50, 0.2)
Co['Po'] = fuzz.gbellmf(Co.universe, 0.14, 2.5, 0.33)
Co['Pr'] = fuzz.gbellmf(Co.universe, 0.14, 2.5, 0.66)
Co['MP'] = fuzz.sigmf(Co.universe, 50, 0.8)

# Resfriado
# TODO:...

# Alergia
# TODO:...

# Influenza
# TODO:...