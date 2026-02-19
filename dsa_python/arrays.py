"""
Topic: Array
"""

# ----------------------------
# Problem 1: Two Sum
# ----------------------------

def two_sum(self, nums, target):

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j] #Return the list, if condition is met and code is exited
            
    return [] #Empty list is returned if condition is not met

# ----------------------------
# Problem 2: Contains Duplicate
# ----------------------------

def contains_duplicate(self, nums):

    Set = set() #Makes sure values aren't repeated
    for i in nums:
        if i in Set:
            return True #Confirms duplicate value
        else:
            Set.add(i) #Updates the Set

    return False

# ----------------------------
# Problem 3: Squares of Sorted Array
# ----------------------------

def sortedSquares(self, nums):
    a=[i*i for i in nums]
    a.sort()
    return a

