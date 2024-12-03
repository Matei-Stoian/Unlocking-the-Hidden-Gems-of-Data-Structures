import math
import mmh3
from bitarray import bitarray
import random

class BloomFilter:

    def __init__(self,items_size,fp_prob):
        """
        items_size : int
            Number of items expected to be stored in bloom filter.
        
        fp_prob: float
            The false positive probability.
        """

        self.fp_prob = fp_prob
        
        self.size = self.get_size(items_size,fp_prob)

        self.hash_count = self.get_hash_count(self.size,items_size)

        self.bit_array = bitarray(self.size)

        self.bit_array.setall(0)


    @classmethod
    def get_size(self,n,p):
        """
        Return m, the size of the bit array computed with the formula.
        m = -(n*ln(p))/(ln(2)^2)
        n: int
            number of items expected to be stored in filter
        p: float 
            False positivie probability.
        """
        m = -(n*math.log(p))/(math.log(2)**2)
        return int(m)


    @classmethod
    def get_hash_count(self,m,n):
        """
        Return the number of hash function needed using the formula:
            k = m/n*ln(2)
        """

        k = (m/n)*math.log(2)
        return int(k)
    
    def add(self,item):
        """
        Add a item to the filter.
        """
        for i in range(self.hash_count):
            hash_poz = mmh3.hash(item,i)%self.size
            self.bit_array[hash_poz] = 1

    def __contains__(self,item):
        """
            Check if the item might be in the filter.
        """
        for i in range(self.hash_count):
            hash_poz = mmh3.hash(item,i) % self.size
            if self.bit_array[hash_poz] == 0:
                return False
        return True
        


if __name__ == '__main__':
    n = 20
    p = 0.05

    bloomf = BloomFilter(n,p)
    print("Size of bit array:{}".format(bloomf.size))
    print("False positive Probability:{}".format(bloomf.fp_prob))
    print("Number of hash functions:{}".format(bloomf.hash_count))

    word_present = ['abound','abounds','abundance','abundant','accessible',
                    'bloom','blossom','bolster','bonny','bonus','bonuses',
                    'coherent','cohesive','colorful','comely','comfort',
                    'gems','generosity','generous','generously','genial']
    word_absent = ['bluff','cheater','hate','war','humanity',
                'racism','hurt','nuke','gloomy','facebook',
                'geeksforgeeks','twitter']

    for item in word_present:
        bloomf.add(item)

    random.shuffle(word_present)
    random.shuffle(word_absent)

    test_words = word_present[:10] + word_absent
    random.shuffle(test_words)
    for word in test_words:
        if word in bloomf:
            if word in word_absent:
                print("'{}' is a false positive!".format(word))
            else:
                print("'{}' is probably present!".format(word))
        else:
            print("'{}' is definitely not present!".format(word))
    