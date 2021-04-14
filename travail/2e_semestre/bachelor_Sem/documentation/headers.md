---
title: "Outil d'analyse de langages"
author: "Hategekimana Fabrice"
theme: "CambridgeUS"
date: 09 mars 2021
header-includes:
- |
  ```{=latex}
  \usepackage{bussproofs}
  \newcommand\myRule[3]
  {
   \begin{prooftree}
   \def\fCenter{\mbox{\ $=$\ }}
   \AxiomC{$#1$}
   \AxiomC{$$}
   \BinaryInf$ #2\fCenter #3$
   \end{prooftree}
  }
  ```
---
