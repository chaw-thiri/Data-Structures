# time = O(d) : d = distance between node 1 and node 3
# space = O(1)
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    searchOne=nodeOne
    searchTwo=nodeThree

    while True:
        foundThreeFromOne=searchOne is nodeThree
        foundOneFromThree=searchTwo is nodeOne
        foundNodeTwo=searchOne is nodeTwo or searchTwo is nodeTwo
        finishedSearching=searchOne is None and searchTwo is None
        if foundThreeFromOne or foundOneFromThree or foundNodeTwo or finishedSearching:
            break

        if searchOne is not None:
            searchOne=searchOne.left if searchOne.value>nodeTwo.value else searchOne.right

        if searchTwo is not None:
            searchTwo=searchTwo.left if searchTwo.value>nodeTwo.value else searchTwo.right

    foundNodeFromOther=searchOne is nodeThree or searchTwo is nodeOne
    foundNodeTwo=searchOne is nodeTwo or searchTwo is nodeTwo
    if not foundNodeTwo or foundNodeFromOther:
        return False

    return searchForTarget(nodeTwo,nodeThree if searchOne is nodeTwo else nodeOne)

def searchForTarget(node,target):
    while node is not None and node is not target:
        node=node.left if target.value <node.value else node.right

    return node is target
