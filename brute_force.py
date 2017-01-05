import itertools
import time
import random
     
def brute_force(mylist, target):
    #get all 2 digit subsets of the list
    results =(list(itertools.combinations(mylist, 2)))
    total = 0
    for set in results:
        #set total to the sum of the current set
        total = sum(set)
        print ("trying the set", set, ",Total sum of set", total )
        #compare the current sum of set to target
        if (total == target):
            print("  A match for" ,str(total),", the Solution: " +str(set))
            return
        else:
            print (" not a match")
    print("no match was found!!!!")
    return
#generate random list and target
mylist = random.sample(range(10), 8)
target = random.randint(1,10)

#call brute force and time it
start_time = time.time()
brute_force(mylist,target)
time = time.time()
print("time taken", str(time))

