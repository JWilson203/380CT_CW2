import itertools
import time
import random

def brute_force(mylist, target):
    #get all 2 digit subsets of the list
    results =[]
    total = 0
    for j in range(0,len(mylist)+1):
        results += itertools.combinations(mylist,j)

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
#generate random list and target, change these for different sizes
mylist = random.sample(range(30), 4)
target = random.randint(1,30)

#call brute force and time it
i=0
for i in range (0, 100):
  start_time = time.time()
  brute_force(mylist, target)
  t3 = time.time() - start_time
  print("time taken", str(t3)+"s")
  if t3 > 0.0:
    with open("4.txt", "a") as myfile:
      myfile.write (str(t3)+"\n")
  i+=1
