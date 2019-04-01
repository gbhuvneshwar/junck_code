#https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
"""


The public names defined by a module are determined by checking the module’s 
namespace for a variable named __all__; if defined, it must be a sequence of 
strings which are names defined or imported by that module. The names given 
in __all__ are all considered public and are required to exist. If __all__ is not defined,
the set of public names includes all names found in the module’s namespace which do not 
begin with an underscore character ('_'). __all__ should contain the entire public API. 
It is intended to avoid accidentally exporting items that are not part of the API
(such as library modules which were imported and used within the module).



"""


from modul1_1 import *
from module_2 import *

#a1 = h1()
try:print _x1
except:pass
print y1




print "---------------"


#a2 = h2()
try:print _x2
except:pass
print y2