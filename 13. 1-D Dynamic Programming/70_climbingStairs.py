class Solution:
    def climbStairs(self, n: int) -> int:
        #Construct the array, start with base cases    
        staircaseSteps = [0] * (n+1) 
        staircaseSteps[0] = 1 
        staircaseSteps[1] = 1 

        for i in range(2,n+1): 
            starcaseSteps[i] = staircaseSteps[i-1] + staircaseSteps[i-2]

        return staircaseSteps[n]
        
