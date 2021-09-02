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
                   [-400., 0., 25., 0.],
                   [0., 0., 0., 0.],
                   [0., 0., 0., 0.]])

B = matlab.double([[-3., 45., 0., 0.],
                   [-40., 0., 25., 0.],
                   [0., 0., 0., 0.],
                   [0., 0., 0., 0.]])

practice_set = [A, B]


def generate(practice_set, tFinal):
    finalset = []
    i = 0
    print("size of practice set")
    print((len(practice_set)))
    while i < len(practice_set):
        print(practice_set[i])
        print("size of this set")
        print(np.size(practice_set[i]))
        reach_check = eng.invokeRCNEWEST(practice_set[i], tFinal, nargout=1)
        finalset.append(reach_check)
        i = i + 1
    input("Press any key to terminate the program")
    # Print bye message
    print("See you later.")
    return finalset
#

generate(practice_set, 200.)
# fucntion([[],[],[]], tfinal):
#     [], tfinal - pass to reach = get back 1 or 0
#     append output1 or 0 to output matrix
#     [], tfinal - pass to reach = get back 1 or 0
#     append output1 or 0 to output matrix
#     [], tfinal - pass to reach = get back 1 or 0
#     append output1 or 0 to output matrix
# output = [0,1,0]


# Initial set radius of [25m, 25m, 0, 0]
#  around point [-900m, -400m, 0m/s, 0m/s]
#
# random_array = np.random.randint(900, size=(4, 4))
#
# random_matlab_array = matlab.double(random_array.tolist(), is_complex=False)
#
#
# # Tfinal must be of type double to work
# Tfinal = 20.0

# Can pass through extra argument for debug mode. InvokeRC6(A,tfinal, debug, nargout=2)
# ave = eng.invokeRC(A, tFinal, "debug", nargout=1)
# # ave = eng.invokeRC(random_matlab_array, tFinal, nargout=1)
# print(ave)

eng.exit()
