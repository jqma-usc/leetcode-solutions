class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Memorize the given list
        minCost = [0] * len(cost)
        #Base cases
        minCost[0] = cost[0]
        minCost[1] = cost[1]
        #Iterate throughout to calculate
        for i in range(2, len(cost)):
            #We have to pay the cost of taking the ith step, and want to take the cheaper option of the previous steps and add them into the minCost
            minCost[i] = cost[i] + min(minCost[i-1], minCost[i-2])
        return min(minCost[-1], minCost[-2]) #Accesses the last and second to last elements in the list
        
