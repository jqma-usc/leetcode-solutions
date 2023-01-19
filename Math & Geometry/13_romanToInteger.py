class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0 #This is the container to be returned
        romanValues = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000} #create a dictionary with the values of the character corresponding in romanValues
        for letters in range(len(s)):
            if(letters < len(s)-1 and romanValues[s[letters]] < romanValues[s[letters+1]]): #Ensure that letters is less than len(s))-1 and compare the values of to check if they are less than the one next to it
                sum -= romanValues[s[letters]]      
            else:
                sum += romanValues[s[letters]]
        return sum
