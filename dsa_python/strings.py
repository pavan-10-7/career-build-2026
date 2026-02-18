"""
Topic: Strings
"""

# ----------------------------
# Problem 1: Valid Anagram
# ----------------------------

def isAnagram(self, s, t):
    if len(s) != len(t):
        return False
    
    arr = [0]*26  #Creates an array of 26 elements representing each alphabet

    for i in range(len(s)):  #This loop updates the values of the indices based on the iterated character
        arr[ord(s) - ord('a')] += 1 
        arr[ord(t) - ord('a')] -= 1
    
    for j in arr: #This checks if all elements are 0, else strings don't match!
        if j != 0:
            return False
    
    return True