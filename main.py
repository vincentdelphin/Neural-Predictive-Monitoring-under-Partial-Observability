# Beginning Script
# Goal: to pass set of states to reach function used in Matlab and return results.
import matlab.engine

eng = matlab.engine.start_matlab('-desktop')

# Navigate to directory with matlab code we want to use.
# Need to add path of CORA file
# Room heating example.

path_of_file = "'/home/commander/MATLAB Add-Ons/Collections/CORA/examples/hybridDynamics/hybridAutomaton'"
print("cd " + path_of_file)
eng.evalc("cd " + path_of_file)

# Need to add variables to reach function used in Matlab.
# R = reach(sys, params, options)
# with input arguments

# • sys dynamic system defined by any of the classes in Sec. 4.2 or 4.3, e.g., linearSys,hybridAutomaton, etc.

# • params struct containing the parameter that define the reachability problem
#   – .tStart initial time t 0 (default value 0)
#   – .tFinal final time t f
#   – .R0 initial set X 0 specified by one of the set representations in Sec. 2.2.1
#   – .U input set U specified as an object of class zonotope (see Sec. 2.2.1.1)
#   – .u time dependent center u c (t) of the time varying input set
#
#      U (t) := u c (t) ⊕ U specified as a matrix for which the number of colums is identical to the number of

#      reachability steps (optional)
#   – .paramInt set of parameter values P specified as an object of class interval (see
#      Sec. 2.2.1.2) (class nonlinParamSys only)
#   – .y0 guess guess for a consistent initial algebraic state (class nonlinDASys only, see Sec. 4.2.8.1).
#   – .startLoc index of the initial location (class hybridAutomaton and parallelHybridAutomaton only)
#   – .finalLoc index of the final location. Reachability analysis stops as
#   soon as the final location is reached (class hybridAutomaton and parallelHybridAutomaton only, optional)

# • options struct containing algorithm settings for reachability analysis. Since the settings are different for each
# type of dynamic system, they are documented in Sec. 4.2 and Sec. 4.3. • spec object of class specification (see
# Sec. 6.3) which represents the specifications the system has to verify. Reachability analysis stops as soon as a
# specification is violated. and output arguments • R • res object of class reachSet (see Sec. 6.1) that stores the
# reachable set R(t i ) at time point as well as the reachable set R(τ i ) for time intervals τ i = [t i ,
# t i+1 ]. Boolean flag that indicates whether the specifications are satisfied (res = 1) or not (res = 0).

Reach = eng.reach()






eng.exit()


