
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        dfs recursion to copy/map the old node to the new node using hashmap

        time complexity: O(N)
        space complexity: O(N)
        """
        # create hashmap to map old nodes to new nodes
        oldToNew: dict["Node"|None, "Node"|None] = {}

        def dfs(node: "Node") -> "Node":
            # case 1: node is already copied: return that node from hashmap
            if node in oldToNew:
                return oldToNew[node]

            # case 2: node is not copied yet:
            # create a deep copy of that node
            copy: "Node" = Node(node.val)
            oldToNew[node] = copy
            # create deep copies of the node's neighbours
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
