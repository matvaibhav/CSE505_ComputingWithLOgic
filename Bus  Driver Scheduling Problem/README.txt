Answer Set Programming for the Bus Driver Scheduling Problem - Encoding:
================================================================


To test the provided encoding using the ASP solver Clingo [1], use 
the following example call which was tested for Clingo 4.4.0:

clingo .\bus.lp .\Instances\c1.lp --opt-strategy=usc,3 --configuration=tweety


The general structure of the program call is given by

clingo .\bus.lp <INSTANCE> <OPTIMIZATION> <CONFIGURATION> 


----------------------------------------------------------------

Clingo [1] can be downloaded under the following link:

http://sourceforge.net/projects/potassco/files/clingo/ 

----------------------------------------------------------------

The data instances were obtained from
http://www.csplib.org/Problems/prob022/data/data.zip

They converted to ASP format using the script convertData.py. 
Format to run it:
python convertData.py <address to the source data files>  <address to the destination ASP compatible format files>
For convenience all converted data instance files are placed n the Instances folder.
----------------------------------------------------------------

