class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        child_node = TreeNode(value)
        self.children.append(child_node)

    def clear_children(self):
        self.children = []

n = TreeNode(10)
n.add_child(10)
n.add_child(5)
n.add_child(1)
print(n.value)
print(n.children)

n.children[0].add_child(1)
print(n.children[0].children)
