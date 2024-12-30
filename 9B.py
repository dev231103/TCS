import skfuzzy as fuzz
from skfuzzy import control as ctrl
import networkx
import numpy as np
import matplotlib.pyplot as plt

quality = ctrl.Antecedent(np.arange(0,11,1),'quality')
service = ctrl.Antecedent(np.arange(0,11,1),'service')
tip = ctrl.Consequent(np.arange(0,26,1),'tip')

quality.automf(3)
service.automf(3)

tip['low'] = fuzz.trimf(tip.universe,[0,0,13])
tip['medium'] = fuzz.trimf(tip.universe,[0,13,25])
tip['high'] = fuzz.trimf(tip.universe,[13,25,25])

quality['average'].view()
plt.title("Quality")
plt.show()

service['poor'].view()
plt.title("Service")
plt.show()

tip['high'].view()
plt.title("Tip")
plt.show()

rule1=ctrl.Rule(quality['poor']|service['poor'],tip['low'])
rule2=ctrl.Rule(service['average'],tip['medium'])
rule3=ctrl.Rule(quality['good']|service['good'],tip['high'])

tipping_control = ctrl.ControlSystem([rule1,rule2,rule3])
tipping = ctrl.ControlSystemSimulation(tipping_control)

tipping.input['quality'] = 6.6
tipping.input['service']=9.8

tipping.compute()

print(tipping.output['tip'])

tip.view(sim=tipping)
plt.title('Result')
plt.show()