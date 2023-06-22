class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def make_tree(tree, node, i, n):
    if n > i:
        if tree[i] is None:
            return None
        temp = TreeNode(tree[i])
        node = temp
        node.left = make_tree(tree, node.left, 2 * i + 1, n)
        node.right = make_tree(tree, node.right, 2 * i + 2, n)
    return node

tree_input = input("木の要素を入力：")
tree_list = list(map(int, tree_input.split()))
root = make_tree(tree_list, None, 0, len(tree_list))

print(root.val, root.left.val, root.left.left.val)
