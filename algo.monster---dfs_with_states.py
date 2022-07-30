from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    def dfs(root: Node, temp_list=[]):
        temp_list.append(str(root.val))
#         print(f'root {root.__dict__}')
#         print(temp_list)
        if not root.children:
#             print(temp_list)
            fl.append(temp_list)
#             print(fl)
            return 

        for child in root.children:
#             print(child.__dict__)
            dfs(child,temp_list.copy())
    fl = []
    dfs(root)
#     print(fl)
    t = []
    for i in fl:
        t.append("->".join(i))
#     print(t)
    return t

# this function build a tree from input
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)