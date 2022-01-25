# use all the letters in "herecat" to generate as many 3 lettered english words as possible
from itertools import permutations
import enchant
# use the spell checking dictionary with british english 
dictionary = enchant.Dict("en_GB")
olu_input = "herecat"
minlen = 3

output_set=set()
letters=[x.lower() for x in olu_input]
for n in range(len(olu_input)):
  for y in list(permutations(letters, n)):
    z="".join(y)
    if len(z)>minlen and dictionary.check(z):
      output_set.add(z)
print( output_set )
print(len(output_set))
