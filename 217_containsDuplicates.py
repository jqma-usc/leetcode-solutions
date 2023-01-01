class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_set = set(nums) #Create a set with the list of number
        return (len(unique_set) != len(nums)) #Return true if the length of the unique set is not equal to the length of the list of numbers 
