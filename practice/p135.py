
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f'<Node: value={self.value}, left={self.left}, right={self.right}>'

    def is_leaf(self):
        return self.left is None and self.right is None

def min_path_sum(node):
    q = []
    q.append([node, node.value])
    result = []
    while q:
        current = q.pop(0)
        print(current)
        if current[0].is_leaf():
            result.append(current[1])
            continue
        if current[0].left:
            q.append([current[0].left, current[1]+current[0].left.value])
        if current[0].right:
            q.append([current[0].right, current[1]+current[0].right.value])
    return min(result)

node = Node(10, Node(5, None, Node(2)), Node(5, None, Node(1, Node(-1), None)))
print(min_path_sum(node))