%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Written by Dr. Len Brin       14 January 2014  %
% Modified by TJ Yusun              Winter 2025  %
% Purpose: Implementation of the Secant Method   %
%          given two initial values x0, x1       %
% INPUT: function g; initial values x0, x1;      %
%        tolerance TOL, maximum iterations N0    %
% OUTPUT: approximation x and number of          %
%        iterations i or message of failure      %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [x,i] = secant(g,x0,x1,TOL,N0)
  i=2;
  y0=g(x0);
  y1=g(x1);
  disp(x0)
  disp(x1)
  while (i<=N0)
    x=x1-y1*(x1-x0)/(y1-y0);
    disp(x)
    if (abs(x-x1)<TOL)
      return
    end%if
    i=i+1;
    x0=x1;
    y0=y1;
    x1=x;
    y1=g(x1);
  end%while
  x="Method failed---maximum number of iterations reached";
end%function
