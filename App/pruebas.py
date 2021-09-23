import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as iso
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
from datetime import datetime

Tecnicas=lt.newList()
a="["+str(2)+"]"
print(a)
print(type(a))