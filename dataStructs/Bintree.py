 
"""

Tree => data, left: Tree, right: Tree
challenge: make a BST, with no toturials and no help.
"""
class TreeNode:
    """ Node """
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return f"{self.data}"

class BST:
    """ Binary search tree """
    def __init__(self) -> None:
        self.root = None
        self.size = 0
    
    def add(self, data) -> None:
        if not self.root:
            self.root = TreeNode(data, self.root)
        else:
            self._add(data)
        self.size += 1
    def _add(self, data, current):
        if data < current.data:
            if not current.left:
                current.left = TreeNode(data)
            else:
                self._add(data, current.left)
        elif data > current.data:
            if  not current.right:
                current.right = TreeNode(data)
            else:
                self._add(data, current.right)
        else:
            print("Already exist")