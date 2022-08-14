#permutation means each and  every way a set of numbers or character can be arranged in a particular order
from itertools import permutations


def findpermutations(inputstr):
    listpermutation = permutations(inputstr) #([inputstr], 6) defining number of permutation

    for items in listpermutation:#list(listpermutation), goes with the above
        print(''.join(items))

if __name__=='__main__':
    inputstr = input('enter string')
    findpermutations(inputstr)
