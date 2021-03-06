"""
Antecendents: inputs definition, membership functions and  universe.

"""

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# -------------------------------------
# Symptoms Universe
# -------------------------------------
helper_array = np.arange(0, 1, 0.001)

Fiebre = np.arange(36, 41, 0.001)
DolorCabeza = helper_array
Mialgia = helper_array
Fatiga = helper_array
CongestionNasal = helper_array
Estornudos = helper_array
DolorGarganta = helper_array
Diarrea = helper_array
Rinorrea = helper_array

# -------------------------------------
# Inputs (antecedents)
# -------------------------------------
Fi = ctrl.Antecedent(Fiebre, 'Fiebre')
DC = ctrl.Antecedent(DolorCabeza, 'DolorCabeza')
Mi = ctrl.Antecedent(Mialgia, 'Mialgia')
Fa = ctrl.Antecedent(Fatiga, 'Fatiga')
CN = ctrl.Antecedent(CongestionNasal, 'CongestionNasal')
Es = ctrl.Antecedent(Estornudos, 'Estornudos')
DG = ctrl.Antecedent(DolorGarganta, 'DolorGarganta')
DR = ctrl.Antecedent(Diarrea, 'Diarrea')
Ri = ctrl.Antecedent(Rinorrea, 'Rinorrea')

# linguistic values
binary = ['No', '~No', 'X']
Fi.automf(3, names=['No', 'Leve', 'Alta'])
DC.automf(3, names=binary)
Mi.automf(3, names=binary)
Fa.automf(3, names=binary)
CN.automf(3, names=binary)
Es.automf(3, names=binary)
DG.automf(5, names=['No', 'Leve', 'Severo', '~No', 'X'])
DR.automf(3, names=binary)
Ri.automf(3, names=binary)

# -------------------------------------
# Generate fuzzy membership functions
# -------------------------------------

# Fiebre
Fi['No'] = fuzz.sigmf(Fi.universe, -30, 0.3)
Fi['Leve'] = fuzz.gbellmf(Fi.universe, 0.587, 3.28, 38.3)
Fi['Alta'] = fuzz.sigmf(Fi.universe, 11.76, 39.1)

# Dolor de cabeza
no_sigmoid = fuzz.sigmf(DC.universe, -30, 0.3)
DC['No'] = no_sigmoid
DC['~No'] = 1 - no_sigmoid

# Mialgia
no_sigmoid = fuzz.sigmf(Mi.universe, -30, 0.3)
Mi['No'] = no_sigmoid
Mi['~No'] = 1 - no_sigmoid

# Fatiga
no_sigmoid = fuzz.sigmf(Fa.universe, -64.3, 0.2)
Fa['No'] = no_sigmoid
Fa['~No'] = 1 - no_sigmoid

# Congestion Nasal
no_sigmoid = fuzz.sigmf(CN.universe, -30, 0.3)
CN['No'] = no_sigmoid
CN['~No'] = 1 - no_sigmoid

# Estornudos
no_sigmoid = fuzz.sigmf(Es.universe, -30, 0.3)
Es['No'] = no_sigmoid
Es['~No'] = 1 - no_sigmoid

# Dolor de garganta
no_sigmoid = fuzz.sigmf(Fi.universe, -30, 0.3)
Fi['No'] = no_sigmoid
Fi['Leve'] = fuzz.gbellmf(Fi.universe, 0.24, 3.3, 0.46)
Fi['Severo'] = fuzz.sigmf(Fi.universe, 31.5, 0.67)
Fi['~No'] = 1 - no_sigmoid

# Diarrea
no_sigmoid = fuzz.sigmf(DR.universe, -30, 0.3)
DR['No'] = no_sigmoid
DR['~No'] = 1 - no_sigmoid

# Estornudos
no_sigmoid = fuzz.sigmf(Ri.universe, -30, 0.3)
Ri['No'] = no_sigmoid
Ri['~No'] = 1 - no_sigmoid