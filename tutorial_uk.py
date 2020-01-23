
import ciw
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

#There are two nodes. Customer 0 arrives at node 0 following a exponential with factor 5
# and at node 2 following a exponential factor 2.
# He gets served following exponentials factors 1 and 9
# Has a probability of changing from 1 to 1 of 0, from 1 to 2 of 0.5 and from 2 to 1 of 0.5
# There are 5 servers on node 1 and 2 on node 2
params = {
	'arrival_distributions' : {'Class 0' : [['Exponential', 5.0], ['Exponential', 2.0]],
							'Class 1' : [['Exponential', 7.0], ['Exponential', 3.0]]},
	'service_distributions' : {'Class 0' : [['Exponential', 1.0], ['Exponential', 9.0]],
							'Class 1' : [['Exponential', 2.0], ['Exponential', 3.0]]},
	'transition_matrices' : {'Class 0' : [[0,0.5],
											[0.5, 0 ]],
							'Class 1' : [[0.2,0.2],
											[0.2, 0.2 ]]},
	'number_of_servers' : [5,2]
}
# Transition_matrices=params['transition_matrices'], is not anymore under create network

ciw.seed(1)
N = ciw.create_network( arrival_distributions= params['arrival_distributions'],
						service_distributions=params['service_distributions'],
						
						number_of_servers=params['number_of_servers'])
Q = ciw.simulation( N )
Q.simulate_until_max_time(100)