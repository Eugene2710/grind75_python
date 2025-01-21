"""
approach: 
use 2 pointers, 1 pointer at the start and 1 at the end. 
if sum is smaller, move left pointer to right, elif larger, move right pointer left. 
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 pointers - 1 pointer at the start and 1 at the end
        a: int = 0
        b: int = len(numbers)-1

        while a<b:
            total: int = numbers[a]+numbers[b]
            if total==target:
                return [a+1,b+1]
            if total<target:
                a+=1
            else:
                b-=1

