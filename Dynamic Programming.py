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

#Driver program to test above function
set = [3,100,200,10,4,30,6]
sum = 9
n = len(set)

if (isSubsetSum(set, n, sum) == True):
   print("Found a subset with given sum")
else:
   print("No subset within given sum")