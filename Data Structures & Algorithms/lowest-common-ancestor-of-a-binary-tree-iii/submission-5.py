"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def height(node):
            # not DFS
            h = 0
            while node:
                node = node.parent
                h += 1
            return h

        heightP, heightQ = height(p), height(q)

        # always height(node1) > height(node2)
        if heightP > heightQ:
            node1, node2 = p, q
            maxHeight = heightP
            minHeight = heightQ
        elif heightP <= heightQ:
            node1, node2 = q, p
            maxHeight = heightQ
            minHeight = heightP


        if maxHeight - minHeight != 0:
            # advnace node1 up, until it reaches minHeight
            while maxHeight != minHeight:
                node1 = node1.parent
                maxHeight -= 1

        # equal levels; climb up into the same parent
        while node1 != node2:
            node1 = node1.parent
            node2 = node2.parent

        return node1



