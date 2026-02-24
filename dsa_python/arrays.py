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


# ----------------------------
# Problem 4: Remove Duplicates from Sorted Array
# ----------------------------

def remDuplicates(self, nums):
    j=0
    for i in range(1,len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j+1


# ----------------------------
# Problem 5: MOve Zeroes
# ----------------------------

def movezeroes(self, nums):
    nonzero, i = 0,0
    while i < len(nums):
        if nums[i] != 0:
            nums[i], nums[nonzero] = nums[nonzero], nums[i]
            nonzero += 1
        i += 1