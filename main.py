# Goal: to pass set of states to reach function used in Matlab and return results.
import matlab.engine


tFinal = 200.0
# String = "reach_values = invokeRC({}, {})".format(states, tFinal)

eng = matlab.engine.start_matlab()

path_of_file = "'C:\\Users\\44772\\AppData\\Roaming\\MathWorks\\MATLAB " \
               "Add-Ons\\Collections\\CORA\\examples\\hybridDynamics\\hybridAutomaton' "
eng.cd(
    r'C:\\Users\\44772\\AppData\\Roaming\\MathWorks\\MATLAB Add-Ons\\Collections\\CORA\\examples\\hybridDynamics\\hybridAutomaton',
    nargout=0)
eng.ls(nargout=0)

matrix = [[-900., 25., 0., 0., 0.],
          [-400., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0.],
          [0., 0., 0., 0., 0.]]
print(matrix)
print(len(matrix))
print(len(matrix[0]))
print('TIME FOR MATLAB')
# ave = eng.invokeRC6(matrix, 20, nargout=1)
ave = eng.MatrixInput(matrix, 20, nargout=1)

# print(ave)
eng.exit()
