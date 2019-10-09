#
# @lc app=leetcode.cn id=558 lang=python3
#
# [558] 四叉树交集
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)
        elif quadTree1.isLeaf:
            return self.intersect(quadTree2, quadTree1)
        elif quadTree2.isLeaf:
            tl = Node(quadTree2.val, True, None, None, None, None)
            tr = Node(quadTree2.val, True, None, None, None, None)
            bl = Node(quadTree2.val, True, None, None, None, None)
            br = Node(quadTree2.val, True, None, None, None, None)
            qt2 = Node(None, False, tl, tr, bl, br)
            return self.intersect(quadTree1, qt2)
        tl = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        tr = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bl = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        br = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if tl.val == tr.val == bl.val == br.val and tl.val != None:
            return Node(tl.val, True, None, None, None, None)
        else:
            return Node(None, False, tl, tr, bl, br)
        
            
# @lc code=end

