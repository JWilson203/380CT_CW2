import random
from random import randint, sample
from itertools import chain, combinations
import time

#Returns true if there is a subset of set[] with sun equal to given sum
def isSubsetSum(set, n, sum):
  # Base Cases
  #If sum is 0 we can use the empty set as our solution.
  if (sum == 0):
    print ("True")
    return True
  #if subset is empty then we cannot make a solution
  if (n == 0 and sum != 0):
    print ("False")
    return False
 
   #If last element is greater than sum, then ignore it
  if (set[n-1] > sum):
    return isSubsetSum(set, n-1, sum)
  else:
    return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])


set = random.sample(range(100), 10)
sum = random.randint(1,100)
n = len(set)
print set
print sum 

i=0
while i < 100:
  start_time = time.time()

  if (isSubsetSum(set, n, sum) == True):
     print("Found a subset with given sum")
  else:
     print("No subset within given sum")

  t3 = time.time() - start_time

  print("time taken", str(t3)+"s")
  if t3 > 0.0:
    with open("30.txt", "a") as myfile:
      myfile.write (str(t3)+"\n")
      i+=1
