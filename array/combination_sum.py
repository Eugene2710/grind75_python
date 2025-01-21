class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        Approach: 
        using a decision tree, use a dfs stack recursion to check if sum(a list which is a stack) of candidates added up is =/</>
        if sum==target, append list of candidates to result
            pop from sum stack
            move to next 
        if sum>target, exit that current loop
            pop from sum stack
        if sum<target, append curr candidate to sum stack 

        e.g. 
        candidates = [2,3,6,7], target = 7
        dfs(i=0,curr=[],total=0)
        curr = [2]
        dfs(0,[2],2)
            curr=[2,2]
            dfs(0,[2,2],4)
                curr=[2,2,2]
                dfs(0,[2,2,2],6)
                    curr=[2,2,2,2]
                    dfs(0,[2,2,2,2],8)
                        total>target -> return
                    curr = [2,2,2]
                    dfs(1,[2,2,2],6)
                    curr=[2,2,2,3]


        Needcode's notes: visualize the decision tree, base case is curSum = or > target, each candidate can have children of itself or elements to right of it inorder to elim duplicate solutions;
        """
        # global varaible to store the combinations
        res: list[list[int]]

        def dfs(i: int, curr: list[int], total: int) -> None:
            # case: when sum==target
            if total==target:
                res.append(curr)
                return
            # case: when sum>target
            if total>target:
                return
            # case: when sum<target, add new candidate into sum stack
            curr.append(candidates[i])
            # update the total, DO NOT update i because you want to add the same candidate in first to check that possibility first
            dfs(i, curr, total+candidates[i])
            # after doing so, pop that candidate
            curr.pop()
            # add the next candidate from that prev stack of candidates - update only i and DO NOT update total because total was defaulted to the previous total from prev stack
            dfs(i+1, curr, total)
        
        dfs(i=0, curr=[], total=0)


