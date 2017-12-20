Answer Set Programming for the Shift Design Problem - Encoding:
================================================================

This directory contains an ASP encoding for the Shift Design Problem. 

To test the provided encoding using the ASP solver Clingo [1], use 
the following example call which was tested for Clingo 4.4.0:

clingo ShiftDesign.lp
       modes/balanced.lp 
       limits/limits_10_10.lp
       ../DataSet1/instances/RandomExample1/60m.lp


The general structure of the program call is given by

clingo ShiftDesign.lp <MODE> <LIMITS> <INSTANCE> 

In the given pattern, <MODE> is one of the following:

.) modes/balanced.lp: The minimization of the number of shifts used, shortage 
      and excess are of equal importance. Corresponds to the original 
      problem formulation of the Shift Design Problem.
             
.) modes/min_deviation.lp: The minimization of shortage and excess are of 
      equal importance, but more important than keeping the number of 
      shifts small.

.) modes/min_shortage.lp: The minimization shortage is most important.
      After minimizing the shortage, excess is minimized and after
      that is done, the number of shifts is minimized.

In the above pattern, <LIMITS> is an optional program specifying
the limits of allowed number of shifts, shortage or excess.
For examples on how to use the concept of limits, see directory 
'limits'.

We note that the use of limits might draw some instances unsatisfiable 
while by omitting limits, there is always a solution for the Shift 
Design Problem.

----------------------------------------------------------------

Clingo [1] can be downloaded under the following link:

http://sourceforge.net/projects/potassco/files/clingo/ 

----------------------------------------------------------------

Custom instances must follow the pattern of the instances delivered 
with this archive (see for instance the directory ../DataSet1 which
contains some sample instances solvable without any deviation).

----------------------------------------------------------------

[1]: M. Gebser and R. Kaminski and B. Kaufmann and T. Schaub, 
Clingo = ASP + Control: Preliminary Report, Technical 
Communications of the Thirtieth International Conference 
on Logic Programming (ICLP'14)
(Available at http://arxiv.org/abs/1405.3694v1)