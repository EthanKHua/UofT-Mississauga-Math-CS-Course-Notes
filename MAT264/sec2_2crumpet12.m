%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TJ Yusun                                          Winter 2025   %
% Purpose: Code for exploring Crumpet 12 in Section 2.2           %
% INPUT: function f; initial value x, max iter N, first and last  %
%        iterates to be printed to output (i and j)               %
% OUTPUT: Nth iterate m and table of values from x_i to x_j       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [m, values] = sec2_2crumpet12(f,x,N,i,j)
values = [];
  for k=1:N
    if i <= k && k <= j
        values = [values; x];
        %disp(k)
        %disp(m)
    end%if
    m = f(x);   % Evaluate function at current iterate
    x = m;      % Set next iterate to function value obtained
    end%for
end%function
