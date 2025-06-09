## General Algorithms
Leetcode questions can generally be broken down into different kinds of patterns.
These patterns help you to quickly adapt a question into a pattern and approach to solve questions quickly.
Here is a list of non-exhaustive patterns to adopt:

### Prefix Sum [Arrays/Strings]
Use Case: Query sum of elements in subarray to reduce time complexity form N^2 to N

e.g Product of array except self

### Pointers  [Arrays/Strings]
2 pointers: left and right, to check for results to reduce time complexity from N^2 to N

e.g Valid palindrome

### Sliding Window [Arrays/Strings]
Find required subarrays to reduce time complexity from N^2 to N

e.g Min window substring

### Monotonic Stack [Array]
Use stack to find next greater/smaller value
- stack to track indices which greater elem have not been found
- populate list with n size
- 
e.g daily temperatures

### Overlapping intervals - merging, inserting
Useful for intervals which may overlap
- sort, iterate through and check if overlaps, if overlap combine, else append

e.g Merge intervals, insert intervals

### Binary Search
Use to find elem/indexes in log N time
- iterate through list - while l<=r
- use 3 pointers - left, mid, right
- readjust mid = l+1 or mid = r-1


### Top K elements
Find K largest/smallest/most frequent elements

### Sorting [Arrays/Strings]


### Hashmaps to cache results [Arrays/Strings]


### DFS/BFS [Arrays/Strings]
DFS: choose starting point -> keep track of visited nodes to avoid cycles, perform operation

### BackTracking [Arrays/Strings]


### Majority Elements [Arrays/Strings]


### Fast/Slow
Check for cycles


### Regex [Arrays/Strings]


## Binary Trees
### Traversals
- In-order: to retrieve values of BST in sorted prder
- Pre-order: to create a copy of BST 
- Post-order: to process child nodes before parent
- Level order: to explore all nodes at current level before next

### DFS
- choose starting point -> keep track of visited nodes to avoid cycles, perform operation on curr -> explore unvisited neighbours

### BFS
use case: finding shortest path between nodes, printing nodes of tree level by level

## Dynamic Programming
### Fibonacci 
Use bottom up approach to and track one and two steps while moving them to the next iteratively to prevent recalculation

e.g. climbing stairs, coin change, min cost climbing stairs


### 0/1 Knapsack


### Longest Common Subsequence


### Longest Increasing Subsequence


### Subset Sum


### Matrix Chain Multiplication
