%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TJ Yusun                                          Winter 2025   %
% Purpose: Basic implementation of the fixed point iteration      %
%          method, where max iterations and tolerance are given.  %
% INPUT: function f; initial value x, max iter N, tolerance tol   %
% OUTPUT: approximation m (or failure)                            %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [m] = fixedpoint(f,x,N,tol)
  for j=1:N
    m = f(x);
    %disp(m);
    if abs(m - x) <= tol
      disp(["Fixed point within given tolerance found in " num2str(j) " iterations."])
      return;
    else
      x = m;
    end%if
  end%for
  disp("Method failed. Max iterations exceeded.")
end%function
