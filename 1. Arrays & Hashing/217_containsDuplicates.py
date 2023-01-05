class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #Create a set with the list of nums
        return (len(set(nums)) != len(nums)) #Return true if the length of the set and length of nums are not equal
