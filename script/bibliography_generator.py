#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

__author__ = ['Nico Curti']
__email__ = ['nico.curti2@unibo.it']


SECTIONS_RE = re.compile(r'\\section\*\s*\{\\scshape\{.*\}\}')
SECTIONS_NAME_RE = re.compile(r'\\section\*\s*\{\\scshape{(.*)\}\}')

filename = '../curriculum.tex'

with open(filename, 'r') as fp:
  data = fp.read()

_, *sections = SECTIONS_RE.split(data)
sections_name = SECTIONS_NAME_RE.findall(data)
assert 'Publications' in sections_name
idx = sections_name.index('Publications')
bibliography = sections[idx]

HEADER = r'''
% sudo apt install texlive-lang-italian
% sudo apt install texlive-fonts-extra
% sudo apt-get install texlive-bibtex-extra biber
\documentclass[a4paper,11pt]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage{graphicx}

%\usepackage[backend=biber]{biblatex}
\usepackage{cv} % backbone style
\usepackage{booktabs}
%\usepackage{fontawesome} % beautiful icons!!
\usepackage{fontawesome5} % very beautiful icons!!
\usepackage{pifont} % more styles for bullet
\usepackage[dvipsnames]{xcolor}
\usepackage[colorlinks=true, allcolors=Blue]{hyperref}

\usepackage{siunitx}
\usepackage{tikz}
\newcommand*{\priority}[1]{\begin{tikzpicture}[scale=0.15]%
    \draw[color=Blue] (0,0) circle (1);
    \fill[fill opacity=0.5,fill=Blue] (0,0) -- (90:1) arc (90:90+#1*3.6:1) -- cycle;
    \end{tikzpicture}}


% Change color to blue
\def\headcolor{\color[rgb]{0,0,0.5}}
% Space before section headings
\titlespacing{\section}{0pt}{2ex}{1ex}

\graphicspath{{./img/}}

\ifdefined\signed
  \newcommand{\SignatureImage}[2][]{%
    \IfFileExists{#2}{%
      \includegraphics[#1]{#2}%
    }{%
      \hfill\makebox[2.0in]{\hrulefill}
    }%
  }%
\else
  \newcommand{\SignatureImage}[2][]{\hfill\makebox[2.0in]{\hrulefill}}
\fi

\name{Nico Curti}
\image{io.png}
\info{
 \faUniversity      & Dept. of Experimental, Diagnostic and Specialty Medicine of Bologna University\\
 \faMapMarker*      & Bologna (Italy)\\
 \faPhone           & +39 333 997 93 99\\
 \faPaperPlane      & nico.curti2@unibo.it\\
 \faGithub          & \url{https://github.com/Nico-Curti}\\
 \faOrcid           & \url{https://orcid.org/0000-0001-5802-1195}\\
}

\pagestyle{fancy}
\lhead{Curriculum vitae}
\rhead{Nico Curti}
\rfoot{\thepage}
\cfoot{}

\newcounter{itemnumber}

\newenvironment{paperlist}{%
  \setcounter{itemnumber}{0}%
  \begin{list}{}{}%
}{\end{list}}

\renewcommand{\headrulewidth}{0.4pt}
\newcommand{\quotes}[1]{``#1''}
\newcommand{\itemicon}[2]{\item[{\includegraphics[scale=#1]{#2}}]}
\newcommand{\enumicon}[2]{% Image, Number
\stepcounter{itemnumber}%
\item[{\includegraphics[scale=#1]{#2}}] \theitemnumber.
}
\newcommand{\icon}[2]{\includegraphics[scale=#1]{#2}}

\newcommand{\legend}[1]{%
  \begingroup
  \renewcommand\thefootnote{}\footnote{#1}%
  \addtocounter{footnote}{-1}%
  \endgroup
}

\newcommand{\journal}[1]{\underline{#1}}
\newcommand{\paperTitle}[1]{\emph{#1}}

\begin{document}

\maketitle

\section*{\scshape{Publications}}
'''

TAIL = r'''
\begin{flushright}
Bologna, \today

\vspace*{0.5cm}

\begin{figure}[hb!]
  \begin{flushright}
    \SignatureImage[scale=0.5]{img/Firma.png}
  \end{flushright}
\end{figure}

\end{flushright}

\vspace*{\fill}
\textbf{Autorizzo al trattamento dei dati personali contenuti in questo documento ai sensi dell'articolo 13 del D. Lgs. 196/2003.}

\end{document}
'''

with open('../publications.tex', 'w') as fp:
    
  fp.write(HEADER)
  fp.write(bibliography)
  fp.write(TAIL)
