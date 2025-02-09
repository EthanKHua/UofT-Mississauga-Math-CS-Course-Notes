% Created by Ethan Hua

\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{eh-homework}[2025/01/29 Homework class]

\LoadClass{article}

\usepackage[margin=1.0in]{geometry}
\usepackage{amssymb,amsmath,amsthm,amsfonts}
\usepackage{enumitem}
\usepackage{xcolor}
\usepackage{mathtools}
\usepackage{systeme}

% My boxes
\usepackage[breakable]{tcolorbox}

% \RequirePackage{background}
% \backgroundsetup{
%     scale=1,
%     color=black,
%     opacity=1,
%     angle=0,
%     contents={
%         \includegraphics[width=\paperwidth,height=\paperheight]{\nightmodebackground}
%     }
% }

\definecolor{pastelblue}{RGB}{96, 145, 245}
\definecolor{pastelgreen}{RGB}{106, 235, 135}
\definecolor{darkgray}{RGB}{60, 60, 60}
\definecolor{lightgray}{RGB}{180, 180, 180}
\definecolor{offwhite}{RGB}{225, 225, 245}

\pagecolor{darkgray}
\color{offwhite}

\usepackage{../../../tex-setup/eh}

\newcommand{\makeboxes}{\newtcolorbox{question}[2][]{fonttitle=\large, fontupper=\large, fontlower=\large, title=Question {##2}., oversize, arc=3mm, outer arc=2mm, opacityback=0.9, coltitle=offwhite, colframe=pastelblue, colback=darkgray, colupper=lightgray, collower=lightgray, leftrule=1mm, rightrule=1mm, toprule=1.5mm, titlerule=1mm, bottomrule=1mm, valign=center, add to natural height=5mm, lower separated=false, before lower=\begin{proof}, after lower= \smallbreak \end{proof}, ##1, breakable=true}}

\AtBeginDocument{\makeboxes}