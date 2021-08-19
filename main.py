# Goal: to pass set of states to reach function used in Matlab and return results.
import matlab.engine
import matlab
import numpy as np
# choices = list(map(float, range(low,high)))
# [random.choices(choices , k=cols) for _ in range(rows)]

# [-900,25,0,0;
# -400,0,25,0;
# 0,0,0,0;
# 0,0,0,0]
# A = matlab.int32([-900, 25, 1, 0])

# random_set_of_states = list(random_set_of_states)
# print(random_set_of_states)
#
# matlab_random_set_of_states = matlab.double([random_set_of_states])
# print(matlab_random_set_of_states)
tFinal = 20.

# String = "reach_values = invokeRC({}, {})".format(states, tFinal)
#
eng = matlab.engine.start_matlab()

path_of_file = "'C:\\Users\\44772\\AppData\\Roaming\\MathWorks\\MATLAB " \
               "Add-Ons\\Collections\\CORA\\examples\\hybridDynamics\\hybridAutomaton' "
eng.cd(
    r'C:\\Users\\44772\\AppData\\Roaming\\MathWorks\\MATLAB '
    r'Add-Ons\\Collections\\CORA\\examples\\hybridDynamics\\hybridAutomaton',
    nargout=0)
eng.ls(nargout=0)


A = matlab.double([[-900., 25., 0., 0.],
                   [-400., 0., 0., 0.],
                   [0., 0., 0., 0.],
                   [0., 0., 0., 0.]])
# a = np.array([[-900., 25., 0., 0.],
#               [-400., 0., 0., 0.],
#               [0., 0., 0., 0.],
#               [0., 0., 0., 0.]])
#
# print(np.array_equiv(A, a))

random_array = np.random.randint(900, size=(4, 4))
print(random_array)
random_matlab_array = matlab.double(random_array.tolist(), is_complex=False)

print(random_matlab_array)


# Tfinal must be of type double to work
Tfinal = 20.0

# Can pass through extra argument for debug mode. InvokeRC6(A,tfinal, debug, nargout=2)

ave = eng.invokeRC6(random_matlab_array, tFinal, nargout=2)
print(ave)
# Only issue is using the reach function.
# eng.exit()
