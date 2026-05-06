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
        node1, node2 = None, None
        maxHeight, minHeight = 0, 0

        if heightP > heightQ:
            node1 = p
            node2 = q
            maxHeight = heightP
            minHeight = heightQ
        elif heightP <= heightQ:
            node1 = q
            node2 = p
            maxHeight = heightQ
            minHeight = heightP


        if maxHeight - minHeight != 0:
            # advnace node1 up, until it reaches minHeight
            while node1 and maxHeight != minHeight:
                node1 = node1.parent
                maxHeight -= 1

        while node1 != node2:
            node1 = node1.parent
            node2 = node2.parent

        return node1



