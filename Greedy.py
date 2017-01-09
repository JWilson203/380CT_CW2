import random
import time

def greedy(S,t):
  print("Set S is ")
  print(S)
  print("and sum needed is "+str(t))
  subset=[]
  tsum=0
  n=len(S)
  S.sort(reverse = True)
  for i in range(0,n):
    if(tsum+S[i]<=t):
      tsum=tsum+S[i]
      subset.append(S[i])
  if(sum(subset)==t):
    print("Yes,the set that has a sum of "+str(t)+" is")
    print(subset)
  else:
    print("There are no subsets with sum "+str(t)+" The closest is")
    print(subset)
  print()
  
start_time = time.time()
greedy([2,1,4,3,6,5],10)  #this combination works
t1 = time.time() - start_time
start_time = time.time()
greedy([4,3,1,5,8],7)     #this combination doesnt work
t2 = time.time() - start_time
start_time = time.time()
greedy(random.sample(range(20), 8),30)
t3 = time.time() - start_time
print("Time taken for the runs : "+str(t1)+"s, "+str(t2)+"s, "+str(t3)+"s")

#time complexity of the function can be calculated
#by breaking down the code. 
#Each declaration line has complexity of N.
#Sorting the array has a complexity of NlogN
#The for loop also has a complexity of N
#So the worse case is NlogN.
#Hence the complexity of algorithm is NlogN
