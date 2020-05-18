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

# Covid-19
Co['PP'] = fuzz.sigmf(Co.universe, -50, 0.2)
Co['Po'] = fuzz.gbellmf(Co.universe, 0.14, 2.5, 0.33)
Co['Pr'] = fuzz.gbellmf(Co.universe, 0.14, 2.5, 0.66)
Co['MP'] = fuzz.sigmf(Co.universe, 50, 0.8)

# Resfriado
Re['PP'] = fuzz.sigmf(Re.universe, -50, 0.2)
Re['Po'] = fuzz.gbellmf(Re.universe, 0.14, 2.5, 0.33)
Re['Pr'] = fuzz.gbellmf(Re.universe, 0.14, 2.5, 0.66)
Re['MP'] = fuzz.sigmf(Re.universe, 50, 0.8)

# Alergia
Al['PP'] = fuzz.sigmf(Al.universe, -50, 0.2)
Al['Po'] = fuzz.gbellmf(Al.universe, 0.14, 2.5, 0.33)
Al['Pr'] = fuzz.gbellmf(Al.universe, 0.14, 2.5, 0.66)
Al['MP'] = fuzz.sigmf(Al.universe, 50, 0.8)

# Influenza
In['PP'] = fuzz.sigmf(In.universe, -50, 0.2)
In['Po'] = fuzz.gbellmf(In.universe, 0.14, 2.5, 0.33)
In['Pr'] = fuzz.gbellmf(In.universe, 0.14, 2.5, 0.66)
In['MP'] = fuzz.sigmf(In.universe, 50, 0.8)

# TODO: create lambda function to gbell & sigmoid memberships