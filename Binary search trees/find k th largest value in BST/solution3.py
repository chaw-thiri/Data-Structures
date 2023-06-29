# solution by algoexpert 
# time O(h+k)
# space O(h) : where h is the heigtht of the tree
# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodesValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodesValue = latestVisitedNodesValue


def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0,-1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.latestVisitedNodesValue

def reverseInOrderTraverse(node, k, treeInfo):
    if node == None or treeInfo.numberOfNodesVisited>=k:
        return

    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited <k:
        treeInfo.numberOfNodesVisited +=1
        treeInfo.latestVisitedNodesValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)
        