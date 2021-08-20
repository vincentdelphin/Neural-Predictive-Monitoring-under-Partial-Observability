function [stateoutput] = invokeRC6(rawinitialstates,tFinal,varargin)
% x = class(rawinitialstates);
% disp(['TYPE = :' , mat2str(rawinitialstates)]);
numvarargs = length(varargin);
correct = [-900,25,0,0;-400,0,25,0;0,0,0,0;0,0,0,0];
initialstates = cast(rawinitialstates, 'like',correct);

% Hybrid Automata Model
HA = spacecraft_levelSet();


% Parameters
params.tFinal = tFinal;
params.startLoc = 1;


% algorithm options
options.timeStep{1} = 2e-1;
options.timeStep{2} = 5e-2;

options.zonotopeOrder = 40;
options.taylorTerms = 3;

options.intermediateOrder = 2;
options.errorOrder = 5;

options.tensorOrder = 2;
options.alg = 'lin';

% guard intersection method
options.guardIntersect = 'levelSet';

[rownum,colnum]=size(initialstates);

% Initialize unsafe set
sizeofSetfStates = size(initialstates(:,colnum));
unsafeSet = ones(sizeofSetfStates);
unsafe_region = interval(unsafeSet - (1e-15), unsafeSet + (1e-15));



% calculate reachable set for each set of states in input matrix
FinalSetofStates = zeros(1,rownum);
plottedunsaferegion = false;
for i=1:rownum
    slack = 1e-15;
    
    lowerBound = initialstates(i,1:colnum) - slack;
    upperBound = initialstates(i,1:colnum) + slack;
    lower = transpose(lowerBound);
    upper = transpose(upperBound);
    init_region = interval(lower,upper);
    
    options.R0 = zonotope(init_region);
    tic
    R = reach(HA,params,options);
    tComp = toc;
    if numvarargs > 0
        if plottedunsaferegion == false
            disp(['computation time for state no. ',num2str(i),' : ',num2str(tComp)]);
            figure; hold on
            plot(unsafe_region);
            title('Unsafe region');
            fprintf('\n')
            plottedunsaferegion = true;
        else
            
            disp(['computation time for state no. ',num2str(i),' : ',num2str(tComp)]);
            figure; hold on
            title('Reachable set for state ', num2str(i));
            plot(R,[1,2],'FaceColor',[.5 .5 .5],'Filled',true,'EdgeColor','none', 'Unify',true);
            fprintf('\n');
        end
    end
    
    %  Reachable set has been computed, need to check if intersects unsafe set
    
    val = query(R,'reachSet');
    reachableSet = val{1};
    res = isIntersecting(unsafe_region,reachableSet);
    
    if res == 1
        res = "The set of states DO intersect the unsafe set.";
        FinalSetofStates(i) = 1;
    elseif res == 0
        res = "The set of states DO NOT intersect the unsafe set.";
        FinalSetofStates(i) = 0;
    else
        msg = 'Error occurred.';
        error(msg)
    end
    
end
stateoutput = FinalSetofStates;
end
