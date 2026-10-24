def maxDepth(node):
    if node is None:
        return 0
    left_depth=maxDepth(node.left)
    right_depth=maxDepth(node.right)
    return 1+max(left_depth,right_depth)
