class Node:
    def __init__(self, data, Left=None, right=None):
        self.data = data
        self.Left = Left
        self.right = right
    def __repr(self):
        return f"<{data} {self.Left} {self.right}/>"
    def __str__(self):
        return str(self.data)

class binTree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if 
