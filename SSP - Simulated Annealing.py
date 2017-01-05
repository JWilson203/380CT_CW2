from random import randint, sample
from itertools import chain, combinations
import time

class SSP():
    def __init__(self, S=[], t=0):
        self.S = S
        self.t = t
        self.n = len(S)
        #
        self.decision = False
        self.total    = 0
        self.selected = []

    def __repr__(self):
        return "SSP instance: S="+str(self.S)+"\tt="+str(self.t)
    
    def random_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted([randint(0,max_n_bit_number) for i in range(n)], reverse=True)
        self.t = randint(0,n*max_n_bit_number)
        self.n = len(self.S)

    def random_yes_instance(self, n, bitlength=10):
        max_n_bit_number = 2**bitlength-1
        self.S = sorted([randint(0,max_n_bit_number) for i in range(n)], reverse=True)
        self.t = sum(sample(self.S, randint(0,n)))
        self.n = len(self.S)

    ###

    def try_at_random(self):
        #empty array for storing subset
        candidate = []
        #set initial temperature
        temp = 100000
        #set total variable
        total = 0
        #set cooling rate
        cooling = 0.003

        while temp > 1:
            #sample of random amount of numbers from parent set
            candidate = sample(self.S, randint(0,self.n))
            #total is the sum of the candidate numbers
            total     = sum(candidate)
            print("Trying: ", candidate, ' sum:', total)

            #if sum of subset integers = target integer, break operation as we have found a solution
            if total == self.t:
                print ("Found a subset. Target integer was: ", self.t)
                break

            #temperature = temp * 1 - cooling rate
            temp *= 1 - cooling


instance = SSP()
start_time = time.time()
instance.random_yes_instance(4)
print(instance)
instance.try_at_random()
time_after = time.time() - start_time
print ("Time taken: " +str(time_after)+"s")
