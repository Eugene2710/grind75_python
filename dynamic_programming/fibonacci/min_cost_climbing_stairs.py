class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        fibonacci: bottom up
        iterate from bottom up while keeping track of 2 possibilities - one step and two steps
        get min cost for each possibility

        time complexity: O(2N-1)
        space complexity: O(1)
        10 | 15 | 20
        start: 0 -> 10+15=25 | 10+20=30
        start: 1 -> 15+20=25 | 15
        """
        # add last step with elem 0 which means it costs 0 to get to this last step
        cost.append(0)

        # start from 3rd last elem(after appending elem 0), iterate backwards
        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        # we can start with either step index 0 or 1
        return min(cost[0], cost[1])