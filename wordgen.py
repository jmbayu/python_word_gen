""" use all the letters in "herecat" to generate as many 3 lettered english words as possible
"""
from itertools import permutations
import enchant

def main():
    '''
    Use enchant spell checking dictionary with british english
    '''
    use_dictionary = enchant.Dict("en_GB")
    tibi_olus_ipnut = "herecat"
    minimum_length = 3
    output_set = set()
    letters = [x.lower() for x in tibi_olus_ipnut]
    for counter in range(len(tibi_olus_ipnut)):
        for letter in list(permutations(letters, counter)):
            new_word = "".join(letter)
            if len(new_word) > minimum_length and use_dictionary.check(new_word):
                output_set.add(new_word)
    print(output_set)
    print(len(output_set))

main()
