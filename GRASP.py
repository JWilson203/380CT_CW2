import random
import time
from random import randint

def greedy_random(target, set):    
    greedyset = set
    total = 0
    temp = []

    while (len(greedyset) != 0):
        n = randint(0, (len(set) - 1))

        total += greedyset[n]
        temp.append(greedyset[n])
        if total > target:
            total -= greedyset[n]
            temp.pop()
        greedyset.pop(n)
    return (total)

def grasp(target,set):
    print "SSP instance: S="+str(set)+"\tt="+str(target)

    best = target
    x = 0

    while x < 100:
        greedy = greedy_random(target, set)
        if target - greedy < best:
            best = greedy
        x += 1
    print best

i=0
while i < 100:
    start_time = time.time()

    grasp(random.randint(1,40), random.sample(range(40), 4))

    t3 = time.time() - start_time
    print("Time taken", str(t3)+"s")
    if t3 > 0.0:
        with open("4.txt", "a") as myfile:
            myfile.write (str(t3)+"\n")
        i+=1