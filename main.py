# Goal: to pass set of states to reach function used in Matlab and return results.
import matlab.engine
import matlab
import numpy as np

tFinal = 20.

eng = matlab.engine.start_matlab()

path_of_file = "'C:\\Users\\44772\\AppData\\Roaming\\MathWorks\\MATLAB " \
               "Add-Ons\\Collections\\CORA\\examples\\hybridDynamics\\hybridAutomaton' "
eng.cd(
    r'C:\\Users\\44772\\AppData\\Roaming\\MathWorks\\MATLAB '
    r'Add-Ons\\Collections\\CORA\\examples\\hybridDynamics\\hybridAutomaton',
    nargout=0)

A = matlab.double([[-900., 25., 0., 0.],
                   [-400., 0., 0., 0.],
                   [0., 0., 0., 0.],
                   [0., 0., 0., 0.]])

random_array = np.random.randint(900, size=(4, 4))

random_matlab_array = matlab.double(random_array.tolist(), is_complex=False)


# Tfinal must be of type double to work
Tfinal = 20.0

# Can pass through extra argument for debug mode. InvokeRC6(A,tfinal, debug, nargout=2)
# ave = eng.invokeRC6(random_matlab_array, tFinal, "debug", nargout=1)
ave = eng.invokeRC6(random_matlab_array, tFinal, nargout=1)
print(ave)

eng.exit()
