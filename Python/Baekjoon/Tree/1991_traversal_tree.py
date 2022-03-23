'''
https://www.acmicpc.net/problem/1991
'''
import sys

input_ = sys.stdin.readline

n = int(input_())
binary_tree = {}

for _ in range(n):
    parent, left, right = input_().split()
    binary_tree[parent] = (left, right)

preorder_path = []
inorder_path = []
postorder_path = []

def preorder_traversal(node):
    if node == '.':
        return
    left, right = binary_tree[node]
    preorder_path.append(node)
    preorder_traversal(left)
    preorder_traversal(right)

def inorder_traversal(node):
    if node == '.':
        return
    left, right = binary_tree[node]
    inorder_traversal(left)
    inorder_path.append(node)
    inorder_traversal(right)

def postorder_traversal(node):
    if node == '.':
        return
    left, right = binary_tree[node]
    postorder_traversal(left)
    postorder_traversal(right)
    postorder_path.append(node)

preorder_traversal('A')
inorder_traversal('A')
postorder_traversal('A')

print(''.join(preorder_path))
print(''.join(inorder_path))
print(''.join(postorder_path))
