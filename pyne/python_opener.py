#!/usr/bin/python
from pyne.mcnp import Mctal 
from fortranformat import FortranRecordReader


#ff2 = FortranRecordReader('(2A8,A19,I5,I11,I15)')
#from pyne.mcnp import Tally
data = Mctal()
#tally = Tally()
data.read("EXAMPLE.INPm",2)
data.read("EXAMPLE.INPm",4)
#tally.read("mctal")

